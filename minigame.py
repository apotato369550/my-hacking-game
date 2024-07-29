# minigame.py

import pygame
import random
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS

# Minigame settings
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10
BALL_SPEED = 5

def play_minigame(screen, clock):
    # Ball and paddle initial positions
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_dx = BALL_SPEED
    ball_dy = BALL_SPEED

    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40

    running = True
    win = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            paddle_x += PADDLE_SPEED

        # Ensure the paddle stays within screen bounds
        paddle_x = max(paddle_x, 0)
        paddle_x = min(paddle_x, SCREEN_WIDTH - PADDLE_WIDTH)

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with walls
        if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy

        # Ball collision with paddle
        if (paddle_y < ball_y + BALL_RADIUS < paddle_y + PADDLE_HEIGHT and
                paddle_x < ball_x < paddle_x + PADDLE_WIDTH):
            ball_dy = -ball_dy

        # Check for win or lose conditions
        if ball_y > SCREEN_HEIGHT:
            running = False
        if ball_y <= 0:
            win = True
            running = False

        # Clear screen
        screen.fill(BG_COLOR)

        # Draw ball and paddle
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)
        pygame.draw.rect(screen, (0, 255, 0), (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

        pygame.display.flip()
        clock.tick(FPS)

    return win
