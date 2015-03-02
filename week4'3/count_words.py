def count_words(words):
    rechnik={}

    for word in words:
        if word in rechnik:
            rechnik[word]+=1
        else:
            rechnik[word]=1
    return rechnik

