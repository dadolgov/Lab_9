"""Coin class. 
Contains state info for the coin and necessary methods for gameplay.
Author: Dmitrii Dolgov
3/15/2026
"""
import random

class Coin:
    """Represents a coin from the player's wallet.

    Attributes:
        __sideup (str): Tells wich side of a coin is up, Heads or Tails
    """
    def __init__(self) -> None:
        self.__sideup=self.toss()  #randomized initial state
    
    def toss(self)->None:
        """Flips the coin, andomly assigning Heads or Tails to __sideup
        """
        if random.randint(0, 1) == 1:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self) -> str:
        """Returns the state of the coin.

        Returns:
            str: The upside of a coin, Heads or Tails
        """
        return self.__sideup
