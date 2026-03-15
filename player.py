
from coin import Coin

class Player:
    """Represents the player and the necessary properties to play the coin game.
    Attributes:
        __name (str): Player's name
        __wallet (str): Player's wallet. Initially contains 20 coins
        __coin (Coin): inherited Coin instance
    """
    def __init__(self, name:str):
        self.__name:str=name
        self.__wallet:int=20
        self.__coin=Coin()
    
    def toss_coin(self):
        """Tosses the coin, using the inherited Coin instance.
        """
        self.__coin.toss()
    
    def get_coin_side(self):
        """Gets the coin upside, Heads or tails 

        Returns:
            str: coin upside, Heads or Tails
        """
        return self.__coin.get_sideup()
    
    def win_coin(self):
        """Increases Player's coin count by 1
        """
        self.__wallet+=1
    
    def lose_coin(self):
        """Decreases Player's coin count by 1
        """
        self.__wallet-=1
    
    def get_wallet(self):
        """Gets the wallet ballance

        Returns:
            int: ammount of coins in Player's wallet
        """
        return self.__wallet
    
    def get_name(self):
        """Get's the Player's name

        Returns:
            str: Player's name
        """
        return self.__name