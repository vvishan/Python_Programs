from contextlib import contextmanager
import time
## context manager : here onec we run With statement contextmanager start enter and run the code and 
#3 exit automatically ,even the exception occurs inside the code

# with context manager

with open("data.txt","r") as p:
    contents = p.read()

## with out context manager manually

f = open("data.txt","r")
try:
    context=f.read()
except:
    f.close()