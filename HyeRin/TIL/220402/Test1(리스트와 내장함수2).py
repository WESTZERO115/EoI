'''
리스트와 내장함수(2)
'''

a=[23,12,36,53,29]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

for x in enumerate(a): #(인덱스번호, 값)의 형태(튜플)로 출력해줌
    print(x)

b=(1,2,3,4,5)
print(b[0])
b[0] = 7 #튜플은 값을 변경할 수 없어서 오류발생

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(60>x for x in a): #하나라도 오류난다면 False가 출력됨
    print("YES")
else:
    print("NO")
print()

if any(15>x for x in a): #조건이 하나라도 성립된다면 True가 출력됨
    print("YES")
else:
    print("NO")
