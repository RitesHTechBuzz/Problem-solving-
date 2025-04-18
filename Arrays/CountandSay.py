# given the value of n, count the number of digits and then return the  new compressed code digit

def CountandSay(self,n:int)->str:
    if n==1:
        return '1'
    
    def help(string):
        freq = []
        count =1
        for i in range(1,len(string)):
            if string[i] ==string[i-1]:
                count +=1
            else:
                freq.append([count,string[i-1]])
                count=1
            
        freq.append([count,string[i]])

        return freq
    
    def create(freq):
        output = ""

        for num in freq:
            output+= str(num[0]) + num[1]

        return output
    
    RLE = '11'
    for i in range(1,n-1):
        freq1 =help(RLE)
        RLE = create(freq1)

    return RLE