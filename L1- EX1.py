#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:18:30 2023

@author: lydiacrompton
"""


##EXERCISE 1: code one variable for 1 neuron

#Code a neuron model variable (membrane potential) in a Main
#2 Declare the type of the variable
#3 Initialize membrane potential value
#4 Compute only one change of membrane potential value
#5 Print this value
#6 Comment each line. Comments are very important for you (you will forget your code) and others (they will hardly understand it)



def main():
    ## Initialize neuron membrane potential in units milliVolts
    V_membrane = float(-75)
    ## update neuron membrane potential 
    V_membrane = V_membrane + 1
    print(V_membrane)    

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
