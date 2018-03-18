#iterative approach for wordbreak problem
#Time =O(n^2) n is size of string, space=O(n) 
'''
d={'arrays', 'dynamic', 'heaps', 'IDeserve', 'learn', 'learning', 'linked', 'list', 'platform', 'programming', 'stacks', 'trees'}
'''
d={"mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"}

def wordcheck(s):
    if s in d:
        return True
    return False

def solution(s):
    arr=[False]*(len(s))
    for i in range(len(s)):
        if wordcheck(s[:i+1]):
            arr[i]=True
            
        if arr[i]==True:
            if i==(len(s)-1):
                return True
            for j in range(i,len(s)):
                if arr[j]==False and wordcheck(s[i+1:j+1]):
                    arr[j]=True
                elif arr[j]==True and j==(len(s)-1):
                    return True        
    print (arr)              
#s='IDeservelearningplatform'
s='mobilesamsungsam'
    
print (solution(s))
