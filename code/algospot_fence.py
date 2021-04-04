# https://algospot.com/judge/problem/read/FENCE
import sys, copy
from collections import deque


def solution(board, left, right):
    global answer
    if left == right:
        ret = board[left]
        answer = max(ret, answer)
        return
    elif right - left == 1:
        ret = max(board[left], board[right], 2*min(board[left], board[right]))
        answer = max(ret, answer)
        return
    elif right - left == 2:
        ret = max(max(board[left:right+1]), 2*min(board[left:right]), 2*min(board[left+1:right+1]), 3*min(board[left:right+1]))
        answer = max(ret, answer)
        return
    mid = (left + right) // 2
    lo, hi = mid, mid+1
    min_height = min(board[mid], board[mid+1])
    ret = 2*min_height
    total = board[mid] + board[mid+1]
    while left < lo or right > hi:
        if hi < right and (lo==left or board[lo-1]<board[hi+1]):
            hi += 1
            total += board[hi]
            min_height = min(min_height, board[hi])
        else:
            lo -=1
            total += board[lo]
            min_height = min(min_height, board[lo])
        ret = max(ret, min_height *(hi-lo+1))
    answer = max(ret, answer)
    if answer < total:
        solution(board, left, mid)
        solution(board, mid + 1, right)
    else:
        return



answer = 0
c = int(sys.stdin.readline())
for _ in range(c):
    n = sys.stdin.readline()
    heights = list(map(int, sys.stdin.readline().split()))
    solution(heights, 0, int(n)-1)
    print(answer)
    answer = 0
