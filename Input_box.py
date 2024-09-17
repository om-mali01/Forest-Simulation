import pygame

class InputBox:

    def __init__(self, x, y, w, h, lable, inactive_color, base_font, Black) -> None:
        self.rectangle = pygame.Rect(x, y, w, h)
        self.color = inactive_color
        self.active = False
        self.text = ""
        self.label = lable
        self.text_surface = base_font.render(self.text, True, Black)

    def event_handel(self, event, active_color, inactive_color, Black, base_font):
        
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                self.active = True
                self.color = active_color
            else:
                self.color = inactive_color
                self.active = False
            
        if event.type == pygame.KEYDOWN:
            if self.active == True:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isdigit():
                        self.text += event.unicode
                self.text_surface = base_font.render(self.text, True, Black)

    def draw(self, screen, base_font, Black):
        label_surface = base_font.render(self.label, True, Black)
        screen.blit(label_surface, (self.rectangle.x, self.rectangle.y - 20))

        screen.blit(self.text_surface, (self.rectangle.x+5, self.rectangle.y+5))
        pygame.draw.rect(screen, self.color, self.rectangle, 2)

    def get_values(self):
        if self.text.isdigit():
            return float(self.text)
        return 0
    
    def create_labeled_rect(screen, color, rect_pos, text, title_font, l, w):
        rect = pygame.Rect(rect_pos[0], rect_pos[1], l, w)
        pygame.draw.rect(screen, color, rect, 2)

        label = title_font.render(text, True, (0,0,0))
        screen.blit(label, (rect.x+100, rect.y+5))