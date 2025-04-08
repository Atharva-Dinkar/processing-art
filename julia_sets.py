import pygame
import time
import numpy as np


def check_if_converge(z, c):
    z1 = z
    for i in range(50):
        # print(z1)
        if np.absolute(z1) > 10:
            return False
        z1 = (z1 * z1) + c
    return True


pygame.init()
L = 500
x_max = 2
x_min = -2
y_max = 1.3
y_min = -1.3
length = L
breadth = int((L*(y_max - y_min))/(x_max - x_min))
iters = 20
blue_square = pygame.image.load('blue_square_tr1x1.png')

screen = pygame.display.set_mode((length, breadth))
pygame.display.set_caption("Julia Sets!")
running = True
count = 0
screen_color = (0, 0, 0)
mandlebrot_list = []

for i in range(length):
    for j in range(breadth):
        z_x = (i / length) * (x_max - x_min) + x_min
        z_y = y_max - (j / breadth) * (y_max - y_min)
        z = z_x + (z_y * 1j)
        if check_if_converge(0, z):
            mandlebrot_list.append((i, j))

screen_grid_complex = np.zeros([length, breadth], dtype=complex)
for i in range(length):
    for j in range(breadth):
        z_x = (i / length) * (x_max - x_min) + x_min
        z_y = y_max - (j / breadth) * (y_max - y_min)
        screen_grid_complex[i][j] = z_x + (z_y * 1j)

# screen.fill(screen_color)

for a in range(len(mandlebrot_list)):
    t = mandlebrot_list[a]
    pygame.draw.rect(screen, (255, 150, 150), pygame.Rect(t[0], t[1], 1, 1))

while running:
    sgc = np.copy(screen_grid_complex)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    screen.fill(screen_color)
    for a in range(len(mandlebrot_list)):
        t = mandlebrot_list[a]
        pygame.draw.rect(screen, (255, 150, 150), pygame.Rect(t[0], t[1], 1, 1))

    (pos_x, pos_y) = pygame.mouse.get_pos()
    real_part = (pos_x / length) * (x_max - x_min) + x_min
    imag_part = y_max - (pos_y / breadth) * (y_max - y_min)
    c = real_part + (imag_part * 1j)
    for i in range(iters):
        sgc = np.multiply(sgc, sgc) + c
    for i in range(length):
        for j in range(breadth):
            if np.absolute(sgc[i][j]) < 10:
                # screen.blit(blue_square, (i, j))
                pygame.draw.rect(screen, (135, 206, 235), pygame.Rect(i, j, 1, 1))
    pygame.display.update()

