import sys

# 0 1 3 6 7 9 12
def solution(min_day, costs):
    sum_list = [0]
    cur_c = 0
    for c in costs:
        cur_c += c
        sum_list.append(cur_c)
    answer = 1000
    for left in range(len(costs)-min_day+1):
        for right in range(left + min_day, len(costs)+1):
            cur_avg = (sum_list[right] - sum_list[left])/(right-left)
            answer = min(cur_avg, answer)
    print(answer)
n = int(sys.stdin.readline())
for _ in range(n):
    s, min_day = map(int, sys.stdin.readline().split())
    costs = list(map(int, sys.stdin.readline().split()))
    solution(min_day, costs)

