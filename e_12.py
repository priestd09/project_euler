#!/usr/bin/env python 
"""
 ##---
 # Julien Lengrand
 #Created on : Sun Jan 15 22:35:08 CET 2012
 #
 # DESCRIPTION : Solves problem 12 of Project Euler
 The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
 Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
 10: 1,2,5,10
 15: 1,3,5,15
 21: 1,3,7,21
 28: 1,2,4,7,14,28
 We can see that 28 is the first triangle number to have over five divisors.
 What is the value of the first triangle number to have over five hundred divisors?
 
 FIXME : This solution is waaaaaay to long ! 
 ##---
"""
def triangle_divisors(div_number):
    """
    Returns the value of the first triangle number to have over div_number 
    divisors
    """
    val = 0
    inc = 0
    nb_div = 0
    while( nb_div <= div_number):
        inc += 1
        val += inc       
        nb_div = divisors(val)
            
    return val

def divisors(value):
    """
    Outputs the number of divisors of value
    """
    nb_div = 2
    for val in range(2, value ):
        if (value % val ==0):
            nb_div += 1

    return nb_div

if __name__ == '__main__':
    print "Answer : %d" % (triangle_divisors(500))