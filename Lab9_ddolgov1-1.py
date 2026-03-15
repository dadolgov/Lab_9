
from player import Player

def main():
    """Main file of Coin game. COntains main gameplay loop.
    Two players are tossing the coins. If both coins match, player 1 wins a coin, player 2 loses.
    If there's no match, player 2 wins, player 1 loses the coin.
    The player who runs out of coins, loses.
    Press y/n to keep or stop playing.
    If players choose to end the game, the final score is shown and 
    the player with highest coin count wins.
    """
    #intro screen and names input
    print("--- Coin Match Game ---")
    p1_name: str = input("Enter name for Player 1: ")
    p2_name: str = input("Enter name for Player 2: ")
    player1: Player = Player(p1_name) 
    player2: Player = Player(p2_name)
    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")
    print("-----------------------")
    #main gameplay loop
    while(True):
        #Gameover check for player 1
        if(player1.get_wallet()==0):
            print(f"{player1.get_name()} is out of coins! {player2.get_name()} is won!")
            break
        #Gameover check for player 2
        if(player2.get_wallet()==0):
            print(f"{player2.get_name()} is out of coins! {player1.get_name()} is won!")
            break
        #asking players to continue playing, 'y' to continue, 'n' to quit
        #entering gibberish restarts the loop
        keep_playing:str = input("Keep playing? y/n ")
        #quit secreen. Final score and winner
        if keep_playing.lower() == 'n':
            print("--- Final Score ---")
            print(f"{player1.get_name()}: {player1.get_wallet()}")
            print(f"{player2.get_name()}: {player2.get_wallet()}")

            if(player1.get_wallet()>player2.get_wallet()):
                print(f"{player1.get_name()} won!")
            elif player2.get_wallet()>player1.get_wallet():
                print(f"{player2.get_name()} won!")
            else:
                print("It's a draw!")
            break
        #game screen
        elif keep_playing.lower()=="y":
            print("Tossing coins...")
            player1.toss_coin()
            player2.toss_coin()
            print(f"{player1.get_name()} tossed {player1.get_coin_side()}")
            print(f"{player2.get_name()} tossed {player2.get_coin_side()}")
            #chosing a winner
            if(player1.get_coin_side()!=player2.get_coin_side()):
                print(f"...No match! {player2.get_name()} won!")
                player1.lose_coin()
                player2.win_coin()
            else:
                print(f"...It's a match! {player1.get_name()} won!")
                player1.win_coin()
                player2.lose_coin()

            print()
            #current score after the toss
            print(f"{player1.get_name()} has {player1.get_wallet()} coins")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins")
            print("-----------------------")
        #keep the loop going untill 'y' or 'n' entered
        else:
            print("Invalid input! Try again.")
            continue
        
#program start
if __name__ == '__main__':
    main()