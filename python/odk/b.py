#!/bin/python3

import math
import os
import random
import re
import sys


def finalInstances(instances, averageUtil):
    flag = False
    cnt = 0
    for av in averageUtil:
        if cnt == 9:
            flag = False
            cnt = 0
            continue
        if flag:
            cnt+=1
            continue
        if av < 25:
            if instances > 1:
                if instances % 2:
                    instances = instances // 2 + 1
                else:
                    instances //= 2
                flag = True
        elif av > 60:
            if instances * 2 > 2 * (10 ** 8):
                continue
            instances *= 2
            flag = True

    return instances


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    instances = int(input().strip())

    averageUtil_count = int(input().strip())

    averageUtil = []

    for _ in range(averageUtil_count):
        averageUtil_item = int(input().strip())
        averageUtil.append(averageUtil_item)

    result = finalInstances(instances, averageUtil)

    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
