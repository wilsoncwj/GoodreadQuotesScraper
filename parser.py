import json
import os

cwd = os.getcwd()

jsonfile = open("wilson.json", "r")
lst = json.load(jsonfile)

num_quotes = len(lst)
print("Number of quotes =", num_quotes)

### Pre-processing steps are below, run the ones you need
# Reorder the ID of the quotes to start from 0.
# for i in range(num_quotes):
#     lst[i]["item"]["id"] = i

### Make the tags a string instead of an element in a list
# for i in range(num_quotes):
#     if len(lst[i]["item"]["tag"]) == 1:
#         lst[i]["item"]["tag"] = lst[i]["item"]["tag"][0]


# copy = []
# for i in range(num_quotes):
#     if len(lst[i]["item"]["tag"]) != 0:
#         copy.append(lst[i])

### Remove all other tags except for the second one
# for i in range(num_quotes):
#     if len(lst[i]["item"]["tag"]) >= 2:
#         lst[i]["item"]["tag"] = lst[i]["item"]["tag"][1]

# # Remove the "likes" word in the dict key "likes", keeping only the numbers as int
# for i in range(num_quotes):
#     lst[i]["item"]["likes"] = int(lst[i]["item"]["likes"])

# print(empty_list[0])
# print(lst[0])
# empty_list[0]["item"] = lst[0]
# print(empty_list[0])

# To add the ID tag for each quote
# for i in range(num_quotes):
#     lst[i]["id"] = i+1


# num_repeated = 0
# for i in range(num_quotes-1):
#     if lst[i] == lst[i+1]:
#         print(lst[i])
#         num_repeated += 1
# print("Number of repeated quotes =", num_repeated)

# num_words = 0

### Checker script to test code
# for i in range(1):
#     temp = lst[i]["quote"][0].strip().split()
#     print(temp)
#     for i in temp:
#         print(i)
#     num_words += len(temp)
# print(num_words)

# for i in range(num_quotes):
#     temp = lst[i]["quote"][0].strip().split()
#     num_words += len(temp)
# print("Total number of words =", num_words)


# # Remove all the extra "returns" in the quote
# for i in range(num_quotes):
#     lst[i]["quote"] = lst[i]["quote"][0]

# # Remove extra whitespaces in quote and author
# for i in range(num_quotes):
#     lst[i]["quote"] = lst[i]["quote"].encode('ascii', 'ignore').decode("utf-8")
#     lst[i]["quote"] = lst[i]["quote"].strip()
#     lst[i]["author"] = lst[i]["author"][0].strip()
#     if lst[i]["author"][-1] == ",":
#         lst[i]["author"] = lst[i]["author"][:-1]

# # Removes empty quotes
# lst_copy = []
# for i in range(num_quotes):
#     if lst[i]["quote"] != "":
#         lst_copy.append(lst[i])

# Save the lst to json
# with open('wilson.json', 'w') as outfile:
#     json.dump(lst, outfile)
