# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA: type, arrB: type) -> type:
    """
    Helper function to merge separate lists into a 
    single sorted list.

    Arguments:
        arrA -- List
        arrB -- List

    Returns:
        List -- sorted combined elements of arrA and arrB
    """
    elements = len(arrA) + len(arrB)
    # merged_arr = [[]] * elements
    merged_arr = []
    # for all elements:
    # if all elements in arrA have been merged
    # into merged-arr, put next element in arrB into
    #  merge_arr
    while len(merged_arr) < elements:
        if not arrA:
            merged_arr.extend(arrB)

        # elif all elements in arrB have been merged
        # into merged-arr, put next element in arrA into
        #  merge_arr
        elif not arrB:
            merged_arr.extend(arrA)

        # elif next elemnt in arrA is smaller than next
        # in arrB, add element to merged_arr
        elif arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))

        # elif next elemnt in arrB is smaller than next
        # in arrA, add element to merged_arr
        elif arrB[0] <= arrA[0]:
            merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # divide arr into sub arrays
    if len(arr) > 1:
        left = merge_sort(arr[: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr

# STRETCH: implement an in-place merge sort algorithm
# merge the arrays without creating an empty array


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
