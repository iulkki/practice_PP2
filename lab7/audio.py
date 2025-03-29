import pygame
from pygame import mixer
import glob

pygame.init()
mixer.init()
pygame.display.set_caption("Music Player")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
done = False

musics = sorted(glob.glob("audioplayer/*.mp3"))
n = 0
paused = False


def start(n):
    mixer.music.load(musics[n])
    mixer.music.set_volume(0.2)
    mixer.music.play()


start(n)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not paused:
                mixer.music.pause()
                paused = True
            else:
                mixer.music.unpause()
                paused = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            n = (n + 1) % len(musics)
            start(n)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            n = (n - 1) % len(musics)
            start(n)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


