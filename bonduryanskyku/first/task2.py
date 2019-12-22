"""

У даному рядку виділити усі слова, що починаються з великої букви, та
вивести їх
"""

text = "How it's going, buddy"
words = text.split()
for word in words:
    if word[0] == word[0].upper():
        print(word)
