def solution(n):
    nums = [0,1]
    
    for i in range(n-1):
        nums.append(nums[i] + nums[i+1])
    # print(nums)
    
    answer = nums[n] % 1234567
    return answer
