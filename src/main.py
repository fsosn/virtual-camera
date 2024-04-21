import pygame
from camera import Camera
from scene import Scene
from object import Object
import random

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
dim = 2
cube_size = 50
gap = 100
column_gap = 200

for col in range(dim):
    for i in range(dim):
        for j in range(dim):
            cube = Object(
                vertices=[
                    (
                        -cube_size + j * (cube_size + gap),
                        -cube_size + i * (cube_size + gap),
                        -cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        cube_size + j * (cube_size + gap),
                        -cube_size + i * (cube_size + gap),
                        -cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        cube_size + j * (cube_size + gap),
                        cube_size + i * (cube_size + gap),
                        -cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        -cube_size + j * (cube_size + gap),
                        cube_size + i * (cube_size + gap),
                        -cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        -cube_size + j * (cube_size + gap),
                        -cube_size + i * (cube_size + gap),
                        cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        cube_size + j * (cube_size + gap),
                        -cube_size + i * (cube_size + gap),
                        cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        cube_size + j * (cube_size + gap),
                        cube_size + i * (cube_size + gap),
                        cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                    (
                        -cube_size + j * (cube_size + gap),
                        cube_size + i * (cube_size + gap),
                        cube_size + col * (cube_size * 3 + gap * 2 - column_gap),
                    ),
                ],
                edges=[
                    (0, 1),
                    (1, 2),
                    (2, 3),
                    (3, 0),
                    (4, 5),
                    (5, 6),
                    (6, 7),
                    (7, 4),
                    (0, 4),
                    (1, 5),
                    (2, 6),
                    (3, 7),
                ],
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
            )
            scene.add_object(cube)


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
    # if keys[pygame.K_q]:
    #     camera.rotate_z(-1)
    # if keys[pygame.K_e]:
    #     camera.rotate_z(1)
    if keys[pygame.K_KP_PLUS]:
        camera.zoom(-1)
    if keys[pygame.K_KP_MINUS]:
        camera.zoom(1)

    screen.fill(BG_COLOR)

    scene.draw(screen, WIDTH, HEIGHT, FOV)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
