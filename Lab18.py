import string

chances = {}
countLetters = {}
words = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]

for symbol in string.ascii_lowercase:
    chances[symbol] = countLetters[symbol] = 0

# Считаем общее количесвто букв и количество каждой буквы по отдельности
countOfLetters = 0
for word in words:
    countOfLetters += len(word)
    for symbol in word:
        countLetters[symbol] += 1

# Считаем вероятность произнесения буквы
for char in countLetters:
    chances[char] = countLetters[char] / countOfLetters

word = input()

# Считаем вероятность произнесения слова
finalChance = chances[word[0]]
for i in range(1, len(word)):
    finalChance *= chances[word[i]]

print(finalChance)
