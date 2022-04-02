'''
람다 함수 (익명의 함수 - 이름이 없는 함수)
'''

def plus_one(x):
    return x+1
print(plus_one(2))

plus_two=lambda x: x+2 #람다함수 사용
print(plus_two(1))

def plus_1one(x):
    return x+1

  a=[1,2,3]

print(list(map(plus_1one, a))) #함수를 정의한 경우
print(list(map(lambda x: x+1, a))) #람다함수 표현한 경우
