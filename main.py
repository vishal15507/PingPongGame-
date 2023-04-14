from turtle import Screen
from paddles import Paddle
from Pong_Game.border import Border
from ball import Ball


screen= Screen()
screen.bgcolor("lavender")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)


border1=Border()
border1.draw_border()
#border.hideturtle()



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

score_left=0
score_right=0
game_play=True
while game_play==True:
    screen.update()
    ball.move()              #we can use time modele as well but it will have that lagging effect on p[addles
    if ball.ycor()>=280 or ball.ycor()<=(-280):
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_ball()
        score_left+=1
        print(f"left={score_left}")
    if ball.xcor()<-380:
        ball.reset_ball()
        score_right+=1
        print(f"right={score_right}")
screen.exitonclick()