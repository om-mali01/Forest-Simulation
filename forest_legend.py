import pygame

def create_labeled_rect(screen, color, rect_pos, text, base_font):
    rect = pygame.Rect(rect_pos[0], rect_pos[1], 25, 25)
    pygame.draw.rect(screen, color, rect)

    label = base_font.render(text, True, (0,0,0))
    screen.blit(label, (rect.x+35, rect.y+5))

def create_text(screen, base_font, text, color, pos):
    new_text = base_font.render(text, True, color)
    screen.blit(new_text, pos)

def Forest_legend(screen):
    black = (0,0,0)
    light_green = (0, 220, 0)
    green = (0, 150, 0)
    dark_green = (0, 50, 0)
    brown = (139, 69, 19)
    grey = (128, 128, 128)
    
    base_font = pygame.font.Font(None, 20)
    title_font = pygame.font.Font(None, 25)

    border = pygame.Rect(550, 330, 400, 150)
    pygame.draw.rect(screen, black, border, 2)

    create_text(screen, title_font, "Forest Legend", (0, 0, 0), (border.x + 100, border.y + 10))

    create_labeled_rect(screen, light_green, (border.x+20, border.y+30), "Young Tree", base_font)
    create_labeled_rect(screen, green, (border.x+20, border.y+65), "Mature Tree", base_font)
    create_labeled_rect(screen, dark_green, (border.x+20, border.y+100), "Old Tree", base_font)
    create_labeled_rect(screen, brown, (border.x+150, border.y+30), "Land", base_font)
    create_labeled_rect(screen, grey, (border.x+150, border.y+65), "Dead Tree", base_font)

