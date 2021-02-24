#insertion sort
def insertionsort(arr):

    for i in range (1,len(arr)):

        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j] :

            arr[j+1] = arr[j]

            j-=1

        arr[j+1] = key
    

arr=[]
n=int(input("Number of values want to sort="))
for i in range (1,n+1):
    inp=int(input(f"Value {i}:"))

    arr.append(inp)


insertionsort(arr)

print("Sorted Array:")
for i in range (len(arr)):
    print("%d" %arr[i])

        
              
              
            
