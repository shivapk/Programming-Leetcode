'''
#previously we have seen wordbreak problem now we will see without dynamic programming
#using dynamic programming
#Time =O(n^2) n is size of string, space=O(n) 
'''
'''
worst case: when the input is a string like "aaaa...aaab" and the dictionary contains all words "a..a" but not a "b".
without dynamic programming:
The for loop will always match n−2 times as we have all words formed by a's. So there are n−2 recursive calls. What we are effectively doing is checking all subsets of the given input. E.g. we are splitting "aaab" into
"a" + "a" + "a" + "b"
We will split the n a's into (2^n)−1 subsets. Hence the O(2^n) time bound.

'''

d={"mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"}

def wordcheck(s):
    if s in d:
        return True
    return False

def solution(s):
    if len(s)==0:
        return True
    for i in range(len(s)):
        if wordcheck(s[:i+1]) and solution(s[i+1:]):
            return True
    return False

#s='IDeservelearningplatform'
s='mobilesamsungsam'
 
print (solution(s))
