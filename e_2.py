#!/usr/bin/env python 
"""
#---
 Advansee
 jlengrand
 Created on : Wed Jan 11 14:42:54 CET 2012

 DESCRIPTION : Solves problem 2 of Project Euler
 Each new term in the Fibonacci sequence is generated by adding the previous 
 two terms. By starting with 1 and 2, the first 10 terms will be:

 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

 By considering the terms in the Fibonacci sequence whose values do not exceed
 four million, find the sum of the even-valued terms.
#---
"""

def even_sum_fib(max_value):
    """
    Sums up all even-valued elements of the Fibonacci sequence whose 
    """
    last_val = 0
    val = 1 # Fibonacci starts with 1
    fib_sum = 0

    while (val <= max_value):
        if (val % 2) == 0:
            fib_sum += val
        
        temp = val
        val += last_val
        last_val = temp
        
    return fib_sum
    
    
    
if __name__ == '__main__':
    val = 4000000
    print "Answer : %d " % (even_sum_fib(val))                        
