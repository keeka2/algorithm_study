# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    left = 0
    right = len(height) - 1

    answer = (right - left)*min(height[left], height[right])
    while True:
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left +=1
            right -=1

        if left >= right:
            break
        else:
            temp_answer = (right - left)*min(height[left], height[right])
            answer = max(answer, temp_answer)

    print(answer)
    return answer

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
