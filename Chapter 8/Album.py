def make_album(artist_name, song_title):
    album_dictionary = {
        'artist': artist_name.title(),
        'title': song_title.title(),
    }
    return album_dictionary

album = make_album('the proclaimers', '500 miles')
print(album)

album = make_album('scott mckenzie', 'san francisco (be sure to wear flowers in your hair)')
print(album)

album = make_album('joni mitchell', 'the circle game')
print(album)

def make_album(artist_name, song_title, tracks=0):
    album_dictionary = {
        'artist': artist_name.title(),
        'title': song_title.title(),
    }
    if tracks: # not empty
        album_dictionary['tracks'] = tracks
    return album_dictionary

album = make_album('the proclaimers', '500 miles')
print(album)

album = make_album('scott mckenzie', 'san francisco (be sure to wear flowers in your hair)')
print(album)

album = make_album('joni mitchell', 'the circle game', tracks=10)
print(album)