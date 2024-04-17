class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = 0
        self.song_list = []
        self.root = tk.Tk()
        self.root.title('😆😆Music Player')
        self.root.geometry('1366x768')
        self.root.config(bg='#03001C')
        self.setup_ui()

    def setup_ui(self):
        play_button = tk.Button(self.root, text='Play', command=self.play_music)
        play_button.place(x=650, y=650)
        play_button.config(bg='#5B8FB9')

        # Add more UI setup here, refactored similar to the play_button creation

    def play_music(self):
        pygame.mixer.music.load(self.song_list[self.current_song])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        current_song_label.config(text=self.song_list[self.current_song])

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def next_song(self):
        self.current_song = (self.current_song + 1) % len(self.song_list)
        pygame.mixer.music.stop()
        self.play_music()

    def prev_song(self):
        self.current_song = (self.current_song - 1) % len(self.song_list)
        pygame.mixer.music.stop()
        self.play_music()

    def add_song(self):
        song_name = simpledialog.askstring('Input', 'Enter the name of the song: ', parent=self.root)
        self.song_list.append(os.path.join('music_folder', song_name))

if __name__ == '__main__':
    app = MusicPlayer()
    app.root.mainloop()
