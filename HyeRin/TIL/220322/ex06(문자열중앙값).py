# 문자열의 중앙에 있는 문자를 추출
# 문자열이 "weekend"라면 중앙의 문자는 "k"가됨
# 문자열이 짝수 개의 문자를 갖고있다면 중앙의 문자로 2개를 출력함
# 문자열이 "monday"라면 중앙의 문자는 "nd"가 됨

str_1 = input("문자열을 입력하세요 : ")
length = len(str_1) # 문자열의 길이를 구하기

if (length % 2 ) == 1 :
    ch = str_1[length//2]
    print("중앙에 있는 한 글자는 ", ch)
else:
    ch1 = str_1[length//2 - 1]
    ch2 = str_1[length//2]
    print("중앙에 있는 두 글자는 ", ch1, ch2)
