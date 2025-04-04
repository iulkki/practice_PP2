import pygame

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Player")

myfont = pygame.font.Font('fonts/Roboto_Condensed-Black.ttf', 40)
text_surface1 = myfont.render('play/pause => space', True, 'white')
text_surface2 = myfont.render('previous => left', True, 'white')
text_surface3 = myfont.render('next => right', True, 'white')

playlist = [
pygame.mixer.Sound('sounds/Nirvana - Come As You Are .mp3'),
pygame.mixer.Sound('sounds/Nirvana - Heart Shaped Box .mp3'),
pygame.mixer.Sound('sounds/Nirvana - Rape Me (OST Выкрутасы).mp3'),
pygame.mixer.Sound('sounds/Nirvana - Smells Like Teen Spirit .mp3')
]

current_track = 0
is_playing = False

running = True
while running:
    screen.fill((176, 111, 217))
    screen.blit(text_surface1, (50, 50))
    screen.blit(text_surface2, (50, 100))
    screen.blit(text_surface3, (50, 150))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    playlist[current_track].stop()
                else:
                    playlist[current_track].play()
                is_playing = not is_playing
            elif event.key == pygame.K_RIGHT:
                playlist[current_track].stop()
                current_track = (current_track + 1) % len(playlist)
                playlist[current_track].play()
                is_playing = True
            elif event.key == pygame.K_LEFT:
                playlist[current_track].stop()
                current_track = (current_track - 1) % len(playlist)
                playlist[current_track].play()
                is_playing = True

pygame.quit()

