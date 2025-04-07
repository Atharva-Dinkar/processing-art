from math import *
import random as rd

num = 40
speed = 4
lim = 300.0
x_max = (displayWidth/100)*100
y_max = displayHeight-100

x_coord = [0]*(num+1)
y_coord = [0]*(num+1)
direction = [0]*num
for i in range(num):
    x_coord[i] = rd.randint(0, x_max)
    y_coord[i] = rd.randint(0, y_max)
    direction[i] = rd.uniform(0, 2*PI)

def setup():
    global displayWidth, displayHeight 
    size((displayWidth/100)*100, displayHeight-100)
    background(0, 0, 0)
    # print((displayWidth/100)*100, displayHeight-100)
    
    

def draw():
    
    background(0, 0, 0)
    if keyPressed:
            if key == 'f':
                factor = 0
    else:
        factor = 1
    x_coord[-1] = mouseX
    y_coord[-1] = mouseY
    fill(255, 255, 255)
    for i in range(num+1):
        circle(x_coord[i], y_coord[i], 5)
        
    stroke(255, 255, 255)
    for i in range(num):
        x1 = x_coord[i]
        y1 = y_coord[i]
        for j in range(i, num+1):
            if ((x_coord[j] >= x1 + lim) or (x1 >= x_coord[j] + lim) or (y_coord[j] >= y1 + lim) or (y1 >= y_coord[j] + lim)):
                continue
            l = sqrt(((x1-x_coord[j])*(x1-x_coord[j]))+((y1-y_coord[j])*(y1-y_coord[j])))
            if (l < lim):
                k = 255.0*(lim-l)/lim
                stroke(k, k, k)
                line(x_coord[i], y_coord[i], x_coord[j], y_coord[j])
        x_coord[i] += factor*speed*cos(direction[i])
        y_coord[i] += factor*speed*sin(direction[i])
        if ((x_coord[i] < 0) or (x_coord[i] > x_max)):
            x_coord[i] = rd.randint(0, x_max)
        if ((y_coord[i] < 0) or (y_coord[i] > y_max)):
            y_coord[i] = rd.randint(0, y_max)
            
        if keyPressed:
            if key == 'f':
                factor = 0
        else:
            factor = 1
    
