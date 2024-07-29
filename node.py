# node.py

class Node:
    def __init__(self, name, defenses):
        self.name = name
        self.defenses = defenses  # Defenses is a dictionary now
        self.hacked = False

def scan(node, output_lines):
    output_lines.append(f"{node.name} Information:")
    for defense, level in node.defenses.items():
        output_lines.append(f"- {defense.replace('_', ' ').title()}: Level {level}")

def hack(player, node, output_lines):
    if node.hacked:
        output_lines.append(f"{node.name} is already hacked.")
        return
    
    for defense, level in node.defenses.items():
        if defense == "firewall" and player.tools["firewall_disabler"]["level"] < level:
            output_lines.append("Failed to bypass Firewall.")
            return
        if defense == "password" and player.tools["password_cracker"]["level"] < level:
            output_lines.append("Failed to crack Password.")
            return
        if defense == "encryption" and player.tools["encryption_breaker"]["level"] < level:
            output_lines.append("Failed to break Encryption.")
            return

    node.hacked = True
    player.credits += 50
    output_lines.append(f"{node.name} hacked successfully! You've earned 50 credits.")
    output_lines.append(f"Total Credits: {player.credits}")
