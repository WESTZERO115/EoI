'''
리스트와 내장함수(1)
'''
import random as r
a=[]
print(a)
b=list()
print(b)

a=[1,2,3,4,5]
print(a)

b=list(range(1,11))
print(b)

c=a+b
print(c)

print(a)
a.append(6) #배열 맨 뒤에 6 넣기
print(a)

a.insert(3, 7) #배열 3번자리에 7 넣기
print(a)

a.pop() #배열 맨 뒤의 값 제거
print(a)
a.pop(3) #배열 3번자리 값 제거
print(a)

a.remove(4) #4라는 값 제거
print(a)

print(a.index(5)) #5의 인덱스값 알려줌

a=list(range(1,11))
print(a)
print(sum(a)) #배열에있는 값 모두 합산
print(max(a)) #배열에 있는 수 중에 제일 큰 값 출력
print(min(a)) #배열에 있는 수 중에 제일 작은 값 출력
print(min(7, 5)) #7과 5 중에 작은 값 출력

a=list(range(1,11))
print(a)
r.shuffle(a) #배열 a의 값들을 무작위로 섞음
print(a)
a.sort(reverse=True) #내림차순으로 정리
print(a)
a.sort() #오름차순으로 정리
print(a)
a.clear() #배열 값 없
print(a)
