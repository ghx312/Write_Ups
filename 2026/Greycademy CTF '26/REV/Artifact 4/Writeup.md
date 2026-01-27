# Challenge Details
Challenge Name: Artifact 4  
Category: Reverse Engineering  
Author: cewau  

# Challenge Description
VM introduction / teaser

# Solve
The function takes in a flag of length 25, it sets a value for X and Y and then check if the `input[X] == key[Y]` for all characters, if they are the same, then continue, this continues for the rest of the characters, by taking down the values of X and Y, we are able to reverse the index swaps of the key, allowing us to unscramble the flag.

# Flag
grey{vm_is_not_that_hard}
