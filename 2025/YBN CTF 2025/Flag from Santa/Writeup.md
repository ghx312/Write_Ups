# Challenge Details
Challenge Name: Flag from Santa  
Category: Cryptography 

# Challenge Description
Santa has sent a flag to everyone on the nice list, unfortunately you did not get one, but you managed to obtain some RSA artifacts Santa used.  

Maybe you can get the flag as well?  

# Solve
Vulnerability: Small Public Exponent + Moduli Coprime + Plaintext Reuse  
The chall.py has 2 pieces of code that give away its vulnerability:  
```
if gcd(n1, n2) != 1 or gcd(n1, n3) != 1 or gcd(n2, n3) != 1:
        continue
```
and  
```
if pow(M, E) < n1 * n2 * n3:
        break
```
1. This ensures that all moduli are coprime.
2. This ensures that the ciphertext will always be less than the product of the moduli.

This vulnerability is set up for Håstad’s attack, which allows us to use the Chinese Remainder Theorem to combine the ciphertexts together and invert them using the small public exponent.  
We can then simply convert the large int (long) into bytes to get the flag.  

# Flag
YBN{P4d_y0ur_ms}
