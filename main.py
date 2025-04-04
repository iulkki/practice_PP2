import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Game of Ball")

ball_x, ball_y = 350, 350
ball_speed = 20

running = True
while running:
    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x > 25:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x < 975:
        ball_x += ball_speed
    if keys[pygame.K_UP] and ball_y > 25:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y < 475:
        ball_y += ball_speed

    pygame.draw.circle(screen, 'Red', (ball_x, ball_y), 25)

    pygame.display.update()

    clock.tick(20)

pygame.quit()








