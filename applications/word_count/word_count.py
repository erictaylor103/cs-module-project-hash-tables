import re

def word_count(s):
    # Your code here
    s = re.sub('[\"\:\;\,\.\-\+\=\/\\\|[\]\{\}\(\)\*\^\&]', '', s)
    wordList = {}

    for c in s.lower().split():
        if c not in wordList:
            wordList[c] = 1
        else:
            wordList[c] += 1
        
    return wordList


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))