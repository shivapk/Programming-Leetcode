# remove start and end spaces
s='   dfdf dfd sfsdf   '
     
def startend(s):
    if s=='' or s==' ':
        return ''
    start=0
    end=len(s)-1
    while start<end:
        if s[start]!=' ' and s[end]!=' ':
            return s[start:end]
        elif s[start]==' ' and s[end]==' ':
            start+=1
            end-=1
        elif s[start]==' ':
            start+=1
        else:
            end-=1
    return (s)

print ('eee',startend(s),'dfdfd')


'''
print (''.join(s.split()))
        
print (s.replace(' ',''))
'''
