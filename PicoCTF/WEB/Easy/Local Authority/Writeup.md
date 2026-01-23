# Challenge Details
Challenge Name: Local Authority  
Category: Web Exploitation/Easy  
Author: LT 'syreal' Jones  

# Challenge Description
Can you get the flag?
Additional details will be available after launching your challenge instance.

# Solve
Going into the wbesite, we see a login interface. Sending a random username and password, we can see the login logic using Burp Suite.

Picture1

We can see that it calls an unknown function from the server named checkPassword() to check the validity of our details.  
By using Inspect > Network, we can see that a secure.js file viewed in the source panel gives us the following

Picture2

Using the details to log in gives us the flag.

# Flag
picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}
