#Given a randomly generated string s and t is generated same way with an extra letter anywhere randomly . Return that letter 

#implementing using XOR as it cancels all the same charaters in both strings and only returns the correct or unique onces

def String_Substraction(s,t):
    output = 0

    for char in s :
        output ^= ord(s)
    
    for char in t:
        output ^= ord(t)

    return chr(output)

    