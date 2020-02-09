#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #maximum = max([arr[i][i]+arr[i][i+1]+arr[i][i+2]+arr[i+1][i+1]+arr[i+2][i]+arr[i+2][i+1]+arr[i+2][i+2] for i in range (0,4) ])

    temp = [[0] * 4]*4
    max_num = -999999
    for i in range (4):
        for j in range (4):
            temp[i][j] = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            print (temp[i][j])

            if temp [i][j] >= max_num:
                max_num = temp[i][j]
            

    #max_num = max(max(i) for i in temp)
    #print (max_num)
    return (max_num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
