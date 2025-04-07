import os
import pygame
from mutagen.mp3 import MP3
import time
import math

current_track_info = {
     'file_path': None,
     'file_name': None,
     'duration': None
}

pygame.mixer.init()

def display_help():
    print("\nCommands:")
    print("'play' - Start playing a music file")
    print("'pause' - Pause the current track")
    print("'resume' - Resume paused track")
    print("'stop' - Stop current playback")
    print("'info' - Show current track information")
    print("'exit' - Quit the music player")
    print("'help' - Show this help message\n")

def get_track_duration(file_path):
    try:
        audio = MP3(file_path)
        length = audio.info.length  
        minutes, seconds = divmod(length, 60)
        return f"{int(minutes)}:{int(seconds):02d}"
    except Exception as e:
        # Catch potential errors like file not found or not a valid MP3
        print(f"Error getting duration for {os.path.basename(file_path)}: {e}")
        return None # Return None to indicate failure

def show_track_info():
    global current_track_info
 
    if current_track_info['file_path'] is None:
       print("No track has been loaded")
       return

    print("\nCurrent Track Information:")
    print(f"Filename: {current_track_info['file_name']}")
    print(f"Duration: {current_track_info['duration']}")
    print(f"File Path: {current_track_info['file_path']}")

    if pygame.mixer.get_busy():
       print("Status: Currently Playing")
    elif pygame.mixer.get_busy() is False:
       print("Status: Paused")
    else:
       print("Status: Stopped")

def play_music():
    global current_track_info

    file_path = input("Enter the full path to your music file: ")

    if not os.path.exists(file_path):
       print("Error: File Not Found")
       return

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        current_track_info['file_path'] = file_path
        current_track_info['file_name'] = os.path.basename(file_path)
        current_track_info['duration'] = get_track_duration(file_path)

        print(f"\nNow playing: {current_track_info['file_name']}")
        print(f"Track duration: {current_track_info['duration']}")

    except pygame.error:
        print("Error: Could not play the file. Supported formats: MP3, WAV, OGG")
 
def main():
    print("\n🎵 Simple Python Music Player 🎵")
    display_help()

    while True:
        command = input("Enter Command: ").lower()

        if command == 'play':
           play_music()
        elif command == 'pause':
            if pygame.mixer.music.get_busy():
               pygame.mixer.music.pause()
               print("Playback paused")
            else:
               print("No Track Playing")
        elif command == 'resume':
            if current_track_info['file_path'] is None:
               print("No track has been loaded. Use 'play' to load track first")
            elif not pygame.mixer.music.get_busy():
               pygame.mixer.music.unpause()
               print("Resuming Playback")
            else:
               print("Track is already playing!")
        elif command == 'stop':
            pygame.mixer.music.stop()
            print("Stopped!")
        elif command == 'info':
            show_track_info()
        elif command == 'help':
            display_help()
        elif command == 'exit':
            print("Bye 👋")
            break
        else:
            print("Invalid command! Type 'help' for available commands")






