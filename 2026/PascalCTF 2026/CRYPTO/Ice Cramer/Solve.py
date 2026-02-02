import re
import sys
import socket

HOST = "cramer.ctf.pascalctf.it"
PORT = 5002

def parse_equations(text):
    equations = []
    solutions = []
    lines = text.strip().split('\n')
    
    for line in lines:
        if '=' not in line or 'Solve' in line or 'flag' in line.lower():
            continue
        
        parts = line.split('=')
        if len(parts) != 2:
            continue
        
        equation_part = parts[0].strip()
        try:
            solution = int(parts[1].strip())
        except ValueError:
            continue

        terms = re.findall(r'([+-]?\s*\d+)\s*\*\s*x_(\d+)', equation_part)
        
        if not terms:
            continue
        
        coefficients = {}
        for coef_str, var_idx in terms:
            coef = int(coef_str.replace(' ', ''))
            var_num = int(var_idx)
            coefficients[var_num] = coef
        
        equations.append(coefficients)
        solutions.append(solution)
    
    return equations, solutions

def solve_linear_system(equations, solutions):
    if not equations:
        return None
    
    max_var = max(max(eq.keys()) for eq in equations)
    num_vars = max_var + 1
    
    A = []
    for eq in equations:
        row = [0] * num_vars
        for var_idx, coef in eq.items():
            row[var_idx] = coef
        A.append(row)
    
    A = np.array(A, dtype=float)
    b = np.array(solutions, dtype=float)
    
    try:
        x = np.linalg.solve(A, b)
        x_rounded = np.round(x).astype(int)
        residual = np.max(np.abs(A @ x_rounded - b))
        if residual > 0.1:
            print(f"[!] Warning: Large residual {residual}")
        return x_rounded
    except np.linalg.LinAlgError:
        x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        x_rounded = np.round(x).astype(int)
        return x_rounded

def ascii_to_flag(ascii_values):
    flag_content = ''.join(chr(val) for val in ascii_values)
    return f"pascalCTF{{{flag_content}}}"

def get_equations_from_server(host, port, timeout=10):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        data = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            if b"Solve the system" in data:
                break
        sock.close()
        return data.decode('utf-8', errors='ignore')
    except socket.timeout:
        print(f"[!] Connection timeout after {timeout}s")
        return None
    except Exception as e:
        print(f"[!] Connection error: {e}")
        return None

def main():
    print("=" * 70)
    print(" PascalCTF Cramer Challenge Solver")
    print(" Solving Linear Systems to Recover Flags")
    print("=" * 70)
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(f"\n[*] Reading equations from: {filename}")
        try:
            with open(filename, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"[!] File not found: {filename}")
            return
        except Exception as e:
            print(f"[!] Error reading file: {e}")
            return
    else:
        print(f"\n[*] Connecting to {HOST}:{PORT}...")
        text = get_equations_from_server(HOST, PORT)
        if text is None:
            print("[!] Failed to retrieve equations from server")
            print(f"\n[*] Usage: {sys.argv[0]} [equations_file.txt]")
            return
        print("[+] Successfully received equations from server")
    print("\n[*] Parsing equations...")
    equations, solutions = parse_equations(text)
    
    if not equations:
        print("[!] No valid equations found")
        print("\n[*] Raw text preview:")
        print(text[:500])
        return
    
    num_vars = max(max(eq.keys()) for eq in equations) + 1
    print(f"[+] Found {len(equations)} equations with {num_vars} variables")
    
    if len(equations) <= 5:
        print("\n[*] All equations:")
    else:
        print("\n[*] Sample equations (first 3):")
    
    for i in range(min(3, len(equations))):
        eq = equations[i]
        eq_str = " + ".join(f"{coef:+d}*x_{idx}" for idx, coef in sorted(eq.items()))
        eq_str = eq_str.lstrip('+').replace('+ -', '- ')
        print(f"    {eq_str} = {solutions[i]}")
    
    if len(equations) > 3:
        print(f"    ... ({len(equations) - 3} more equations)")
    
    print("\n[*] Solving system using linear algebra...")
    ascii_values = solve_linear_system(equations, solutions)
    
    if ascii_values is None:
        print("[!] Failed to solve the system")
        return
    
    print(f"[+] Solution found!")
    print(f"\n[*] ASCII values: {list(ascii_values)}")
    
    if all(32 <= val <= 126 for val in ascii_values):
        print("[+] All values are printable ASCII characters ✓")
    else:
        print("[!] Warning: Some values are not printable ASCII")
        non_printable = [i for i, val in enumerate(ascii_values) if not (32 <= val <= 126)]
        print(f"    Non-printable at indices: {non_printable}")
    
    flag = ascii_to_flag(ascii_values)
    
    print("\n" + "=" * 70)
    print(f" FLAG: {flag}")
    print("=" * 70)
    
    return flag

if __name__ == "__main__":
    main()
