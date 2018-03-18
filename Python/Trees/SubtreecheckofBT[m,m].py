#Given 2 binary trees s, t. check whether tree t has exactly the same structure and node values with a subtree of s
#Time: O(m) where m is the given tree/main tree#tree traversal+string comparision=m + m+n=m
#space: O(m) # as we are using to store preorder traversal(main_tree array)
'''
logic: if preorder traversal of both the target tree is a subset of preorder traversal of main tree

'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def issubtreeofotherBT(self,tmain,ttest):#check test_tree in main_tree
        main_tree=self.preorder(tmain,True)
        test_tree=self.preorder(ttest,True)
        '''
        if test_tree in main_tree: #without KMP it takes O(m*n), m,n are 2 string lengths
            return True
        '''
        return self.kmp(main_tree,test_tree)
    
        
    def preorder(self,root,left):
        if root is None:
            if left:
                return 'null'  #if you dont use null then it will fail in some cases
            else:
                return 'null'
            
        return ' '+str(root.val)+' '+self.preorder(root.left,True)+' '+self.preorder(root.right,False)
    
    def kmp(self,given_string,target_string):
        if len(given_string)==0 and len(target_string)!=0:
            return False
        if len(target_string)==0:
            return True
        if len(target_string)>len(given_string):
            return False
        # create longest prefix suffix array that will hold the longest prefix suffix length till this point
        arr = self.target_array(target_string)
        curr_target = 0 # index for target_string j  pointer
        curr_given = 0 # index for given_string  i pointer
        while curr_given < len(given_string):
            if target_string[curr_target] == given_string[curr_given]:
                curr_given += 1
                curr_target += 1
            if curr_target == len(target_string):
                return True # if you wantprint Found pattern at this index (curr_given-curr_target)

            # mismatch after curr_target matches
            elif curr_given < len(given_string) and target_string[curr_target] != given_string[curr_given]:
                # Do not match arr[0..arr[curr_target-1]] characters,
                # they will match anyway
                if curr_target != 0:
                    curr_target = arr[curr_target-1]
                else:
                    curr_given += 1
        return False #not found
    
    def target_array(self,pattern):
        arr=[0]*(len(pattern))
        prev_len = 0 # j length of the previous longest prefix suffix
        # arr[0] is always 0 so no need to do anything, start i from 1
        curr = 1  #i
        # the loop calculates arr[i] for i = 1 to length-1
        while curr < len(pattern):
            if pattern[curr]==pattern[prev_len]:
                prev_len += 1
                arr[curr] = prev_len
                curr += 1
            else:
                if prev_len != 0:
                    prev_len = arr[prev_len-1]
                    # Also, note that we do not increment curr here
                else:
                    arr[curr] = 0
                    curr += 1
        return arr
        
            
        
        
        
root1 =  Node(15)
root1.left = Node(10)
root1.left.right=Node(12)
root1.right = Node(20)
root1.left.left = Node(8)
root1.left.left.right=Node(6)
root1.left.right = Node(12)
root1.right.right = Node(25)

root2 =  Node(10)
root2.left = Node(8)
root2.right = Node(12)
root2.left.right=Node(6)
s=Solution()
print (s.issubtreeofotherBT(root1,root2))

        
            
