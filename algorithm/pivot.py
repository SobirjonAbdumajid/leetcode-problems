
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):

    print(arr)

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, len(arr) - 1)

    for val in arr:
        print(val, end=" ")


