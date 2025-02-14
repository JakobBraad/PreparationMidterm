import requests

from find3letterwords import punctuation

link = "https://blabla.txt"

result = request.get(link)
print(result.text)
unique_words = {}
lines = result.text.splitlines()

for line in lines:
    for p in punctuation:
        line = line.replace(p," ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0) + 1


print(unique_words["romeo"])

print(unique_words["juliet"])

freq = list(unique_words.values())
freq.sort(reverse=True)
freq = freq[:10]

print(freq)
print("The most common 10 words are:")
for f in freq:
    for key, value in unique_words.items():
        if value ==f:
