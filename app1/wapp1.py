import json
from difflib import get_close_matches

#stroing the entire contents of json into dictionary data
data = json.load(open("./data.json"))

def getUserInput(statement):
    return input(statement).lower()

def getDefinition(word):
    if (word in data):
        return data[word]
    else:
        print("No such word found, getting word recommendations...")
        maxrecommendations = 10
        listOfCloseMatches = get_close_matches(word, data.keys(), maxrecommendations)
        if (len(listOfCloseMatches) > 0):
            i = 0
            while (i < maxrecommendations and i < len(listOfCloseMatches)):
                assumedWord = listOfCloseMatches[i]
                binput = input("Did you meant " + assumedWord + " ? [y/N/x=exit]: ").lower()
                if (binput == 'x'):
                    return "Bye Bye"
                elif (binput == 'y'):
                    return data[assumedWord]
                else:
                    i += 1
            return("No more words, Bye Bye!")
        else:
            return "Word doesn't exist"

userInputWord = getUserInput("Enter a word: ")

print(getDefinition(userInputWord))

