import pygame
import random
import math
from config.settings import *

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.lifetime = PARTICLE_LIFETIME
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]
        self.alpha = 255
        
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.lifetime -= 1
        self.alpha = int((self.lifetime / PARTICLE_LIFETIME) * 255)
        
    def draw(self, screen):
        if self.lifetime > 0:
            surface = pygame.Surface((4, 4), pygame.SRCALPHA)
            pygame.draw.circle(surface, (*self.color, self.alpha), (2, 2), 2)
            screen.blit(surface, (int(self.x), int(self.y)))

class Effects:
    def __init__(self):
        self.particles = []
        
    def create_food_particles(self, pos):
        for _ in range(PARTICLE_COUNT):
            self.particles.append(Particle(pos[0] + GRID_SIZE//2, 
                                        pos[1] + GRID_SIZE//2, RED))
    
    def create_snake_particles(self, pos):
        for _ in range(PARTICLE_COUNT // 2):
            self.particles.append(Particle(pos[0] + GRID_SIZE//2, 
                                        pos[1] + GRID_SIZE//2, GREEN))
    
    def update(self):
        self.particles = [p for p in self.particles if p.lifetime > 0]
        for particle in self.particles:
            particle.update()
    
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
            
def draw_glow(screen, pos, color, radius):
    glow_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    for i in range(radius):
        alpha = int(255 * (1 - (i / radius)))
        pygame.draw.circle(glow_surf, (*color, alpha), 
                         (radius, radius), radius - i)
    screen.blit(glow_surf, (pos[0] - radius + GRID_SIZE//2, 
                           pos[1] - radius + GRID_SIZE//2), 
                special_flags=pygame.BLEND_ALPHA_SDL2)