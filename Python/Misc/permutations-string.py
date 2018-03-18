string='AAAA'
list=list(string)
end=len(string)
add=[]

def permu(list,start,end,add):
    if start==end:
        if ''.join(list) not in add:
                new= ''.join(list)
                print (new)
                add.append(new)

    for i in range(start,end+1):
        list[start],list[i]=list[i],list[start]
        permu(list,start+1,end,add)
        list[start],list[i]=list[i],list[start]

    
permu(list,0,end-1,add)
    
