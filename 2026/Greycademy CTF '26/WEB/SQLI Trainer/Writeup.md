# Challenge Details
Challenge Name: SQLi Trainer  
Category: Web Exploitation  
Author: jro  

# Challenge Description
SQL is the most common language used to query relational databases.

However, it is easy for programmers to create a situation where user-controlled data is insecurely inserted into a SQL query.

Can you exploit it?

http://challs.nusgreyhats.org:32901

# Solve
This payload combines the results of the first query with the second, where the name is admin, directly accessing the flag.
`' UNION SELECT 'admin'--`

# Flag
grey{SQLi_1s_st1ll_rel3v4nt_1n_2026}
