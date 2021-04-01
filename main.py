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
ACCESS_TOKEN = 'BQC8Y5H91gdBEY8nNSsC25TgHNxLBkIAbosSO1rFrb7G8IIEq02vj_4b_LvivVogjhrknlaiOfRUtlkw573mM17-8ZzyQa8lPBopbFKN_BvhOrkTf-chFRoeX8VwVTPWmLJpHVq66JVR_V5ESo9ffEKPEX-yTtR5XfI'

#Get's list of users playlists
def get_user_playlist_list():
    global response
    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_id)
    response = requests.get(query,
                            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
    response = response.json()
    return response

playlist_list = get_user_playlist_list()
playlist_list_access = playlist_list["items"]

#Get's users selected playlists
def get_playlist_choices():
    user_input = input("Enter playlist name: ")
    playlist_choices = user_input.split(", ")
    playlist_ids = []
    for playlist in playlist_list_access:
        for choice in playlist_choices:
            if playlist['name'].lower() == choice.lower():
                playlist_ids.append(playlist["id"])
            else:
                pass
    return playlist_ids

user_playlist_choices = get_playlist_choices()

# Get's all songs within selected playlists and stores within dictionary
def find_songs():
    dj_tracks_list = []
    n = 3
    track_uris = {}
    for playlist_id in user_playlist_choices:
        track_uris[playlist_id] = []
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(ACCESS_TOKEN)})

        response_json = response.json()

        for i in response_json["items"]:
            track_uris[playlist_id].append(i["track"]["uri"])
    return track_uris

user_choices_songs = find_songs()

songs_dicts = user_choices_songs.values()

songs_list = list(songs_dicts)

""" Step 3 """
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
    


