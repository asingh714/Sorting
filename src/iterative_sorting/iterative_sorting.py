# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
                
        if cur_index != i:
            temp = arr[i]
            arr[i] = arr[cur_index]
            arr[cur_index] = temp
        print(arr)

    return arr


print(selection_sort([7, 4, 2, 1, 9, 3, 8]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
