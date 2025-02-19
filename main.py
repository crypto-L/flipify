import sys
import credentials
import spotipy
import logging
import spotify_scopes as scopes
from spotipy.oauth2 import SpotifyOAuth
from domain.track import Track


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        stream=sys.stdout)

    creds = credentials.Credentials('config.ini')
    auth_manager = SpotifyOAuth(
        client_id=creds.spotify_api_client_id,
        client_secret=creds.spotify_api_client_secret,
        redirect_uri=creds.spotify_redirect_uri,
        scope=scopes.USER_LIBRARY_READ
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)

    total_tracks = sp.playlist(playlist_id=creds.original_playlist_id)['tracks']['total']
    logging.info(f"Total tracks to fetch: {total_tracks}")

    playlist = sp.playlist_items(playlist_id=creds.original_playlist_id,
                                 fields='items(track(name,id,is_playable)),next')

    fetched_count = 0
    tracks = []
    while True:
        new_tracks = [Track(**item['track']) for item in playlist['items'] if item.get('track')]
        tracks.extend(new_tracks)

        fetched_count += len(new_tracks)
        logging.info(f"Fetched {fetched_count}/{total_tracks} tracks...")

        if playlist['next']:
            playlist = sp.next(playlist)
        else:
            break


if __name__ == "__main__":
    main()
