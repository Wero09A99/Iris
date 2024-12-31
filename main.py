# Example file showing a circle moving on screen
import pygame
import const

# pygame setup
pygame.init()
screen = pygame.display.set_mode((const.ANCHO, const.ALTO))
clock = pygame.time.Clock()
running = True
delta_time = 0

player = pygame.image.load("niko.png")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

background = pygame.image.load("skyline.png")
background = pygame.transform.scale(background, (const.ALTO * 2, const.ANCHO * 2))

map_width, map_height = background.get_size()

velocity = 500 #Velocidad del jugador

camera_offset = pygame.Vector2(0, 0)


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= velocity * delta_time
    if keys[pygame.K_s]:
        player_pos.y += velocity * delta_time
    if keys[pygame.K_a]:
        player_pos.x -= velocity * delta_time
    if keys[pygame.K_d]:
        player_pos.x += velocity * delta_time
    # Actualizar el desplazamiento de la cámara
    camera_offset.x = max(
        0, 
        min(
            player_pos.x - screen.get_width() / 2, 
            max(0, map_width - screen.get_width())
        )
    )
    camera_offset.y = max(
        0, 
        min(
            player_pos.y - screen.get_height() / 2, 
            max(0, map_height - screen.get_height())
        )
    )

    #Area de dibujo XD
    screen.blit(background, (-camera_offset. x, -camera_offset.y))
    screen.blit(player, (player_pos.x - camera_offset.x, player_pos.y - camera_offset.y))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    delta_time = clock.tick(60) / 1000

pygame.quit()