"""
Coin class, contains info and methods about the coin in the game
"""
import random

class Coin:
    def __init__(self, sideup:str)->None:
        self.__sideup=sideup
    
    def toss(self)->None:
        if random.randint(0,1)==1:
            self.__sideup="Heads"
        else:
            self.__sideup="Tails"


    def get_sideup(self)->str:
        return self.__sideup
