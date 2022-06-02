def insertion_sort(arr):

    for i in range(len(arr)):

        temp = arr[i]

        j = i - 1 

        while j >= 0 and temp < arr[j]:

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

    return arr
if __name__ == "__main__":

    arr = [int(i) for i in input("Enter the elements separated by space : ").split(' ')]

    print("Array elements before swapping are : {}".format(arr))

    print("Array elements after swapping are : {}".format(insertion_sort(arr)))
