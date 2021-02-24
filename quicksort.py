#quicksort sorting algorithm#
def quicksort(arr):
    n=len(arr)
   #if only one element
    if n<=1:
        return arr

    else:
        #pop will give last element, as mid point for array sorting 
        pivot = arr.pop()
        q_greater = []
        q_smaller   = []

        #logic for quicksort arranging with respect to middle value

    for i in arr:
             
        if pivot < i:
                #if element is greater than pivot's value all to q_greater list
            q_greater.append(i)

                #if element is smaller than pivot's value add to q_lower list
        else:
            q_smaller.append(i)
                

    return quicksort(q_smaller) + [pivot] + quicksort(q_greater)


arr=[]
n=int(input("Number of values want to sort="))
for i in range (1,n+1):
    inp=int(input(f"Value {i}:"))

    arr.append(inp)

print(f"sorted array is {quicksort(arr)}")






            
        
        
