class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400


directory_wav = 'data/data_output/wav/'
directory_mid = 'data/data_output/mid/'
instrument_poss = ['violin', 'piano', 'bass']
length_poss = ['short', 'medium', 'long']

vel_min, vel_max = 35, 127 #Velocità note

bpm = 60  # tempo (beats per minute)

y_scale = 0.5  # scaling parameter for y-axis data_input (1 = linear)

# note set for mapping (or use a few octaves of a specific scale)
note_names = ['C1', 'C2', 'G2',
              'C3', 'E3', 'G3', 'A3', 'B3',
              'D4', 'E4', 'G4', 'A4', 'B4',
              'D5', 'E5', 'G5', 'A5', 'B5',
              'D6', 'E6', 'F#6', 'G6', 'A6']

# 4 octaves of major scale
note_names1 = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
               'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
               'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
               'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']

# 4 octaves of major pentatonic scale
note_names2 = ['C2', 'D2', 'E2', 'G2', 'A2',
               'C3', 'D3', 'E3', 'G3', 'A3',
               'C4', 'D4', 'E4', 'G4', 'A4',
               'C5', 'D5', 'E5', 'G5', 'A5']
