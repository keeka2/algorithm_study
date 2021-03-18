# https://www.acmicpc.net/problem/1890
import sys
def solution(numbers):
    DP = [[1,0], [0,1]]

    for i in range(2, 41):
        zero = DP[i-1][0] + DP[i-2][0]
        one = DP[i-1][1] + DP[i-2][1]
        DP.append([zero, one])
    for n in numbers:
        print(DP[n][0], DP[n][1])

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

solution(numbers)
