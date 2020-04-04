import json
import os
import re

cwd = os.getcwd()

jsonfile = open("wilson.json", "r")
lst = json.load(jsonfile)

# Number of records
num_quotes = len(lst)
print("Number of quotes =", num_quotes)

# Number of words
num_words = 0
for i in range(num_quotes):
    num_words += len(lst[i]["item"]["quote"].split())
print("Number of words =", num_words)

# Number of unique words
unique = []
for i in range(num_quotes):
    temp = re.findall(r'[^\s!,(+=/).?<>*":;0-9\#\$\%\&\-\'\[\]\\]+', lst[i]["item"]["quote"])
    for word in temp:
        word = word.lower()
        if word not in unique:
            unique.append(word)
print("Number of unique words =", len(unique))
