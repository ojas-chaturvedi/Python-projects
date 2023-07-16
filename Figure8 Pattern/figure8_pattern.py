import turtle
import math
import random

def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

def grav_mag(m1,x1,y1,m2,x2,y2):
    return m1*m2/dist(x1,y1,x2,y2)**2

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5,-5,5,5)
screen.title("3 Body Simulation")
screen.colormode(255)

r = 1

m1 = 1
m2 = 1
m3 = 1

m4 = 1
m5 = 1
m6 = 1

m7 = 1
m8 = 1

x1,y1 = 0.97000436*r,-0.24308753*r
x2,y2 = -x1,-y1
x3,y3 = 0,0

vx3,vy3 = -0.93240737*r,-0.86473146*r
vx1,vy1 = -vx3/2,-vy3/2
vx2,vy2 = vx1,vy1

x4,y4 = 0.97000436*r,-0.24308753*r
x5,y5 = -x1,-y1
x6,y6 = 0,0

vx6,vy6 = -0.93240737*r,-0.86473146*r
vx4,vy4 = -vx6/2,-vy6/2
vx5,vy5 = vx4,vy4

x7, y7 = 3, 0
x8, y8 = -3, 0

vx7,vy7 = 0, .25
vx8,vy8 = 0, -.25

t_step = 0.0001

pointer1 = turtle.Turtle()
pointer1.penup()
pointer1.shape("circle")
pointer1.color("red")
pointer1.speed(0)
pointer1.goto(x1,y1)
pointer1.pendown()

pointer2 = turtle.Turtle()
pointer2.penup()
pointer2.shape("circle")
pointer2.color("red")
pointer2.speed(0)
pointer2.goto(x2,y2)
pointer2.pendown()

pointer3 = turtle.Turtle()
pointer3.penup()
pointer3.shape("circle")
pointer3.color("red")
pointer3.speed(0)
pointer3.goto(x3,y3)
pointer3.pendown()

pointer4 = turtle.Turtle()
pointer4.penup()
pointer4.shape("circle")
pointer4.color("orange")
pointer4.speed(0)
pointer4.goto(x4,y4)
pointer4.pendown()

pointer5 = turtle.Turtle()
pointer5.penup()
pointer5.shape("circle")
pointer5.color("orange")
pointer5.speed(0)
pointer5.goto(x5,y5)
pointer5.pendown()

pointer6 = turtle.Turtle()
pointer6.penup()
pointer6.shape("circle")
pointer6.color("orange")
pointer6.speed(0)
pointer6.goto(x6,y6)
pointer6.pendown()

pointer7 = turtle.Turtle()
pointer7.penup()
pointer7.shape("circle")
pointer7.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
pointer7.speed(0)
pointer7.goto(x7,y7)
pointer7.pendown()

pointer8 = turtle.Turtle()
pointer8.penup()
pointer8.shape("circle")
pointer8.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
pointer8.speed(0)
pointer8.goto(x8,y8)
pointer8.pendown()

i = 0

while True:
    i += 1

    f12 = grav_mag(m1,x1,y1,m2,x2,y2)
    f12_theta = math.atan2(y2-y1,x2-x1)
    f13 = grav_mag(m1,x1,y1,m3,x3,y3)
    f13_theta = math.atan2(y3-y1,x3-x1)
    f23 = grav_mag(m2,x2,y2,m3,x3,y3)
    f23_theta = math.atan2(y3-y2,x3-x2)

    f45 = grav_mag(m4,x4,y4,m5,x5,y5)
    f45_theta = math.atan2(y5-y4,x5-x4)
    f46 = grav_mag(m4,x4,y4,m6,x6,y6)
    f46_theta = math.atan2(y6-y4,x6-x4)
    f56 = grav_mag(m5,x5,y5,m6,x6,y6)
    f56_theta = math.atan2(y6-y5,x6-x5)

    f78 = grav_mag(m7,x7,y7,m8,x8,y8)
    f78_theta = math.atan2(y8-y7, x8-x7)

    x1,y1 = vx1*t_step+x1,vy1*t_step+y1
    x2,y2 = vx2*t_step+x2,vy2*t_step+y2
    x3,y3 = vx3*t_step+x3,vy3*t_step+y3
    x4,y4 = vx4*t_step+x4,vy4*t_step+y4
    x5,y5 = vx5*t_step+x5,vy5*t_step+y5
    x6,y6 = vx6*t_step+x6,vy6*t_step+y6
    x7,y7 = vx7*t_step+x7,vy7*t_step+y7
    x8,y8 = vx8*t_step+x8,vy8*t_step+y8

    vx1 += f12*math.cos(f12_theta)/m1*t_step + f13*math.cos(f13_theta)/m1*t_step
    vy1 += f12*math.sin(f12_theta)/m1*t_step + f13*math.sin(f13_theta)/m1*t_step
    vx2 += f12*math.cos(f12_theta+math.pi)/m2*t_step + f23*math.cos(f23_theta)/m2*t_step
    vy2 += f12*math.sin(f12_theta+math.pi)/m2*t_step + f23*math.sin(f23_theta)/m2*t_step
    vx3 += f13*math.cos(f13_theta+math.pi)/m3*t_step + f23*math.cos(f23_theta+math.pi)/m3*t_step
    vy3 += f13*math.sin(f13_theta+math.pi)/m3*t_step + f23*math.sin(f23_theta+math.pi)/m3*t_step

    vx4 += f45*math.cos(f45_theta)/m4*t_step + f46*math.cos(f46_theta)/m4*t_step
    vy4 += f45*math.sin(f45_theta)/m4*t_step + f46*math.sin(f46_theta)/m4*t_step
    vx5 += f45*math.cos(f45_theta+math.pi)/m5*t_step + f56*math.cos(f56_theta)/m5*t_step
    vy5 += f45*math.sin(f45_theta+math.pi)/m5*t_step + f56*math.sin(f56_theta)/m5*t_step
    vx6 += f46*math.cos(f46_theta+math.pi)/m6*t_step + f56*math.cos(f56_theta+math.pi)/m6*t_step
    vy6 += f46*math.sin(f46_theta+math.pi)/m6*t_step + f56*math.sin(f56_theta+math.pi)/m6*t_step
    
    vx7 += f78*math.cos(f78_theta)/m7*t_step
    vy7 += f78*math.sin(f78_theta)/m7*t_step
    vx8 += f78*math.cos(f78_theta+math.pi)/m8*t_step
    vy8 += f78*math.sin(f78_theta+math.pi)/m8*t_step

    if i%5000 == 0:
        pointer1.goto(x1,y1)
        pointer2.goto(x2,y2)
        pointer3.goto(x3, y3)
        pointer4.goto(x4,y4)
        pointer5.goto(x5,y5)
        pointer6.goto(x6,y6)
        pointer7.goto(x7,y7)
        pointer8.goto(x8,y8)