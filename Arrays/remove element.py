# remove the given element form array 
def remove(self ,nums:List[int],val:int)-> int:
    nums.sort()
    for i in range(len(nums)-1,0,-1):
        if nums[i] == val:
            nums.pop(i)
    
    return len(nums)


 
