def longest_reapeating_char_replacment(s, k):
    n = len(s)
    count = [0]* 26
    l =0
    lenght =0

    for r in range(n):
        count[(ord(r)-65)] += 1
        while (r-l+1)- max(count) > k:
            count[s[l]] -= 1
            l += 1
        lenght = max(lenght,r-l+1)
    return lenght