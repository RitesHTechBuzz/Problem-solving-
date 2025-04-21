#Return the majority element from the given arrays
from collections import Counter
def majority(self,nums:list[int])->int:
    nums.sort()
    c = Counter(nums)
    return max(c.keys(),key=c.get)