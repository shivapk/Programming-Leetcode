A=[1,1,1,1,1]
E=[1,2,1,3,2,4,2,5]
#Time Complexity is O(N), where N is the length of A. As it is tree, number of edges=nodes-1 hence no need to take len(E) in to consideration
#Space Complexity is O(N).
from collections import defaultdict
from itertools import izip

def pairwise(iterable):
    a = iter(iterable)
    return izip(a, a)

def traversal(node,ans):
        if not node: return 0
        left = traversal(node.left,ans)
        right = traversal(node.right,ans)
        lcount=rcount= 0
        if node.left and node.left.val == node.val:
            lcount = left + 1
        if node.right and node.right.val == node.val:
            rcount = right + 1
        ans[0] = max(ans[0], lcount + rcount)
        return max(lcount, rcount)

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def solution(A, E):
    if len(A)==0 or len(E)==0:
        return 0
    if len(E) !=(len(A)-1)*2:
        return 'Catch:Length of A and E are not as stated in the question'
    arr=[0]+[Node(A[i-1]) for i in range(1,len(A)+1)]
    for i,j in pairwise(E):
            if i==j:
                return 'vertices should have different number'
            if arr[i].left:
                arr[i].right=arr[j]
            else:
                arr[i].left=arr[j]
    ans=[0]
    result=traversal(arr[1],ans)
    return ans[0]
    

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print (root.val)
    inorder(root.right)
    #return adjlist


print (solution(A,E))
