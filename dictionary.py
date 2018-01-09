#importing the libraries
import json
from difflib import get_close_matches

#creating a variable to load and open the json file
data = json.load(open("data.json"))

#program that takes the user input and converts it to lowercase. checks the input against the file, returns deffinition or else statement. elif checks for typos, % getclosematch states the closest match
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=.8)) > 0:
        yn= input("Did you mean %s instead Enter y if yes, or n if no: " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "That word does not exist. Please double check it."
        else:
            return "Sorry, we didn't understand your answer."
    else:
        return "That word does not exist. Please double check it."

#variable word gets users input
word = input("Enter word: ")

#printing the definition
output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
