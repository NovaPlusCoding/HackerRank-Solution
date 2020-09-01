#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r = s[::-1]

    list1 = [ord(x) for x in s]
    list2 = [ord(x) for x in r]

    for i in range(len(list1)-1):
        list1[i] = abs(list1[i] - list1[i+1])
    list1.pop()

    for i in range(len(list2)-1):
        list2[i] = abs(list2[i] - list2[i+1])
    list2.pop()

    if list1 == list2:
        return "Funny"
    else:
        return "Not Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
