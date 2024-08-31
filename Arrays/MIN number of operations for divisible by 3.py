#Find the number of operations requried to convert a given number into a number that is divisible by 3:

class Solutions:
    def Min(self,nums:List[int])->List[int]:
        count =0
        ans =[]
        for i in nums:
            if nums[i]%3 ==0:
                continue
            else:
                count += 1
            return count 