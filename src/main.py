import pygame
from camera import Camera
from scene import Scene
from utils.cube_generator import generate_cubes

pygame.init()

WIDTH, HEIGHT = 800, 600
FOV = 60
FPS = 60
BG_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Camera")
clock = pygame.time.Clock()

camera = Camera(pos=(200, 100, 500))
scene = Scene(camera)
generate_cubes(scene)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera.move_forward()
    if keys[pygame.K_s]:
        camera.move_backward()
    if keys[pygame.K_a]:
        camera.move_left()
    if keys[pygame.K_d]:
        camera.move_right()
    if keys[pygame.K_SPACE]:
        camera.move_up()
    if keys[pygame.K_LSHIFT]:
        camera.move_down()
    if keys[pygame.K_UP]:
        camera.rotate_x(1)
    if keys[pygame.K_DOWN]:
        camera.rotate_x(-1)
    if keys[pygame.K_LEFT]:
        camera.rotate_y(-1)
    if keys[pygame.K_RIGHT]:
        camera.rotate_y(1)
    if keys[pygame.K_q]:
        camera.rotate_z(1)
    if keys[pygame.K_e]:
        camera.rotate_z(-1)
    if keys[pygame.K_KP_PLUS]:
        camera.zoom(-1)
    if keys[pygame.K_KP_MINUS]:
        camera.zoom(1)

    screen.fill(BG_COLOR)
    scene.draw(screen, WIDTH, HEIGHT)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
