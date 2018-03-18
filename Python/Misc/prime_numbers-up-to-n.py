#first n prime numbers
n=int(input('enter:'))
list=[]
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for i in range(2,n+1):
    if (isprime(i)):
        list.append(i)
   
print (list)   
