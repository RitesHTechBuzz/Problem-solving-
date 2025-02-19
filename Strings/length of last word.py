# return the length of last word

def lenoflasword(self , s:str)->int:
    last_word = s.split()
    return len(last_word[-1])