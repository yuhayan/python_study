def solution(A,B):
    answer = 0
    # A가 최솟값, B는 최대값이어야 곱이 최솟값이 됨
    A.sort()
    B.sort(reverse = True)
    
    for a, b in zip(A,B):
        answer += a*b        
    return answer
