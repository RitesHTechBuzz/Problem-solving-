# to check if the elements in a array are either incerasing or decreasing 

def monotonic(self,nums):
    increasing  = decreasing = True
    for i in range( 1 ,len(nums)):
        if nums[i-1] < nums[i]:
            decreasing = False
        elif nums[i-1] > nums[i]:
            increasing = False
    return increasing or decreasing