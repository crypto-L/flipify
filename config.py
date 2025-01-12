import os


def get_spotify_credentials():
    client_id = os.getenv('SPOTIFY_API_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_API_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

    if client_id is None or client_secret is None or redirect_uri is None:
        raise ValueError("One or more required environment variables are missing")

    return {
        "CLIENT_ID": client_id,
        "CLIENT_SECRET": client_secret,
        "REDIRECT_URI": redirect_uri
    }
