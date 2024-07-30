# node.py

from minigame import play_bypass_minigame, play_crack_minigame, play_decrypt_minigame

class Node:
    def __init__(self, name, defenses):
        self.name = name
        self.defenses = defenses  # Defenses is a dictionary now
        self.hacked = False

def scan(node, output_lines):
    output_lines.append(f"{node.name} Information:")
    for defense, level in node.defenses.items():
        output_lines.append(f"- {defense.replace('_', ' ').title()}: Level {level}")

def hack(player, node, output_lines, screen, clock):
    if node.hacked:
        output_lines.append(f"{node.name} is already hacked.")
        return
    
    output_lines.append("Choose a method to hack:")
    output_lines.append("- Crack")
    output_lines.append("- Bypass")
    output_lines.append("- Decrypt")

def perform_hack(player, node, output_lines, screen, clock, method):
    if method == "bypass" and "firewall" in node.defenses:
        if player.tools["firewall_disabler"]["level"] >= node.defenses["firewall"]:
            output_lines.append("Starting bypass minigame...")
            won = play_bypass_minigame(screen, clock)
        else:
            output_lines.append("Firewall disabler level too low.")
            return
    elif method == "crack" and "password" in node.defenses:
        if player.tools["password_cracker"]["level"] >= node.defenses["password"]:
            output_lines.append("Starting crack minigame...")
            won = play_crack_minigame(screen, clock)
        else:
            output_lines.append("Password cracker level too low.")
            return
    elif method == "decrypt" and "encryption" in node.defenses:
        if player.tools["encryption_breaker"]["level"] >= node.defenses["encryption"]:
            output_lines.append("Starting decrypt minigame...")
            won = play_decrypt_minigame(screen, clock)
        else:
            output_lines.append("Encryption breaker level too low.")
            return
    else:
        output_lines.append("Invalid method or defense type.")
        return

    if won:
        node.hacked = True
        player.credits += 50
        output_lines.append(f"{node.name} hacked successfully! You've earned 50 credits.")
        output_lines.append(f"Total Credits: {player.credits}")
    else:
        output_lines.append("Minigame failed. Hack unsuccessful.")
