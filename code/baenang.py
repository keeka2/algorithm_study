# https://www.acmicpc.net/problem/12865
import sys

def solution(prd, K):
    DP = []
    for _ in range(len(prd)+1):
        DP.append([0 for _ in range(K+1)])
    prd_num = 1
    for p in prd:
        w,v = p[0], p[1]
        for cur_weight in range(1, K+1):
            if cur_weight - w>=0:
                DP[prd_num][cur_weight] = max(DP[prd_num-1][cur_weight-w] + v, DP[prd_num-1][cur_weight])
            else:
                DP[prd_num][cur_weight] = DP[prd_num-1][cur_weight]
        prd_num+=1
    print(DP[-1][-1])





N, K = map(int, sys.stdin.readline().split(' '))
prd = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split(' '))
    prd.append([W,V])
solution(prd, K)

