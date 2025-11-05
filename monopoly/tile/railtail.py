from monopoly.tile.tile import *
class PropertyTile(Tail):
    def __init__(self,name,type,price,rent):
        super().__init__(name,type)
        self.price = price
        self.rent = rent
        self.available = True

    def print(self):
        super().print(),print(f"the price is {self.price}\nthe rent is {self.rent}")

    def get_available(self):
        return self.available

    def set_available(self,bol):
        self.available = bol