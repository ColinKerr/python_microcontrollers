import os
from machine import Pin
from MusicPlayer import *

class Jukebox:
    def __init__(self, directory, bpm=140):
        self.directory = directory
        self.songs = self.load_songs()
        self.pins = [Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT), Pin(14, Pin.OUT)]
        self.bpm = bpm
        self.ms_pb = int((1000*60)//self.bpm)
        self.note_time = int(self.ms_pb // 4)


    def load_songs(self):
        songs = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".lines"):
                songs.append(filename)
        print("Loaded songs:", len(songs))
        return songs
    
    def play_all(self):
        for song in self.songs:
            print(f"Playing {song}...")
            voice_groups = load_voice_groups_from_file(self.directory + "/" + song)
            player = MusicPlayer(voice_groups, self.note_time, self.pins)
            player.start()
            while player.playing:
                pass
            print(f"Finished playing {song}.")


if __name__ == "__main__":
    jukebox = Jukebox("/")
    jukebox.play_all()