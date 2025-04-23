#rotate the array from a given index to the right 

def rotateArray(self, nums:list[int],k:int)->list:
    k%=len(nums)
    nums[:] = nums[-k:]+nums[:-k]

    #nums[-k:] represents all the last k elements
    #nums[:-k] all the elements except the k elements