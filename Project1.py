import json
from difflib import SequenceMatcher

# Dictionary
data = json.load(open("/mnt/Sourabh/My Projects/Python/Project1/data.json", "r"))


def search(word):
    word = word.lower()
    if word in data:
        definition = data[str(word)]
        for define in definition:
            print(define)
    else:
        max = 0
        value = ''
        for key in data:
            if SequenceMatcher(None, word, key).ratio() > max:
                max = SequenceMatcher(None, word, key).ratio()
                value = key
        if max > 0.7:
            print("Did you meant " + value)
            reply = input("y or n: ").lower()
            if reply == "y" or reply == "yes":
                definition = data[str(value)]
                for define in definition:
                    print(define)
            elif reply == 'n' or reply == 'no':
                print("Sorry , We Didn't recognised your word")
        else:
            print("Word not found, Try Something else")


while True:
    searchKey = input("Enter a word to Search: ")
    if searchKey == 'exit':
        break
    else:
        search(searchKey)

print("ThankYou for using my Dictionary")
