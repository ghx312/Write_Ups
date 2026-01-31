# Challenge Details
Challenge Name: Flag in Flame  
Category: Forensics/Easy  
Author: Prince Niyonshuti N.  

# Challenge Description
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial.  

Hint 1: Use base64 to decode the data and generate the image file.  

# Solve
Downloading the file we get a txt file filled with base64 which can be identified as the last 2 characters are equal signs ,'=', decoding this big file gives us an image with text at the bottom that says:  
"7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F32353631613139347D"  
This is in hexadecimal, decoding this from Hex gives us the flag.  

# Flag
picoCTF{forensics_analysis_is_amazing_2561a194}
