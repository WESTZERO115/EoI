# 자동판매기를 시뮬레이션하는 프로그램
# 1000원짜리 지폐와 500원, 100원짜리 동전을 사용할 수 있음
# 사용자가 가진 금액을 입력받아 동전으로 거스름돈을 계산

itemPrice = int(input("물건값을 입력하세요 : "))
money = int(input("가진 돈을 입력하세요 : "))

nod_money = money - itemPrice

# 거스름돈 500원 계산
nCoin500 = nod_money // 500
nod_money2 = nod_money - nCoin500 * 500 # 500원으로 나눈 나머지값

# 거스름돈 100원 계산
nCoin100 = nod_money2 // 100
#node_money = nod_money % 100 # 500원으로 나눈 나머지값

print("500원의 개수 : ", nCoin500, ", 100원의 개수 : ", nCoin100)
