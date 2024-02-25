import speech_recognition
import pyttsx3





# removing punctuation

punctuation = '!""()-_{}[];:/?\<>.@#$%^&*~`'

answer = ""

sampleString = "Hey Guys! This is Dylan. Do you have a cup of Coffee?"

for i in sampleString:
    if i not in punctuation:
        answer += i

print(f"this was the input string: {sampleString}")
print(f"This is the input without punctuations: {answer}")

print()

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


# for speech recognition

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_bing(audio)
            text = text.lower()

            print(f"Recognized {text}")

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue


