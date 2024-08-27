#Find the middle element of the linked list :
Class Solution:
def MiddleNode(self,head: Optional[ListNode])->Optional[ListNode] :
    count = 0
    curr = head

    while curr is not None :
        count +=1
        curr = curr.next

        mid = count//2

        curr = head 
        for _ in range(mid):
            curr = curr.next

        return curr