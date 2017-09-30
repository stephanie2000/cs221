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

words = sentence.split()

pairs = list()
for i in range(len(words)-1):
    pair = [words[i],words[i+1]]
    pairs.append(pair)

print pairs



sentence = 'a a a a a'
words = sentence.split()

#make a dictionary of adjacent words
d = dict()
for i in range(len(words)-1):
    if words[i] not in d.keys():
        d[words[i]] = list()
    if words[i] in d.keys():
        d[words[i]].append(words[i+1])


print d
s = set()
n=len(words)

def addWords(d,text,k,n):

    if len(text)==n:
        return text

    for l in d[k]:  #go through each pair per key
        if l not in d.keys() and text == n-1:
            text.append(l)
            return text
        if l in d.keys(): #if the value of the key is also a key, jump to it
            text.append(k) #add the current key 
            addWords(d,text,l,n)
        

for i,k in enumerate(d):
    text=list()
    #test= addWords(d,text,k,n)
    s.add(tuple(text))
    print text


print list(s)
###################33
sentence = 'the cat and the mouse'
words = sentence.split()

#make pairs of words (adjacent)
pairs = list()
keys = list()
for i in range(len(words)-1):
    pair = [words[i],words[i+1]]
    keys.append(words[i])
    pairs.append(pair)


s = set()
n=len(words)

def addWords(pairs,text,i,n,keys):
    first = pairs[i][0]
    last = pairs[i][1]
    if len(text)==n:
        return text
    elif last not in keys and len(text) == n-1:
        text.append(last)
        return text
    elif len(text)==n-1:
        return text.append(first)
    elif last in keys: #if the value of the key is also a key, jump to it
        text.append(first) #add the current key
        indices = [j for j,x in enumerate(keys) if x==last]#find location of next pair
        for j in indices:        
            return addWords(pairs,text,j,n,keys)
    else:
        return 0 #no sentence was formed (dead end)
        

for i,pair in enumerate(pairs):
    text = list()
    addWords(pairs,text,i,n,keys)
    s.add(tuple(text))
    print text

