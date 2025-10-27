import socket, ssl, time, random, sys

HOST = "0e5d79d13f0130c4.syndroem.zone.re"
PORT = 443
ERROR_LEN = 3488
WEIGHT = 4
TIMEOUT = 20.0

def make_weight4_vector():
    pos = random.sample(range(ERROR_LEN), WEIGHT)
    v = ['0'] * ERROR_LEN
    for p in pos:
        v[p] = '1'
    return ''.join(v)

def read_until_prompt(filelike, token, timeout=20):
    deadline = time.time() + timeout
    buf = []
    while time.time() < deadline:
        line = filelike.readline()
        if not line:
            break
        buf.append(line)
        if token in line:
            return "".join(buf)
    return "".join(buf)

def try_once():
    sock = socket.create_connection((HOST, PORT), timeout=TIMEOUT)
    ctx = ssl.create_default_context()
    ssock = ctx.wrap_socket(sock, server_hostname=HOST)
    f = ssock.makefile("r", encoding="utf-8", newline="\n")
    try:
        welcome = read_until_prompt(f, "Enter the error:", timeout=10)
        vec = make_weight4_vector()
        ssock.sendall((vec + "\n").encode())
        resp_lines = []
        ssock.settimeout(5.0)
        try:
            while True:
                line = f.readline()
                if not line:
                    break
                resp_lines.append(line)
                if "flag" in line.lower() or "{" in line and "}" in line:
                    break
        except Exception:
            pass
        full = "".join(resp_lines)
        return full
    finally:
        try:
            ssock.close()
        except:
            pass

if __name__ == "__main__":
    random.seed()
    try:
        out = try_once()
    except Exception as e:
        print(e)

#flag{g0t_th3_ikEA_syNdroeM?_mWTIBN_RAl5yniv6Lg}
