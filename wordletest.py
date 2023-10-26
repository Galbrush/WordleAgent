#dis ma try to find the perfect wordle world mofos
import string
import pprint
import operator

foWordleList = open("wordlelist.txt", "r")
strWordleList = foWordleList.read()
strWordleListSplit = strWordleList.split("\n")
myDickLetters = {}
myDickWords = {}

def check_double_letters(string):
    doubles = []
    for l in string:
        if string.count(l) > 1:
            doubles.append(letter)
    
    if len(doubles) == 0:
        return True
    
    return False

#1st step: sort alphabet by frequency of use by adding values

alphabet = list(string.ascii_lowercase)
for letter in alphabet:
        
    letterValue = strWordleList.count(letter)
    myDickLetters[letter] = letterValue

#3rd step: calculate value of each word
for word in strWordleListSplit:
    wordvalue = 0
    for letter in word:
        wordvalue += myDickLetters[letter]
    myDickWords[word] = wordvalue

#4th step: eliminate double letters
for key in list(myDickWords.keys()):
    if check_double_letters(key) == True:
        del myDickWords[key]

pprint(myDickWords)
perfect_word = max(myDickWords.items(), key=operator.itemgetter(1))[0]

print(perfect_word)

