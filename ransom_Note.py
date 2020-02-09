#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #print (magazine, note)
    #print (set(note).intersection(magazine))
    #print (len(note))
    #print (len(list(set(note).intersection(magazine))))

    '''if (len(list(set(note).intersection(magazine)))) == len(note):
        print ("Yes")
    else:
        print ("No")'''

    word_counts = Counter(magazine)
    for word in note:
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            print ("No")
            return 
    print ("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
