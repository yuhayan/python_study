def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b #최대공약수

def solution(arr):
    answer = 0
    
    # a와 b의 최소공배수는 a*b / (a,b의 최대공약수)
    for i in range(len(arr)-1):
        b = gcd(arr[i], arr[i+1])
        arr[i+1] = (arr[i] * arr[i+1]) / b
        print(arr)
    answer = arr[-1]
    return answer
