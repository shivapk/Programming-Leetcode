# KMP Algorithm
'''
The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches),
we already know some of the characters in the text of next window. We take advantage of this information to
avoid matching the characters that we know will anyway match.
O(n) time to create array, O(m) for main algorithm, total O(m+n)
#we create longest prefix suffix array based on target_string that will hold the longest prefix suffix length till this point
'''
#Time complexity: 0(m+n) where m is the text/given string and n is the target string
#space complexity=O(n) where n is the target string(memorize: smaller one is n)
def KMP_search(given_string, target_string):
    if len(given_string)==0 and len(target_string)!=0:
        return False
    if len(target_string)==0:
        return True
    if len(target_string)>len(given_string):
        return False
    # create longest prefix suffix array that will hold the longest prefix suffix length till this point
    arr = target_array(target_string)
    curr_target = 0 # index for target_string j  pointer
    curr_given = 0 # index for given_string  i pointer
    while curr_given < len(given_string):
        if target_string[curr_target] == given_string[curr_given]:
            curr_given += 1
            curr_target += 1
        if curr_target == len(target_string):
            return (curr_given-curr_target)  #print Found pattern at this index
            #curr_target = arr[curr_target-1]   #add this step if you want to print multiple
 
        # mismatch after curr_target matches
        elif curr_given < len(given_string) and target_string[curr_target] != given_string[curr_given]:
            # Do not match arr[0..arr[curr_target-1]] characters,
            # they will match anyway
            if curr_target != 0:
                curr_target = arr[curr_target-1]
            else:
                curr_given += 1
    return False #not found
 
def target_array(pattern):
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
 
given_string = 'jkj'#"kfdkfskfabcdakmkabcdhjhjkhabcd"
target_string ='xjkfgjklfgj'# "abcd"
print (KMP_search(given_string, target_string))
