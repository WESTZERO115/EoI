# 쇼핑몰에서 물건을 구입할 때, 구입액이 5만원이면 5% 할인을 받음
# 구입금액을 입력받고 최종금액을 출력

total_price = int(input("구입 금액을 입력하세요 : "))

if total_price >- 50000 :
    discount = total_price * 0.05
    sales_price = total_price - discount
    print("할인 대상입니다. 최종 지불금액 : ", sales_price)
else :
    print("할인 금액 대상이 아닙니다. 최종 지불금액 : ", total_price)
