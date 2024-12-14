import random
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE

def generate_random_position():
    """Generate a random position aligned to the grid"""
    x = random.randrange(0, WINDOW_WIDTH - GRID_SIZE, GRID_SIZE)
    y = random.randrange(0, WINDOW_HEIGHT - GRID_SIZE, GRID_SIZE)
    return (x, y)