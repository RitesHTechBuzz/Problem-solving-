#running Array Sum 

class Solutions:
    def RunningSum(self,nums:List[int])->List[int]:
        for i in range(0,len(nums)):
            nums[i] +=nums[i-1]
            return nums
        