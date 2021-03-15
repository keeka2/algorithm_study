# https://programmers.co.kr/learn/courses/30/lessons/70130
def solution(a):
    num_index = {}
    num_list = []
    for i in range(len(a)):
        if a[i] in num_index:
            num_index[a[i]]["idx_list"].append(i)
            num_index[a[i]]["count"] += 1
        else:
            num_index[a[i]] = {"idx_list": [], "count": 0}
            num_index[a[i]]["idx_list"].append(i)
            num_index[a[i]]["count"] += 1

    for n in num_index:
        num_list.append([n, num_index[n]["idx_list"], num_index[n]["count"]])

    num_list.sort(key=lambda x:x[2])
    ret_answer = 0
    while num_list:
        cur_list = num_list.pop()
        number, index_list, count = cur_list[0], cur_list[1], cur_list[2]
        if ret_answer >= count * 2:
            break
        visited_index = {-1:True, len(a):True}
        answer = 0
        for index in index_list:
            left = index - 1
            right = index + 1
            if left not in visited_index and a[left] != number:
                answer += 2
                visited_index[left] = True
            elif right not in visited_index and a[right] != number:
                answer += 2
                visited_index[right] = True
            else:
                pass
        ret_answer = max(ret_answer, answer)

    return ret_answer

a = [4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]
print(solution(a))