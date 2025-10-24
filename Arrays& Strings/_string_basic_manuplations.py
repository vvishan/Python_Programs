s = "abcdefgh"

# reverse the string
def reverse_string(st):
    return st[::-1]

print(reverse_string(s))
#-----------------------------------------------------------------------
# check palindrome
def check_palindrome(d):
    return d == d[::-1]
a="madam"
print(check_palindrome(a))
#------------------------------------------------------------------------
# count vowela and constants

b = " hello world"
def count_vowels(b):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in b :
        if char in vowels:
            count += 1
    return count
print(count_vowels(b))


#------------------------------------------------------------
# removing all spaces from the string

text = " python is fun"
text = text.replace(" ","")
print(text)

#------------------------------------------------------------
# find length of the longest word
text1 = " python is great"
words = text1.split()
print(max(words,key= len))