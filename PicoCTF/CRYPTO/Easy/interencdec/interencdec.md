# Challenge Details
Challenge Name: interencdec  
Category: Cryptography/Easy  
Author: NGIRIMANA Schadrack

# Challenge Description
Can you get the real meaning from this file?

# Solve
We are given a file with the following text inside it:  
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==  

This is base64, as there is a == at the back, decoding it will yield:  
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='  

This is also base64, we will then decode it once more, yielding us:  
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}  

We know that the flag format is picoCTF{}, which matches up with the ciphertext's format:  
Using a Caesar cipher of key 7, we can decode and obtain the flag

# Flag
Flag: picoCTF{caesar_d3cr9pt3d_86de32d2}
