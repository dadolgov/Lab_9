"""
PLayer class

"""

from coin import Coin

class Player:
    def __init__(self, name:str):
        self.__name:str=name
        self.__wallet:int=20
        self.__coin=Coin()
    
    def toss_coin(self):
         return self.__coin.toss()
    
    def get_coin_side(self):
        return self.__coin.get_sideup()
    
    def win_coin(self):
        self.__wallet+=1
    
    def lose_coin(self):
        self.__wallet-=1
    
    def get_wallet(self):
        return self.__wallet
    
    def get_name(self):
        return self.__name