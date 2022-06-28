from rend import Render


class Button1:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, size):
        self.pos = pos
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False


class Button(Render):
    def __init__(self, position, size, screen, virtual_surface, text, font, base_color, hovering_color):
        super().__init__(size, screen, virtual_surface)
        self.position = position
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.hovering_color = hovering_color
        self.font = font
        self.text_input = text
        self.base_color = base_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=((self.x_pos * self.size[0]) / 1280, (self.y_pos * self.size[1]) / 720))

    def draw(self):
        rect = self.text.get_rect(center=self.position)
        self.text_render(self.text, rect)

    def change_color(self, mouse_position):
        if mouse_position[0] in range(self.rect.left, self.rect.right) and \
           mouse_position[1] in range(self.rect.top, self.rect.bottom):

            self.text = self.font.render(self.text_input, True, self.hovering_color)

            return True
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

            return False
