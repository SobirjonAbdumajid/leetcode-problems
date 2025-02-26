# def even_index_chars(text):
#     return ''.join(text[i] for i in range(0, len(text), 2))
#
#
# def get_second_largest(numbers: list[int]):
#     unique_nums = sorted(set(numbers), reverse=True)
#     if len(unique_nums) < 2:
#         raise ValueError("List must have at least two distinct numbers")
#     return unique_nums[1]
#
# def get_second_largest(numbers: list[int]):
#     numbers.remove(max(numbers))
#     return max(numbers)


def even_index_chars(text):
    return ''.join(text[i] for i in range(0, len(text), 2))


def get_second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    unique_nums = sorted(set(numbers), reverse=True)
    if len(unique_nums) < 2:
        raise ValueError("List must have at least two distinct numbers")
    return unique_nums[1]

