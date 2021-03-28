# https://programmers.co.kr/learn/courses/30/lessons/72414

def time_to_int(time):
    hh,mm,ss = map(int,time.split(":"))
    int_time = hh*3600 + mm*60 + ss
    return int_time

def time_to_str(time):
    hh = str(time // 3600)
    time = time % 3600

    mm = str(time // 60)
    time = time % 60

    ss = str(time)
    t = [hh,mm,ss]

    tt = []
    for a in t:
        if len(a) == 1:
            tt.append(f"0{a}")
        else:
            tt.append(a)
    return ":".join(tt)


def solution(play_time, adv_time, logs):
    play_time_int = time_to_int(play_time)
    adv_time_int = time_to_int(adv_time)
    play_sec_list = [0 for _ in range(play_time_int+2)]

    for log in logs:
        start, end = log.split("-")
        start_time_int = time_to_int(start)
        end_time_int = time_to_int(end)
        play_sec_list[start_time_int] += 1
        play_sec_list[end_time_int] -= 1
    for i in range(1, len(play_sec_list)):
        play_sec_list[i] += play_sec_list[i-1]
    cur = 0
    for i in range(adv_time_int):
        cur += play_sec_list[i]
    answer = 0
    temp_max_play = cur
    left = 0
    right = adv_time_int
    for _ in range(adv_time_int, len(play_sec_list)):
        cur -= play_sec_list[left]
        cur += play_sec_list[right]
        left += 1
        right += 1
        if cur>temp_max_play:
            temp_max_play = cur
            answer = left
    return time_to_str(answer)