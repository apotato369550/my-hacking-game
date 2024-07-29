# player.py

class Player:
    def __init__(self, output_lines):
        self.credits = 100
        self.tools = {
            "password_cracker": {"level": 1, "cost": 50},
            "firewall_disabler": {"level": 1, "cost": 50},
            "encryption_breaker": {"level": 1, "cost": 50}
        }
        self.output_lines = output_lines

    def upgrade_tool(self, tool):
        if tool in self.tools:
            if self.credits >= self.tools[tool]["cost"]:
                self.credits -= self.tools[tool]["cost"]
                self.tools[tool]["level"] += 1
                self.tools[tool]["cost"] += 50  # Increase cost for next upgrade
                self.output_lines.append(f"{tool.replace('_', ' ').title()} upgraded to level {self.tools[tool]['level']}!")
                self.output_lines.append(f"New upgrade cost for {tool.replace('_', ' ').title()}: {self.tools[tool]['cost']} credits")
            else:
                self.output_lines.append("Not enough credits to upgrade this tool.")
        else:
            self.output_lines.append("Invalid tool.")
