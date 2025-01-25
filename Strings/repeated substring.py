# to check if a string can generate the pattern repeated multiple times

def substring(self,s):
    n = len(s)
    for i in range(1,n//2 + 1):
        if n%i == 0:
            substring = s[:i]
            if substring * (n//2) == s:
                return True
    
    return False