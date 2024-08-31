#Check if sum of child nodes is equal to root nodes 

def CheckSum(self, root:Optional[TreeNode])->bool:
    return root.val == (root.left.val+root.right.val)
