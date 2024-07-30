# minigame.py

import pygame
import sys
import random
import string
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS

# Minigame settings
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10
BALL_SPEED = 5

def play_bypass_minigame(screen, clock):
    return generic_minigame(screen, clock, "Bypass")

def play_crack_minigame(screen, clock):
    return typing_minigame(screen, clock, "Crack")

def play_decrypt_minigame(screen, clock):
    return memory_minigame(screen, clock, "Decrypt")

def generic_minigame(screen, clock, minigame_type):
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_dx = BALL_SPEED
    ball_dy = BALL_SPEED

    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - 40

    running = True
    win = False
    top_bounces = 0
    required_bounces = random.randint(3, 5)

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

        paddle_x = max(paddle_x, 0)
        paddle_x = min(paddle_x, SCREEN_WIDTH - PADDLE_WIDTH)

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy
            top_bounces += 1

        if paddle_y < ball_y + BALL_RADIUS < paddle_y + PADDLE_HEIGHT and paddle_x < ball_x < paddle_x + PADDLE_WIDTH:
            ball_dy = -ball_dy

        if ball_y > SCREEN_HEIGHT:
            running = False
        if top_bounces >= required_bounces:
            win = True
            running = False

        screen.fill(BG_COLOR)
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)
        pygame.draw.rect(screen, (0, 255, 0), (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

        pygame.display.flip()
        clock.tick(FPS)

    return win

def typing_minigame(screen, clock, minigame_type):
    target_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(7, 14)))
    input_text = ""
    running = True
    win = False

    while running:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == target_text:
                        win = True
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        draw_text(screen, f"Type: {target_text}", (10, 10))
        draw_text(screen, f"Input: {input_text}", (10, 50))

        pygame.display.flip()
        clock.tick(FPS)

    return win

def memory_minigame(screen, clock, minigame_type):
    possible_inputs = ["^", "v", "<", ">"]
    pattern_length = random.randint(4, 10)
    pattern = [random.choice(possible_inputs) for _ in range(pattern_length)]
    input_pattern = []
    running = True
    win = False

    while running:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_pattern == pattern:
                        win = True
                    running = False
                else:
                    if event.key == pygame.K_UP:
                        input_pattern.append("^")
                    elif event.key == pygame.K_DOWN:
                        input_pattern.append("v")
                    elif event.key == pygame.K_LEFT:
                        input_pattern.append("<")
                    elif event.key == pygame.K_RIGHT:
                        input_pattern.append(">")
                    
                    if len(input_pattern) > len(pattern) or input_pattern[-1] != pattern[len(input_pattern) - 1]:
                        running = False

        draw_text(screen, f"Decryption process activated. Use the arrow keys then hit enter to decrypt.", (10, 10))
        draw_text(screen, f"{' '.join(pattern)}", (10, 50))
        draw_text(screen, f"Input: {' '.join(input_pattern)}", (10, 90))

        pygame.display.flip()
        clock.tick(FPS)

    return win

def draw_text(screen, text, pos):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, pos)
