import pygame
import sys
from game.snake import Snake
from game.food import Food
from game.ui import UI
from game.start_screen import StartScreen
from game.effects import Effects
from config.settings import *
import time

class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.food = Food()
        self.ui = UI()
        self.start_screen = StartScreen()
        self.effects = Effects()
        self.game_state = STATE_START
        self.last_update = time.time()
        self.snake_update_delay = 1.0 / SNAKE_SPEED
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if self.game_state == STATE_START:
                if event.key == pygame.K_SPACE:
                    self.game_state = STATE_PLAYING
            
            elif self.game_state == STATE_PLAYING:
                if event.key in [pygame.K_UP, pygame.K_DOWN, 
                               pygame.K_LEFT, pygame.K_RIGHT]:
                    if (event.key == pygame.K_UP and self.snake.direction != pygame.K_DOWN or
                        event.key == pygame.K_DOWN and self.snake.direction != pygame.K_UP or
                        event.key == pygame.K_LEFT and self.snake.direction != pygame.K_RIGHT or
                        event.key == pygame.K_RIGHT and self.snake.direction != pygame.K_LEFT):
                        self.snake.direction = event.key
                        self.effects.create_snake_particles(self.snake.positions[0])
                elif event.key == pygame.K_p:
                    self.game_state = STATE_PAUSED
            
            elif self.game_state == STATE_PAUSED:
                if event.key == pygame.K_p:
                    self.game_state = STATE_PLAYING
            
            if event.key == pygame.K_r and self.game_state != STATE_START:
                self.reset_game()
        
        # Handle button clicks in game over screen
        if self.game_state == STATE_GAME_OVER:
            action = self.ui.handle_game_over_events(event)
            if action == 'restart':
                self.reset_game()
            elif action == 'menu':
                self.game_state = STATE_START
            elif action == 'exit':
                pygame.quit()
                sys.exit()
    
    def update(self):
        self.food.update()
        self.effects.update()
        
        if self.game_state == STATE_PLAYING:
            current_time = time.time()
            if current_time - self.last_update >= self.snake_update_delay:
                self.snake.update()
                self.last_update = current_time
                
                if self.snake.positions[0] == self.food.position:
                    self.snake.length += 1
                    self.snake.score += FOOD_SCORE
                    self.effects.create_food_particles(self.food.position)
                    self.food = Food()
                    self.snake_update_delay = max(
                        1.0 / (SNAKE_SPEED + (self.snake.score / 50)), 
                        1.0 / (SNAKE_SPEED * 2)
                    )
                
                if self.snake.check_collision():
                    self.game_state = STATE_GAME_OVER
    
    def draw(self):
        if self.game_state == STATE_START:
            self.start_screen.draw(self.screen)
        else:
            # Create gradient background
            for y in range(WINDOW_HEIGHT):
                progress = y / WINDOW_HEIGHT
                color = [int(GRADIENT_START[i] + (GRADIENT_END[i] - GRADIENT_START[i]) * progress) 
                        for i in range(3)]
                pygame.draw.line(self.screen, color, (0, y), (WINDOW_WIDTH, y))
            
            self._draw_grid()
            self.food.draw(self.screen)
            self.snake.draw(self.screen)
            self.effects.draw(self.screen)
            self.ui.draw(self.screen, self.snake.score, 
                        self.game_state == STATE_GAME_OVER, 
                        self.game_state == STATE_PAUSED)
    
    def _draw_grid(self):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (*GRID_COLOR, 128), 
                           (x, 0), (x, WINDOW_HEIGHT), 1)
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (*GRID_COLOR, 128), 
                           (0, y), (WINDOW_WIDTH, y), 1)
    
    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.effects = Effects()
        self.game_state = STATE_PLAYING
        self.snake_update_delay = 1.0 / SNAKE_SPEED