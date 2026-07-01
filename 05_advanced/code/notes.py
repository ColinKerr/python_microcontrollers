from machine import PWM, Timer
from math import floor

# This format treats each four character sequence as a note
# Note format is [note][octave][duration], note is two characters, octave is 0-8 and duration is 1-9.
# Notes are C, CS, D, DS, E, F, FS, G, GS, A, AS, B and __ for rest. And are found in notes.py.

# Takes in a string of notes and returns a list of objects with note frequency and duration.
def parse_notes(note_array, step_size, append_rest=True):
    note_sequence = []
    for n in note_array:
        if len(n) != 4:
            raise ValueError("Note format is incorrect. Each note must be 4 characters long.")
        note = n[:2]
        octave = int(n[2])
        duration = int(n[3])
        frequency = int(notes[note][octave])
        time = int(duration * step_size)
        note_sequence.append([frequency, time])
        if append_rest and note[0] != "_":
            note_sequence.append([0, floor(step_size/4)])
    return note_sequence


# Takes in a list of functions and calls them in sequence to play the sequence.
def play_sequence(note_sequence, timer, pin):
    if note_sequence:
        note = note_sequence.pop(0)
        sound = PWM(pin, freq=note[0], duty=512) if note[0] > 0 else None
        timer.init(mode=Timer.ONE_SHOT, period=note[1], callback=(lambda t: play_next_sequence(t, sound, note_sequence, timer, pin)))

def play_next_sequence(t, sound, note_sequence, timer, pin):
    if sound:
        sound.deinit()
    timer.deinit()
    if note_sequence:
        print(len(note_sequence), "notes left to play")
        note = note_sequence.pop(0)
        sound = PWM(pin, freq=note[0], duty=512) if note[0] > 0 else None
        timer.init(mode=Timer.ONE_SHOT, period=note[1], callback=(lambda t: play_next_sequence(t, sound, note_sequence, timer, pin)))

A = "A_34"
AL = "A_39"
B = "B_34"
BL = "B_39"
C = "C_44"
CL = "C_49"
D = "D_44"
DL = "D_49"
E = "E_44"
EL = "E_49"
F = "F_44"
FL = "F_49"
G = "G_34"
GL = "G_39"
P = "__11"
PL = "__19"

notes = {
"C_" : [16.35, 32.7,  65.41,  130.81, 261.63, 523.25, 1046.5,  2093,    4186],
"CS" : [17.32, 34.65, 69.3,   138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
"D_" : [18.35, 36.71, 73.42,  146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64],
"DS" : [19.45, 38.89, 77.78,  155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
"E_" : [20.6,  41.2,  82.41,  164.81, 329.63, 659.25, 1318.51, 2637.02, 5274.04],
"F_" : [21.83, 43.65, 87.31,  174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65],
"FS" : [23.12, 46.25, 92.5,   185,    369.99, 739.99, 1479.98, 2959.96, 5919.91],
"G_" : [24.5,  49,    98,     196,    392,    783.99, 1567.98, 3135.96, 6271.93],
"GS" : [25.96, 51.91, 103.83, 207.65, 415.3,  830.61, 1661.22, 3322.44, 6644.88],
"A_" : [27.5,  55,    110,    220,    440,    880,    1760,    3520,    7040],
"AS" : [29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62],
"B_" : [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13],
"__" : [0, 0, 0, 0, 0, 0, 0, 0, 0]
}
