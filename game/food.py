import pygame
from config.settings import GRID_SIZE, RED
from utils.random_utils import generate_random_position
from game.effects import draw_glow

class Food:
    def __init__(self):
        self.position = generate_random_position()
        self.glow_animation = 0
        self.glow_direction = 1
        
    def update(self):
        # Pulsating glow effect
        self.glow_animation += 0.1 * self.glow_direction
        if self.glow_animation >= 1:
            self.glow_direction = -1
        elif self.glow_animation <= 0:
            self.glow_direction = 1
    
    def draw(self, screen):
        x, y = self.position
        
        # Draw glow effect
        glow_radius = int(10 * (0.7 + 0.3 * self.glow_animation))
        draw_glow(screen, self.position, RED, glow_radius)
        
        # Draw main food body
        pygame.draw.circle(screen, RED, 
                         (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 
                         GRID_SIZE // 2 - 2)
        
        # Draw highlight for 3D effect
        pygame.draw.circle(screen, (241, 96, 80), 
                         (x + GRID_SIZE // 2 - 2, y + GRID_SIZE // 2 - 2), 
                         GRID_SIZE // 4 - 1)