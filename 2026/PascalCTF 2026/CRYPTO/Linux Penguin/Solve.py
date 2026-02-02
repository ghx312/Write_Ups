import socket

WORDS = [
    "biocompatibility", "biodegradability", "characterization", "contraindication",
    "counterbalancing", "counterintuitive", "decentralization", "disproportionate",
    "electrochemistry", "electromagnetism", "environmentalist", "internationality",
    "internationalism", "institutionalize", "microlithography", "microphotography",
    "misappropriation", "mischaracterized", "miscommunication", "misunderstanding",
    "photolithography", "phonocardiograph", "psychophysiology", "rationalizations",
    "representational", "responsibilities", "transcontinental", "unconstitutional"
]

def solve():
    s = socket.socket()
    s.connect(("penguin.ctf.pascalctf.it", 5003))

    buf = b""
    def read_until(marker):
        nonlocal buf
        while marker not in buf:
            buf += s.recv(4096)
        idx = buf.index(marker) + len(marker)
        result = buf[:idx]
        buf = buf[idx:]
        return result.decode()

    def send(msg):
        s.sendall((msg + "\n").encode())

    # ---------------------------------------------------------------
    # Server flow (from source):
    #   wallpaper()                          <- banner + "Welcome..."
    #   for i in range(7):
    #     print("Give me 4 words...")        <- prompt paragraph
    #     input("Word 1: ")                  <- waits for input
    #     input("Word 2: ")
    #     input("Word 3: ")
    #     input("Word 4: ")
    #     print("Encrypted words: ...")      <- encrypted output
    #   print("Can you now guess...")
    #   print("Ciphertext: ...")             <- the 5 encrypted words
    #   for i in range(5):
    #     input("Guess the word N: ")        <- waits for guess
    #     print("Correct guess: ..." or "Wrong guess...")
    #   print_flag()
    # ---------------------------------------------------------------

    ct_to_word = {}

    for round_num in range(7):
        # Wait for "Word 1: " prompt (first round has banner before it)
        read_until(b"Word 1: ")

        batch = WORDS[round_num*4 : round_num*4 + 4]
        print(f"[*] Round {round_num+1}/7: {batch}")

        # Send word 1, wait for "Word 2: ", send word 2, etc.
        send(batch[0])
        read_until(b"Word 2: ")
        send(batch[1])
        read_until(b"Word 3: ")
        send(batch[2])
        read_until(b"Word 4: ")
        send(batch[3])

        # Now read "Encrypted words: <hex> <hex> <hex> <hex>\n"
        enc_line = read_until(b"\n").strip()
        print(f"    {enc_line}")

        # Parse
        cts = enc_line.split("Encrypted words:")[1].strip().split()
        for word, ct in zip(batch, cts):
            ct_to_word[ct] = word

    print(f"\n[+] Built table with {len(ct_to_word)} entries")

    # Read up to and including the Ciphertext line
    ct_line = read_until(b"Ciphertext: ")
    # Now read the rest of that line (the actual ciphertexts)
    rest = read_until(b"\n").strip()
    challenge_cts = rest.split()

    print(f"[*] Challenge: {len(challenge_cts)} ciphertexts")

    # Lookup
    answers = []
    for ct in challenge_cts:
        w = ct_to_word.get(ct, None)
        answers.append(w)
        print(f"    {ct[:40]}... -> {w}")

    if None in answers:
        print("[!] Failed to lookup one or more ciphertexts!")
        s.close()
        return

    # Submit guesses
    for i, ans in enumerate(answers):
        read_until(f"Guess the word {i+1}: ".encode())
        print(f"[*] Submitting guess {i+1}: {ans}")
        send(ans)

    # Read remaining output (correct messages + flag)
    import time
    time.sleep(1)
    s.settimeout(2)
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            print(chunk.decode(), end="")
    except:
        pass

    s.close()

solve()