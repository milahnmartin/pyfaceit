import requests


class Pyfaceit:
    '''This Class Will Contain all Methods to retrieve player information from faceit,
        this including specific data from specific maps, the methods will respond in Python dict.'''

    def __init__(self,API_KEY, pname: str) -> None:
        self.api_key = API_KEY
        self.pname = pname
        self._player_id = None
        self.game_id = "csgo"
        self.api_header = {
            "Authorization": "Bearer "+self.api_key,
            "content-type": "application/json"}

    @property
    def player_id(self) -> str:
        '''Method returns faceit player id that will be usefull and is needed
            when working with the other methods.'''
        try:
            player_id_request = requests.get(
                f"https://open.faceit.com/data/v4/players?nickname={self.pname}&game=CSGO",
                headers=self.api_header)
            player_id_data = player_id_request.json()
            player_id = player_id_data["player_id"]
            return player_id
        except KeyError as error:
            raise KeyError from error

    @player_id.setter
    def player_id(self) -> None:
        self._player_id = self.player_id

    def player_information(self) -> dict:
        '''This method returns information that the Faciet API requires for players,
            Developers would hardly use this method and ismostly used as a private method
            inside the Pyfaceit class to retrieve other data'''
        try:
            if self.player_id is None:
                raise Exception('Player does not exist')
            player_data = requests.get(
                f"https://open.faceit.com/data/v4/players/{self.player_id}",
                headers=self.api_header)
            player_data_json = player_data.json()
            return player_data_json
        except KeyError as error:
            raise KeyError from error

    def player_stats(self) -> dict:
        '''This method returns All PLayer faceit data incoluding all map information in a
            python dict.This method uses the player_id method to retrieve all data from the
            faceit api.'''
        try:
            player_stats_request = requests.get(
                f'https://open.faceit.com/data/v4/players/{self.player_id}/stats/{self.game_id}',
                headers=self.api_header)
            player_stats_json = player_stats_request.json()
            return player_stats_json
        except KeyError as error:
            raise KeyError from error

    def player_stats_map(self, pmap: str) -> dict:
        '''Method Returns Python dict containing information
            For specific map'''
        if '_' not in pmap:
            pmap = 'de_' + pmap

        pdata = self.player_stats()
        map_data = pdata['segments']
        for maps in map_data:
            if maps['label'] == pmap:
                return maps
        return {}
