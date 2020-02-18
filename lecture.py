import random


def fibonacci(n):
    if n < 0:
        print('No negative numbers')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(40))

"""
[ 5 9 3 7 2 8 1 6]
[3 2 1][5][9 7 8 6]
[2 1 ][3][5][9 7 8 6]
 [1 ][2][][3][5][9 7 8 6]
 [1 ][2][][3][5][][9] [7 8 6]
 [1 ][2][][3][5][7 8 6][9] []
 [1 ][2][][3][5][7] [8][9] []

"""


def partition_data(arr):
    left = []
    right = []
    # find pivot point
    pivot = arr[0]

    for item in arr[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return left, pivot, right


def quick_sort(arr):
    # decide base case
    if len(arr) <= 1:
        return arr
    # move values to less/greater than lists
    left, pivot, right = partition_data(arr)
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_2(arr):
    if arr:
        pivot = random.choice(arr)
        low = [n for n in arr if n < pivot]
        middle = [n for n in arr if n == pivot]
        high = [n for n in arr if n > pivot]
        return [*quick_sort_2(low), *middle, *quick_sort_2(high)]
    else:
        return []


# print(quick_sort([5, 6, 23, 65, 4, 23]))
print(quick_sort_2([5, 6, 23, 65, 4, 23]))
