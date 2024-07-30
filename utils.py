# utils.py

import pygame
import sys
from settings import FONT_COLOR, INPUT_COLOR
from node import scan, hack, perform_hack

def draw_text(surface, text, pos, font, color=FONT_COLOR):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

def handle_input(event, input_text, state, player, nodes, output_lines, screen, clock):
    if event.key == pygame.K_RETURN:
        output_lines.append("> " + input_text)
        if state == "normal":
            if input_text == "scan":
                output_lines.append("Choose a node to scan:")
                for i, node in enumerate(nodes):
                    output_lines.append(f"[{i + 1}] {node.name}")
                state = "scan"
            elif input_text == "hack":
                output_lines.append("Choose a node to hack:")
                for i, node in enumerate(nodes):
                    output_lines.append(f"[{i + 1}] {node.name}")
                state = "hack"
            elif input_text == "upgrade":
                output_lines.append("Choose a tool to upgrade:")
                output_lines.append("[1] Password Cracker")
                output_lines.append("[2] Firewall Disabler")
                output_lines.append("[3] Encryption Breaker")
                state = "upgrade"
            elif input_text == "help":
                show_help(output_lines)
            elif input_text == "exit":
                pygame.quit()
                sys.exit()
            else:
                output_lines.append("Invalid command.")
        elif state == "scan":
            choice = int(input_text) - 1
            if 0 <= choice < len(nodes):
                scan(nodes[choice], output_lines)
            else:
                output_lines.append("Invalid node.")
            state = "normal"
        elif state == "hack":
            choice = int(input_text) - 1
            if 0 <= choice < len(nodes):
                hack(player, nodes[choice], output_lines, screen, clock)
                state = f"hack_{choice}"
            else:
                output_lines.append("Invalid node.")
                state = "normal"
        elif state.startswith("hack_"):
            choice = int(state.split("_")[1])
            node = nodes[choice]
            method = input_text.lower()
            if method in ["bypass", "crack", "decrypt"]:
                perform_hack(player, node, output_lines, screen, clock, method)
            else:
                output_lines.append("Invalid method.")
            state = "normal"
        elif state == "upgrade":
            if input_text == "1":
                player.upgrade_tool("password_cracker")
            elif input_text == "2":
                player.upgrade_tool("firewall_disabler")
            elif input_text == "3":
                player.upgrade_tool("encryption_breaker")
            else:
                output_lines.append("Invalid choice.")
            state = "normal"
        input_text = ""
    elif event.key == pygame.K_BACKSPACE:
        input_text = input_text[:-1]
    else:
        input_text += event.unicode
    return input_text, state

def show_help(output_lines):
    output_lines.append("Welcome to the Hacking Game!")
    output_lines.append("Commands:")
    output_lines.append("scan - Scan a node")
    output_lines.append("hack - Hack a node")
    output_lines.append("upgrade - Upgrade your tools")
    output_lines.append("help - Show commands")
    output_lines.append("exit - Exit the game")
