def ror(x, n):
    for _ in range(n):
        x = (x >> 1 | (x & 1) << 7) & 0xff
    return x

def reverse_mystery(output, key_byte):
    return output ^ key_byte

key = b'merry christmas'
check = [40, 139, 226, 176, 128, 74, 139, 141, 176, 177, 68, 142, 35, 66, 65, 
         100, 22, 2, 99, 142, 69, 17, 115, 24, 8, 194, 178, 3, 160, 60, 30, 0, 
         0, 75, 5, 40, 16, 56, 46, 99, 7]
rotations = [10, 15, 53, 60, 54, 35, 55, 63, 36, 27, 6, 23, 37, 5, 21,
             57, 24, 16, 13, 63, 40, 32, 52, 2, 51, 21, 20, 48, 67, 1,
             57, 30, 50, 6, 46, 21, 56, 1, 57, 45, 31]

flag = []
for i in range(41):
    key_byte = key[i % 15]
    intermediate = ror(check[i], rotations[i])
    flag_byte = reverse_mystery(intermediate, key_byte)
    flag.append(flag_byte)
flag = bytes(flag)
print('Flag:', flag.decode())
