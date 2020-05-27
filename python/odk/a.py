
import math
import os
import random
import re
import sys



#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#

def funWithAnagrams(text):
    deleted = [False] * len(text)

    for i in range(len(text)-1):
        for j in range(i+1, len(text)):
            if deleted[i]:
                continue
            if sorted(text[i]) != sorted(text[j]):
                continue
            deleted[j] = True
    new_text = []
    for k in range(len(text)):
        if deleted[k]:
           continue
        new_text.append(text[k])
    new_text.sort()
    # Write your code here
    return new_text

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)
    for res in result:
        print(res)
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    #
    # fptr.close()

'''
5
ad
asd
dsa
ccd
da
'''