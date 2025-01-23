#Return true if anagram
from collections import Counter
def anagram(self , s, t):
    f1 = Counter(s)
    f2 = Counter(t)
    return f1 == f2

