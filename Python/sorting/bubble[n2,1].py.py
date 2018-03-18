#bubble sort
#Time=O(n^2)
#space=O(1)
def bubblesort(myList):
  for j in range(len(myList)):
    for i in range(len(myList)-j-1):
        if myList[i]>myList[i+1]:
            myList[i],myList[i+1]=myList[i+1],myList[i]
  return myList
            
myList=['a','h','b','c','e']

print bubblesort(myList)