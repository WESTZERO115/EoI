#사용자로부터 참석하는 인원의 수를 받아 해당하는 인원의 수에 따라서
#치킨은 인원당 1마리, 맥주는 인원당 2잔, 케이크는 인원당 4개를 출력

number = int(input("참석자 수를 입력하세요 : "))
chickens = number
beers = number * 2
cakes = number * 4

print("치킨의 수 : ", chickens)
print("맥주의 수 : ", beers)
print("케이크의 수 : ", cakes)
