from vpython import*
import random
from time import*

def make_w4():   
    
    f1 = box(pos=vector(0,-20,0) , length = 40 , width = 40, heigth = 0.5, color = color.white
    )
    return f1 

def make_w():

    f2 = box(pos=vector(0,20,0) , length = 40 ,  width = 40, heigth = 0.5, color = color.white
    )
    return f2

def make_wall1():   
    f3 = box(pos=vector(20,0,0) , size = vector(0.5,40,40), color = color.white
    )
    return f3

def make_wall2():
    f4 = box(pos=vector(-20,0,0) , size = vector(0.5,40,40) , color = color.white
    )
    return f4

def  make_wall3():  
    f5 = box(pos=vector(0,0,-20), size = vector(40,40,0.5) , color = color.white
    )
    return f5


def make_balls():
    balls = []
    for i in range(20):
        x=random.randint(-15,15)
        y=random.randint(-10,19)
        z=random.randint(-13,0)
        c = random.choice([color.green, color.cyan, color.red, color.yellow])
        ball=sphere(pos=vector(x,y,z),radius=1,color=c)
        vx = random.random() *2 -1
        vy = random.random() *2 -1
        vz = random.random() *2 -1
        ball.velocity = vector(vx, vy, vz)
        balls.append(ball)
    return balls

def move_balls(balls,dt):
    for ball in balls:
        ball.pos = ball.pos + ball.velocity * dt

def hit_w4(balls):
    for ball in balls:
        if ball.pos.y < (f.pos.y + 0.5):
            ball.velocity.y = (-1)*ball.velocity.y 
            
        

def hit_w(balls):
    for ball in balls:
        if ball.pos.y > (c.pos.y - 1):
            ball.velocity.y = (-1)*ball.velocity.y

def hit_w1(balls):
    for ball in balls:
        if ball.pos.x > w1.pos.x - 0.5:
            ball.velocity.x = (-1)*ball.velocity.x

def hit_w2(balls):
    for ball in balls:
        if ball.pos.x < w2.pos.x + 0.5:
            ball.velocity.x = (-1)*ball.velocity.x

def hit_w3(balls):
    for ball in balls:
        if ball.pos.z < w3.pos.z + 0.5 or ball.pos.z > 15:
            ball.velocity.z = (-1)*ball.velocity.z

def hit_balls(balls):
    for i in balls:
        for j in balls:
            if i!=j and ((i.pos.x-j.pos.x)**2 + (i.pos.y-j.pos.y)**2 + (i.pos.z-j.pos.z)**2)**0.5 < 2:
                i.velocity= - i.velocity
                j.velocity=- j.velocity
                i.color=color.black
                j.color=color.black

def make_cube():
    make_w4()
    make_w()
    make_wall1()
    make_wall2()
    make_wall3()

balls = make_balls()
dt = 0.3
t = 0
t+=dt
f = make_w4()
c = make_w()
w1 = make_wall1()
w2 = make_wall2()
w3 = make_wall3()


while t<10 :
    rate(100)
    move_balls(balls,dt)
    hit_w4(balls)
    hit_w(balls)
    hit_w1(balls)
    hit_w2(balls)
    hit_w3(balls)
    hit_balls(balls)

