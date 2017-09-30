import collections
import math
import random
from itertools import permutations
import copy

"""
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """

#1. must have same amount of words, n = amnt of words
#2. there are n - 1 pairs of words
#3. the end of one pair must be equal to the start of another pair-follows 4.
#4. words in the second spot of the pairs that do not appear as keys in the dict have to go at the end of the sentence - if it needs to make n words
sentence = 'the cat and the mouse'
unique = ['cat','and','mouse']
words = sentence.split()

#make a dictionary of adjacent words
d = dict()
for i in range(len(words)-1):
    if words[i] not in d.keys():
        d[words[i]] = list()
    if words[i] in d.keys():
        d[words[i]].append(words[i+1])
    
#create list to hold d.keys() permutes
keys = d.keys()


#perm_keys = list(permutations(keys))

#pairs = list()
#for i in range(len(words)-1):
#    pair = [words[i],words[i+1]]
#    pairs.append(pair)

#print pairs
lst=list()
text=list()
n=len(words)
def addWords(d,c,text,n):
    if len(text)==n: 
        return text

    if len(text)!=n:
        for i,k in enumerate(c):
            for l in c[k]:
                if l in d.keys():
                    c = copy.copy(d)
		    c.pop(k)
                    text.append(k)
                    lst.append(addWords(d,c,text,n)) #add new sentence
                if l not in d.keys() and text == n-1:
                    text.append(l)
                    lst.append(text)

addWords(d,copy.copy(d),text,n)
print lst
#need to keep entire dictionary-and start at index i in dict in recursive call
#how to add mouse if its not seen in another key?
    



#RETURN A LIST FROM SET



