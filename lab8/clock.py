import pygame
import time
from datetime import datetime


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("Mickey Clock")


bg = pygame.image.load('images/clock.png')
left_arm = pygame.image.load('images/leftarm.png')
right_arm = pygame.image.load('images/rightarm.png')

running = True
while running:

    now = datetime.now()
    minutes = now.minute
    seconds = now.second


    angle_minutes = -(minutes * 6)  # 360 градусов / 60 = 6 градусов
    angle_seconds = -(seconds * 6)  # 360 градусов / 60 = 6 градусов


    screen.blit(bg, (0, 0))

    rotated_right_arm = pygame.transform.rotate(right_arm, angle_minutes)
    right_arm_rect = rotated_right_arm.get_rect(center=(700, 525))
    screen.blit(rotated_right_arm, right_arm_rect.topleft)


    rotated_left_arm = pygame.transform.rotate(left_arm, angle_seconds)
    left_arm_rect = rotated_left_arm.get_rect(center=(700, 525))
    screen.blit(rotated_left_arm, left_arm_rect.topleft)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


clock.tick(1)
pygame.quit()
