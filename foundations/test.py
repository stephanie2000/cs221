import collections
import math
import random


"""
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
"""



#text=""
#text="a"
#text="aa"
#text="ab"
text = "animal"

numChars = 2
length = 7
text=' '.join(chr(random.randint(ord('a'), ord('a') + numChars - 1)) for _ in range(length))
print text


def computePalindrome(c,lst):
    
    if len(lst) == 1: return 1

    #decide if length of substring defined by lst is even or odd
    sublst = c[lst[0]:lst[1]+1]
    if len(sublst) % 2 == 1:
        mid = len(sublst)/2 #middle index
        iterLen = mid - 1 #how many times to remove until we hit middle 
        for it in range(iterLen):
            if sublst != sublst[::-1]:
                #check to see if it is still symmetric
                if sublst[1+it] != sublst[-2+it]:
                    sublst.remove(sublst[1+it])
                    sublst.remove(sublst[-2-it])

        return len(sublst)

    else: #even
        iterLen = (len(sublst)/2) - 1
        for it in range(iterLen):
            if sublst != sublst[::-1]:
                #check to see if moving inward pairs are equal
                if sublst[1+it] != sublst[-2+it]:
                    sublst.remove(sublst[1+it])
                    #print sublst, sublst[-2+it-1], it
                    sublst.remove(sublst[-2-it])


        return len(sublst)

#get all the duplicates in the string
chars = list(text)
d = dict()
for i,c in enumerate(chars):
     if c not in d.keys():
         d[c] = list()
         d[c].append(i)
     else:
         d[c].append(i)
temp = d
for k in temp.keys():
    if len(d[k]) == 1:
        d.pop(k)

#for each possible pairs of indices that chars are duplicates at-compute their palindrome
#between these pairs
#this is because palindromes need to be symmetric (have same beg. and end.)
lengths = list()
for k in d:
    for l in range(len(d[k])-1):
        i = d[k][l] #start of palindrome
        j = d[k][l + 1] #end of palindrome
        #compute palindrome for pair of indices
        lenPal = computePalindrome(chars,list([i,j]))
        lengths.append(lenPal)

#then take max of lengths to get max palindrome
print max(lengths)
