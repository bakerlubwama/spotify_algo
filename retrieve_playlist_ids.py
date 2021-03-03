"""
Step 1: Get a List of a User's Playlists API request

Step 2: Get user’s playlists choice (by name)
- Ask user to give us playlists (up to 3-5)
- Compare name with response from early step and retrieve desired playlist ids"""

import requests
import json

SPOTIFY_GET_USER_PLAYLIST_URL = 'https://api.spotify.com/v1/users/baker162589/playlists'
ACCESS_TOKEN = 'BQAFXVoG3xkxu09HNiPtwF3yrUvEIAO0HL_vl85azX7L9aDKFZ88rL3z2_lMdGFEuWbjrFtfbVI-QYjvA-qp1eBpyhDDvPlGqiyEtwpKCQ7eSNm21CSFykZ9F5fYM6oyFQOFTRBkGtOy9wHiTakx_lDY7pYOcErMHfVkPNySeoMzUh5MKwnUJcvCWtJZvd7i5TnGQsSCR7Uf_zQr0bDug1sc1uo'


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

playlist_list = get_user_playlist_list()
#print(json.dumps(playlist_list, indent=2))

def get_playlist_choices():
    user_input = input("Enter playlist name: ")
    playlist_ids = []
    for playlist in response:
        if playlist["name"].lower() == user_input.lower():
            playlist_ids.append(playlist["id"])
        else:
            pass
    return playlist_ids


bakers_choices = get_playlist_choices()
print(bakers_choices)