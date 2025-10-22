def is_subsequence(word, main_string):
    i = 0
    j = 0
    while i < len(main_string) and j < len(word):
        if main_string[i] == word[j]:
            j += 1
        i+=1
    return j == len(word)

def find_subsequence(mainstring, words):
    result =[]
    for word in words:
        if is_subsequence(word,mainstring):
            result.append(word)
    return result

