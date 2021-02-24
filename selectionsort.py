#selectionsort
arr = []
n = int(input("enter the number of elements"))
for i in range(0,n):
    inp = int(input("enter the elements"))
    arr.append(inp)
print(arr)


for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
             min_idx = j
             arr[i], arr[min_idx] = arr[min_idx], arr[i]

print ("Sorted array") 
for i in range(len(arr)): 
    print("%d" %arr[i]),  
 




    

            
            
    
