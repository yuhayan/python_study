# 1181 단어 정렬
# n = int(input())
# list = []

# for i in range(n):
#   list.append(input())
#   list.sort(key = len)

# for i in list:
#     print(i)
#---------------------------------------------------
# 1436 영화감독 숌
# n = int(input())
# first = 666
# cnt = 0

# while True:
#   if '666' in str(first):
#     cnt+=1
#   if cnt == n:
#     print(first)
#     break
#   first += 1
#---------------------------------------------------
# 2609 최대공약수 최소공배수
# a, b = map(int, input().split())

# def gcd(a, b):
#       while b > 0:
#             mod = a%b
#             a = b
#             b = mod
#       return a

# def lcm(a, b):
#       res = a*b / gcd(a,b)
#       return res

# print(gcd(a,b))
# print(int(lcm(a,b)))
#---------------------------------------------------
# 2751 수 정렬하기 2
# import sys

# n = int(sys.stdin.readline())
# num_list = []

# for _ in range(n):
#       num_list.append(int(sys.stdin.readline()))

# num_list.sort()

# for i in num_list:
#   print(i)
#---------------------------------------------------
# 7568 덩치
# n = int(input())
# spec = []

# for _ in range(n):
#   w, h = map(int, input().split())
#   spec.append((w,h))

# for i in spec:
#   rank = 1
#   for j in spec:
#     if i[0] < j[0] and i[1] < j[1]:
#       rank += 1

#   print(rank, end=' ')
#---------------------------------------------------
# 10814 나이순 정렬
# n = int(input())
# user = []

# for _ in range(n):
#   age, name = input().split()
#   user.append((int(age),name))

# user.sort(key = lambda x: x[0])

# for i in user:
#       print(i[0],i[1])

#---------------------------------------------------
# 10989 수 정렬하기3
# import sys

# n = int(sys.stdin.readline())
# num_list = [0] * 10001

# for i in range(n):
#   num_list[int(sys.stdin.readline())] += 1

# for i in range(10001):
#   if num_list[i] != 0:
#     for j in range(num_list[i]):
#       print(i)
#---------------------------------------------------
# 11650 좌표 정렬하기
# n = int(input())
# location=[]

# for _ in range(n):
#   x, y = map(int, input().split())
#   location.append((x,y))
# location.sort()

# for i in location:
#       print(i[0], i[1])
#---------------------------------------------------
# 11651 좌표 정렬하기2
# import sys
# n = int(sys.stdin.readline())
# location=[]

# for _ in range(n):
#   x, y = map(int, sys.stdin.readline().split())
#   location.append((x,y))

# location.sort(key = lambda x:(x[1], x[0]))

# for i in location:
#       print(i[0], i[1])

#---------------------------------------------------

#---------------------------------------------------

#---------------------------------------------------

#---------------------------------------------------

#---------------------------------------------------


    