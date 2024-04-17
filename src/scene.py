class Scene:
    def __init__(self, camera):
        self.camera = camera
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw(self, screen, width, height, fov):
        for obj in self.objects:
            obj.draw(screen, self.camera, width, height, fov)
