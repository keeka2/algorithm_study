# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import deque


def lengthOfLongestSubstring(s):
    current_string = deque([])
    current_string_word = {}
    answer = 0
    for word in s:
        if word in current_string_word:
            answer = max(answer, len(current_string))
            while current_string:
                left_word = current_string.popleft()
                del current_string_word[left_word]
                if left_word == word:
                    break
        current_string.append(word)
        current_string_word[word] = True
        print(current_string)
    answer = max(len(current_string), answer)
    return answer


s = "pwwkew"
answer = lengthOfLongestSubstring(s)
print(answer)
