# Challenge Details
Challenge Name: hashcrack  
Category: Cryptography/Easy  
Author: Nana Ama Atombo-Sackey

# Challenge Description
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords.  
Can you gain access to the secret stored within the server?  
Additional details will be available after launching your challenge instance.  

# Solve
We are provided with a hash and are told to enter the password for the given hash:  
Hash 1: 482c811da5d5b4bc6d497ffa98491e38 (32 Bytes of Hex) -> MD5  
Hash 2: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 (40 Bytes of Hex) -> SHA1  
Hash 3: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 (64 Bytes of Hex) -> SHA256  

We can use hashcat to obtain the unhashed plaintext with this bash command format, using the mode table below for different hash functions:  
hashcat -m <mode> -a 0 hash1 /usr/share/wordlists/rockyou.txt (E.g hashcat -m 0 -a 0 ciphertext1 /usr/share/wordlists/rockyou.txt for MD5)  

Mode Table:  
MD5 -> 0  
SHA1 -> 100  
SHA256 -> 1400  

Password 1: password123  
Password 2: letmein  
Password 3: qwerty098  

Keying the passwords into the Oracle gives us the following flag  

# Flag
Flag: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}
