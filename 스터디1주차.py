''' 1000번
a, b = input().split()
print(int(a)+int(b))'''

''' 1001번
a, b = input().split()
print(int(a)-int(b))'''

''' 2475번 c
a = list(map(int, input().split())) 
b = [] 
for i in range(0, len(a)) : b.append(a[i]**2) 
print(sum(b)%10)'''

''' 2557번
print("Hello World!") '''

''' 10171번
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")'''

''' 10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")'''

''' 10869
a, b = map(int, input().split()) 
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)'''

''' 10998
a, b = map(int, input().split())
print(a*b) '''

''' 11654
a = input()
print(ord(a))'''

''' 1008
a, b = map(int, input().split())
print(a/b)'''

''' 1330
a, b = map(int, input().split())
if a>b:
  print('>')
elif a<b:
  print('<')
else:
  print('==')'''

''' 2753
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
  print('1')
else:
  print('0')'''

''' 9498
a = int(input())
if 100 >= a >= 90:
  print('A')
elif 89 >= a >= 80:
  print('B')
elif 79 >= a >= 70:
  print('C')
elif 69 >= a >= 60:
  print('D')
else:
  print('F')'''

''' 2438
a = int(input())
for i in range (1,(a+1)):
  print("*"*i)''' 

''' 2429
a = int(input())
for i in range (1,(a+1)):
  print(" "*(a-i) + "*"*i )'''
  
''' 2739 c
a = int(input())
for i in range(1, 10):
  print("%d * %d = %d" %(a, i, a*i))'''

''' 2741
a = int(input())
for i in range(1, a+1, 1):
  print(i)'''

''' 2742
a = int(input())
for i in range(a, 0, -1):
  print(i)'''

''' 2884 c
h, m = map(int, input().split())
if m>44 :
  print(h, m-45)
elif m<45 and h>0 :
  print(h-1, m+15)
else:
  print(23, m+15)'''

''' 10818
n = int(input())
nums = list(map(int, input().split()))
max = nums[0]
min = nums[0]
for i in range (1, len(nums), 1):
  if max < nums[i]:
    max = nums[i]

for i in range (1, len(nums), 1):
  if min > nums[i]:
    min = nums[i]

print(min, max)'''

''' 10871 c
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")'''

''' 10950 c
T = int(input())
for i in range(T):
  A, B = map(int, input().split())
  print(A+B)'''

''' 10951 c
while True:
  try:
      a, b = map(int, input().split())
      print(a+b)
  except:
      break'''

''' 10952 c
while True:
  a, b = map(int, input().split())
  if (a==0 and b==0):
    break
  else: 
   print(a+b)'''

'''' 상수
a, b = input().split()
reversed_a = '';
reversed_b = '';

for i in range(len(a)-1, -1, -1):
  reversed_a +=a[i]
for i in range(len(b)-1, -1, -1):
  reversed_b +=b[i]

print(max(int(reversed_a), int(reversed_b)))'''

'''10809 알파벳찾기
word = input()
alpha = list(range(97,123))

for i in alpha:
  print(word.find(chr(i)))'''