# https://programmers.co.kr/learn/courses/30/lessons/72413

def check():
    pass
def solution(n, s, a, b, fares):
    fares.sort(key=lambda x: x[2])
    answer = 0
    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)
