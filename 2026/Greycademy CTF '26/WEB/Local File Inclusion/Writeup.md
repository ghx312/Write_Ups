# Challenge Details
Challenge Name: Local File Inclusion  
Category: Web Exploitation  
Author: Iscara  

# Challenge Description
In web security, a majority of vulnerabilities stem from untrusted user input being used improperly. A local file inclusion occurs when user-inputted file paths are used to retrieve files without sufficient input validation, allowing a malicious user to read private files on the system.

Let's try! The flag is at /flag.txt. The leading slash means that it's in the root directory. You're gonna have to go up the tree somehow.

http://challs.nusgreyhats.org:32903

# Solve
The file directories are in linux, so we are able to do ../ to move up 1 directory, since there are 2, we can do ../../flag.txt to get there. We can input this into the search bar right after the path to directly access the flag.txt

# Flag
grey{pretend_these_are_the_epstein_files}
