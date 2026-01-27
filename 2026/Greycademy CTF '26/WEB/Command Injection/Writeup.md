# Challenge Details
Challenge Name: Command Injection  
Category: Web Exploitation  
Author: Iscara  

# Challenge Description
In web security, a majority of vulnerabilities stem from untrusted user input being used improperly. A command injection occurs when user input is placed into shell commands without sufficient input validation, allowing a malicious user to run arbitrary commands on the server.

Let's try! Your goal here is to be able to execute and read the output of arbitrary commands on the server.

http://challs.nusgreyhats.org:32902

# Solve
We were able to run commands by backing it out with backticks, by running \`ls\`, we are able to see the flag.txt file, we can then run \`cat flag.txt\` to view the file.

# Flag
grey{injectable}
