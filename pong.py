playerA=input("What is playrer 1's name?")
playerB=input("What is playrer 2's name?")

import time
import turtle
import winsound
scoreA=(0)
scoreB=(0)
gamescore=(int(scoreA+scoreB))

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#title screen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0, 0)
pen.write("First to 10 points wins", align= "center", font=("courier", 24, "normal"))

time.sleep(5)
pen.clear()


#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)




#paddle B 
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.3
ball.dy = 0.3


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: {}   {}: {}".format(playerA, scoreA, playerB, scoreB), align="center", font=("courier", 24, "normal"))

#function

def paddle_a_up():
    y= paddle_a.ycor()
    y+=20
    paddle_a.sety(y)


def paddle_a_down():
    y= paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y= paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down") 


#main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("pongsound.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("pongsound", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx*=-1
        scoreA=(scoreA+1)
        print(scoreA)
        print(scoreB)
        print("------------------")
        pen.clear()
        pen.write("{}: {}   {}: {}".format(playerA, scoreA, playerB, scoreB), align="center", font=("courier", 24, "normal"))
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx*=-1
        scoreB=(scoreB+1)
        print(scoreA)
        print(scoreB)
        print("------------------")
        pen.clear()
        pen.write("{}: {}   {}: {}".format(playerA, scoreA, playerB, scoreB), align="center", font=("courier", 24, "normal"))
        
        


    #paddle and ball collission
    if (ball.xcor() > 340 and ball.xcor()<350)and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pongsound", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor()>-350)and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pongsound", winsound.SND_ASYNC)
 


    if paddle_a.ycor() >= 250:
        paddle_a.sety(250)

    if paddle_a.ycor() <= -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() >= 250:
        paddle_b.sety(250)

    if paddle_b.ycor() <= -250:
        paddle_b.sety(-250) 
        
    if scoreA>10 or scoreB>10:
        ball.goto(0,100)
        ball.dx=0
        ball.dy=0
        paddle_a.goto(0,100)
        paddle_b.goto(0,100)
        paddle_a.color("black")
        paddle_b.color("black")
        ball.color("black")
            


        pen=turtle.Turtle()
        pen.speed(0)
        pen.color("yellow")
        pen.up()
        pen.hideturtle()
        pen.goto(0, 0)

        if scoreA> scoreB:
            pen.write("{} is the winner".format(playerA), align="center", font=("courier", 40, "normal"))
        if scoreB> scoreA:
            pen.write("{} is the winner".format(playerB), align="center", font=("courier", 40, "normal"))


    
    
