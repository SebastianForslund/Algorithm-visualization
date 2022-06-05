import math
import random

# Not own code


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break
    return array


def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j = j-1
        InputList[j+1] = nxt_element


def selectionSort(array):

    for s in range(len(array)):
        min_idx = s

        for i in range(s + 1, len(array)):

            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])


def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1


def countingSort(nums):
    i_lower_bound, upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound, upper_bound = min(nums), max(nums)

    counter_nums = [0]*(upper_bound-lower_bound+1)
    for item in nums:
        counter_nums[item-lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]


def bogoSort(array):
    while(array != sorted(array)):
        for index, item in enumerate(array):
            rand = random.randint(0, len(array)-1)
            array[index] = array[rand]
            array[rand] = item
            if array == sorted(array):
                break
