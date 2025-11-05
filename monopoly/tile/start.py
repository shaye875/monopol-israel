from monopoly.tile.tile import *
class Start(Tail):
    def add_bonus(self,player):
        player.price+=200
        print(f"you have {player.price}")