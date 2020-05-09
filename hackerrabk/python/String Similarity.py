
import math
import os
import random
import re
import sys

# Complete the stringSimilarity function below.

t = int(input("Enter the string"))
for t_itr in range(t):
    s = input()
    char_array = list(s)
    n = len(s)
    c = len(s)
    z = [n]
    R = 0
    L = 0
    for i in range(1, n):
        if (i > R):
            L = R = i
            while R < n and char_array[R-L] == char_array[R]:
                R += 1
            z.append(R-L)
            R -= 1
            c += z[i]
        else:
            k = i-L
            if z[k] < R-i+1:
                z.append(z[k])
                c += z[i]
            else:
                L = i
                while R < n and s[R-L] == s[R]:
                    R += 1
                z.append(R-L)
                c += z[i]
                R -= 1
    s = c
    print(s)
