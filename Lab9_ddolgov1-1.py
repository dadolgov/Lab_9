
from player import Player

def main():
    print("--- Coin Match Game ---")
    p1_name: str = input("Enter name for Player 1: ")
    p2_name: str = input("Enter name for Player 2: ")
    player1 = Player(p1_name) 
    player2 = Player(p2_name)
    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")
    print("-----------------------")

    while(True):
        if(player1.get_wallet()==0):
            print(f"{player1.get_name()} is out of coins! {player2.get_name()} is won!")
            break
        if(player2.get_wallet()==0):
            print(f"{player2.get_name()} is out of coins! {player1.get_name()} is won!")
            break
        keep_playing:str = input("Keep playing? y/n ")
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
        elif keep_playing.lower()=="y":
            print("Tossing coins...")
            player1.toss_coin()
            player2.toss_coin()
            print(f"{player1.get_name()} tossed {player1.get_coin_side()}")
            print(f"{player2.get_name()} tossed {player2.get_coin_side()}")

            if(player1.get_coin_side()!=player2.get_coin_side()):
                print(f"...No match!{player2.get_name()} won!")
                player1.lose_coin()
                player2.win_coin()
            else:
                print(f"...It's a match! {player1.get_name()} won!")
                player1.win_coin()
                player2.lose_coin()

            print()
            print(f"{player1.get_name()} has {player1.get_wallet()} coins")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins")
            print("-----------------------")
        else:
            print("Wrong input! try again.")
            continue

if __name__ == '__main__':
    main()