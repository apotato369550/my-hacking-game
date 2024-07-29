# main.py

import pygame
import sys
from player import Player
from node import Node, scan, hack
from utils import draw_text, handle_input, show_help
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, FONT_COLOR, BG_COLOR, INPUT_COLOR, FPS

# Initialize Pygame
pygame.init()

# Screen and font settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hacking Game")
font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()

# Terminal variables
input_text = ""
output_lines = []
state = "normal"

# Initialize player and nodes
player = Player(output_lines)
nodes = [
    Node("Server1", {"firewall": 1, "password": 1}),
    Node("Server2", {"firewall": 2, "password": 2, "encryption": 2}),
    Node("Server3", {"encryption": 3})
]

def main():
    global input_text, state
    running = True
    
    # Initial instructions
    show_help(output_lines)

    while running:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                input_text, state = handle_input(event, input_text, state, player, nodes, output_lines, screen, clock)
        
        # Render output lines
        y_offset = 10
        for line in output_lines[-20:]:  # Show only the last 20 lines
            draw_text(screen, line, (10, y_offset), font)
            y_offset += FONT_SIZE + 5
        
        # Render input text
        draw_text(screen, "> " + input_text, (10, y_offset), font, INPUT_COLOR)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
