# Find the number of steps to Reduce the Given Number to Zero also Divide By Two if even :

class Solution:
    def numberOfSteps(self,num:int)->int:
        if num == 0:
            return 0 
        elif num%2 == 0:
            return 1+self.numberOfSteps(num//2)
        elif num%2 !=0:
            return 1+self.numberOfSteps(num-1)