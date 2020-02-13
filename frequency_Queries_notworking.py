#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):

    dList = []
    returnArray = []

    print ("1",queries[0][0])
    print ("2",queries[1][0])
    print ("3",queries[2][0])
    print ("4",len(queries)-1)


    for i in range (0,(len(queries)-1)):
        print ("i",i)
        if queries[i][0] == 1:
            dList.append(queries[i][1])
            print (dList)
        elif queries[i][0] == 2 and queries[i][1] in dList:
            dList.remove(queries[i][1])
        elif queries[i][0] == 3 and len(dList) != 0:
            result = list(filter(lambda x: (x%queries[i][1] == 0), dList))
            print ("Result",result)
            if (len(result)) != 0:
                
                returnArray.append(1)
            else:
                returnArray.append(0) 
            result.clear() 


    return returnArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
