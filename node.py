# node.py

from minigame import play_minigame

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
    
    # Start the minigame
    output_lines.append("Initiating server hacking protocol...")
    won = play_minigame(screen, clock)

    if won:
        node.hacked = True
        player.credits += 50
        output_lines.append(f"{node.name} hacked successfully! You've earned 50 credits.")
        output_lines.append(f"Total Credits: {player.credits}")
    else:
        output_lines.append("Hack unsuccessful.")
