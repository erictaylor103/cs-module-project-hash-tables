import re

def word_count(s):
    # Your code here
    s = re.sub('[\"\:\;\,\.\-\+\=\/\\\|[\]\{\}\(\)\*\^\&]', "", s)
    words = {}

    for c in s.lower().split():
        if c not in words:
            words[c] = 1
        else:
            words[c] += 1
    
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))