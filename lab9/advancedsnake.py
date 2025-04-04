import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL = 20

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'

def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if [x, y] not in snake:
            weight = random.randint(1, 3)
            return [x, y, weight, time.time()]

food = spawn_food()

score = 0
level = 1
speed = 10

font = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    head = snake[0][:]

    if direction == 'UP':    head[1] -= CELL
    if direction == 'DOWN':  head[1] += CELL
    if direction == 'LEFT':  head[0] -= CELL
    if direction == 'RIGHT': head[0] += CELL

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("wall!")
        break

    if head in snake:
        print("yourself!")
        break

    snake.insert(0, head)

    if head == food[:2]:
        score += food[2]

        food = spawn_food()

        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()


    if time.time() - food[3] > 5:
        food = spawn_food()

    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL, CELL))

    pygame.draw.rect(screen, RED, (*food[:2], CELL, CELL))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
