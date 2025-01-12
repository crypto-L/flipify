import os
import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def main():
    os.environ['SPOTIFY_API_CLIENT_ID'] = '-'
    os.environ['SPOTIFY_API_CLIENT_SECRET'] = '-'
    os.environ['SPOTIFY_REDIRECT_URI'] = '-'

    creds = config.get_spotify_credentials()
    scope = "user-library-read"

    auth_manager = SpotifyOAuth(
        client_id=creds.get('CLIENT_ID'),
        client_secret=creds.get('CLIENT_SECRET'),
        redirect_uri=creds.get('REDIRECT_URI'),
        scope=scope
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlist = sp.playlist_items(playlist_id='-',
                                 fields='items(track(name,id)),next')

    while playlist['next']:
        print(playlist)
        playlist = sp.next(playlist)


if __name__ == "__main__":
    main()
