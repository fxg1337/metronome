import pygame
import time

# Initialize pygame
pygame.init()

# Set up screen
width, height = 250, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Metronome")

# Colors
BLACK = (0, 0, 0)

# Metronome variables
ball_radius = 20
ball_color = (255, 255, 255)
ball_x = width // 2
ball_y = height // 4
direction = 1  # 1 for down, -1 for up
speed = 5

# Sound variables
sound = pygame.mixer.Sound("bit\metronome-85688.wav")
sound.play()

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Draw metronome
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update ball position
    ball_y += direction * speed

    # Detect collision with top and bottom of screen
    if ball_y <= ball_radius or ball_y >= height - ball_radius:
        direction *= -1
        sound.play()

    pygame.display.flip()

    # Delay for consistent speed
    time.sleep(0.01)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Clean up
pygame.quit()

