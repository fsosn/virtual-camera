import pygame


class Object:
    def __init__(self, vertices, edges, color=(255, 255, 255)):
        self.vertices = vertices
        self.edges = edges
        self.color = color

    def draw(self, screen, camera, width, height):

        projected_vertices = [
            camera.project(vertex, width, height) for vertex in self.vertices
        ]

        for edge in self.edges:
            start_point = projected_vertices[edge[0]]
            end_point = projected_vertices[edge[1]]
            if start_point is not None and end_point is not None:
                pygame.draw.line(screen, self.color, start_point, end_point, 2)
