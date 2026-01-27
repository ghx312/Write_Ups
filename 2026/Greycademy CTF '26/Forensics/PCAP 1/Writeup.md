# Challenge Details
Challenge Name: PCAP 1  
Category: Forensics
Author: glendoodle  

# Challenge Description
What could go wrong with a login server that isn't encrypted? Find the attempted login with Greyhats as the username  

# Solve
As per mentioned in the challenge description, you can grep the file for the unencrypted flag using this command.  
`grep -a "grey" baby.pcap`
This will give you the flag

# Flag
grey{ju57_f0110w_7h3_57234m}
