import pygame, sys, os
pygame.init()
# Window
window_size = (800,600)
game_window = pygame.display.set_mode(window_size)
# Sprite
sprite = pygame.image.load(os.path.join('Assets', 'sprite.png')) 
sprite_rect = sprite.get_rect()


# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        sprite_rect.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        sprite_rect.x += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        sprite_rect.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        sprite_rect.y += 5
    # Update Display
    game_window.fill((0,0,0))
    game_window.blit(sprite, sprite_rect)
    pygame.display.update()
# Quit Pygame
pygame.quit()