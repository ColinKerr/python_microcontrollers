from machine import Pin, PWM, Timer

"""
Plays music using PWM pins.  
On ESP32-S3 it seems that you can only half of the PWM channels at a time, leading to a maximum of 4 voices.
Unsure if this limit is a bug in the logic a limitation of the python library or some other limitation.

Use `load_voice_groups_from_file` to load a song and to see the sheet music format.
"""
class MusicPlayer:
    def __init__(self, voice_groups, note_time, pins):
        self.voice_groups = voice_groups
        self.current_group = []
        self.note_time = note_time
        self.pins = pins
        self.voice_limit = len(pins)
        self.group_index = 0
        self.note_index = 0
        self.group_timer = Timer(0)
        self.pwms = [[0, None]] * len(pins)
        self.playing = False
        print("PWM Count:", len(self.pwms))
    
    def start(self):
        self.playing = True
        self.current_group = self.voice_groups.pop(0)
        self.play_next_note()
    
    def play_next_note(self, t=None):
        if t:
            t.deinit()

        if self.note_index >= len(self.current_group[0]):
            if not self.start_next_group():
                self.clean_up_pwms()
                print("Song done")
                return
        
        if self.current_group:
            for i, voice in enumerate(self.current_group):
                if (i >= self.voice_limit):
                    print("Voice limit reached, skipping voice", i + 1, "of", len(self.current_group))
                    continue
                note = voice[self.note_index]
                pwm = self.pwms[i]
                sustain = True
                if pwm[0] != note and note != -1:
                    if pwm[1] is not None:
                        #print("PWM Deinit old note", pwm[0], "on voice", i + 1)
                        pwm[1].deinit()
                    sustain = False
                if sustain:
                    pass
                elif note > 0:
                    #print("PWM init, Playing note", note, "on voice", i + 1)
                    pwm = PWM(self.pins[i], freq=note, duty=512)
                    self.pwms[i] = [note, pwm]
                else:
                    self.pwms[i] = [0, None]
            self.note_index += 1
            self.group_timer.deinit()
            self.group_timer.init(mode=Timer.ONE_SHOT, period=self.note_time, callback=lambda t: self.play_next_note(t))

    def start_next_group(self):
        self.note_index = 0
        if self.voice_groups:
            self.current_group = self.voice_groups.pop(0)
            print(len(self.voice_groups), "voice groups left to play")
            return True
        return False
    
    def clean_up_pwms(self):
        for pwm in self.pwms:
            if pwm[1] is not None:
                pwm[1].deinit()
        self.playing = False

def load_voice_groups_from_file(file_path):
    """
    Reads a text file containing musical notes and returns groups of voices that should be played together.
    The number at the start of the line is the octave.
    Lower case letters are normal notes, upper case letters are sharp notes
    - is a rest note, which means no sound will be played for that note.
    > is a sustain note, which means the previous note will continue to play.
    5|e-e---e---c-e---g---------|
    4|a-a---a---a-a---b---------|
    4|F-F---F---F-F---g-------g-|
    3|------------------------g-|
    2|d-d---d---d-d---g-------g-|
    1|------------------------g-|
    Groups are seperated by empty lines.
    A voice is a list of frequencies to play, a voice must exist for each concurrent frequency to play.
    When the example above is parsed it will produce four voices.
    
    This format was adapted (slightly) from the format provided by pianoletternotes.blogspot.com.
    """
    note_line_groups = read_notes_from_file(file_path)
    return parse_note_line_groups(note_line_groups)


def read_notes_from_file(file_path):
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
            freq = int(notes[note][octave])
            line_freqs.append(freq)
        freq_lines.append(line_freqs)

    return freq_lines

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
"-" : [0,     0,     0,      0,      0,      0,      0,       0,       0],          # Rest note
">" : [-1,    -1,    -1,     -1,     -1,     -1,     -1,      -1,      -1]          # Sustain note
}