#first n prime numbers
n=int(input('enter:'))
list=[]
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
start=2
while len(list)<n:
    if (isprime(start)):
        list.append(start)
    start+=1
print (list)   
