#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_=-99999
    for i in range(4):
        for j in range(4):
            sum_ = int(sum(arr[i][j:j+3])+sum(arr[i+2][j:j+3])+arr[i+1][j+1])
            if  sum_ > max_:
                max_ = sum_
    print (max_)
