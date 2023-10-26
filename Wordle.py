
# find optimal first word for wordle
#https://github.com/dwyl/english-words/blob/master/words.txt
import pprint

with open(r"C:\Users\cathr\Documents\corncob_lowercase.txt", "r") as foWrdList:
    content = foWrdList.read()

#print (content[:100]) #prints the first 100 characters

wrdList = content.split("\n")
#print (wrdList[:100])
wrdListShort = [x for x in wrdList if len(x) == 5]
specialCharacters = ("[@_!#$%^&*()<>?/|}{~:].'")
#print (wrdListShort[:100])
#wrdLlistShortNormal = [x for x in wrdListShort if specialCharacters not in x]

# for each item in list compare to specialCharacters
# if in string - append to new list

wrdListShortNormal = []

for strWord in wrdListShort:
    booleanNotSpecial = True
    
    for strChar in strWord:

        if strChar in specialCharacters:
            
            booleanNotSpecial = False     
            
    if booleanNotSpecial == True:
        wrdListShortNormal.append(strWord)

numList = len(wrdListShortNormal)
numListlong = len(wrdList)
print(numListlong)
print(numList)
print (wrdListShortNormal)

"""if "resup" in wrdListShortNormal:
    print("Yeah it fucking is, bitch")"""


with open (r"C:\Users\cathr\Documents\wordlelist.txt", "w") as f:
    for item in wrdListShortNormal:
        f.write("%s\n" % item)
