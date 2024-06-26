import numpy as np
import math


class Camera:
    def __init__(self, pos=(0, 0, 0), rotation=(0, 0, 0), fov=60):
        self.pos = np.array(pos, dtype=float)
        self.rotation = np.array(rotation, dtype=float)
        self.step_size = 5
        self.fov = fov

    def move_forward(self):
        dx = math.sin(math.radians(self.rotation[1])) * self.step_size
        dy = -math.sin(math.radians(self.rotation[0])) * self.step_size
        dz = -math.cos(math.radians(self.rotation[1])) * self.step_size

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_backward(self):
        dx = -math.sin(math.radians(self.rotation[1])) * self.step_size
        dy = math.sin(math.radians(self.rotation[0])) * self.step_size
        dz = math.cos(math.radians(self.rotation[1])) * self.step_size

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_left(self):
        dx = math.sin(math.radians(self.rotation[1] - 90)) * self.step_size
        dy = 0
        dz = -math.cos(math.radians(self.rotation[1] - 90)) * self.step_size

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_right(self):
        dx = math.sin(math.radians(self.rotation[1] + 90)) * self.step_size
        dy = 0
        dz = -math.cos(math.radians(self.rotation[1] + 90)) * self.step_size

        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[2] += dz

    def move_up(self):
        self.pos[1] += self.step_size

    def move_down(self):
        self.pos[1] -= self.step_size

    def rotate_x(self, angle):
        self.rotation[0] += angle

    def rotate_y(self, angle):
        self.rotation[1] += angle

    def rotate_z(self, angle):
        self.rotation[2] += angle

    def zoom(self, amount):
        if self.fov + amount < 15 or self.fov + amount > 60:
            pass
        else:
            self.fov += amount

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

        return np.dot(
            rotation_matrix_z,
            np.dot(rotation_matrix_x, np.dot(rotation_matrix_y, translation_matrix)),
        )

    def project(self, point, width, height):
        view_matrix = self.view_matrix()
        projection_matrix = self.perspective_projection(width, height)
        point = np.dot(
            projection_matrix, np.dot(view_matrix, np.array(point + (1,), dtype=float))
        )

        if point[2] <= 0:
            return None

        if point[3] != 0:
            point /= point[3]

        x, y = point[:2]
        return np.array([width / 2 + x * width / 2, height / 2 + y * height / 2])

    def perspective_projection(self, width, height):
        aspect_ratio = width / height
        near = 1
        far = 1000
        f = 1 / math.tan(math.radians(self.fov) / 2)

        return np.array(
            [
                [f / aspect_ratio, 0, 0, 0],
                [0, f, 0, 0],
                [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
                [0, 0, -1, 0],
            ]
        )
