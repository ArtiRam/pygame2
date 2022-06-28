import pygame
import map_conf
from button import Button
from rend import Render, set_font


file = 'gfx\Overworld.png'


class Game:
    def __init__(self):
        pygame.init()
        self.mouse_position = pygame.mouse.get_pos()
        self.file = None
        self.image = None
        self.rect = None
        self.size = self.set_size(800, 600)
        self.screen = pygame.display.set_mode(self.size)
        self.virtual_surface = pygame.Surface((1280, 720))
        self.render = Render(self.size, self.screen, self.virtual_surface)
        self.background = None
        self.running = True
        self.play_button = None
        self.settings_button = None
        self.quit_button = None

    def set_size(self, width, hight):
        self.size = width, hight
        return self.size

    def get_size(self):
        return self.size

    def menu_render(self):

        menu_text = set_font(50).render("Главное Меню", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        self.render.image_render('Background.png', (0, 0))
        self.render.text_render(menu_text, menu_rect)

        pygame.display.set_caption("Hellow World!")
        self.mouse_position = pygame.mouse.get_pos()

        self.play_button = Button(position=(640, 250), size=self.size, screen=self.screen,
                                  virtual_surface=self.virtual_surface, font=set_font(50),
                                  base_color="#d7fcd4", text="Старт", hovering_color='Black')

        self.settings_button = Button(position=(640, 350), size=self.size, screen=self.screen,
                                      virtual_surface=self.virtual_surface, font=set_font(50),
                                      base_color="#d7fcd4", text="Настройки", hovering_color='Black')

        self.quit_button = Button(position=(640, 450), size=self.size, screen=self.screen,
                                  virtual_surface=self.virtual_surface, font=set_font(50),
                                  base_color="#d7fcd4", text="Выход", hovering_color='Black')

        for button in [self.play_button, self.settings_button, self.quit_button]:
            button.change_color(self.mouse_position)
            button.draw()

    def run(self):
        while self.running:
            self.menu_render()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_l:
                        self.load_image(file)

                    elif event.key == pygame.K_q:
                        self.map_creator()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.change_color(self.mouse_position):
                        self.map_creator()

                    elif self.settings_button.change_color(self.mouse_position):
                        self.load_image(file)

                    elif self.quit_button.change_color(self.mouse_position):
                        self.running = False
            pygame.display.update()
        pygame.quit()

    def load_image(self, file):
        self.file = file
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()

        self.screen = pygame.display.set_mode(self.rect.size)
        pygame.display.set_caption(f'Разрешение: {self.rect.size}')
        self.screen.blit(self.image, self.rect)

    def map_creator(self):
        for row in range(len(map_conf.tile_map)):

            for column in range(len(map_conf.tile_map[row])):
                self.render.image_render(map_conf.textures[map_conf.tile_map[row][column]],
                                 (column * map_conf.tilesize, row * map_conf.tilesize))


game = Game()
game.run()
