class Player:
    def __init__(self,name,location,price):
        self.name = name
        self.location = location
        self.price = price
        self.property = []

    def take_price(self,amount):
        self.price-=amount
        print(f"you have {self.price}")

    def get_price(self,amount):
        self.price+=amount
        print(f"you have {self.price}")

    def move(self,num):
        self.location+=num

    def buynig(self,tile):
        self.property.append(tile)
        print(f"have:")
        for p in self.property:
            p.print()

