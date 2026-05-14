"""
Program Name: Unit_9_Lab

Author: Zachary Ostheimer

Purpose: This program has all the m player logic

Starter Code: No starter code was used.

Date: 2026-05-13

"""

from coin import Coin                               

class Player:
 
    def __init__(self, name):
        self.__name = name                          
        #store the player name
        self.__wallet = 20                          
        #every player starts with 20 coins
        self.__coin = Coin()                        
      
 
    def toss_coin(self):
        self.__coin.toss()                         
        #flips coin
 
    def get_coin_side(self):
        return self.__coin.get_sideup()             
        #ask the coin which side is up and return it
 
    def win_coin(self):
        self.__wallet += 1                         
         #add 1 coin to  wallet
 
    def lose_coin(self):
        self.__wallet -= 1                         
         #remove 1 coin from wallet
 
    def get_wallet(self):
        return self.__wallet                        
        #return  current coin count
 
    def get_name(self):
        return self.__name                          
        #return player's name