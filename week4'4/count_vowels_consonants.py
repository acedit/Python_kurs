def count_vowels_consonants(word):
    rechnik={"consonants":0,"vowels":0}

    for symbol in word:
        if symbol in "aeiouyAEIOUY":
            rechnik["vowels"]+=1
        if symbol in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
            rechnik["consonants"]+=1
    return rechnik

