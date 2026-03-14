
from player import Player

def main():
    print("--- Coin Match Game ---")
    player1 = Player("P 1") 
    player2 = Player("P 2")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")

    while(True):
        if(input("Keep playing? y/n ")=='n'):
            break
        else:

            
            player1.toss_coin()
            player2.toss_coin()
            print(f"{player1.get_name()} tossed {player1.get_coin_side()}")
            print(f"{player2.get_name()} tossed {player2.get_coin_side()}")

            if(player1.get_coin_side()!=player2.get_coin_side()):
                print(f"No match!{player2.get_name()} won!")
                player1.lose_coin()
                player2.win_coin()
            else:
                print(f"Coins matched! {player1.get_name()} won!")
                player1.win_coin()
                player2.lose_coin()

            print(f"{player1.get_name()} has {player1.get_wallet()} coins")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins")




main()