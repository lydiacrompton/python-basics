#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:22:06 2023

@author: lydiacrompton
"""

#EXERCISE 3: Neuron with I/O

#1 Using command line, make the argument of the Main receive a single spike value.
#2 Compute new membrane potential using the new spike value
#3 Output is the print of membrane potential value


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