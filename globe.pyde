from math import *

t = 0
phi = 0
theta = 0
radius = 400
no_of_pts_phi = 15
no_of_pts_theta = 30
x_ang = 0
y_ang = 0
z_ang = 0
rotation_step = 0.0001

i_spe = 4
j_spe = 18
def spherical(p_angle, t_angle, r):
    x1 = r*sin(p_angle)*cos(t_angle)
    y1 = r*sin(p_angle)*sin(t_angle)
    z1 = r*cos(p_angle)
    return (x1, y1, z1)

def cur_point(p_angle, t_angle, r):
    return (width/2 + radius*sin(p_angle)*sin(t_angle), height/2 - radius*cos(p_angle))

def rotate_x(p, ang):
    x1 = p[0]
    y1 = p[1]
    z1 = p[2]
    x2 = x1
    y2 = y1*cos(ang)-z1*sin(ang)
    z2 = y1*sin(ang)+z1*cos(ang)
    return (x2, y2, z2)

def rotate_y(p, ang):
    x1 = p[0]
    y1 = p[1]
    z1 = p[2]
    x2 = z1*sin(ang)+x1*cos(ang)
    y2 = y1
    z2 = z1*cos(ang)-x1*sin(ang)
    return (x2, y2, z2)

def rotate_z(p, ang):
    x1 = p[0]
    y1 = p[1]
    z1 = p[2]
    x2 = x1*cos(ang)-y1*sin(ang)
    y2 = x1*sin(ang)+y1*cos(ang)
    z2 = z1
    return (x2, y2, z2)

def project_x(p):
    x1 = p[0]
    y1 = p[1]
    z1 = p[2]
    return (width/2 + y1, height/2 - z1)

def setup():
    global displayWidth, displayHeight 
    size((displayWidth/100)*100, displayHeight-100)
    background(0, 0, 0)

def draw():
    global x_ang, y_ang, z_ang, t
    
    background(0, 0, 0)
    stroke(255)
    phi_step = pi/no_of_pts_phi
    theta_step = (2*pi)/no_of_pts_theta
    for i in range(no_of_pts_phi):
        for j in range(2*no_of_pts_theta):
            p1 = spherical(i*phi_step, t+(pi/2)+j*theta_step, radius)
            p2 = spherical(i*phi_step, t+(pi/2)+(j+1)*theta_step, radius)
            p3 = spherical((i+1)*phi_step, t+(pi/2)+j*theta_step, radius)
            p4 = spherical((i+1)*phi_step, t+(pi/2)+(j+1)*theta_step, radius)
            
            
            
            if keyPressed:
                if key == 'q':
                    x_ang += rotation_step
                if key == 'w':
                    y_ang += rotation_step
                if key == 'e':
                    z_ang += rotation_step
                if key == 'a':
                    x_ang -= rotation_step
                if key == 's':
                    y_ang -= rotation_step
                if key == 'd':
                    z_ang -= rotation_step
                if key == 'z':
                    t += 0.00005
                if key == 'x':
                    t -= 0.00005
            
            p1 = rotate_x(p1, x_ang)
            p2 = rotate_x(p2, x_ang)
            p3 = rotate_x(p3, x_ang)
            p4 = rotate_x(p4, x_ang)
            
            p1 = rotate_y(p1, y_ang)
            p2 = rotate_y(p2, y_ang)
            p3 = rotate_y(p3, y_ang)
            p4 = rotate_y(p4, y_ang)
            
            p1 = rotate_z(p1, z_ang)
            p2 = rotate_z(p2, z_ang)
            p3 = rotate_z(p3, z_ang)
            p4 = rotate_z(p4, z_ang)
            
            p1p = project_x(p1)
            p2p = project_x(p2)
            p3p = project_x(p3)
            p4p = project_x(p4)
            
            a = (255*sin(0.5*pi*i/no_of_pts_phi), 127.5*(1+sin(j*theta_step)), 200)
            fill(a[0], a[1], a[2])
            noStroke()
            if (p1[0]+p2[0]+p3[0]+p4[0]) >= 0:
                quad(p1p[0], p1p[1], p2p[0], p2p[1], p4p[0], p4p[1], p3p[0], p3p[1])
            # stroke(255)
            # line(p1p[0], p1p[1], p2p[0], p2p[1])
            # line(p1p[0], p1p[1], p3p[0], p3p[1])
        
    # global t
    # t += 0.02
    
