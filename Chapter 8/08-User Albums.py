# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {
        "artist": artist_name,
        "title": album_title
    }

    if num_songs is not None:
        album["number_of_songs"] = num_songs

    return album


while True:
    print("\nEnter album information (type 'q' to quit).")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Album title: ")
    if title.lower() == 'q':
        break

    album = make_album(artist, title)
    print("Album created:", album)