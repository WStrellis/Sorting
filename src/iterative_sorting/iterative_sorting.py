# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    if len(arr) < 2:
        return arr
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # find next smallest
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # swap if smaller item was found
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    end = len(arr) - 1
    while end:
        swaps = False
        for i in range(0, end):
            item = arr[i]
            if arr[i] > arr[i + 1]:
                swaps = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        end -= 1
        if not swaps:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
