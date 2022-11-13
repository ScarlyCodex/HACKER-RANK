#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    #Initializing the class with the init_ constructor
    def __init__(self,total_items, item_coins):
        self.total_items = total_items
        self.item_coins = item_coins
        
    #Method buy with its respective parameters
    def buy(self, num_items, num_coins):
        #According the description of the problem, here is the formula
        fChange = num_coins - (num_items * item_coins)

        #This works as a counter, rItems stands for remaining Items in the machine\
        #after each request, the initializing starts at the moment of the first request
        rItems = total_items - num_items
        
        #Simple condition applying the formula above
        if fChange <= 0:
            return str("Not enough coins")  

        #Another condition using our counter
        #Which, in fact, will not take the value from 0 onwards due to the nature \
        #of the iteration
        elif rItems == 0:
            return str("Not enough items in the machine")

        #Just passing the final Change 
        else:
            return fChange
    
if __name__ == '__main__':
    fptr = open(os.environ('[OS_PATH]'), 'w')

    total_items, item_coins = map(int, input().split())
    machine = VendingMachine(total_items, item_coins)

    n = int(input())
    
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            #Calling metho buy with these arguments
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")
            
    fptr.close()
