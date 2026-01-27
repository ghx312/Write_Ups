# Challenge Details
Challenge Name: Related Riddles  
Category: Cryptography  

# Challenge Description
Find m given two rsa ciphertexts under the same (n,e) with known additive offsets  

# Solve  
Vulnerability: $(m + a)^3 < n$, Small Public Exponent  
There is no modular reduction since $(m + a)^3 < n$, we can take the cube root and deduct a from the result.  

# Flag
YBN25{on the first day of christmas i got a turkey}
