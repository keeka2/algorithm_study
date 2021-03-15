# https://leetcode.com/problems/jump-game-ii/

def jump_game2(nums):
    answer = 0
    max_length = len(nums) - 1
    cur_position = 0
    while True:
        max_jump_interval = nums[cur_position] + cur_position
        if max_jump_interval >= max_length:
            answer += 1
            break

        nxt_max_jump_interval = 0
        for i in range(cur_position + 1, max_jump_interval + 1):
            temp_nxt_max_jump_interval = i + nums[i]
            if temp_nxt_max_jump_interval > nxt_max_jump_interval:
                cur_position = i
                nxt_max_jump_interval = temp_nxt_max_jump_interval
        answer += 1
    return answer


nums = [2, 3, 0, 1, 4]
print(jump_game2(nums))
