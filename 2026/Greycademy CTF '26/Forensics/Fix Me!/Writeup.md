Why this PNG file not opening :/# Challenge Details
Challenge Name: 
Category: 
Author:

# Challenge Description
Why this PNG file not opening :/

# Solve
The OS system will use the name of the file to open up their corresponding viewer, with PNG as the image viewer on windows, that programme than reads the PNG file header to determine what to do with it. These header bytes are called magic number, this is PNG's magic number: 89 50 4E 47 0D 0A 1A 0A and these are the header bytes of the actual given PNG file: 47 52 45 59 48 41 54 53, which spell out GREYHATS. Hence we must change the header of the PNG file in order to get the image viewer to view it correctly. Changing it gives us the corrected PNG file and we are able to view the flag.

![ScreenShot](./Images/fixme_fixed.png)

# Flag
grey{sign4tur3s_c001}
