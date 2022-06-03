def partition(Arr, start, end):
    
    pivot = end 

    pIndex = start

    for i in range(start, end):
    
        if Arr[i] <= Arr[pivot]:
            Arr[i], Arr[pIndex] = Arr[pIndex], Arr[i]
            pIndex += 1

    Arr[pIndex], Arr[pivot] = Arr[pivot], Arr[pIndex] 

    return pIndex   

def quickSort(Arr, start, end):

    if start < end:

        pIndex = partition(Arr, start, end)
        quickSort(Arr, start, pIndex - 1)
        quickSort(Arr, pIndex + 1, end)

if __name__ == "__main__" :

    arr = [int(i) for i in input("Please enter the array elements separated by space : ").split(" ")]
    
    quickSort(arr, 0, len(arr) - 1)

    for i in arr:
        print(i, end = " ")