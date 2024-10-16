# Chapter 8/User_Albums.py

def make_album(artist_name, song_title):
    album_dictionary = {
        'artist': artist_name.title(),
        'title': song_title.title(),
    }
    return album_dictionary

activate = True
while activate:
    print("\nenter 'q' at any time to quit!")
    name = input("Please give the name of the artist: ")
    if name == 'q':
        print("Thanks for responding.")
        break
    
    song = input("Please give the name of the song: ")
    if song == 'q':
        print("Thanks for responding.")
        break
    
    album = make_album(name, song)
    print(album)
    
    activate = False
