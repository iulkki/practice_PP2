import pygame

pygame.init()

WIDTH, HEIGHT = 618, 359
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x > ball_radius:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x < WIDTH - ball_radius:
        ball_x += ball_speed
    if keys[pygame.K_UP] and ball_y > ball_radius:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y < HEIGHT - ball_radius:
        ball_y += ball_speed

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.update()
    clock.tick(30)

pygame.quit()

