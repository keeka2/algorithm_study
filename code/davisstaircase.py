# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
DP = [0, 1, 2, 4]
mod = 10000000007

def stepPerms(n):
    if n < len(DP):
        return DP[n] % mod
    for i in range(len(DP), n+1):
        DP.append(DP[i-1]+DP[i-2]+DP[i-3])

    return DP[n] % mod

if __name__ == '__main__':
    s = int(input())
    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)
        print(res)
