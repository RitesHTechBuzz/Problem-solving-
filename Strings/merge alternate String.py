# merge alternate letters from two given words 

def String(self , word1, word2):
    i,j =0,0
    merged = []
    m = len(word1)
    n  = len(word2)

    while i <m and j < n:
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    while i < m :
        merged.append(word1[i])
        i += 1

    while j < n :
        merged.append(word2[j])
        j += 1
    
    return ''.join(merged)
