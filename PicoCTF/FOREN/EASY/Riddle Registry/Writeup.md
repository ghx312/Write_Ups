# Challenge Details
Challenge Name: Riddle Registry  
Category: Forensics/Easy  
Author: Prince Niyonshuti N.

# Challenge Description
Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.  
Find the PDF file here Hidden Confidential Document and uncover the flag within the metadata.  

Hint 1: Don't be fooled by the visible text; it’s just a decoy!  
Hint 2: Look beyond the surface for hidden clues  

# Solve
Checking the metadata of the given file allows us to see the author.  
Using this command `exiftool confidential.pdf`  
The author's name is encoded in base64. Decoding it gives us the flag.  

# Flag
picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}
