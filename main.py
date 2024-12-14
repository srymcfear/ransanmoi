import os
import sys
import config.settings
import game.game_manager

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

import pygame
from game.game_manager import GameManager
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("FEAR - Snake Game")
    clock = pygame.time.Clock()
    
    game = GameManager(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_input(event)
        
        game.update()
        game.draw()
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()