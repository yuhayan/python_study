def solution(numbers):
    # 숫자들을 문자열로 변환하여 정렬
    nums = [str(n) for n in numbers]
    nums.sort(key=lambda n: n*3, reverse = True)
    # 3을 곱해주는 이유: [9,5,34,30,3] 일 때 30보다 3이 앞으로 와야한다. num은 1000이하의 숫자이므로 최댓값을 고려해 3을 곱해주고, 3을 곱하면 
    #[999,555,343434,333,303030] 으로 정렬 가능
    # print(nums)
    
    # 굳이 int로 했다가 다시 str하는 이유는
    # [0,0,0,0]같은 경우는 0으로 반환시켜주기 위해 int로 변환
    answer = str(int(''.join(nums)))
    
    return answer
