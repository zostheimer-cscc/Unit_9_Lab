"""
Program Name: Unit_9_Participation

Author: Zachary Ostheimer

Purpose: This program creates a Coin class to simuloate  flipping

Starter Code: No starter code was used.

Date: 2026-05-13

"""

import random
 
 
class Coin:
 
    def __init__(self):
        self.__sideup = 'Heads'                     
        #start the coin on heads by default
 
    def toss(self):
        number = random.randint(0, 1)               
        #pick a random 0 or 1
        if number == 0:
            self.__sideup = 'Heads'                 
            #0 means heads
        else:
            self.__sideup = 'Tails'                 
            #1 means tails
 
    def get_sideup(self):
        return self.__sideup                        
    #return whichever side is facing up
 