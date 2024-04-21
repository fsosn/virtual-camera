from object import Object

colors = [
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255),
    (255, 165, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
]


def generate_cubes(scene, dim=2, cube_size=50, gap=100):
    color_index = 0
    for col in range(dim):
        for i in range(dim):
            for j in range(dim):
                cube = Object(
                    vertices=[
                        (
                            -cube_size + j * (cube_size + gap),
                            -cube_size + i * (cube_size + gap),
                            -cube_size + col * (cube_size * 3),
                        ),
                        (
                            cube_size + j * (cube_size + gap),
                            -cube_size + i * (cube_size + gap),
                            -cube_size + col * (cube_size * 3),
                        ),
                        (
                            cube_size + j * (cube_size + gap),
                            cube_size + i * (cube_size + gap),
                            -cube_size + col * (cube_size * 3),
                        ),
                        (
                            -cube_size + j * (cube_size + gap),
                            cube_size + i * (cube_size + gap),
                            -cube_size + col * (cube_size * 3),
                        ),
                        (
                            -cube_size + j * (cube_size + gap),
                            -cube_size + i * (cube_size + gap),
                            cube_size + col * (cube_size * 3),
                        ),
                        (
                            cube_size + j * (cube_size + gap),
                            -cube_size + i * (cube_size + gap),
                            cube_size + col * (cube_size * 3),
                        ),
                        (
                            cube_size + j * (cube_size + gap),
                            cube_size + i * (cube_size + gap),
                            cube_size + col * (cube_size * 3),
                        ),
                        (
                            -cube_size + j * (cube_size + gap),
                            cube_size + i * (cube_size + gap),
                            cube_size + col * (cube_size * 3),
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
                    color=colors[color_index],
                )
                scene.add_object(cube)
                color_index = (color_index + 1) % len(colors)
