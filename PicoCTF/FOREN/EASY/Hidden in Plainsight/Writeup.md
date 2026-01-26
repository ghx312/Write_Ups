# Challenge Details
Challenge Name: Hidden in Plainsight  
Category: Forensics/Easy  
Author: Yahaya Meddy  

# Challenge Description
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image here.

Hint 1: Download the jpg image and read its metadata

# Solve
Use exiftool to fine metadata of the picture.  
`exiftool img.jpg`  
You get this line in the comments.  
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9  
Decode from base64  
stehide:cEF6endvcmQ=  
Decode the message from base64 again  
pAzzword  

Use steghide and the following password to extract the flag from the image  
steghide extract -sf img.jpg -p pAzzword  

# Flag
picoCTF{h1dd3n_1n_1m4g3_e7f5b969}
