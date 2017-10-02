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
#text = "abcabaa"

numChars = 10
length = 10
text=' '.join(chr(random.randint(ord('a'), ord('a') + numChars - 1)) for _ in range(length))
print text


def computePalindrome(c,lst,i):

    if len(c) == 0:
            lengths.append(0)
            return 1
    for l in range(len(lst)): #iterate through each pair starting from i
        #decide if length of substring defined by lst is even or odd
        sublst = c[i:lst[l]] #add an additional 1 due to list slicing
        if sublst == sublst[::-1]:
            lengths.append(len(sublst))
            break
        if len(sublst)==3 or len(sublst)==2:
            lengths.append(1)
            break
        iterLen = (len(sublst)/2) - 1 
        #print iterLen
        for it in range(iterLen):
            print iterLen, it, sublst
            if it > (iterLen-1): break
            if sublst != sublst[::-1]:
                #check to see if it is still symmetric
                #print sublst, "-",1+it,"-",-2-it,"-",-2+it, "IT: ",it,"ITER ", iterLen
                if sublst[1+it] != sublst[-2-it]:
                    temp = list()
                    temp = [x for x in sublst]
                    temp.pop(1+it)
	            computePalindrome(temp,[len(temp)],0) # it is now an even case
                    temp =  [x for x in sublst]
                    #print -2-it, " ", temp
                    temp.pop(-2-it)
                    computePalindrome(temp,[len(temp)],0) # it is now an even case
                   # print sublst," ",sublst[1+it], "-",sublst[-2+it]
                    sublst.pop(-2-it)
                    sublst.pop(1+it)
                    #print sublst



def dups(t):
    #get all the duplicates in the string
    c = list(t)
    d = dict()
    for i,c in enumerate(c):
        if c not in d.keys():
             d[c] = list()
             d[c].append(i)
        else:
             d[c].append(i)
    temp = d
    for k in temp.keys():
        if len(d[k]) == 1:
            d.pop(k)
    return d

#for each possible pairs of indices that chars are duplicates at-compute their palindrome
#between these pairs
#this is because palindromes need to be symmetric (have same beg. and end.)
dupdict = dups(text)
chars = list(text)
lengths = list()

for k in dupdict:
    for l in range(len(dupdict[k])-1):
        temp = [x+1 for x in dupdict[k][(l+1):]]
        computePalindrome(chars,temp,dupdict[k][l])


#then take max of lengths to get max palindrome
print max(lengths)

