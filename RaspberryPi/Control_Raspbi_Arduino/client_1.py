import pygame

pygame.init()

pygame.key.set_repeat(100, 100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Forward!')
            if event.key == pygame.K_a:
                print('Left!')
            if event.key == pygame.K_d:
                print('Right!')
            if event.key == pygame.K_s:
                print('Stop!')
            if event.key == pygame.K_q:
                print('quit!')
                sys.exit(0)
