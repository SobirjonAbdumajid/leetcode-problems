from typing import List


def linear_search(arr: List[int], target: int) -> int:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


if __name__ == "__main__":
    a = [3, 1, 4, 2, 5]
    print("Original:", a)
    print("Linear search for 4 ->", linear_search(a, 4))  # 0-based index (2)

    # Simple tests
    assert linear_search(a, 6) == -1
    print("All tests passed.")
