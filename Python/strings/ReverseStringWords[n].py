s='how are you'
#in this approach len(s), len(a) are equal
#time complexity =O(n)

def reverse(s):
    if s=='':
        return s
    end=len(s)
    a=''
    for i in range(len(s)-1,-1,-1):
        if s[i]==' ':
            a+=s[i+1:end]+' '
            end=i
    if s[i]!=' ':
        a+=s[i:end]
    return a

print (reverse(s))


'''
#if you want no spaces at front and in between the words only 1 space is needed then this below approach
class Solution(object):
    def reverseWords(self, s):
        if s=='':
            return ''
        end=len(s)
        a=[]
        print (len(s))
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                if s[i+1:end]==' ' or s[i+1:end]=='':
                    end=i
                else:
                    a.append(s[i+1:end]) 
                    end=i
        if s[0]!=' ':
            a.append(s[0:end])
        print (a)
        return (' '.join(a)).strip()
'''
