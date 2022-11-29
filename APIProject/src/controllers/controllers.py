from flask import Flask, request
from src.util.const import *
from .helpers import *
from audiolazy import str2midi
from midiutil import MIDIFile
from music21 import converter, instrument
from midi2audio import FluidSynth
import numpy as np
import uuid
import os

app = Flask(__name__)

def generate_audio():
    request_data = request.get_json()
    instrument_selected = request_data["instrument"]
    length = request_data["length"]
    data = request_data["data"]
    order = request_data["order"]

    data.sort(key=lambda x: x["date"])
    numerical_values = np.array([item.get('double') for item in data])
    id_values = np.array([item.get('id') for item in data])
    duration_beats = get_duration(length)
    n_data = len(numerical_values)

    # Tempo delle note - il calcolo è proporzionale ai dati inseriti
    val = duration_beats / (n_data + 1)
    time_data = np.arange(0, duration_beats, val)

    bpm = 60  # if bpm = 60, 1 beat = 1 sec
    duration_sec = duration_beats * 60 / bpm

    duration_notes = get_duration_notes(id_values, time_data, duration_sec)

    if min(numerical_values) == max(numerical_values):  # la funzione di mapping ha dei limiti e devono essere controllati
        y_data = np.zeros(len(numerical_values))
        print("Dati che non rispettano i parametri", y_data)
    else:
        y_data = map_value(numerical_values, min(numerical_values), max(numerical_values), 0, 1)
        print("Normalized data:", y_data)
        y_data = y_data ** y_scale  # In questo modo dovremmo avere una differenza più marcata tra le note
        print("Scaled data:", y_data)

    note_midis = [str2midi(n) for n in note_names]  # conversione delle note in midi
    n_notes = len(note_midis)

    # Conversione dei dati in note e calcolo velocità
    midi_data = []
    vel_data = []
    for i in range(n_data):
        if order == "DESC":
            note_index = round(map_value(y_data[i], 0, 1, n_notes - 1, 0))
        else:
            note_index = round(map_value(y_data[i], 0, 1, 0, n_notes - 1))
        midi_data.append(note_midis[note_index])

        note_velocity = round(map_value(y_data[i], 0, 1, vel_min, vel_max))  
        vel_data.append(note_velocity)

    my_midi_file = MIDIFile(numTracks=1, deinterleave=False, removeDuplicates=False)
    my_midi_file.addTempo(track=0, time=0, tempo=bpm)

    for i in range(n_data):
        my_midi_file.addNote(track=0, channel=0, pitch=midi_data[i], time=time_data[i],
                             duration=duration_notes[i], volume=vel_data[i])

    output_filename = str(uuid.uuid4())

    with open(directory_mid + output_filename + '.mid', "wb") as f:
        my_midi_file.writeFile(f)

    print('Saved', directory_mid + output_filename + '.mid')

    # Conversione in un file con un determinato strumento
    s = converter.parse(directory_mid + output_filename + '.mid')
    instrument21 = get_instrument(instrument_selected)
    for p in s.parts:
        p.insert(0, instrument21)

    s.write('midi', directory_mid + output_filename + '.mid')

    fs = FluidSynth('data/data_input/FluidR3Mono_GM.sf3')
    fs.midi_to_audio(directory_mid + output_filename + '.mid', directory_wav + output_filename + '.flac')

    #Rimozione file mid per ridurre lo spazio occupato sul server
    basedir = os.path.abspath(os.path.dirname(__file__))
    os.remove(os.path.join(basedir, '..', '..', directory_mid, output_filename + '.mid'))
    return directory_wav + output_filename + '.flac'


def get_duration(length) -> float:
    if length == "short":
        return 30
    elif length == "medium":
        return 52.8
    else:
        return 90


def get_instrument(instrument_sel):
    if instrument_sel == "violin":
        return instrument.Violin()
    elif instrument_sel == "piano":
        return instrument.Piano()
    else:
        return instrument.Bass()

def get_duration_notes(array_id, time_data, duration_sec):
    conc = dict(zip(array_id, time_data))
    order = {k: v for k, v in sorted(conc.items(), key=lambda item: item[1])}
    num = np.array([x for x in order.values()])
    time_data = np.append(num, duration_sec)
    d = np.diff(time_data)
    conc2 = dict(zip(order.keys(), d))
    return [v for idd in array_id for k,v in conc2.items() if k == idd ]