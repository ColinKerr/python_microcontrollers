import os
from machine import Pin
from MusicPlayer import *
from irrecvdata import irGetCMD

PLAY = 0xffa857
STOP = 0xffa25D # Use power for stop
BACK = 0xffe01f
NEXT = 0xff906f

class Jukebox:
    def __init__(self, directory, bpm=140):
        self.directory = directory
        self.songs = self.load_songs()
        self.current_song_index = 0
        self.pins = [Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT), Pin(14, Pin.OUT)]
        self.bpm = bpm
        self.ms_pb = int((1000*60)//self.bpm)
        self.note_time = int(self.ms_pb // 4)
        self.current_player = None

    def load_songs(self):
        songs = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".lines"):
                songs.append(filename)
        print("Loaded songs:", len(songs))
        return songs
    
    def play_all(self):
        self.play_song(self.current_song_index)

    def play_next_song(self):
        self.current_song_index += 1
        if self.current_song_index >= len(self.songs):
            self.current_song_index = 0

        self.play_song(self.current_song_index)

    def play_song(self, song_index):
        song = self.songs[song_index]
        print(f"Playing {song}...")
        voice_groups = load_voice_groups_from_file(self.directory + "/" + song)
        self.current_player = MusicPlayer(voice_groups, self.note_time, self.pins, self.play_next_song)
        self.current_player.start()
    
    def play(self):
        if self.current_player is None:
            self.play_all()
        elif not self.current_player.playing:
            self.current_player.start()
    
    def pause(self):
        if self.current_player is not None:
            self.current_player.pause()

    def back(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
        if self.current_player is not None and self.current_player.playing:
            self.current_player.stop()
        self.play_song(self.current_song_index)

    def next(self):
        if self.current_player is not None and self.current_player.playing:
            self.current_player.stop()
        self.play_next_song()

    def stop(self):
        if self.current_player is not None:
            self.current_player.stop()
            self.current_player = None
        self.current_song_index = 0
    
    def isPlaying(self):
        if self.current_player is not None and self.current_player.playing:
            return True
        
        return False

    def commandHandler(self, irValue):
        if irValue == PLAY:
            if self.isPlaying():
                self.pause()
            else:
                self.play()
        elif irValue == STOP:
            self.stop()
        elif irValue == BACK:
            self.back()
        elif irValue == NEXT:
            self.next()


if __name__ == "__main__":
    jukebox = Jukebox("/")
    remote = irGetCMD(21, commandHandler=jukebox.commandHandler)
