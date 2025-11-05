from monopoly.tile.tile import *
class JoToJailTile(Tail):
    pass

    def go_to_jail(self,board,player):
        for i,tile in enumerate(board.checkered):
            if tile.name == "jail":
                 player.location = i
        print("you into the jail")
