#Determine if theres is element duplication using hashmaps

def hasDuplicate(self , nums :list[int])->bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
    
    return False 