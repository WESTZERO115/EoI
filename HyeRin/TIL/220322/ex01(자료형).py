from math import *

#파이썬에서의 자료형(Data-type)
#int형을 출력
print(type(17))

#float형을 출력
print(type(17.0827))

#str형을 출력
print(type("안녕하세요"))

#반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱
#반지름이 5인 구의 부피
r = 5.0
volume = 4.0/3.0  * pi * r ** 3
volume2 = 4.0/3.0  * pi * pow(r, 3)
print("구의 부피 : ", volume, volume2)
print("파이 값 : ", pi)

#구의 겉넓이 공식 : 4 * PI * r의 제곱
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이 : ", outer_area)
