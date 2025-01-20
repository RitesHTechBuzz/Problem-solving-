# given two arrays num1 and num2 with number of elements represented by m and n need to return num1 with merged sorted array .
#num1 has  0  for all the values that has to be replaced later after sorting from num2

def merge_sorted_arrays(nums1,m,nums2,n):
    i = m-1
    j = n-1
    k = m+n-1

    while i>= 0 and j >=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -=1

    while j>=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        
