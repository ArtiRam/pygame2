import pygame


class Render:
    def __init__(self, size, screen, virtual_surface):
        self.size = size
        self.virtual_surface = virtual_surface
        self.screen = screen
        self.scaled_surface = pygame.transform.scale(self.virtual_surface, self.size)

    def screen_blit(self):
        scaled_surface = pygame.transform.scale(self.virtual_surface, self.size)
        self.screen.blit(scaled_surface, (0, 0))

    def image_render(self, file_name, position):
        self.virtual_surface.blit(pygame.image.load(file_name), position)
        self.screen_blit()

    def text_render(self, text_object, rect_object):
        self.virtual_surface.blit(text_object, rect_object)
        self.screen_blit()


def set_font(size):
    return pygame.font.Font("font.ttf", size)
