import pygame


class Object:
    def __init__(self, vertices, edges, color=(255, 255, 255)):
        self.vertices = vertices
        self.edges = edges
        self.color = color

    def draw(self, screen, camera, width, height, fov):

        projected_vertices = [
            camera.project(vertex, width, height, fov) for vertex in self.vertices
        ]

        for edge in self.edges:
            start_point = projected_vertices[edge[0]]
            end_point = projected_vertices[edge[1]]
            pygame.draw.line(screen, self.color, start_point, end_point, 2)
