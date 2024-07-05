import time
from ahk import AHK
from .config import config

# Initialize AHK
ahk = AHK()

class Contacts:
    def __init__(self, contact):
        self.contact = contact
        self.dialpad()
        time.sleep(config['waits']['medium'])
        self.dial_number(config['contacts'][contact])

    # Function to perform the sequence of actions to open the phone and navigate
    def dialpad(self):
        ahk.click(button='middle')  # Middle click to open the phone
        time.sleep(config['waits']['phone_open'])  # Delay to ensure the action is registered
        ahk.send('{Up}')  # Press 'up'
        time.sleep(config['waits']['short'])
        ahk.send('{Right}')  # Press 'right'
        time.sleep(config['waits']['short'])
        ahk.send('{Enter}')  # Press 'enter'
        time.sleep(config['waits']['short'])
        ahk.click(button='middle')  # Middle click to get to dialpad

    # Function to dial a number
    def dial_number(self, number):
        number = number.replace("-", "")  # Remove hyphens from the number
        digit_positions = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2),
            '0': (3, 1)
        }
        
        current_position = [0, 0]  # Start at '1'
        
        for digit in number:
            if digit in digit_positions:
                target_position = digit_positions[digit]
                move_y = target_position[0] - current_position[0]
                move_x = target_position[1] - current_position[1]

                # Debug statements
                print(f"Dialing digit: {digit}")
                print(f"Current position: {current_position}")
                print(f"Target position: {target_position}")
                print(f"Move Y: {move_y}, Move X: {move_x}")
                
                if move_y > 0:
                    for _ in range(move_y):
                        ahk.send('{Down}')
                        time.sleep(config['waits']['short'])
                elif move_y < 0:
                    for _ in range(abs(move_y)):
                        ahk.send('{Up}')
                        time.sleep(config['waits']['short'])
                
                if move_x > 0:
                    for _ in range(move_x):
                        ahk.send('{Right}')
                        time.sleep(config['waits']['short'])
                elif move_x < 0:
                    for _ in range(abs(move_x)):
                        ahk.send('{Left}')
                        time.sleep(config['waits']['short'])
                
                ahk.send('{Enter}')  # Select the digit
                time.sleep(config['waits']['short'])
                
                current_position = target_position  # Update current position
                print(f"Updated position: {current_position}")
        
        ahk.click(button='middle')  # Close the phone
        print("Phone closed")

