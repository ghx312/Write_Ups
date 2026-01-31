# Challenge Details
Challenge Name: DISKO 1  
Category: Forensics/Easy  
Author: Darkraicg492  

# Challenge Description
Can you find the flag in this disk image?
Download the disk image here.

Hint 1: Maybe Strings could help? If only there was a way to do that?  

# Solve
Instead of strings, I used grep, since I know what the flag format is, I can use the command `grep -a 'picoCTF{' disko-1.dd` in order to extract all phrases containing picoCTF{  

# Flag
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
