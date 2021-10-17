def make_album(artist, album, songs = None):
    
    if songs:
        artist_data = {'artist_name':artist, 'album_name': album, 'no_songs': songs}
    else:
        artist_data = {'artist_name':artist, 'album_name': album}
    return artist_data


print(make_album('arne', 'reinsdyr',22))
print(make_album('ingrid', 'klær'))