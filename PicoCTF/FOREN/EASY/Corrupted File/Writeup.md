# Challenge Details
Challenge Name: Corrupted File  
Category: Forensics/Easy  
Author: Yahaya Meddy  

# Challenge Description
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file here.

Hint 1: Try checking the file’s header.  
Hint 2: JPEG  
Hint 3: Tools like xxd or hexdump can help you inspect and edit file bytes.  

# Solve
Checking the file header, we can see that it is an invalid file header, using hexedit, we can edit the first 2 bytes to FF D8, this gives us an image containing the flag.  

# Flag
picoCTF{r3st0r1ng_th3_by73s_684e09bc}
