# binary_code = "01010010 01100001 01101101 01100001 01111010 01101111 01101110 00100000 01101101 01110101 01100010 01101111 01110010 01100001 01101011 11111001110001001"
#
# text = ''.join(chr(int(b, 2)) for b in binary_code.split())
#
# print(text)
#
#
# # text = "Ramazon muborak🎉"
# #
# # binary_code = ' '.join(format(ord(char), '08b') for char in text)
# #
# # print(binary_code)


_list = []
nums = [-4,-1,0,3,10]
for i in nums:
    _list.append(i**2)
print(sorted(nums))
print(sorted(_list))