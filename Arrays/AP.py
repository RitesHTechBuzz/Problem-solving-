#Check for AP 

def ap_sol(self , arr):
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(1,len(arr)):
        if arr[i+1] - arr[i] != diff:
            return False
    return True