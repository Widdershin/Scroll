import pygame
from .helpers import Vector2


class Component(object):
    instances = []

    def __init__(self):
        super().__init__()
        self.__class__.instances.append(self)

    def draw(self):
        pass


class Position(Component):
    def __init__(self, position):
        super().__init__()
        self.position = position


class Sprite(Component, pygame.sprite.Sprite):
    def __init__(self, sprite_path):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert()
        self.group = pygame.sprite.Group()
        self.add(self.group)
        self.sprite_path = sprite_path
        self.screen = pygame.display.get_surface()
        self.rect = self.image.get_rect()

    def draw(self):
        print("Drawing")
        self.screen.blit(self.image, Vector2(100, 100))
