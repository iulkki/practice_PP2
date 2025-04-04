import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

RED = (255, 0, 0)

bg = pygame.image.load("AnimatedStreet.png")

player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")
coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (40, 40))

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound('crash.wav')
collect_sound = pygame.mixer.Sound('collect.wav')

player_x = 160
player_y = 500
enemy_x = random.randint(40, SCREEN_WIDTH - 40)
enemy_y = 0
coin_x = random.randint(40, SCREEN_WIDTH - 40)
coin_y = 0

speed = 5
coin_speed = 5
score = 0
coins = 0
N = 5

coin_values = [1, 5, 10]
coin_value = random.choice(coin_values)

running = True
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
        player_x += 5

    enemy_y += speed
    if enemy_y > SCREEN_HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(40, SCREEN_WIDTH - 40)
        score += 1

    coin_y += coin_speed
    if coin_y > SCREEN_HEIGHT:
        coin_y = 0
        coin_x = random.randint(40, SCREEN_WIDTH - 40)
        coin_value = random.choice(coin_values)

    if abs(player_x - enemy_x) < 50 and abs(player_y - enemy_y) < 50:
        crash_sound.play()
        screen.fill(RED)
        pygame.display.update()
        time.sleep(1)
        running = False

    if abs(player_x - coin_x) < 40 and abs(player_y - coin_y) < 40:
        collect_sound.play()
        coins += 1
        score += coin_value
        coin_y = 0
        coin_x = random.randint(40, SCREEN_WIDTH - 40)
        coin_value = random.choice(coin_values)

    if coins >= N:
        speed = speed = 5 + coins // 5

    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    screen.blit(coin_img, (coin_x, coin_y))

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
