import turtle

okno = turtle.Screen()
okno.title('Hra Pong created by Roman Klimcik')
okno.bgcolor('black')
okno.setup(width=1000, height=800)
okno.tracer(0)

# Hrac 1
hrac_a = turtle.Turtle()
hrac_a.speed(0)
hrac_a.shape('square')
hrac_a.color('green')
hrac_a.shapesize(stretch_wid=7, stretch_len=1)
hrac_a.penup()
hrac_a.goto(-450, 0)

# Hrac 2
hrac_b = turtle.Turtle()
hrac_b.speed(0)
hrac_b.shape('square')
hrac_b.color('green')
hrac_b.shapesize(stretch_wid=7, stretch_len=1)
hrac_b.penup()
hrac_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('gold')
ball.shapesize(stretch_len=2, stretch_wid=2)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4



def hrac_a_up():
    y = hrac_a.ycor()
    y += 25
    hrac_a.sety(y)


def hrac_a_down():
    y = hrac_a.ycor()
    y -= 25
    hrac_a.sety(y)

def hrac_b_up():
    y = hrac_b.ycor()
    y += 25
    hrac_b.sety(y)


def hrac_b_down():
    y = hrac_b.ycor()
    y -= 25
    hrac_b.sety(y)


# ovladani
okno.listen()

okno.onkeypress(hrac_a_up, "w")
okno.onkeypress(hrac_a_down, "s")
okno.onkeypress(hrac_b_up, "Up")
okno.onkeypress(hrac_b_down, "Down")

while True:
    okno.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 375:
        ball.sety(375)
        ball.dy *= -1

    if ball.ycor() < -375:
        ball.sety(-375)
        ball.dy *= -1

    if ball.xcor() > 520:
        ball.goto(0, 0)
        ball.dx *= -1


    if ball.xcor() < -520:
        ball.goto(0, 0)
        ball.dx *= -1

    # if (ball.xcor() > 430 and ball.xcor() < 100) and (ball.ycor() < hrac_b.ycor() + 40 and ball.ycor() > hrac_b.ycor() -40):
    #     ball.setx(340)
    #     ball.dx *= -1

    if (ball.xcor() > 420 and ball.xcor() < 425) and (ball.ycor() < hrac_b.ycor() + 40 and ball.ycor() > hrac_b.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -420 and ball.xcor() > -425) and (ball.ycor() < hrac_a.ycor() + 40 and ball.ycor() > hrac_a.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1

