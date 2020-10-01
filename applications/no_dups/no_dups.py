def no_dups(s):
    # Your code here
    cache = {}
    words = s.split()
    words_list = []

    for word in words:
        if word not in cache:
            cache[word] = 1 #this is just an initializer.
            words_list.append(word) #append the word to the word_list if not in cache already
    print (words_list)
    joined_words_list = " ".join(words_list)
    print(joined_words_list)
    return joined_words_list


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))