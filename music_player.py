import tkinter as tk
from tkinter import simpledialog
import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(song_list[current_song])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    current_song_label.config(text=song_list[current_song])

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def play_or_resume():
    if pygame.mixer.music.get_busy():
        resume_music()
    else:
        play_music()

def next_song():
    global current_song
    current_song += 1
    if current_song >= len(song_list):
        current_song = 0
    pygame.mixer.music.stop()
    play_music()

def prev_song():
    global current_song
    current_song -= 1
    if current_song < 0:
        current_song = len(song_list) - 1
    pygame.mixer.music.stop()
    play_music()

def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)
    volume_label.config(text=f'Volume: {int(volume*100)}')

music_file = "Input file path here"
song_list = []

def add_song():
    song_name = simpledialog.askstring("Input", "Enter the name of the song: ", parent=root)
    song_list.append(music_file + song_name)

current_song = 0

root = tk.Tk()
root.title("😆😆Music Player")
root.geometry('1366x768')

play_button = tk.Button(root, text="Play", command=play_music)
play_button.place(x=650, y=650)
play_button.config(bg='#5B8FB9')

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.place(x=550, y=650)
pause_button.config(bg='#5B8FB9')

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.place(x=740, y=650)
resume_button.config(bg='#5B8FB9')

next_button = tk.Button(root, text="Next", command=next_song)
next_button.place(x=845, y=650)
next_button.config(bg='#5B8FB9')

prev_button = tk.Button(root, text="Prev", command=prev_song)
prev_button.place(x=470, y=650)
prev_button.config(bg='#5B8FB9')

volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=set_volume)
volume_scale.set(0.5)
volume_scale.place(x=1200, y=650)
volume_scale.config(bg='#5B8FB9')

volume_label = tk.Label(root)
volume_label.place(x=1200, y=630)

current_song_label = tk.Label(root)
current_song_label.place(x=500, y=600)

add_button = tk.Button(root, text="Add Song", command=add_song)
add_button.pack()


pygame.mixer.init()
root.config(bg='#03001C')
root.mainloop()
