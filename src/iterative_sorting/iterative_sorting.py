# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j

        if cur_index != i:
            arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
