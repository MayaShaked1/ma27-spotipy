from music.loading_and_parsing_json.load_songs import all_artists, artist_all_albums, all_songs_sorted_each_artist, \
    songs_in_album


def get_all_artist():
    return all_artists


def get_albums_name_artist(id_artist):
    count = 0
    for album in artist_all_albums:
        if (list(album.keys())[0]) == id_artist:
            return artist_all_albums[count]
        count += 1
    return 0


def get_10_popular_songs_artist(id_artist):
    count = 0
    for song in all_songs_sorted_each_artist:
        if (list(song.keys())[0]) == id_artist:
            return all_songs_sorted_each_artist[count]
        count += 1
    return 0


def get_all_songs_in_album(id_album):
    count = 0
    for song in songs_in_album:
        if (list(song.keys())[0]) == id_album:
            return songs_in_album[count]
        count += 1
    return 0
