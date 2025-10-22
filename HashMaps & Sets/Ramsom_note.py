ramson = "ab"
magzine = "dfgabcdf"
from collections import defaultdict
def Ramson_note(ramson,magzine):
    s = defaultdict(int)
    for letters in magzine:
        s[letters] += 1
    
    for c in ramson:
        if c not in s:
            return False
        elif s[c]==1:
            del s[c]
        else:
            s[c] -= 1
    return True
      
            
print(Ramson_note(ramson,magzine))