from pwn import *

conn = remote('challs.nusgreyhats.org', 35000)

try:
    while True:
        line = conn.recvuntil(b'=').decode()
        expression = line.strip().split('\n')[-1].replace('=', '').strip()
        result = eval(expression)
        conn.sendline(str(result).encode())
except:
    pass

print(conn.recvall(timeout=2).decode())
conn.close()
#flag{m4th_g3niu5}
