# Challenge Details
Challenge Name: Artifact 3  
Category: Reverse Engineering  
Author: cewau

# Challenge Description
Intermediate reverse engineering with some common decompilation constructs  

# Solve
Decompling the programme using ghidra, looking at `FUN_001012ad`, takes in a string, runs it through `FUN_00101184`, which reduces the ord( ) of all characters except the last 5 in the string by 3 and then removes the order of HELLO from the back of the input string. The result of this manipulation to the flag is printed in the function in plaintext. By reversing this process, we can get the flag.

# Flag
grey{real_reversing}
