#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cardPackets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY cardTypes as parameter.
#

# Cards w sports figures on them

# Each sport has diff categories of cards
# desireable cards w most popular sports personalities
# small pieces of a player's jersey attached

# Number of each category of card

# Want to make some number of packets
# Want to make some number of packets
# Contain equal numbers of any type of card

# Add more cards of each type until each can be divided equallu among number of packets.

# determine number of additional cards needed to create a number of packets with equal type distrubition

def cardPackets(cardTypes):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cardTypes_count = int(input().strip())

    cardTypes = []

    for _ in range(cardTypes_count):
        cardTypes_item = int(input().strip())
        cardTypes.append(cardTypes_item)

    result = cardPackets(cardTypes)

    fptr.write(str(result) + '\n')

    fptr.close()