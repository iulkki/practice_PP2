import pygame
import random
import time
import psycopg2

# connect to database
conn = psycopg2.connect(
    host="localhost",
    database="snake_game",
    user="player"
)
cur = conn.cursor()

# table create if not exists
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE
);
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER,
    level INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')
conn.commit()

# user log in
username = input("Enter your username: ")
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    print(f"Welcome back, {username}!")
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    last_data = cur.fetchone()
    if last_data:
        print(f"Last score: {last_data[0]}, level: {last_data[1]}")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    print(f"New user created: {username}")

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
paused = False

font = pygame.font.SysFont("Arial", 20)
big_font = pygame.font.SysFont("Arial", 50)

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
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    cur.execute(
                        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                        (user_id, score, level)
                    )
                    conn.commit()
                    print(f"Game paused and saved: score = {score}, level = {level}")

    if not paused:
        head = snake[0][:]
        if direction == 'UP':    head[1] -= CELL
        if direction == 'DOWN':  head[1] += CELL
        if direction == 'LEFT':  head[0] -= CELL
        if direction == 'RIGHT': head[0] += CELL

        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            print("Hit wall!")
            break

        if head in snake:
            print("Hit yourself!")
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
    else:
        pause_text = big_font.render("PAUSED", True, WHITE)
        screen.blit(pause_text, (WIDTH // 3, HEIGHT // 3))

    pygame.display.update()
    clock.tick(speed if not paused else 5)

pygame.quit()
cur.close()
conn.close()
