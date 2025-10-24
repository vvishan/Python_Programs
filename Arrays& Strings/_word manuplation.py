# Reverse words in sentence
s = "pyhton is fun"

def reverse_sentence(sen):
    return " ".join(sen.split()[::-1])

print(reverse_sentence(s))

# captalizing the first letter in sentence

capital = s. title()
print(capital)

# check if sentence is Pangram

import string
s1 = "The quick brown fox jumps over a lazy dog"
print(set(string.ascii_lowercase)<= set(s1.lower()))

#Removing duplicates from the string

s2 = "programming"
seen = ""
for ch in s2:
    if ch not in seen:
        seen += ch
print(seen)