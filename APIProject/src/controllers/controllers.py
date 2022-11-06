from flask import Flask, request
from src.util.const import *
from .helpers import *
from audiolazy import str2midi
from midiutil import MIDIFile
from music21 import converter, instrument
from midi2audio import FluidSynth
import numpy as np
import uuid
app = Flask(__name__)
import os

def generate_audio():
    request_data = request.get_json()
    instrument_selected = request_data["instrument"]
    length = request_data["length"]
    data = request_data["data"]

    data.sort(key=lambda x: x["date"])
    n_data = len(data)

    duration_beats = get_duration(length)  # desired duration in beats (1 beat = 1 second if bpm=60)

    numerical_values = np.array([item.get('double') for item in data])

    # Compress Time - Mettendo min come parametro non si sente per niente la prima nota
    time_data = map_value(numerical_values, 0, max(numerical_values), 0, duration_beats)
    print(time_data)

    # calculate duration in seconds
    bpm = 60  # if bpm = 60, 1 beat = 1 sec
    duration_sec = duration_beats * 60 / bpm  # duration in seconds (actually, onset of last note)
    print('Duration:', duration_sec, 'seconds')

    # normalize and scale data_input
    if min(numerical_values) == max(numerical_values):  # la funzione di mapping ha dei limiti e devono essere controllati
        y_data = np.zeros(len(numerical_values))
        print("Dati che non rispettano i parametri", y_data)
    else:
        y_data = map_value(numerical_values, min(numerical_values), max(numerical_values), 0, 1)
        print("Normalized data:", y_data)
        y_data = y_data ** y_scale  # In questo modo dovremmo avere una differenza più marcata tra le note

    # Make list of MIDI numbers of chosen notes for mapping
    note_midis = [str2midi(n) for n in note_names]  # make a list of midi note numbers
    n_notes = len(note_midis)
    print('Resolution:', n_notes, 'notes')

    # Map y-axis data_input to MIDI notes and velocity
    midi_data = []
    vel_data = []
    for i in range(n_data):
        print(y_data[i])
        print(map_value(y_data[i], 0, 1, n_notes - 1, 0))
        note_index = round(map_value(y_data[i], 0, 1, n_notes - 1, 0))  # bigger craters are mapped to lower notes
        midi_data.append(note_midis[note_index])

        note_velocity = round(map_value(y_data[i], 0, 1, vel_min, vel_max))  # bigger craters will be louder
        vel_data.append(note_velocity)

    # Calcolo durata della nota con due opzioni
    # farla durare dal momento in cui dovrebbe iniziare fino alla fine
    # KeyError: '240' --> causato dal fatto che si sovrappongono note di durata differente
    # https://github.com/MarkCWirt/MIDIUtil/issues/24
    duration_time_note = np.array([duration_sec - x for x in time_data])
    print(duration_time_note)
    # farla durare tanto quanto le altre note
    duration_time_note_v2 = split(duration_sec - round(min(time_data)), n_data)
    print(duration_time_note_v2)

    # Save MIDI filex
    # https://readthedocs.org/projects/midiutil/downloads/pdf/latest/
    my_midi_file = MIDIFile(numTracks=1, deinterleave=False, removeDuplicates=False)  # one track
    my_midi_file.addTempo(track=0, time=0, tempo=bpm)

    real_duration = duration_time_note_v2  if duration_time_note_v2 != -1 else duration_time_note
    print(real_duration)
    for i in range(n_data):
        my_midi_file.addNote(track=0, channel=0, pitch=midi_data[i], time=time_data[i],
                             duration=real_duration[i],
                             volume=vel_data[i])

    """"""
    output_filename = str(uuid.uuid4())

    with open(directory_mid + output_filename + '.mid', "wb") as f:
        my_midi_file.writeFile(f)
    print('Saved', output_filename + '.mid')

    # Conversione in un file con un determinato strumento
    s = converter.parse(directory_mid + output_filename + '.mid')
    instrument21 = get_instrument(instrument_selected)
    for p in s.parts:
        p.insert(0, instrument21)

    s.write('midi', directory_mid + output_filename + '.mid')

    fs = FluidSynth('/Users/andreaongaro/Documents/Università/Laurea/Progetto '
                    'Sonificazione/APIProject/data/data_input/FluidR3Mono_GM.sf3')
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
