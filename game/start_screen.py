import pygame
import math
from config.settings import *
from utils.drawing_utils import draw_gradient_background, create_text_surface

class StartScreen:
    def __init__(self):
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 74)
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.animation_time = 0
        
    def draw(self, screen):
        self.animation_time += 0.02
        
        # Draw background
        draw_gradient_background(screen)
        
        # Draw animated snake pattern
        self._draw_animated_snake(screen)
        
        # Draw title
        self._draw_title(screen)
        
        # Draw start instruction
        self._draw_start_instruction(screen)
        
        # Draw controls
        self._draw_controls(screen)
    
    def _draw_animated_snake(self, screen):
        for i in range(20):
            x = WINDOW_WIDTH//2 + math.cos(self.animation_time + i/2) * 100
            y = 100 + i * 20
            size = 15 + math.sin(self.animation_time * 2 + i/3) * 5
            pygame.draw.circle(screen, GREEN, (int(x), y), int(size))
    
    def _draw_title(self, screen):
        title_surface = create_text_surface(
            "Snake Game", 
            self.title_font, 
            WHITE, 
            (0, 0, 0, 128), 
            3
        )
        title_rect = title_surface.get_rect(
            center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 60)
        )
        screen.blit(title_surface, title_rect)
    
    def _draw_start_instruction(self, screen):
        pulse = (math.sin(self.animation_time * 4) + 1) / 2
        start_color = [int(255 * pulse)] * 3
        start_text = create_text_surface(
            'Press SPACE to Start',
            self.font,
            start_color
        )
        start_rect = start_text.get_rect(
            center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 20)
        )
        screen.blit(start_text, start_rect)
    
    def _draw_controls(self, screen):
        controls_surface = pygame.Surface((300, 150), pygame.SRCALPHA)
        pygame.draw.rect(controls_surface, (0, 0, 0, 128), 
                        controls_surface.get_rect(), border_radius=10)
        
        controls = [
            ('Controls:', WHITE),
            ('↑ ↓ ← → : Move Snake', BLUE),
            ('P : Pause Game', GREEN),
            ('R : Restart Game', RED)
        ]
        
        for i, (text, color) in enumerate(controls):
            control_text = create_text_surface(text, self.small_font, color)
            control_rect = control_text.get_rect(
                center=(150, 30 + i * 30)
            )
            controls_surface.blit(control_text, control_rect)
        
        screen.blit(controls_surface, 
                   (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2 + 60))