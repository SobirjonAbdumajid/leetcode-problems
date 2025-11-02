from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Ikkilik qidiruv: tartiblangan ro'yxatda ishlaydi.
    Return: topilsa indeksi, topilmasa -1.
    Murakkablik: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
