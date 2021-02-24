#Bubble Sorting Algorithm#

def bubblesort(arr):
    n=len(arr)


    #For the iterations/Rounds i
    for i in range(n):

     #for inner proceeding of elements
        for j in range(0,n-i-1):

     #ascending order
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

#calling function
#defining an empty array
arr=[]
n=int(input("Number of values want to sort="))
for i in range (1,n+1):
    inp=int(input(f"Value {i}:"))

    arr.append(inp)


bubblesort(arr)

print("Sorted Array:")
for i in range (len(arr)):
    print("%d" %arr[i])
            
        
