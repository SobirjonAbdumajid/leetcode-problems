# def even_index_chars(text):
#     return ''.join(text[i] for i in range(0, len(text), 2))
#
#
# user_input = input("Enter a string: ")
# result = even_index_chars(user_input)
# print(result)
#
#
# # import pytest
# # from solutions import even_index_chars, second_largest
# #
# # # Fixture for even_index_chars
# # @pytest.fixture
# # def string_inputs():
# #     return [
# #         "PYnative",
# #         "Hello",
# #         "a",
# #         "",
# #         "Python3"
# #     ]


text = "2+3-1*(3-1)*2*(5*2)"
# text = "1+1/2"


def solution(s):
    if "(" not in s:
        return eval(s)
    start = s.index("(")
    end = s.index(")", start)
    return eval(text[start + 1:end])
    # _list = text.split("(")[0]
    # _list.extend(s.split("(")[1:])  # ["3-1)*2"]
    # # _list.append(text.split("("))[1:]
    # return eval(text)


print(solution(text))
