import os
import json
from music import artist_album_song as songs

path_to_json = r'D:\Users\Maya\course\gitCodesPython\spotipy\songs\\'  # the path from content root does not work
all_artists = []  # unique list of all the artists
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    path = path_to_json + file_name
    with open((path_to_json + file_name), 'r') as json_file:
        data = json.load(json_file)
        id_song = data["track"]["id"]
        song_name = data["track"]["name"]
        popularity_score_song = data["track"]["popularity"]
        id_album = data["track"]["album"]["id"]
        album_name = data["track"]["album"]["name"]
        for artist in range(len(data["track"]["artists"])):
            is_exist = False
            id_artist = data["track"]["artists"][artist]["id"]
            artist_name = data["track"]["artists"][artist]["name"]
            artists = songs.Artist(id_artist, artist_name)
            for check_artist in all_artists:  # is the artist already exist?
                if check_artist.id_number == id_artist:
                    is_exist = True
            if not is_exist:
                all_artists.append(artists)
            album = songs.Album(id_album, album_name, artists)
            album.add_track(id_song, song_name, artists)
for art in all_artists:
    print(art)
