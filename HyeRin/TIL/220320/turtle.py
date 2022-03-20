#파이썬 터틀 모듈을 가져오고 있다.
import turtle

#그림을 그리기 위해서 캔버스(그리는 공간)을 불러온다.
t = turtle.Pen()

# 캔버스의 마우스 형태의 그림을 거북이 모양으로 바꾸어 준다.
t.shape("turtle")

#펜의 색깔을 파란색으로 설정
t.pencolor("blue")

#직선으로 100픽셀만큼 선을 그려라.
t.forward(100)

#오른쪽 90도만큼 방향을 바꾸어라
t.right(90)

#오른쪽 방향으로 90픽셀만큼 그려라
t.forward(90)

t.right(90)
t.forward(90)

t.right(90)
t.forward(90)
