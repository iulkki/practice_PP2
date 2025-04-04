import pygame

white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    current_color = white
    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    current_color = red
                elif event.key == pygame.K_g:
                    current_color = green
                elif event.key == pygame.K_b:
                    current_color = blue
                elif event.key == pygame.K_y:
                    current_color = yellow
                elif event.key == pygame.K_w:
                    current_color = white
                elif event.key == pygame.K_BACKSPACE:
                    current_color = black

                if event.key == pygame.K_v:
                    draw_rectangle(screen, pygame.mouse.get_pos(), 200, 100, current_color)
                elif event.key == pygame.K_c:
                    draw_circle(screen, pygame.mouse.get_pos(), current_color)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    last_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    if last_pos is not None:
                        start_pos = last_pos
                        end_pos = pygame.mouse.get_pos()
                        draw_line(screen, start_pos, end_pos, radius, current_color)
                        last_pos = end_pos

        pygame.display.flip()
        clock.tick(60)


def draw_line(screen, start, end, width, color):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    iterations = max(dx, dy)

    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] * (1 - progress) + end[0] * progress)
        y = int(start[1] * (1 - progress) + end[1] * progress)
        pygame.draw.circle(screen, color, (x, y), width)


def draw_rectangle(screen, mouse_pos, width, height, color):
    rect = pygame.Rect(mouse_pos[0], mouse_pos[1], width, height)
    pygame.draw.rect(screen, color, rect, 3)


def draw_circle(screen, mouse_pos, color):
    pygame.draw.circle(screen, color, mouse_pos, 100, 3)


main()



