# Challenge Details
Challenge Name: Ice Cramer  
Category: Cryptography  
Author: Alan Davide Bovo <@AlBovo>  
Final Points: 50  

# Challenge Description
Elia’s swamped with algebra but craving a new ice-cream flavor, help him crack these equations so he can trade books for a cone!
nc cramer.ctf.pascalctf.it 5002

# Solve
The encryption protocol takes in the content of the flag (Without the flag format) and converts them into their ASCII value, takes a random k ranging from -100 to 100 then puts them into a series of equation.  
Taking in the equations, we can use Cramer's Rule to solve for the system of equations since there are as many variables as there are equations.  

# Flag
pascalCTF{0h_My_G0DD0_too_much_m4th_:O}
