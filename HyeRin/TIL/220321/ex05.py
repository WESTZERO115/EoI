#초를 입력받아서 시, 분, 초로 변경하는 프로그램

time = int(input("초를 입력하세요 : "))

#60으로 나눈 나머지는 초를 의미
seconds = time % 60

#60으로 나눈 몫을 다시 60으로 나눈 나머지는 분을 의미
minutes = seconds % 60

#60으로 나눈 몫을 다시 60으로 나눈 몫은 시간을 의미
hour = (time // 60) // 60
print(hour, "시간 ", minutes, "분 ", seconds, "초" )
