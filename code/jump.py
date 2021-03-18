# https://www.acmicpc.net/problem/1890
import sys
def solution(N, board):
    DP = []
    for _ in range(N):
        DP.append([0 for _ in range(N)])

    first_jump = board[0][0]
    DP[first_jump][0] = 1
    DP[0][first_jump] = 1

    for x in range(N):
        for y in range(N):
            jump_size = board[x][y]
            if jump_size == 0:
                continue
            x_jump = x + jump_size
            y_jump = y + jump_size
            if x_jump < N:
                DP[x_jump][y] += DP[x][y]
            if y_jump < N:
                DP[x][y_jump] += DP[x][y]

    print(DP[-1][-1])

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split(" "))))

solution(N, board)

# 4
# 2 3 3 1
# 1 2 1 3
# 1 2 3 1
# 3 1 1 0