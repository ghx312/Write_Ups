# These are the index swaps extracted and reverse so that we can rev the flag from the key.
checks = [ 
    (0, 8), (1, 15), (2, 7), (3, 22), (4, 23),
    (5, 21), (6, 12), (7, 0), (8, 11), (9, 17),
    (10, 1), (11, 13), (12, 14), (13, 18), (14, 2),
    (15, 19), (16, 9), (17, 4), (18, 20), (19, 3),
    (20, 10), (21, 5), (22, 16), (23, 6), (24, 24)
]

key = '____aadeghhimnorrstttvy{}'
flag = [None for _ in range(25)] 

for inp_idx, key_idx in checks:
    flag[inp_idx] = key[key_idx]

print(''.join(flag))
#grey{vm_is_not_that_hard}
