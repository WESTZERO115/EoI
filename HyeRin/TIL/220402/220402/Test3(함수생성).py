'''
함수 만들기
'''

def add(a, b): #함수를 먼저 정의해야 인터프리터가 인식할 수 있음
    c = a + b
    print(c)
add(3, 2)
add(5, 7)

def add(a, b):
    c=a+b
    return c #return은 함수를 종료하는 역할
x=add(3,2)
print(x)

def add(a, b):
    c=a+b
    d=a-b
    return c, d
print(add(3,2))

def isPrime(x): #소수를 출력하는 함수
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=' ')
