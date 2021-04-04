import sys


# https://algospot.com/judge/problem/read/PICNIC

def rec(removed_friend_list, visited, n):
    global answer
    if len(visited) == n:
        answer += 1
        return
    if len(removed_friend_list)*2 + len(visited) < n:
        return

    for i in range(len(removed_friend_list)):
        p1, p2 = removed_friend_list[i]
        if p1 not in visited and p2 not in visited:
            visited[p1] = True
            visited[p2] = True
            rec(removed_friend_list[i + 1:], visited, n)
            del visited[p1]
            del visited[p2]


def solution(n, friend_list):
    global answer
    answer = 0
    for i in range(len(friend_list)):
        visited = {}
        p1, p2 = friend_list[i]
        visited[p1] = True
        visited[p2] = True
        rec(friend_list[i+1:], visited, n)
        del visited[p1]
        del visited[p2]
    print(answer)
answer = 0
c = int(sys.stdin.readline())
for _ in range(c):
    n, m = map(int, sys.stdin.readline().split())
    friends = list(map(int, sys.stdin.readline().split()))
    friend_list = []
    for i in range(m):
        p1, p2 = friends[2 * i], friends[2 * i + 1]
        friend_list.append([p1,p2])
    solution(n, friend_list)

#
# 1
# 6 10
# 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5