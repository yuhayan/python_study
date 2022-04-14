from itertools import permutations

def solution(numbers):
    nums = []
    for i in range(1, len(numbers)+1):
        temp = permutations(numbers, i)
        for j in temp:
            nums.append(int(''.join(j)))
    
    nums = list(set(nums))
    
    answer = len(nums)
    for i in nums:
        if i < 2:
            answer -= 1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                answer -= 1
                break
    # print(nums)
    return answer
