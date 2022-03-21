#내장 함수 및 math 라이브러리 함수 이용
from math import *     #한번만 코딩하면 된다. math라이브러리 함수의 모든 것을 호출

#4.0의 제곱근 구하기
print(sqrt(4.0))

#3.0의 제곱 구하기, 연산자 **와 동일함
print(pow(3,2))

#절대값 구하기
print(abs(-77))
print(abs(77))

#반올림 하기
print(round(1.222))
print(round(1.572))

#주어진 매개변수 값 중에서 최대값 구하기
print(max(10, -20, 100, 9999))
#주어진 매개변수 값 중에서 최소값 구하기
print(min(10, -20, 100, 9999))
