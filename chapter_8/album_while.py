def make_album(artist, album, songs = None):
    
    if songs:
        artist_data = {'artist_name':artist, 'album_name': album, 'no_songs': songs}
    else:
        artist_data = {'artist_name':artist, 'album_name': album}
    return artist_data


while True:
    print('\nGive input to the program:')
    print('If you want to quit, type "q" at any time.')

    artist = input('Write the name of the artist: ')

    if artist == 'q':
        break

    album = input('Write the name of the album: ') 

    if album == 'q':
        break
    
    album_dict = make_album(artist, album)

    print(album_dict)