def selection_sort(arr):

    for i in range(len(arr) - 1):
        
        min_index = i
        
        for j in range(min_index+1 , len(arr)):

            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":

    arr = [int(i) for i in input("Please enter the array elements separated by space : ").split(" ")]

    print("Array before sorting the elements is: {}".format(arr))

    print("Array after sorting the elements is : {}".format(selection_sort(arr)))