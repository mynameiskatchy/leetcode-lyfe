#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    def fizz(n):
        return n%3 == 0

    def buzz(n):
        return n%5 == 0

    for i in range(1, n+1):
        if fizz(i) and buzz(i):
            print("FizzBuzz")
        elif fizz(i):
            print("Fizz")
        elif buzz(i):
            print("Buzz")
        else:
            print(i)
    return None
    
if __name__ == '__main__':
    def fizz(n):
        return True if (n%3 ==0 and n%5 !=0) else False
    def buzz(n):
        return True if (n%5 ==0 and n%3 !=0) else False
    print(fizz(3), fizz(5), buzz(3), buzz(5), fizz(15), buzz(15))
    print(fizzBuzz(15))
