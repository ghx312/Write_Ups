import socket
import re
p = 1844669347765474229
a = 0
b = 1
n = 1844669347765474230
Gx = 27
Gy = 728430165157041631

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modinv(a, m):
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    return (x % m + m) % m

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        if self.x is None:
            return "O"
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self.x == other.x and self.y == (-other.y % p):
            return Point(None, None)
        if self.x == other.x:
            s = (3 * self.x**2 + a) * modinv(2 * self.y, p) % p
        else:
            s = (other.y - self.y) * modinv(other.x - self.x, p) % p
        x3 = (s*s - self.x - other.x) % p
        y3 = (s * (self.x - x3) - self.y) % p
        return Point(x3, y3)
    
    def __rmul__(self, scalar):
        result = Point(None, None)
        addend = self
        while scalar:
            if scalar & 1:
                result = result + addend
            addend = addend + addend
            scalar >>= 1
        return result
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def baby_step_giant_step(G, Q, order):
    m = int(order**0.5) + 1
    
    baby_steps = {}
    current = Point(None, None)
    for j in range(m):
        baby_steps[(current.x, current.y)] = j
        current = current + G
    
    mG = m * G
    current = Q
    for i in range(m):
        key = (current.x, current.y)
        if key in baby_steps:
            j = baby_steps[key]
            return (i * m + j) % order
        current = current + Point(mG.x, (-mG.y) % p)
    
    return None

def pohlig_hellman(G, Q):
    #From FactorDB
    factors = [(2, 1), (3, 2), (5, 1), (7, 1), (11, 1), (13, 1), 
               (17, 1), (19, 1), (23, 1), (29, 1), (31, 1), 
               (37, 1), (41, 1), (43, 1), (47, 1)]
    
    remainders = []
    moduli = []
    
    print("\n[+] Starting Pohlig-Hellman attack...")
    
    for prime, exp in factors:
        prime_power = prime ** exp
        print(f"[*] Solving modulo {prime}^{exp} = {prime_power}...", end=" ")
        
        cofactor = n // prime_power
        G_reduced = cofactor * G
        Q_reduced = cofactor * Q
        
        x_i = baby_step_giant_step(G_reduced, Q_reduced, prime_power)
        
        if x_i is not None:
            print(f"✓ x ≡ {x_i} (mod {prime_power})")
            remainders.append(x_i)
            moduli.append(prime_power)
        else:
            print(f"✗ Failed")
    
    print("\n[+] Applying Chinese Remainder Theorem...")
    result = 0
    N = 1
    for m in moduli:
        N *= m
    
    for r, m in zip(remainders, moduli):
        Ni = N // m
        Mi = modinv(Ni, m)
        result = (result + r * Ni * Mi) % N
    
    print(f"[+] Verifying solution...", end=" ")
    test_Q = result * G
    if test_Q == Q:
        print("✓ Correct!")
    else:
        print("✗ Verification failed!")
    
    return result

def connect_and_solve(host, port):
    print(f"[+] Connecting to {host}:{port}...")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    data = b""
    while True:
        chunk = sock.recv(4096)
        data += chunk
        if b"Q = " in data:
            break
    
    output = data.decode('utf-8')
    print("\n" + "="*70)
    print(output)
    print("="*70)
    
    q_match = re.search(r'Q = \((\d+), (\d+)\)', output)
    if not q_match:
        print("[-] Failed to extract Q coordinates!")
        sock.close()
        return
    
    Qx = int(q_match.group(1))
    Qy = int(q_match.group(2))
    
    print(f"\n[+] Extracted Q = ({Qx}, {Qy})")
    
    G = Point(Gx, Gy)
    Q = Point(Qx, Qy)
    
    secret = pohlig_hellman(G, Q)
    
    print(f"\n[+] Secret found!")
    print(f"    Decimal: {secret}")
    print(f"    Hex: {hex(secret)}")
    
    print(f"\n[+] Submitting secret to server...")
    
    sock.recv(4096)
    
    sock.send(b"1\n")
    sock.recv(4096)
    
    hex_secret = hex(secret)[2:] + "\n"
    sock.send(hex_secret.encode())
    
    response = sock.recv(4096).decode('utf-8')
    print("\n" + "="*70)
    print(response)
    print("="*70)
    
    flag_match = re.search(r'(pascalCTF\{[^}]+\})', response)
    if flag_match:
        flag = flag_match.group(1)
        print(f"\n🚩 FLAG: {flag}")
    else:
        print("\n[-] No flag found in response")
    
    sock.close()

if __name__ == "__main__":
    print("="*70)
    print("CURVE BALL - AUTOMATED SOLVER")
    print("="*70)
    
    HOST = "curve.ctf.pascalctf.it"
    PORT = 5004
    
    try:
        connect_and_solve(HOST, PORT)
    except Exception as e:
        print(f"\n[-] Error: {e}")
        import traceback
        traceback.print_exc()