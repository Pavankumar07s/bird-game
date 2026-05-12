import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Bird properties
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_speed_y = 0
gravity = 0.5
jump_strength = -8

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_SPACE:
            bird_speed_y = jump_strength

    # Apply gravity
    bird_speed_y += gravity
    bird_y += bird_speed_y

    # Keep bird on screen (simple bounds)
    if bird_y > SCREEN_HEIGHT - 20:
        bird_y = SCREEN_HEIGHT - 20
        bird_speed_y = 0
    if bird_y < 0:
        bird_y = 0
        bird_speed_y = 0

    # Drawing
    screen.fill(BLUE)  # Sky color
    pygame.draw.circle(screen, WHITE, (int(bird_x), int(bird_y)), 20)  # Simple bird

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
