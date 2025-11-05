from monopoly.data import *
from monopoly.tile.taxtile import *
from monopoly.tile.jailtail import *
from monopoly.tile.railtail import *
from monopoly.tile.bonustail import *
from monopoly.tile.gotojailtail import *
from monopoly.tile.propertytile import *
from monopoly.tile.start import *
class Board:
    def __init__(self):
        self.checkered = []

    def create_board(self):
        for t in tiles_data:
            if t["type"] == "property" and t["city"] != None:
                tile = PropertyTail(t["name"],t["type"],t["price"],t["rent"],t["city"])
            elif t["type"] == "tax":
                tile = TaxTile(t["name"],t["type"],t["amount"])
            elif t["type"] == "bonus":
                tile = BonusTile(t["name"],t["type"],t["amount"])
            elif t["type"] == "property":
                tile = PropertyTile(t["name"],"rail",t["price"],t["rent"])
            elif t["type"] == "go_to_jail":
                tile = JoToJailTile(t["name"],t["type"])
            elif t["type"] == "jail":
                tile = JailTile(t["name"],t["type"])
            elif t["type"] == "start":
                tile = Start(t["name"],t["type"])

            self.checkered.append(tile)

    def print_boatd(self):
        i = 1
        for tile in self.checkered:
            print(i)
            tile.print()
            i+=1
