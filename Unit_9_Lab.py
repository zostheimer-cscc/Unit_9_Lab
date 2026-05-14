"""
Program Name: Unit_9_Lab

Author: Zachary Ostheimer

Purpose: This program has all the  game logic  for the coin toss

Starter Code: No starter code was used.

Date: 2026-05-13

"""

from Player import Player                           
 
def main():
    player1 = Player("Player 1")                   
    player2 = Player("Player 2")                   
 
    print("--- Coin Match Game ---")
    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")
 
    answer = input("\nDo you want to toss the coins? (y/n): ")  
 
    while answer == 'y' or answer == 'Y':
 
        print("\nTossing...")
 
        player1.toss_coin()                        
        player2.toss_coin()                         
 
        side1 = player1.get_coin_side()            
        side2 = player2.get_coin_side()            
 
        print(player1.get_name(), "tossed", side1)
        print(player2.get_name(), "tossed", side2)
 
        if side1 == side2:                          
            #both coins match
            player1.win_coin()                      
            #player 1 wins a coin
            player2.lose_coin()                     
            #player 2 loses a coin
            print("...It's a Match!", player1.get_name(), "wins a coin.")
        else:                                       
            #coins do not match
            player2.win_coin()                      
            #player 2 wins a coin
            player1.lose_coin()                     
            #player 1 loses a coin
            print("...No Match!", player2.get_name(), "wins a coin.")
 
        print()
        print(player1.get_name(), "has", player1.get_wallet(), "coins.")
        print(player2.get_name(), "has", player2.get_wallet(), "coins.")
 
        if player1.get_wallet() == 0:               
            #check if player 1 is out of coins
            print("\nGame Over!", player1.get_name(), "has run out of coins!")
            break
 
        if player2.get_wallet() == 0:               
            #check if player 2 is out of coins
            print("\nGame Over!", player2.get_name(), "has run out of coins!")
            break
 
        answer = input("\nDo you want to toss the coins? (y/n): ")  
        #ask to play again
 
    print("\n--- Final Score ---")
    print(player1.get_name() + ":", player1.get_wallet())   
    #show player 1 total
    print(player2.get_name() + ":", player2.get_wallet())   
    #show player 2 total
 
    if player1.get_wallet() > player2.get_wallet():         
        #compare wallets
        print(player1.get_name(), "wins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(player2.get_name(), "wins!")
    else:
        print("It's a draw!")                       
        #equal coins means a tie
 
 
if __name__ == '__main__':
    main()                                          