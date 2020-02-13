#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

# Complete the countTriplets function below.
def countTriplets(arr, r):

    tuple2 = Counter()
    tuple3 = Counter()

    print ("t2",tuple2)
    print ("t3",tuple3)

    count = 0

    for i in arr:
        count += tuple3[i]
        
        tuple3[i * r] += tuple2[i]
        
        tuple2[i * r] += 1
        

    return count 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
