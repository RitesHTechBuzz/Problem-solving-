#based on the integer in array skip till that number , return True if reached at last of array.

def jumpgame(self,nums:list[int])->bool:
    max_reach = 0
    for i in range(len(nums)):
        if i> max_reach:
            return False
        max_reach  = max(max_reach,i+nums[i])
    return True   
