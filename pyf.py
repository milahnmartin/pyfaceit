import pyfaceit

class Data(pyfaceit.Pyfaceit):
    def __init__(self, pname) -> None:
        super().__init__(pname)




p_info = Data('Ultrafy')
print(p_info.player_stats_map('mirage'))