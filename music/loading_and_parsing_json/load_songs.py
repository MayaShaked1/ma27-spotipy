import os
import json
from music import artist_album_song as songs
from music.searching import searching_options as search

path_to_json = r'D:\Users\Maya\course\gitCodesPython\spotipy\songs\\'  # the path from content root does not work
all_artists = []  # unique list of all the artists
artist_all_albums = []  # albums name of each artist
all_songs_sorted_each_artist = []  # list of all the songs of each artist
songs_in_album = []  # list of all the songs in album
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    path = path_to_json + file_name
    with open((path_to_json + file_name), 'r') as json_file:
        data = json.load(json_file)
        print(data)
        id_song = data["track"]["id"]
        song_name = data["track"]["name"]
        popularity_score_song = data["track"]["popularity"]
        id_album = data["track"]["album"]["id"]
        album_name = data["track"]["album"]["name"]
        for artist in range(len(data["track"]["artists"])):
            id_artist = data["track"]["artists"][artist]["id"]
            artist_name = data["track"]["artists"][artist]["name"]
            artists = songs.Artist(id_artist, artist_name)
            album_artist = songs.Album(id_album, album_name, artists)
            song = songs.Song(id_song, song_name, artists, album_artist, popularity_score_song)
            if not search.get_all_artist(artists, all_artists):
                all_artists.append(artists)
            if not search.songs_artist(artists, artist_all_albums):
                artist_all_albums.append({id_artist: [album_artist.name]})
                all_songs_sorted_each_artist.append({id_artist: [[song.name, song.popularity]]})
            else:
                artist_all_albums = search.songs_artist_is_exist(artists, album_name, artist_all_albums)
                search.sorted_songs_artist_is_exist(artists, song_name, popularity_score_song,
                                                    all_songs_sorted_each_artist)
        if not search.album_already_exist(album_artist, songs_in_album):
            songs_in_album.append({album_artist.id_number: [song.name]})
        else:
            songs_in_album = search.all_songs_album(id_album, song_name, songs_in_album)


def all_artists_lists():
    return all_artists


def artist_all_albums():
    return artist_all_albums


def all_songs_sorted_each_artist():
    return all_songs_sorted_each_artist


def songs_in_album():
    return songs_in_album
