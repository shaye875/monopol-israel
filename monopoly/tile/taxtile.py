from monopoly.tile.tile import *
class TaxTile(Tail):
    def __init__(self,name,type,amount):
        super().__init__(name,type)
        self.amount = amount

    def print(self):
        super().print(),print(f"the amount is {self.amount}")

    def take_tax(self,player):
        player.price-=self.amount
        print(f"you have {player.price}")
