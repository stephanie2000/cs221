import collections
import math
import random




numChars = 5
length = 400
text=' '.join(chr(random.randint(ord('a'), ord('a') + numChars - 1)) for _ in range(length))

def computePalLen(text,d):
    if(text in d):
	return d[text]
    if len(text)==0: return 0


    if text == text[::-1]: 
        d[text]=len(text)

    elif text[0] == text[-1]:
        d[text] = 2 + computePalLen(text[1:len(text)-1],d)
    else:
        d[text]= max(computePalLen(text[0:len(text)-1],d),computePalLen(text[1:len(text)],d))


    return d[text]


dictPal = dict()

print computePalLen(text,dictPal)

