import requests
class Pyfaceit:

    

    def __init__(self,pname) -> None:
        self.pname = pname
        self._player_id = None
        self.game_id = "csgo"
        self.api_header = {"Authorization":"Bearer " + '3b5a9d07-4b77-4be4-bf5d-f9ff3d6cb7b6',"content-type": "application/json"}
    
    
    @property
    def player_id(self) -> str | int | None:
        try:
            player_id_request = requests.get(f"https://open.faceit.com/data/v4/players?nickname={self.pname}&game=CSGO",headers=self.api_header)
            player_id_data = player_id_request.json()
            player_id = player_id_data["player_id"]
            return player_id
        except KeyError:
            print('Error Occured',self.pname,'doesnt exist')
            return None
        
    @player_id.setter
    def player_id(self) -> None:
        self._player_id = self.player_id
    

    def player_information(self) -> dict:
        try:
            if self.player_id is None:
                raise Exception('Player does not exist')
            player_data = requests.get(f"https://open.faceit.com/data/v4/players/{self.player_id}",headers=self.api_header)
            player_data_json = player_data.json()
            return player_data_json
        except Exception:
            return None
    
    def player_stats(self) -> dict:
        try:
            player_stats_request = requests.get(f'https://open.faceit.com/data/v4/players/{self.player_id}/stats/{self.game_id}',headers=self.api_header)
            player_stats_json = player_stats_request.json()
            return player_stats_json
        except Exception:
            return None
    
    def player_stats_map(self,pmap) -> dict:
        if '_' not in pmap:
            pmap = 'de_' + pmap
        
        try:
            pdata = self.player_stats()
            map_data = pdata['segments']
            for map in map_data:
                if map['label'] == pmap:
                    return map

        except Exception:
            return None