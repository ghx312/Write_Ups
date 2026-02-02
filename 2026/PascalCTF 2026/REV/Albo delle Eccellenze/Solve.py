import socket
import time

def solve_albo(host="albo.ctf.pascalctf.it", port=7004):
    print(f"[*] Connecting to {host}:{port}...")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((host, port))
        print("[+] Connected successfully!")
        
        banner = sock.recv(4096).decode('utf-8', errors='ignore')
        print("\n[*] Received banner:")
        print(banner)
        
        answers = [
            "Test",
            "User",
            "01/01/2000",
            "M",
            "Offlaga"
        ]
        
        print("\n[*] Sending answers:")
        for i, answer in enumerate(answers, 1):
            print(f"    [{i}] {answer}")
            sock.sendall((answer + "\n").encode())
            time.sleep(0.1)
        
        print("\n[*] Waiting for response...")
        time.sleep(0.5)
        
        response = b""
        while True:
            try:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk
            except socket.timeout:
                break
        
        response = response.decode('utf-8', errors='ignore')
        print("\n[*] Response from server:")
        print(response)
        
        if "flag" in response.lower() or "pascal" in response.lower():
            print("\n[+] FLAG FOUND!")
            for line in response.split('\n'):
                if 'flag' in line.lower() or 'pascal' in line.lower():
                    print(f"    {line}")
        
        sock.close()
        print("\n[+] Connection closed")
        
    except socket.timeout:
        print("[-] Connection timed out")
    except ConnectionRefusedError:
        print("[-] Connection refused - is the server running?")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("Albo CTF Challenge - Automatic Solver")
    print("=" * 60)
    print("\nSolution Strategy:")
    print("- Binary analysis revealed 'Offlaga' as a special place name")
    print("- Entering 'Offlaga' triggers flag file reading")
    print("- Other inputs can be arbitrary valid values")
    print("=" * 60)
    print()
    
    solve_albo()