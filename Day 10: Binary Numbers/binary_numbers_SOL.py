import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n = list(bin(n))
    del n[:2]
    count,max_=0,-99999
    
    for i in range(len(n)):
        if n[i]=='1':
            count+=1
            for j in n[i+1:]:
                if j=='1':
                    count+=1
                else:
                    break
        if count>max_:
            max_=count
        count=0
    print (max_)
    
