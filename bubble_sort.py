from turtle import pen


def bubble_sort(arr):

    for i in range(len(arr) - 1):
        swapped = False  # to make the algorithm efficient O(n)
        for j in range(len(arr) - 1 - i):

            if arr[j] > arr[j+1] :

                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        
        if swapped == False: # if array is already sorted 
            break
    
    return arr 


if __name__ == "__main__":

    arr = [int(i) for i in input("Please enter the elements separated by space: ").split(" ")]

    print("Array before sorting: {}".format(arr))

    print("Array after sorting : {}".format(bubble_sort(arr)))
