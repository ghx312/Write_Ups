# Colab exploit cell: attempt connection to manual.flu.xxx:1024 and recover flag
import socket, time, sys

HOST = "manual.flu.xxx"
PORT = 1024
N = 256
PIECE_BYTES = 32
TIMEOUT = 10.0

def read_until_token(f, token, timeout=30):
    end = time.time() + timeout
    buf = []
    while time.time() < end:
        line = f.readline()
        if not line:
            raise RuntimeError("connection closed while waiting for token")
        buf.append(line)
        if token in line:
            return "".join(buf)
    raise RuntimeError("timeout waiting for token")

def query_hex(sock, sockfile, hex_in):
    read_until_token(sockfile, "Please enter")
    sock.sendall((hex_in + "\n").encode())
    read_until_token(sockfile, "Here is what the intern put together:")
    # next non-empty line should be hex
    while True:
        line = sockfile.readline()
        if not line:
            raise RuntimeError("connection closed while waiting for assembled hex")
        s = line.strip()
        if s:
            return bytes.fromhex(s)

def gf2_invert(rows):
    n = len(rows)
    A = rows[:]
    I = [1 << (n-1-r) for r in range(n)]
    for col in range(n):
        pivot_row = None
        for r in range(col, n):
            if (A[r] >> (n-1-col)) & 1:
                pivot_row = r
                break
        if pivot_row is None:
            raise RuntimeError("matrix not invertible")
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            I[col], I[pivot_row] = I[pivot_row], I[col]
        for r in range(n):
            if r != col and ((A[r] >> (n-1-col)) & 1):
                A[r] ^= A[col]
                I[r] ^= I[col]
    return I

def run_exploit():
    print("Connecting to", HOST, PORT)
    sock = socket.create_connection((HOST, PORT), timeout=TIMEOUT)
    sockfile = sock.makefile("r", encoding="utf-8", newline="\n")
    try:
        zero = b"\x00" * PIECE_BYTES
        print("Querying zero vector...")
        k_bytes = query_hex(sock, sockfile, zero.hex())
        k = int.from_bytes(k_bytes, "big")
        print("Received k.")

        cols = []
        for i in range(N):
            v = (1 << (N-1-i)).to_bytes(PIECE_BYTES, "big")
            out = query_hex(sock, sockfile, v.hex())
            cols.append(int.from_bytes(out, "big") ^ k)
            if (i+1) % 32 == 0:
                print(f"Basis queries done: {i+1}/{N}")

        print("Building matrix rows...")
        rows = [0]*N
        for col_idx, col_val in enumerate(cols):
            for bit in range(N):
                if (col_val >> (N-1-bit)) & 1:
                    rows[bit] |= (1 << (N-1-col_idx))

        print("Inverting matrix (GF(2))...")
        inv_rows = gf2_invert(rows)

        print("Sending finish to get final ciphertext...")
        read_until_token(sockfile, "Please enter")
        sock.sendall(b"finish\n")
        read_until_token(sockfile, "The intern says they've understood")
        y_hex = None
        while True:
            line = sockfile.readline()
            if not line:
                break
            s = line.strip()
            if s and all(c in "0123456789abcdefABCDEF" for c in s) and len(s) >= PIECE_BYTES*2:
                y_hex = s
                break
        if y_hex is None:
            raise RuntimeError("Could not find final ciphertext in server output")

        y = int.from_bytes(bytes.fromhex(y_hex), "big")
        masked = y ^ k

        flag_int = 0
        for row_idx, inv_row in enumerate(inv_rows):
            bit = bin(inv_row & masked).count("1") & 1
            if bit:
                flag_int |= (1 << (N-1-row_idx))

        flag = flag_int.to_bytes(PIECE_BYTES, "big")
        try:
            print("Recovered flag:", flag.decode())
        except:
            print("Recovered flag (bytes):", flag)
    finally:
        sock.close()

try:
    run_exploit()
except Exception as e:
    print("Exploit failed in Colab runtime:", e)
    print("If this fails due to network restrictions, run the same script on your local machine or on a small cloud VM.")

#flag{crypt0_kn0wl3dg3_g4in3d_:3}
