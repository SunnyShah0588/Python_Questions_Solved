'''Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat". "atco cta". etc.) '''
from collections import Counter

s = "TactCj"

string =s.replace(" ","")
string = string.lower()

print (string)
p = Counter(string)
length = len(string)
odd = 1

for i in p:
    if p[i] % 2 == 0:
        length -= 2
    elif p[i] % 2 != 0:
        length -= p[i]
        odd -= 1
        
if odd < 0:
    print ("NO")
else:
    print ("Yes")
