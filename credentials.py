import configparser
import constants as c


class Credentials:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.spotify_api_client_id = self.config.get('api', c.SPOTIFY_API_CLIENT_ID)
        self.spotify_api_client_secret = self.config.get('api', c.SPOTIFY_API_CLIENT_SECRET)
        self.spotify_redirect_uri = self.config.get('api', c.SPOTIFY_REDIRECT_URI)
        self.original_playlist_id = self.config.get('app', c.ORIGINAL_PLAYLIST_ID)

