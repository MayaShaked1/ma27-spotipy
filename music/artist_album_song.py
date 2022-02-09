class Song:
    def __init__(self, id_number, name, artist, album_name, popularity):
        self.id_number = id_number
        self.name = name
        self.artist = artist
        self.album_name = album_name
        self.popularity = popularity

        artist.add_song(self)

    def __repr__(self):
        return "<Test id:%s name:%s artist:%s album:%s popularity:%s>" % (
            self.id_number, self.name, self.artist, self.album_name, self.popularity)

    def __str__(self):
        return "-id number of a song is- %s, -name of the song is- %s," \
               " -artist's info- %s, -album's info- %s, -popularity score- is %s" % (
                   self.id_number, self.name, self.artist, self.album_name, self.popularity)


class Album:
    def __init__(self, id_number, name, artist):
        self.id_number = id_number
        self.name = name
        self.artist = artist

        self.tracks = []

        artist.add_album(self)

    def add_track(self, id_number, name, artist=None):
        if artist is None:
            artist = self.artist

        track_number = len(self.tracks)

        song = Song(id_number, name, artist, self, track_number)

        self.tracks.append(song)

    def __repr__(self):
        return "<Test id:%s name:%s>" % (
            self.id_number, self.name)

    def __str__(self):
        return "id is %s, name is %s" % (
            self.id_number, self.name)


class Artist:
    def __init__(self, id_number, name):
        self.id_number = id_number
        self.name = name

        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def __repr__(self):
        return "<Test id:%s name:%s artist:%s album:%s popularity:%s>" % (
            self.id_number, self.name)

    def __str__(self):
        return "id is %s, name is %s" % (
            self.id_number, self.name)



