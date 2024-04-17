import numpy as np
import math


class Camera:
    def __init__(self, pos=(0, 0, 0), rotation=(0, 0, 0)):
        self.pos = np.array(pos, dtype=float)
        self.rotation = np.array(rotation, dtype=float)
        self.move_speed = 5

    def move_forward(self):
        dx = math.sin(math.radians(self.rotation[1])) * self.move_speed
        dy = -math.sin(math.radians(self.rotation[0])) * self.move_speed
        dz = -math.cos(math.radians(self.rotation[1])) * self.move_speed

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_backward(self):
        dx = -math.sin(math.radians(self.rotation[1])) * self.move_speed
        dy = math.sin(math.radians(self.rotation[0])) * self.move_speed
        dz = math.cos(math.radians(self.rotation[1])) * self.move_speed

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_left(self):
        dx = math.sin(math.radians(self.rotation[1] - 90)) * self.move_speed
        dy = 0
        dz = -math.cos(math.radians(self.rotation[1] - 90)) * self.move_speed

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_right(self):
        dx = math.sin(math.radians(self.rotation[1] + 90)) * self.move_speed
        dy = 0
        dz = -math.cos(math.radians(self.rotation[1] + 90)) * self.move_speed

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_up(self):
        self.pos[1] += self.move_speed

    def move_down(self):
        self.pos[1] -= self.move_speed

    def rotate(self, axis, angle):
        if axis == "x":
            self.rotation[0] += angle
        elif axis == "y":
            self.rotation[1] += angle
        elif axis == "z":
            self.rotation[2] += angle

    def view_matrix(self):
        rx, ry, rz = np.radians(self.rotation)
        cos_rx, sin_rx = np.cos(rx), np.sin(rx)
        cos_ry, sin_ry = np.cos(ry), np.sin(ry)
        cos_rz, sin_rz = np.cos(rz), np.sin(rz)

        translation_matrix = np.array(
            [
                [1, 0, 0, -self.pos[0]],
                [0, 1, 0, -self.pos[1]],
                [0, 0, 1, -self.pos[2]],
                [0, 0, 0, 1],
            ]
        )

        rotation_matrix_x = np.array(
            [
                [1, 0, 0, 0],
                [0, cos_rx, -sin_rx, 0],
                [0, sin_rx, cos_rx, 0],
                [0, 0, 0, 1],
            ]
        )

        rotation_matrix_y = np.array(
            [
                [cos_ry, 0, sin_ry, 0],
                [0, 1, 0, 0],
                [-sin_ry, 0, cos_ry, 0],
                [0, 0, 0, 1],
            ]
        )

        rotation_matrix_z = np.array(
            [
                [cos_rz, -sin_rz, 0, 0],
                [sin_rz, cos_rz, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )

        return np.dot(rotation_matrix_x, np.dot(rotation_matrix_y, translation_matrix))

    def project(self, point, width, height, fov):
        view_matrix = self.view_matrix()
        projection_matrix = self.perspective_projection(width, height, fov)
        point = np.dot(
            projection_matrix, np.dot(view_matrix, np.array(point + (1,), dtype=float))
        )

        if point[3] != 0:
            point /= point[3]

        x, y = point[:2]
        return np.array([width / 2 + x * width / 2, height / 2 + y * height / 2])

    def perspective_projection(self, width, height, fov):
        aspect_ratio = width / height
        near = 0.1
        far = 1000
        f = 1 / math.tan(math.radians(fov) / 2)

        return np.array(
            [
                [f / aspect_ratio, 0, 0, 0],
                [0, f, 0, 0],
                [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
                [0, 0, -1, 0],
            ]
        )
