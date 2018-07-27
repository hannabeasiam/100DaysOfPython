def palindrome(word):
    lower_word = word.lower()
    list_lower_word = list(lower_word)
    to_str = ''.join(list_lower_word)


    if lower_word == to_str:
        return word

print(palindrome('Malayalam'))