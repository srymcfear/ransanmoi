import pygame
from config.settings import GRADIENT_START, GRADIENT_END, WINDOW_WIDTH, WINDOW_HEIGHT

def draw_gradient_background(screen):
    """Draw a gradient background"""
    for y in range(WINDOW_HEIGHT):
        progress = y / WINDOW_HEIGHT
        color = [
            int(GRADIENT_START[i] + (GRADIENT_END[i] - GRADIENT_START[i]) * progress)
            for i in range(3)
        ]
        pygame.draw.line(screen, color, (0, y), (WINDOW_WIDTH, y))

def create_text_surface(text, font, color, shadow_color=None, shadow_offset=0):
    """Create a text surface with optional shadow"""
    text_surface = font.render(text, True, color)
    
    if shadow_color:
        shadow_surface = font.render(text, True, shadow_color)
        combined_surface = pygame.Surface(
            (text_surface.get_width() + shadow_offset,
             text_surface.get_height() + shadow_offset),
            pygame.SRCALPHA
        )
        combined_surface.blit(shadow_surface, (shadow_offset, shadow_offset))
        combined_surface.blit(text_surface, (0, 0))
        return combined_surface
    
    return text_surface