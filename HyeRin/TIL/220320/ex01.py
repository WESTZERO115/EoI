#변수의 두 개의 값을 서로 바꾸는 예제

#num1이라는 변수에 100을 저장함
num1 = 100
num2 = 200


#num1의 데이터 타입을 확인하는 방법 - type()함수
#print(type(num1))

print("num1 : ", num1, ", num2 : ", num2)

#두 개의 변수값을 바꾸기 위해서는 임시 변수가 필요하다.
temp = num1
num1 = num2
num2 = temp
print("num1 : ", num1, ", num2 : ", num2)
