target = "dobvxob^i\\obsbo+$\"\x1b."

flag = ""
for i in range(15):
    char_val = ord(target[i])
    char_val += 3
    flag += chr(char_val)

hello = "HELLO"
for i in range(5):
    char_val = ord(target[15 + i])
    char_val += ord(hello[i])
    flag += chr(char_val)

print(flag)
#grey{real_reversing}
