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
#sentence = 'the cat and the mouse'
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
    #text = list()
    indices = [j for j,x in enumerate(keys) if x ==last]#find location of next pair

    if len(text) == n: return text #if we are at length of sentence we are done

    text.append(first)
    if indices: 
        temp = list()
        for j in indices: #make a copy of the current sentence,before branching off 2 othr pairs
           temp = copy.copy(text)
           temp2 = addWords(pairs,text,j,n,keys)
           sentences.add(tuple(text))
           text = temp #return to copy of the sentence before it was completed
    elif not indices and len(text) == n - 1: 
        text.append(last)
        return text
    else:
        text = list()
        return text
   
        
sentences = set()
for i,pair in enumerate(pairs):
    w = list()
    addWords(pairs,w,i,n,keys)


#print s
sentences = [' '.join(map(str,list(x))) for x in sentences if len(x) == n ]
#for s in sentences:
#   print s
#print type(sentences)
#need to keep entire dictionary-and start at index i in dict in recursive call
#how to add mouse if its not seen in another key?
    



#RETURN A LIST FROM SET



