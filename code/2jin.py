# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    zero_count = 0
    transform = 0
    while True:
        c = 0
        for w in s:
            if w == "1":
                c += 1
            else:
                zero_count += 1
        s = str(bin(c))[2:]
        transform += 1
        if s == "1":
            answer = [transform, zero_count]
            break

    return answer


s = "01110"
print(solution(s))