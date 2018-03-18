#Time=O(n); n is len of s traversing string once and array once as array is of fixed size so traversing array is constant time
def solution(s):
    if len(s)==0:
        return None
    a=[-1]*256
    k=0 
    for i in s:
        if a[ord(i)]==-1:
            a[ord(i)]=k
        else:
            a[ord(i)]=-2
        k+=1
    #now find minimum value greater than or equal to 0
    ans=float('inf')
    flag=False
    for i in a:
        if i>=0 and ans>i:
                ans=i
                flag=True
    
    return s[ans] if flag else None
            
                
#S=''
S='ADBCGHIEFKJLADTVDERFSWVGHQWCNOPENSMSJWIERTFB'
print (solution(S))
