# deleting punctuation from string
questionString = "Hey fellas! I'm new in town here can you help me navigate this area?"

Output = ""
toRemove = '!""()-_{}[];:/?\<>.@#$%^&*~`'

for char in questionString:
    if char not in toRemove:
        Output = Output + char

print(questionString)
print()
print("below is the same string without the punctuation.")
print(Output)



# program to print a sorted string input

inputStr = "willingly stealing a bike from the mailmen"
splitting = inputStr.split()
toSort = tuple(splitting)
sorting = sorted(toSort)

sortedStr = ""

for word in sorting:
    sortedStr += word
    sortedStr += " "

print()
print(f"question String: {inputStr}")
print(f"sorted string: {sortedStr}")