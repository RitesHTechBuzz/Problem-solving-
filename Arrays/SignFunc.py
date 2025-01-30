# return -1 0 1 based on product of numbers in integer array:

def signfunc(self, nums):
    count = 0
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            count += 1

        if count %2 == 0:
            return 1
        return -1