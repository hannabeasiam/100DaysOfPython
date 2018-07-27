def disemvowel(word):
    words = word.copy()
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        i = letter.lower()
        if i in vowels:
            words.remove(i)

    return words

