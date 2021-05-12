from random import randint
from Player import Player

class RandomPlayerJV(Player):

    def __init__(self):
        self.count = -1

    def name(self):
        return "Random JV"

    def move(self, player_code, board):
        self.count += 3
        return self.count
