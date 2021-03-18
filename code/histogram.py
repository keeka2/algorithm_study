# https://www.acmicpc.net/problem/1725
import sys, copy

answer = 0
def histogram(board):
    global answer
    max_h = 0
    min_h = 1000000000
    for h in board:
        min_h = min(h, min_h)
        max_h = max(h, max_h)
    size = min_h * len(board)
    answer = max(size, answer)
    index = board.index(min_h)
    if min_h == max_h:
        pass
    else:
        if index>0:
            histogram(board[:index])
        if index+1<len(board):
            histogram(board[index+1:])



n = int(sys.stdin.readline())
board = []
for i in range(n):
    board.append(int(sys.stdin.readline()))
histogram(board)
print(answer)
