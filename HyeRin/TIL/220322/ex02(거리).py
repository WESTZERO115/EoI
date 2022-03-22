from math import *

#지구에서 가장 가까운 별은 프록시마 켄타우리라는 별
#프록시마 켄타우리는 지구로부터 40 * 10의 12승 km 떨어져있음
#빛의 속도로 이 별에 간다면 시간이 얼마나 걸리는지

#빛의 속도 값
light_speed = 300000
distance = 40 * pow(10, 12)
print(distance)

seconds = distance /light_speed
print("걸리는 시간 : ", seconds, "초")
light_year = seconds / (60 * 60 * 24 * 365)
print("걸리는 연도 : ", light_year, "년")
