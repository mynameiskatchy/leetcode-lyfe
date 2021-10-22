#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'prison' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY h
#  4. INTEGER_ARRAY v
#

def prison(n, m, h, v):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    h_count = int(input().strip())

    h = []

    for _ in range(h_count):
        h_item = int(input().strip())
        h.append(h_item)

    v_count = int(input().strip())

    v = []

    for _ in range(v_count):
        v_item = int(input().strip())
        v.append(v_item)

    result = prison(n, m, h, v)

    fptr.write(str(result) + '\n')

    fptr.close()
