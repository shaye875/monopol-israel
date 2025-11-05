from random import choice

from monopoly.play.board import *
from monopoly.play.dice import *
from monopoly.play.player import *

class Game:
    @staticmethod
    def play():

     board = Board()
     board.create_board()

     player1 = Player("shaye",0,1500)
     player2 = Player("avi",0,1500)
     while True:
        print("the turb is",player1.name)
        input("print to drop the dice")
        dice = Dice()
        player1.move(dice.num())
        board.checkered[player1.location].print()
        if board.checkered[player1.location].type == "property" or board.checkered[player1.location].type == "rail":
            if board.checkered[player1.location].get_available() == True:

                choice = input("is available if you want to buy enter buy")
                if choice == "buy":
                    player1.take_price(board.checkered[player1.location].price)
                    player1.buynig(board.checkered[player1.location])
                    board.checkered[player1.location].set_available(False)
            else:
                for p in player2.property:
                    if p.name == board.checkered[player1.location].name:
                        print("its ",player2.name)
                        player1.take_price(int(p.rent))
                        player2.get_price(int(p.rent))
        elif board.checkered[player1.location].type == "tax":
            board.checkered[player1.location].take_tax(player1)
        elif board.checkered[player1.location].type == "bonus" or board.checkered[player1.location].type == "start":
            board.checkered[player1.location].add_bonus(player1)
        elif board.checkered[player1.location].type == "go_to_jail":
            board.checkered[player1.location].go_to_jail(board,player1)
        print("the turb is", player2.name)
        input("print to drop the dice")
        player2.move(dice.num())
        board.checkered[player2.location].print()
        if board.checkered[player2.location].type == "property" or board.checkered[player2.location].type == "rail":
            if board.checkered[player2.location].get_available() == True:

                choice = input("is available if you want to buy enter buy")
                if choice == "buy":
                    player2.take_price(board.checkered[player2.location].price)
                    player2.buynig(board.checkered[player2.location])
                    board.checkered[player2.location].set_available(False)
            else:
                for p in player1.property:
                    if p.name == board.checkered[player2.location].name:
                        print("its ", player1.name)
                        player2.take_price(int(p.rent))
                        player1.get_price(int(p.rent))
        elif board.checkered[player2.location].type == "tax":
            board.checkered[player2.location].take_tax(player2)
        elif board.checkered[player2.location].type == "bonus" or board.checkered[player2.location].type == "start":

            board.checkered[player2.location].add_bonus(player2)
        elif board.checkered[player2.location].type == "go_to_jail":
            board.checkered[player2.location].go_to_jail(board, player2)
        if player1.price <= 0:
            print(player2.name,"is won")
            break
        if player2.price <= 0:
            print(player1.name,"is won")
            break



