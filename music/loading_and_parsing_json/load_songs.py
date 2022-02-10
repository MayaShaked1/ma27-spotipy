import os
import json
from music import artist_album_song as songs
from music.searching import searching_options as search

path_to_json = r'D:\Users\Maya\course\gitCodesPython\spotipy\songs\\'  # the path from content root does not work
all_artists = []  # unique list of all the artists
artist_all_albums = []
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    path = path_to_json + file_name
    count = 0
    with open((path_to_json + file_name), 'r') as json_file:
        data = json.load(json_file)
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
            else:
                artist_all_albums=search.songs_artist_is_exist(artists, album_name, artist_all_albums)

            # all_artists.append({id_artist:[album_name]})
            # all_artists.append({id_artist: [search.]})
            # for check_artist in all_artists:  # is the artist already exist?
            #     if check_artist.id_number == id_artist:
            #         is_exist = True
            # if not is_exist:
            #     all_artists.append(artists)
            # album = songs.Album(id_album, album_name, artists)
            # album.add_track(id_song, song_name, artists)
    count += 1
# for art in all_artists:
#     print(art)
for album in artist_all_albums:
    print(album)
