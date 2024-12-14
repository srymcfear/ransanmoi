import pygame
from config.settings import *
from utils.ui_components import Button
from utils.drawing_utils import create_text_surface

class UI:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Create buttons
        button_width = 200
        button_height = 50
        center_x = WINDOW_WIDTH // 2 - button_width // 2
        
        self.restart_button = Button(
            "Restart Game", 
            button_width, 
            button_height,
            (center_x, WINDOW_HEIGHT // 2 + 20),
            (46, 204, 113),  # Green
            (39, 174, 96)    # Darker green
        )
        
        self.menu_button = Button(
            "Back to Menu", 
            button_width, 
            button_height,
            (center_x, WINDOW_HEIGHT // 2 + 90),
            (52, 152, 219),  # Blue
            (41, 128, 185)   # Darker blue
        )
        
        self.exit_button = Button(
            "Exit Game", 
            button_width, 
            button_height,
            (center_x, WINDOW_HEIGHT // 2 + 160),
            (231, 76, 60),   # Red
            (192, 57, 43)    # Darker red
        )
    
    def draw(self, screen, score, game_over, paused):
        # Draw score
        score_text = self.font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))
        
        if game_over:
            self._draw_game_over(screen, score)
        elif paused:
            self._draw_paused(screen)
        else:
            # Draw controls hint
            controls = self.small_font.render('P: Pause  R: Restart', True, BLACK)
            screen.blit(controls, (WINDOW_WIDTH - 150, 10))
    
    def _draw_game_over(self, screen, score):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = create_text_surface('Game Over!', self.font, WHITE)
        score_text = create_text_surface(f'Final Score: {score}', self.font, WHITE)
        
        screen.blit(game_over_text, 
                   (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                    WINDOW_HEIGHT//2 - 80))
        screen.blit(score_text, 
                   (WINDOW_WIDTH//2 - score_text.get_width()//2, 
                    WINDOW_HEIGHT//2 - 30))
        
        # Draw buttons
        self.restart_button.draw(screen)
        self.menu_button.draw(screen)
        self.exit_button.draw(screen)
    
    def _draw_paused(self, screen):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.font.render('Game Paused', True, WHITE)
        continue_text = self.font.render('Press P to Continue', True, WHITE)
        
        screen.blit(pause_text, 
                   (WINDOW_WIDTH//2 - pause_text.get_width()//2, 
                    WINDOW_HEIGHT//2 - 30))
        screen.blit(continue_text, 
                   (WINDOW_WIDTH//2 - continue_text.get_width()//2, 
                    WINDOW_HEIGHT//2 + 30))
    
    def handle_game_over_events(self, event):
        if self.restart_button.handle_event(event):
            return 'restart'
        elif self.menu_button.handle_event(event):
            return 'menu'
        elif self.exit_button.handle_event(event):
            return 'exit'
        return None