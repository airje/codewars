def solution(nums):
    a=[]
#     nums.sort()
    try:
        nums.sort()
        return nums
    except AttributeError:
        return a