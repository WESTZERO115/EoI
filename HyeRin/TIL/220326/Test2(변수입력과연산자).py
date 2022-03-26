'''
변수입력과 연산자
'''
a=input("숫자를 입력하세요 : ")
print(a)

a,b=(input("숫자를 입력하세요 : ").split() #split() 함수는 띄어쓰기를 분리자로 하여 문자(a,b)를 분리함
print(a, b)
print(a+b)
a=int(a)
b=int(b)
c=a+b
print(c)
print(type(c))

a,b=map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a=4.3
b=5
c=a+b
print(type(c))
print(c)
