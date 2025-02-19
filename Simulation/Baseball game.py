# if C = remove last element 
#if D =  double the last element 
#if + =  add the last two elements
# if just an integer then add it to the list
from typing import List

def baseball(self , operations:List[str])->int:
    result = []
    for op in operations:
        if op =='C':
            result.pop()
        elif op == 'D':
            result.append(result[-1]*2)
        elif op == '+':
            result.append(result[-1]+result[-2])
        else:
            result.append(int(op))
    return sum(result)

