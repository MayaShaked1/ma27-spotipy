from searching.getting_value_to_key import get_all_artist, get_albums_name_artist, get_10_popular_songs_artist, \
    get_all_songs_in_album


def main():
    print("all artist:")
    all_artists = get_all_artist()
    for artist in all_artists:
        print(artist)


main()
