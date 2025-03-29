import pygame
import time

pygame.init()

clock_bg = pygame.image.load("mouse/clock.png")
minute_hand = pygame.image.load("mouse/rightarm.png")
second_hand = pygame.image.load("mouse/leftarm.png")

WIDTH, HEIGHT = clock_bg.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")


def rotate_hand(image, angle, pos):
    rotated = pygame.transform.rotate(image, -angle)
    rect = rotated.get_rect(center=pos)
    screen.blit(rotated, rect.topleft)

bg_sound = pygame.mixer.Sound('mouse/Lab7_analog_clock_tictac.mp3')
bg_sound.play()


running = True
while running:
    screen.blit(clock_bg, (0, 0))


    t = time.localtime()
    sec_angle = t.tm_sec * 6
    min_angle = t.tm_min * 6


    center = (WIDTH // 2, HEIGHT // 2)
    rotate_hand(second_hand, sec_angle, center)
    rotate_hand(minute_hand, min_angle, center)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()

