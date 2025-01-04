import turtle

suyog = turtle.Screen()
suyog.bgcolor("black")
one_piece = turtle.Turtle()
one_piece.width(7)
colors = ["#f5ac2f", "#279cf5", "#d820f5", "#a2f52f", "#f527c1"]


def draw_suyog(i, x, y):
    one_piece.pencolor("linen")
    one_piece.color(colors[i % 7])
    one_piece.lt(70)
    one_piece.penup()
    one_piece.goto(x, y)
    one_piece.pendown()
    one_piece.circle(22)
    one_piece.end_fill()


def ballon(x, y):
    one_piece.pensize(4)
    for i in range(5):
        draw_suyog(i, x, y)


def f1():
    for i in range(7):
        one_piece.pensize(5)
        one_piece.pencolor('light blue')
        one_piece.color(colors[i % 19])
        one_piece.begin_fill()
        one_piece.left(330)
        one_piece.forward(55)
        one_piece.begin_fill()
        one_piece.rt(110)
        one_piece.circle(33)
        one_piece.end_fill()
        one_piece.rt(11)
        one_piece.backward(33)
        one_piece.end_fill()


def cake(x, y):
    one_piece.fd(x)
    one_piece.rt(90)
    one_piece.fd(y)
    one_piece.rt(90)
    one_piece.fd(x)
    one_piece.rt(90)
    one_piece.fd(y)


def move(x, y):
    one_piece.up()
    one_piece.setposition(0, 0)
    one_piece.setheading(90)
    one_piece.rt(90)
    one_piece.fd(x)
    one_piece.lt(90)
    one_piece.fd(y)
    one_piece.pendown()


def mov(x, y):
    one_piece.up()
    one_piece.setposition(0, 0)
    one_piece.setheading(90)
    one_piece.lt(90)
    one_piece.fd(x)
    one_piece.rt(90)
    one_piece.fd(y)
    one_piece.pendown()


def A(size):
    one_piece.rt(19)
    one_piece.forward(size)
    one_piece.rt(141)
    one_piece.fd(size)
    one_piece.backward(size / 2)
    one_piece.rt(105)
    one_piece.fd(int(size / 3))


def B(size):
    one_piece.forward(size)
    one_piece.rt(90)
    for i in range(18):
        one_piece.rt(9)
        one_piece.fd(size // 20)
    for i in range(18):
        one_piece.rt(size // 5)
        one_piece.backward(size // 20)


def D(size):
    one_piece.fd(size)
    one_piece.rt(90)
    one_piece.fd(size // 10)
    for i in range(13):
        one_piece.rt(13)
        one_piece.fd(size // 8)


def E(size):
    one_piece.rt(90)
    one_piece.fd(int(size / 3))
    one_piece.back(int(size / 3))
    one_piece.left(90)
    one_piece.fd(size / 2)
    one_piece.rt(90)
    one_piece.fd(int(size / 3))
    one_piece.back(int(size / 3))
    one_piece.lt(90)
    one_piece.fd(size / 2)
    one_piece.rt(90)
    one_piece.fd(int(size / 3))


def H(size):
    one_piece.fd(size)
    one_piece.backward(size // 2)
    one_piece.rt(90)
    one_piece.fd(size // 2)
    one_piece.lt(90)
    one_piece.fd(size // 2)
    one_piece.backward(size)


def I(size):
    one_piece.fd(size)
    one_piece.rt(90)
    one_piece.circle(size // 8)

def L(size):
    one_piece.rt(90)
    one_piece.fd(int(size / 2))
    one_piece.back(int(size / 2))
    one_piece.lt(90)
    one_piece.fd(size)

def N(size):
    one_piece.fd(size)
    one_piece.rt(150)
    one_piece.fd(size + int(size / 6))
    one_piece.lt(150)
    one_piece.fd(size)


def P(size):
    one_piece.fd(size)
    one_piece.rt(90)
    one_piece.fd(size // 8)
    for i in range(8):
        one_piece.rt(20)
        one_piece.fd(size // 9)

def R():
    one_piece.fd(60)
    one_piece.rt(90)
    one_piece.fd(7)
    for i in range(15):
        one_piece.rt(12)
        one_piece.fd(3)
    one_piece.lt(120)
    one_piece.fd(40)


def S(size):
    one_piece.rt(90)
    for i in range(0, 5):
        if i < 3:
            one_piece.fd(size / 2)
            one_piece.lt(90)
            if i == 2:
                one_piece.rt(90)
        else:
            one_piece.right(90)
            one_piece.fd(size / 2)


def T(size):
    one_piece.fd(size)
    one_piece.rt(90)
    one_piece.fd(size // 2)
    one_piece.backward(size // 2)


def Y(size):
    one_piece.fd(size)
    one_piece.left(60)
    one_piece.fd(size // 2)
    one_piece.backward(size // 2)
    one_piece.rt(90)
    one_piece.fd(size // 1.5)

one_piece.speed(19)


mov(120, 30)
one_piece.color("#f7b543")
# one_piece.color(colors[8 % 5])
one_piece.begin_fill()
cake(40, 180)
one_piece.end_fill()
mov(110, 75)
one_piece.color("#d152f7")
one_piece.begin_fill()
cake(40, 160)
one_piece.end_fill()
mov(100, 120)
one_piece.color("#f54eb8")
one_piece.begin_fill()
cake(40, 140)
one_piece.end_fill()
mov(30, 170)
one_piece.width(11)
one_piece.pencolor("red")
one_piece.circle(7)
move(180, 307)
mov(0, 0)
ballon(-490, 200)
ballon(490, 200)
ballon(183, -150)
ballon(-133, -150)

one_piece.speed(7)
one_piece.width(9)
one_piece.pencolor("#319df5")
mov(150, 205)
one_piece.pencolor("#95ed28")
style = ('Arial', 50, 'italic')
one_piece.write("SUYOG", font=style)

one_piece.pencolor("cyan")
one_piece.width(13)
mov(260, -80)
H(100)
one_piece.width(7)
mov(190, -80)
A(65)
mov(135, -80)
P(60)
mov(100, -80)
P(60)
mov(52, -80)
Y(60)
mov(28, -80)
B(60)
move(12, -80)
I(60)
move(36, -80)
R()
move(80, -80)
T(100)
move(102, -80)
H(60)
move(150, -80)
one_piece.pencolor('hotpink')
D(200)
move(160, -80)
A(60)
move(220, -80)
Y(60)
suyog.exitonclick()