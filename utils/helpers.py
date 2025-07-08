#spotify authentication
#get top tracks max 20
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pandas as pd


# Load environment variables from .env file
load_dotenv()

# Function to authenticate with Spotify using Spotipy

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="user-top-read"
    ))
    return sp


# Function to get the user's top tracks
def get_top_tracks(sp, limit=20):
    results = sp.current_user_top_tracks(limit=limit)
    top_tracks = []
    for item in results['items']:
        track_info = {
            'name': item['name'],
            'artist': ', '.join([artist['name'] for artist in item['artists']]),
            'album': item['album']['name'],
            'url': item['external_urls']['spotify'],
            'popularity': item['popularity'],
            'duration_ms': item['duration_ms'],
            'image': item['album']['images'][0]['url'] if item['album']['images'] else None,
        }
        top_tracks.append(track_info)
        # Fetch audio features for the track
    
    # Convert the list of dictionaries to a DataFrame
    return pd.DataFrame(top_tracks)
