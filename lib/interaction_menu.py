import time
from ahk import AHK
from .config import config

# Initialize AHK
ahk = AHK()

class InteractionMenu:
    def __init__(self, offset=0):
        self.open_interaction_menu()
        self.offset = offset

    def open_interaction_menu(self):
        ahk.send('m')  # Press 'M' to open the interaction menu
        time.sleep(config['waits']['medium'])  # Delay to ensure the menu is opened

    def navigate_to_menu(self, menu_path):
        menu_level = config['interaction_menu']['level01']
        if 'CEO' in menu_path:
            self.offset = 0
        print(f"Offset: {self.offset}")
        for _ in range(self.offset):
            print("Pressing down for offset")
            ahk.send('{Down}')
            time.sleep(config['waits']['very_short'])
        for menu in menu_path:
            if menu in menu_level:
                items = list(menu_level.keys())
                index = items.index(menu)
                print(f"Navigating to menu: {menu} at index {index}")
                for _ in range(index):
                    ahk.send('{Down}')
                    time.sleep(config['waits']['very_short'])
                ahk.send('{Enter}')
                time.sleep(config['waits']['medium'])
                menu_level = menu_level[menu] if isinstance(menu_level[menu], dict) else {}
            else:
                print(f"Menu item '{menu}' not found")
                return

# Example usage
if __name__ == "__main__":
    # Initialize InteractionMenu with a menu path
    interaction_menu = InteractionMenu(1)
    interaction_menu.navigate_to_menu(['Health and Ammo', 'Body Armor', 'Standard Armor'])
