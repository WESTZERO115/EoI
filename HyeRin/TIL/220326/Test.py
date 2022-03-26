
'''
변수명 정하기
1) 영문, 숫자, _ 로 이루어진다
2) 대소문자를 구분한다.
3) 문자나, _ 로 시작한다.
4) 특수문자를 사용하면 안된다($, %)
5) 키워드를 사용하면 안된다(if, for 등)
'''

a=1
A=2
A1=3
_b=4
#2b=4
print(a, A, A1)

#값 교환
a, b=10,20
print(a,b)
a, b=b, a
print(a, b)

#변수 타입
a=12345
print(a)
print(type(a))
b=1234.1234556
print(b)
print(type(b))
a="student"
print(a)
print(type(a))

#출력방식
print("number")
a,b,c=1,2,3
print(a,b,c)
print("number : ",a,b,c)
print(a,b,c, sep=', ') #a,b,c 사이에 콤마넣고 띄어쓰기
print(a,b,c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c)
