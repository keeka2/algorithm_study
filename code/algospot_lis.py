# https://algospot.com/judge/problem/read/LIS
import sys

def binary_search(lis_arr, target):
    left = 0
    right = len(lis_arr)

    while left < right:
        mid = (left + right) // 2
        if lis_arr[mid] == target:
            left = mid
            break
        elif lis_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if lis_arr[left] > target:
        lis_arr[left] = target
    elif lis_arr[left] < target:
        lis_arr[left + 1] = target
    else:
        lis_arr[left] = target
    # print(lis_arr)


def lis(arr):
    if not arr:
        print(0)
        return
    lis_arr = [arr[0]]
    for n in arr[1:]:
        if n > lis_arr[-1]:
            lis_arr.append(n)
        elif n == lis_arr[-1]:
            pass
        else:
            binary_search(lis_arr, n)
    print(len(lis_arr))
#
# binary_search([5,6,7,9], 2)
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    sys.stdin.readline()
    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    lis(arr)