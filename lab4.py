# removing punctuation

punctuation = '!""()-_{}[];:/?\<>.@#$%^&*~`'

answer = ""

sampleString = "Hey Guys! This is Dylan. Do you have a cup of Coffee?"

for i in sampleString:
    if i not in punctuation:
        answer += i

print(f"this was the input string: {sampleString}")
print(f"This is the input without punctuations: {answer}")



# program to sort letters of word in a string
questionString1 = "the big brown fox jumps over a lazy dog"
splitted = questionString1.split()

tupleQuesString1 = tuple(splitted)
sorted = sorted(tupleQuesString1)

sortedString = ""
for word in sorted:
    sortedString += word + " "


print(f"this is the question String: {questionString1}")
print(f"this is the sorted string: {sortedString}")