# Challenge Details
Challenge Name: Artifact 14 Pointers
Category: Reverse Engineering
Author: cewau

# Challenge Description
Exploration on arrays and pointer arithmetic.

# Solve
We basically run the code given to us, but change it such that it directly references the value instead of comparing the referenced value without the given flag.  
To sum it up, every single pointer increases the memory address value by 100, with the initial array starting at 100 and each value within it increasing by 1, so 100 or dst[0] = 'a'.  
By pointing to it twice, this increases the memory value to 300, we then treat ptr as the center and increase or decrease the value by the size of the datatype on the left multiplied by the difference on the right.  
When we finish this, this will point us towards a char within dst.  

# Flag
grey{puzzle_and_pointer_expert}
