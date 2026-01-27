# Challenge Details
Challenge Name: Artifact 1  
Category: Reverse Engineering  
Author: cewau  

# Challenge Description
Introductory decompilation (hands on 1) / disassembly (hands-on 2) analysis  

# Solve
Challenge stores the flag in plaintext inside the code, accessing `FUN_001011f3` and then `FUN_001011b8` shows where the flag is located in.  

![Screenshot](./Images/Raw.jpg)

OR

You may read the function and what they do. By reading the function, you realise that it takes in an input from the user, compared it with a hardcoded input at 0x539, and if they are the sam,e outputs the flag. By decoding the bytes at 0x539, you get the number 1337, which, when input into the programme, outputs the flag.

![Screenshot](./Images/REV.jpg)

# Flag
grey{i_am_a_reverse_engineer!}
