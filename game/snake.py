import pygame
from config.settings import *

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.length = INITIAL_SNAKE_LENGTH
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = pygame.K_RIGHT
        self.score = 0
        
        # Create initial snake body
        for i in range(self.length - 1):
            x = self.positions[0][0] - (i + 1) * GRID_SIZE
            y = self.positions[0][1]
            self.positions.append((x, y))
    
    def update(self):
        current = self.positions[0]
        x, y = current
        
        if self.direction == pygame.K_UP:
            y -= GRID_SIZE
        elif self.direction == pygame.K_DOWN:
            y += GRID_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= GRID_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += GRID_SIZE
            
        # Add new head position
        self.positions.insert(0, (x, y))
        
        # Remove tail if not growing
        if len(self.positions) > self.length:
            self.positions.pop()
    
    def draw(self, screen):
        for i, pos in enumerate(self.positions):
            # Create gradient effect from head to tail
            color_value = max(46 - i * 2, 0)
            color = (color_value, 204 - i * 3, 113 - i * 2)
            
            pygame.draw.rect(screen, color, 
                           (pos[0], pos[1], GRID_SIZE-2, GRID_SIZE-2), 
                           border_radius=4)
            
            # Draw eyes on the head
            if i == 0:
                self._draw_eyes(screen, pos)
    
    def _draw_eyes(self, screen, head_pos):
        x, y = head_pos
        eye_radius = 2
        
        # Adjust eye positions based on direction
        if self.direction == pygame.K_RIGHT:
            eyes = [(x + GRID_SIZE - 6, y + 5), (x + GRID_SIZE - 6, y + GRID_SIZE - 7)]
        elif self.direction == pygame.K_LEFT:
            eyes = [(x + 4, y + 5), (x + 4, y + GRID_SIZE - 7)]
        elif self.direction == pygame.K_UP:
            eyes = [(x + 5, y + 4), (x + GRID_SIZE - 7, y + 4)]
        else:
            eyes = [(x + 5, y + GRID_SIZE - 6), (x + GRID_SIZE - 7, y + GRID_SIZE - 6)]
            
        for eye_pos in eyes:
            pygame.draw.circle(screen, BLACK, eye_pos, eye_radius)
    
    def check_collision(self):
        head = self.positions[0]
        # Check wall collision
        if (head[0] < 0 or head[0] >= WINDOW_WIDTH or 
            head[1] < 0 or head[1] >= WINDOW_HEIGHT):
            return True
        
        # Check self collision
        if head in self.positions[1:]:
            return True
        
        return False