def valid_palindrome(string):
    n = len(string)
    l = 0
    r = n-1

    while l < r:
        if not string[l].isalnum():
            l += 1
            continue
        if not string[r].isalnum():
            r -= 1
            continue

        if string[l].lower() != string[r].lower():
            return False
        l += 1
        r -= 1
    return True

input = "ra_c_eCaR"
print(valid_palindrome(input))
