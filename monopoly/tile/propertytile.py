from monopoly.tile.tile import *
class PropertyTail(Tail):
    def __init__(self,name,type,price,rent,city):
        super().__init__(name,type)
        self.price = price
        self.rent = rent
        self.city = city
        self.available = True

    def print(self):
        super().print(),print(f"the price is {self.price}\nthe rent is {self.rent}\nthe city is {self.city}")

    def get_available(self):
        return self.available

    def set_available(self,bol):
        self.available = bol





