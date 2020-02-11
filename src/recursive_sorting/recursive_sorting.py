# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    merged_arr = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged_arr.append(left[left_i])
            left_i += 1
        else:
            merged_arr.append(right[right_i])
            right_i += 1

    if left_i < len(left):
        merged_arr.extend(left[left_i:])

    if right_i < len(right):
        merged_arr.extend(right[right_i:])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
