"""
Step 1: Get a List of a User's Playlists API request
Step 2: Get user’s playlists choice (by name)
- Ask user to give us playlists (up to 3-5)
- Compare name with response from early step and retrieve desired playlist ids"""

import requests
import json
import random

#Account information
spotify_id = input("Enter your spotify user id: ")
ACCESS_TOKEN = 'BQAChsqs-w7J28BdkwFjnz9e1r4g9XHtfjwtVxSLqveFGh_iZY5hRZZx_vViI5To4E39dq0MbU1h82g1SRIau9Pn7LkL4ISWyz19HugvpSIpgk-tsRUoFRWVcmkkJszx4lNNuVIVYkQwwpMMVe1LnLeqXE9KgJYmcmscoeUSWFjYT40heBxHCUTt-K64YH83xu6vkDjownI4gupL_hFLCq6pjmaA'

#Get's list of users playlists
def get_user_playlist_list():
    global response
    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_id)
    response = requests.get(query,
                            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
    response = response.json()
    #print(response)
    return response

playlist_list = get_user_playlist_list()
playlist_list_access = playlist_list["items"]

#Get's users selected playlists
def get_playlist_choices(list):
    user_input = input("Enter playlist name: ")
    playlist_choices = user_input.split(", ")
    #print(playlist_choices)
    playlist_ids = []
    for playlist in list:
        for choice in playlist_choices:
            if playlist['name'].lower() == choice.lower():
                playlist_ids.append(playlist["id"])
            else:
                pass
    #print(playlist_ids)
    return playlist_ids

user_playlist_choices = get_playlist_choices(playlist_list_access)

# Get's all songs within selected playlists and stores within dictionary
def find_songs(choices):
    dj_tracks_list = []
    n = 3
    track_uris = {}
    for playlist_id in choices:
        track_uris[playlist_id] = []
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(ACCESS_TOKEN)})

        response_json = response.json()

        for i in response_json["items"]:
            track_uris[playlist_id].append(i["track"]["uri"])
    #print(track_uris)
    return track_uris

user_choices_songs = find_songs(user_playlist_choices)

songs_dicts = user_choices_songs.values()
#print(songs_dicts)

songs_list = list(songs_dicts)
#print(songs_list)

#Step 3
#Selects n random songs from each playlist and stores in new list. However list is a list of sublists. i.e [[1,2,3],[4,5,6],[7,8,9]]
def song_selection(songs, n):
    new_list = []
    for sublist in songs:
        new_list.append(random.sample(sublist, n))
    #print(new_list)
    return new_list

dj_random_selection = song_selection(songs_list, 3)

#cleans previous list of random songs, converting list of lists to flatlist i.e [1,2,3,4,5,6,7,8,9]
def song_selection_flatten(selection):
    flat_list = []
    for sublist in selection:
        for item in sublist:
            flat_list.append(item)
    #print(flat_list)
    return flat_list

dj_final_selection = song_selection_flatten(dj_random_selection)
#print(dj_final_selection)

#print(dj_final_selection) # prints final selection of songs consisting of n number of songs from each of the selected playlists




#step 4: add tracks to queue
QUEUE_ACCESS_TOKEN = 'BQD-d3UBtpBNxP3zgHIagjXBIP8zPV3trhVF7UpWW6YkG1apwt6CH_Z7VFhijvAGpxzOw7FPMaGpbp8e2N_BBoRBIfOllOa3pjIQl5i5VaBMUR5ZNaiQ29kbIR3t-eUlF3H5iR8kl4saQIaI_sKlktJ2nJy43oCjUo1FQgZsi8rWTMDDpIWRhGjuz7QjPadf5YwojrmqFBoZWslKRoUlWSak05GO'
ADD_ITEM_TO_QUEUE_URL = 'https://api.spotify.com/v1/me/player/queue?uri={}'

def queue_tracks(track_list):
    for track in track_list:
        requests.post(
            ADD_ITEM_TO_QUEUE_URL.format(track),
            headers={
                "Authorization": f"Bearer {QUEUE_ACCESS_TOKEN}"
            }
        )


queue_djs_tracks = queue_tracks(dj_final_selection)
