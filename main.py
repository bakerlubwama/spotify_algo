"""
Step 1: Get a List of a User's Playlists API request

Step 2: Get user’s playlists choice (by name)
- Ask user to give us playlists (up to 3-5)
- Compare name with response from early step and retrieve desired playlist ids"""

#import packages
import requests
import json
#initating access token and API URL
SPOTIFY_GET_USER_PLAYLIST_URL = 'https://api.spotify.com/v1/users/baker162589/playlists'
ACCESS_TOKEN = 'BQBewDpg8gbyo2YivD9y6aGVJkGX8LBXVj9AuR5b2R7C_UE71n1mjK-_vTj_NsB5lD6KzzxjYyEpMj41oommBKmp69vb62rCMJbwiwO6gLAfy6L9tY52h4EW72XPM3x_-g9AenslDTyasCvKISO75sxU5of26nclneNzLWWI2Ub17P2adB8i-EcB58VgCeeqASmTtax_DCkGSZleasf2QTP-dqc'

# defining get user playlist function
def get_user_playlist_list():
    global response
    response = requests.get(
        SPOTIFY_GET_USER_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    response = response.json()
    return response
#getting user's playlist
playlist_list = get_user_playlist_list()
print(json.dumps(playlist_list, indent=2))

#defining function that get user's playlist choices
def get_playlist_choices():
    user_input = input("Enter playlist name: ")
    playlist_choices = user_input.split(", ")
    print(playlist_choices)
    playlist_ids = []
    for playlist in response["items"]:
        for choice in playlist_choices:
            if playlist["name"].lower() == choice.lower():
                playlist_ids.append(playlist["id"])
            else:
                pass
    return playlist_ids


user_choices = get_playlist_choices()
print(user_choices)

#step 3: take 5 random songs from each 
#Selects n random songs from each playlist and stores in new list. However list is a list of sublists. i.e [[1,2,3],[4,5,6],[7,8,9]]
def song_selection():
    new_list = []
    n = 3
    for sublist in songs_list:
        new_list.append(random.sample(sublist,n))
    return new_list

dj_random_selection = song_selection()

#cleans previous list of random songs, converting list of lists to flatlist i.e [1,2,3,4,5,6,7,8,9]
def song_selection_flatten():
    flat_list = []
    for sublist in dj_random_selection:
        for item in sublist:
            flat_list.append(item)
    return flat_list

dj_final_selection = song_selection_flatten()

print(dj_final_selection) # prints final selection of songs consisting of n number of songs from each of the selected playlists


#step 4: add tracks to queue
def queue_tracks():
    


