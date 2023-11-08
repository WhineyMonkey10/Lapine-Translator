import difflib
import datetime
import colorama

with open("words.txt") as file:
    data = {}
    for line in file:
        if "-" in line:
            key, *values = line.strip().split("-")
            definitions = "-".join(values).lower().strip().split(", ")
            for definition in definitions:
                data[definition.strip()] = key.lower().strip()


def translate(word):
    word = word.lower()
    matches = difflib.get_close_matches(word, data.keys(), n=1, cutoff=0.5)
    if matches:
        return data[matches[0]]
    else:
        return None

word = input("Enter sentence: ")
startTime = datetime.datetime.now()
translated = []
for word in word.split():
    translated_word = translate(word)
    if translated_word != None:
        translated.append(translated_word)
    else:
        translated.append(word)
finished_sentence = ""


for word in translated:
    finished_sentence += word + " "
finsihedTime = datetime.datetime.now()

print(finished_sentence)

print(f"{colorama.Fore.GREEN}Time taken: {finsihedTime - startTime}")