#5000원이 있을 때 사탕의 갯수가 120원이라면 살 수 있는 최대의 사탕 수

myMoney = 5000
candyPrice = 120

#최대로 살 수 있는 사탕의 갯수
#/는 실수, //는 정수로 출력됨
numCandies = myMoney // candyPrice
print("살 수 있는 사탕의 수 : ", numCandies)

#사탕 사고 남은 잔돈
balance = myMoney % candyPrice
print("사탕 사고 남은 돈 : ", balance)
