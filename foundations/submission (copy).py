import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max([word.lower() for word in text.split()])     


    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
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
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)


    #NOTE: we form the sentence by ensuring the last part of a pair of words is the first
    #      part of another pair of words
    #####################################################
    # Takes in a list of pairs of words and returns a list that forms a sentence (similar)
    #
    # @param[in] pairs    Is a list containing a list of paired words.    
    # @param[in] text     Is a list containing words.
    # @param[in] i        An index to access next pair of words that follow last pair added.
    # @param[in] n        Length of original set of words in the original sentence.
    # @param[in] keys     A list containg the first part of all pairs of words.
    #
    # @return
    #
    # @pre @a pairs is a list of lists (pairs of words).
    # @pre @a i is an int.
    # @pre @a keys is a list.  
    #     
    def addWords(pairs,text,i,n,keys):
        first = pairs[i][0]
        last = pairs[i][1]
        indices = [j for j,x in enumerate(keys) if x ==last]#find location of next pair

        if len(text) == n: return text #if we are at length of sentence we are done

        text.append(first)
        if indices: 
            temp = list()
            for j in indices: #make a copy of the current sentence,before branching off
               temp = [t for t in text]
               temp2 = addWords(pairs,text,j,n,keys)
               sentences.add(tuple(text))
               text = temp #return to copy of the sentence before it was completed
        elif not indices and len(text) == n - 1: 
            text.append(last)
            sentences.add(tuple(text)) 
            return text
        else:
            text = list()
            return text
    ###################################################
    words = sentence.split() #split the string

    #make pairs of words (adjacent)
    pairs = list()   
    keys = list() #hold on to first half of pairs
    for i in range(len(words)-1):
        pair = [words[i],words[i+1]]
        keys.append(words[i])
        pairs.append(pair)

    n=len(words)
        
    sentences = set() #don't want duplicates
    for i,pair in enumerate(pairs): #create sent. for each pair in orig sent. 
        w = list()
        addWords(pairs,w,i,n,keys) #use recursion

    #get rid of any short sentences that made it
    sentences = [' '.join(map(str,list(x))) for x in sentences if len(x) == n ]
    return sentences
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collection.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)

    #since we have sparse vectors-we only care about common nonzero elements
    v1_int_v2 = list(set(v1.keys()).intersection(set(v2.keys()))) #get intersection of keys
    lst = list()
    for e in v1_int_v2:
        lst.append(v1[e]*v2[e])

    return sum(lst)
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    v1_int_v2 = list(set(v1.keys()).intersection(set(v2.keys()))) #get intersection of keys
    not_int = list(set(v1_int_v2) - set(v2.keys())) #not in intersection 
    if not not_int:  not_int = list(set(v2.keys())-set(v1_int_v2))
    for k in v2.keys(): v2[k] = scale*v2[k]
    for e in v1_int_v2: v1[e] = v1[e]+v2[e]
    for e in not_int: v1[e] = v2[e]

    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    d = collections.defaultdict(int)
    for w in text.split():
        if w in d.keys():
            d[w]+=1
        if w not in d.keys():
            d[w] = 1
        if d[w] > 1:
            d.pop(w)

    return set(d.keys())

    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    def computePalindrome(c,lst):

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
                        sublst.remove(sublst[-2-it])


            return len(sublst)

    if text == text[::-1]: return len(text)
    if len(text) == 0: return 0
    if len(text) == 2 and text != text[::-1]: return 1;
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
    return max(lengths)
    # END_YOUR_CODE
