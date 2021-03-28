# https://www.acmicpc.net/problem/16930
import sys


def solution(start, end, K, board, visited):
    max_x = len(board)
    max_y = len(board[0])
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for k in range(2, K + 1):
        for i in range(4):
            dx.append(dx[i] * k)
            dy.append(dy[i] * k)

    move_length = 4*K

    for x in range(max_x):
        for y in range(max_y):
            if board[x][y] == "#":
                visited[x][y] = 1

    bfs = [start]
    count = 0
    while bfs:
        temp_bfs = []
        count += 1
        while bfs:
            x, y = bfs.pop()
            for i in range(move_length):
                nxt_x = x + dx[i]
                nxt_y = y + dy[i]
                if 0 <= nxt_x < max_x and 0 <= nxt_y < max_y:
                    if visited[nxt_x][nxt_y] == 0:
                        visited[nxt_x][nxt_y] = 1
                        temp_bfs.append([nxt_x, nxt_y])
                if x == end[0] and y == end[1]:
                    return count
        for v in visited:
            print(v)
        print()
        bfs = temp_bfs[:]
    return -1


N, M, K = list(map(int, sys.stdin.readline().split(" ")))
board = []
visited = []
for i in range(N):
    board.append(list(sys.stdin.readline().strip()))
    visited.append([0 for _ in range(M)])

x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split(" ")))
start = [x1 - 1, y1 - 1]
end = [x2 - 1, y2 - 1]
visited[x1 - 1][y1 - 1] = 1
c = solution(start, end, K, board, visited)
print(c)
