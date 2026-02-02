# Challenge Details
Challenge Name: Linux Penguin  
Category: Cryptography  
Author: Alan Davide Bovo <@AlBovo>  
Final Points: 147  

# Challenge Description
I've just installed Arch Linux and I couldn't be any happier :)  
nc penguin.ctf.pascalctf.it 5003  

# Solve
This challenge uses ECB for its encryption but it doesn't matter.  
The server takes in 28 words and outputs their corresponding ciphertext using the same key, after this encryption stage, we get 5 ciphertext which are 5 out of 28 words that we submitted and we must input the correct plaintext of the given 5 ciphertext back to the server to get the flag.  

# Flag
pascalCTF{why_4r3_th3_bl0ck_4lw4ys_th3_s4m3???}
