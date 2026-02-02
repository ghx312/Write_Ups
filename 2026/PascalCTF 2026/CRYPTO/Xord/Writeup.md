# Challenge Details
Challenge Name: Xord  
Category: Cryptography    
Author: Filippo Boschi <@pllossi>  
Final Points: 50  

# Challenge Description
I just discovered bitwise operators, so I guess 1 XOR 1 = 1?  

# Solve
The seed in the encryptor is fixed at `1337`, which means that the secret key is fixed and public; we can simply decrypt it by using the same seed and XORing it with the ciphertext.  

# Flag
pascalCTF{1ts_4lw4ys_4b0ut_x0r1ng_4nd_s33d1ng}  
