# ref https://www.clcoding.com/2024/04/sorting-algorithms-using-python.html


def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i+1, n):

            if arr[j] < arr[min_idx]:

                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr



# Example usage:

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)

def quick_sort(arr):

    if len(arr) <= 1:

        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)



# Example usage:

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Example usage:

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

sorted_arr = bubble_sort(arr)

print("Sorted array:", sorted_arr)

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and key < arr[j]:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr



# Example usage:

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

sorted_arr = insertion_sort(arr)

print("Sorted array:", sorted_arr)


