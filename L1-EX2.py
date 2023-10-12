#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:31:13 2023

@author: lydiacrompton
"""

#EXERCISE 2: Variable types 

#Do not declare the type of the variable as in step 1 of exercise 1
#2 Initialize the variable with value 1. Using debugging, check what is the type of the variable.
#3 Compute the value of the variable multiplying it by 0.7. Using debugging, check what is the type of the variable. Did it change? Why? Add your answer in a comment
#4 Initialize the variable with value 1.0. Using debugging, check what is the type of the variable.

def main():
    var = 1
    ## Put a break point at the print statement and check the var type in debugger
    print(var)
    
    var = var * 0.7
    ## Put a break point at the print statement and check the var type in debugger
    print(var)
    
    var2 = 1.0
    ## Put a break point at the print statement and check the var type in debugger
    print(var2)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()