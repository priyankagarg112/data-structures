# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def partition(arr,l,h):
    pivot = arr[l]
    a = l
    for i in range(l+1, h+1):
        if arr[i] < pivot:
            a=a+1
            arr[a],arr[i]= arr[i],arr[a]
    
    arr[a],arr[l]= arr[l],arr[a]
    # print(arr)
    return a


def quicksort(arr,l,h):
    if l>=h:
        return
    m = partition(arr,l,h)
    
    quicksort(arr, l, m-1)
    quicksort(arr, m+1, h)
    

arr=[5,2,1,8,4,0,9,67,89,22,6]
quicksort(arr, 0, len(arr)-1)

print(arr)
