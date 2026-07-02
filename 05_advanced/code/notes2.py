
# def play_sequence(note_sequence, timer, pin):
#     if note_sequence:
#         note = note_sequence.pop(0)
#         sound = PWM(pin, freq=note[0], duty=512) if note[0] > 0 else None
#         timer.init(mode=Timer.ONE_SHOT, period=note[1], callback=(lambda t: play_next_sequence(t, sound, note_sequence, timer, pin)))

# def play_next_sequence(t, sound, note_sequence, timer, pin):
#     if sound:
#         sound.deinit()
#     timer.deinit()
#     if note_sequence:
#         print(len(note_sequence), "notes left to play")
#         note = note_sequence.pop(0)
#         sound = PWM(pin, freq=note[0], duty=512) if note[0] > 0 else None
#         timer.init(mode=Timer.ONE_SHOT, period=note[1], callback=(lambda t: play_next_sequence(t, sound, note_sequence, timer, pin)))


def read_notes_from_file(file_path):
    """
    Reads a text file containing musical notes and returns groups of note lines that should be played together
    Groups are seperated by empty lines.
    """
    note_lines_groups = []
    with open(file_path, 'r') as file:
        current_group = []
        note_lines_groups.append(current_group)
        for line in file:
            stripped_line = line.strip()
            if not stripped_line:  
                current_group = []
                note_lines_groups.append(current_group)
            else:
                current_group.append(stripped_line)
    return note_lines_groups

def create_merged_frequency_lines(freq_lines):
    voice_lines = []
    first_voice = freq_lines[0]
    voice_lines.append(first_voice)
    for line in freq_lines[1:]:
        for i in range(len(line)):
            if line[i] == 0:
                continue
            found_spot = False
            for voice in voice_lines:
                if voice[i] == 0 and line[i] != 0:
                    voice[i] = line[i]
                    found_spot = True
                    break
            if not found_spot:
                new_voice = [0] * len(line)
                new_voice[i] = line[i]
                voice_lines.append(new_voice)

    return voice_lines

def parse_note_line_groups(note_line_groups):
    voice_groups = []
    for group in note_line_groups:
        if len(group) == 0:
            continue
        freq_lines = parse_note_lines(group)
        voices = create_merged_frequency_lines(freq_lines)
        voice_groups.append(voices)
    return voice_groups

def parse_note_lines(note_lines):
    freq_lines = []
    for line in note_lines:
        octave = int(line[0])
        line_freqs = []
        for note in line[2:-1]:
            freq = notes[note][octave]
            line_freqs.append(freq)
        freq_lines.append(line_freqs)

    return freq_lines


notes = {
"c" : [16.35, 32.7,  65.41,  130.81, 261.63, 523.25, 1046.5,  2093,    4186],
"C" : [17.32, 34.65, 69.3,   138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
"d" : [18.35, 36.71, 73.42,  146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64],
"D" : [19.45, 38.89, 77.78,  155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
"e" : [20.6,  41.2,  82.41,  164.81, 329.63, 659.25, 1318.51, 2637.02, 5274.04],
"f" : [21.83, 43.65, 87.31,  174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65],
"F" : [23.12, 46.25, 92.5,   185,    369.99, 739.99, 1479.98, 2959.96, 5919.91],
"g" : [24.5,  49,    98,     196,    392,    783.99, 1567.98, 3135.96, 6271.93],
"G" : [25.96, 51.91, 103.83, 207.65, 415.3,  830.61, 1661.22, 3322.44, 6644.88],
"a" : [27.5,  55,    110,    220,    440,    880,    1760,    3520,    7040],
"A" : [29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62],
"b" : [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13],
"-" : [0, 0, 0, 0, 0, 0, 0, 0, 0]
}