# Lecture 14: zyBook 7.5 - 7.7
# Nested dictionaries, function arguments, functions returning multiple outputs 

# zyDE 7.5.1: Nested dictionaries example: Music library.
music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}
# print all the songs of the "The Wall" by "Pink Floyd"
print(music['Pink Floyd']['The Wall']['songs'])

# Fast operations with a dict: lookup/search, update/insert and delete

# iterate through the library
def print_library(music):
    for artist in music:
        print('Albums of ', artist)
        for album in music[artist]:
            print("\t", album)
            print("\t songs: ", music[artist][album]['songs'])




print_library(music)

# Add an artist
def add_artist(library, artist):
    ''' just adds a new artist if the artist is not in the music library'''
    if artist in library:
        print(artist, "exists already")
    else:
        library[artist] = {}
    return

# Add an album
def add_album(library, artist, album, songs, year, platinum):
    if artist in library:
        # Add the album
        if album not in library[artist]:
            # Add the album
            library[artist][album] =  {'songs': songs, 'year': year,'platinum': platinum}      
        else:
            print(album, "already exists")
    else:
        print(artist, "not in the library")
    
add_artist(music, "The Eagles")
print_library(music)
add_album(music,  "The Eagles", "Hotel California", ["Hotel California", "Desperado", "One of these nights"], 1976, True)
print_library(music)



# lists and recursion

def min_val(alist):
    '''find the min in a list of numbers, alist must have alteast one value'''
    # base case: solution for the simplest input, or input where the output is simplest
    if len(alist) == 0:
        return None
    if len(alist) == 1:
        return alist[0]
    
    # recursive case
    first_elem = alist[0]
    min_of_rest = min_val(alist[1:])
    if first_elem < min_of_rest:
        return first_elem
    else:
        return min_of_rest

print(f"{min_val([10])=}")
print(f"{min_val([10, -1, 0, 10, 5])=}")





















