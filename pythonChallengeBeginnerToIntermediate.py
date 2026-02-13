import string 

## Beginner 1

# score = int(input("What score did you get (be honest)? "))
# score = int(score/50)
# match score:
#     case 0:
#         print("Failed")
#     case 1:
#         print("Passed")

## Beginner 2

# score = int(input("Input Number "))
# score = int(score%2)
# print(score)
# match score:
#     case 0:
#         print("Even")
#     case 1:
#         print("Odd")

## Beginner 3

# print(sum([int(x) for x in input("Write your list, comma separated: ") if x != ',' and x != ' ']))

## Intermediate 1

# text = input("Write the text to sort here: ")
# k = int(input("Number of top frequency words: "))
# wordList = []
# temp = ''

# for x in text.lower(): #creates list of words excl. punctuation
#     if x in string.ascii_lowercase or x == '\'' :
#         temp = temp + x
#     elif temp != '':
#         wordList.append(temp)
#         temp = ''
# wordList.append(temp) 
# wordList = [x for x in wordList if x != '']
# freq = []
# for x in wordList:
#      freq.append((x, wordList.count(x))) #creates ist of tuples w/ freq of word next to it
# freq = sorted(list(set(freq)), key=lambda x : x[1], reverse=True)[0:k] # sorts by frequency
# print(freq)

## Intermediate 2. Warning, very bad code below!!

temp = ''
wordList = []
text = input("Write the text w/ anagrams here: ")

for x in text.lower(): #creates list of words excl. punctuation
    if x in string.ascii_lowercase or x == '\'' :
        temp = temp + x
    elif temp != '':
        wordList.append(temp)
        temp = ''
wordList.append(temp) 

anagramCheck = [sorted(x) for x in wordList] #sorts words to check for anagrams
result = []
print(anagramCheck)
ind = [[i for i in range(len(anagramCheck)) if anagramCheck[i] == anagramCheck[x]] for x in range(len(anagramCheck))] #checks the words duplicates and gives index of anagrams
duplicateList = [[(wordList[x]) for x in ind[i]] for i in range(len(ind))] #makes a list full of duplicates (i was stuck trying to avoid it on the same line of code but fix it on the next line instead)
[result.append(x) for x in duplicateList if x not in result] # fixes duplicates
print(result)

