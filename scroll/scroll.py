import time
import pygame

from .entity import Entity


class Scroll(object):
    """The base game object"""
    def __init__(self, resolution):
        super().__init__()
        pygame.init()
        self.resolution = resolution
        self.is_running = False
        self.clock = pygame.time.Clock()
        self.deltatime = 0

    def run(self):
        self.screen = pygame.display.set_mode(self.resolution)
        self.is_running = True

        while self.is_running:

            #time.sleep(1 / 60 * 1000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.update()
            self.draw()

    def update(self):
        for entity in Entity.entities:
            entity.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        for entity in Entity.entities:
            entity.draw()

        pygame.display.flip()
        self.clock.tick(60)
