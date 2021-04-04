# https://algospot.com/judge/problem/read/FENCE
import sys


def solution(board, word_dict, find_word):
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    start_word = find_word[0]
    if start_word in word_dict:
        stack = word_dict[start_word][:]
        idx_stack = [1 for _ in range(len(stack))]
    else:
        return "NO"

    while stack:
        cur_x, cur_y = stack.pop()
        cur_idx = idx_stack.pop()

        if cur_idx == len(find_word):
            return "YES"
        word = find_word[cur_idx]
        if word not in word_dict:
            return "NO"

        for i in range(8):
            nxt_x, nxt_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nxt_x < 5 and 0 <= nxt_y < 5 and word == board[nxt_x][nxt_y]:
                stack.append([nxt_x, nxt_y])
                idx_stack.append(cur_idx + 1)
        if not stack:
            return "NO"
    return "YES"


c = int(sys.stdin.readline())
for _ in range(c):
    board = []
    word_dict = {}
    for x in range(5):
        row = list(sys.stdin.readline().strip())
        board.append(row)
        for y in range(5):
            w = row[y]
            if w in word_dict:
                word_dict[w].append([x, y])
            else:
                word_dict[w] = [[x, y]]
    for _ in range(int(sys.stdin.readline().strip())):
        find_word = sys.stdin.readline().strip()
        pos = solution(board, word_dict, find_word)
        print(find_word, pos)
