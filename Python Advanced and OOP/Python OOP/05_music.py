class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


# song = Music("Houdini", "Eminem", "Abra-abracadabra")
# print(song.print_info())
# print(song.play())
