import time
import keyboard
from threading import Thread
from ahk import AHK
from lib.interaction_menu import InteractionMenu
from lib.contacts import Contacts
from lib.config import config
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Initialize AHK
ahk = AHK()

# Global context
context = {
    'personal_vehicle': True,
    'vip': False,
    'indoors': True,
}

# Function to get the value of start_offset based on context
def offset():
    return 1 if get_context('indoors') else 0

# Function to update context persistently
def update_context(key, value):
    global context
    context[key] = value
    print(f"Context updated: {key} = {value}")
    update_ui()

# Function to read context
def get_context(key):
    return context.get(key, None)

# Function to toggle context value
def toggle_context(key):
    current_value = get_context(key)
    new_value = not current_value
    update_context(key, new_value)
    print(f"Toggled context {key}: {new_value}")

# Function to update UI based on context
def update_ui():
    for key, (label, dot) in context_labels.items():
        color = "green" if context[key] else "red"
        dot.config(bg=color)

# Action: Open Armor Menu
def open_armor_menu():
    log("Action: Open Armor Menu")
    InteractionMenu(offset()).navigate_to_menu(['Health and Ammo', 'Body Armor'])

# Action: Open Snack Menu
def open_snack_menu():
    log("Action: Open Snack Menu")
    InteractionMenu(offset()).navigate_to_menu(['Health and Ammo', 'Snacks'])

# Action: Toggle Personal Vehicle
def toggle_personal_vehicle():
    log("Action: Toggle Personal Vehicle")
    log(f"Current personal vehicle context: {get_context('personal_vehicle')}")
    if get_context('personal_vehicle'):
        log("Returning personal vehicle to storage...")
        InteractionMenu(offset()).navigate_to_menu(['Manage Vehicles', 'Return Personal Vehicle to Storage'])
        send_key('{Enter}')
        update_context('personal_vehicle', False)
    else:
        log("Requesting personal vehicle...")
        InteractionMenu(offset()).navigate_to_menu(['Manage Vehicles', 'Request Personal Vehicle'])
        send_key('{Enter}')
        update_context('personal_vehicle', True)
    send_key('{Enter}')
    send_key('m')

# Action: Call CEO Buzzard
def call_ceo_buzzard():
    log("Action: Call CEO Buzzard")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'CEO Vehicles', 'Buzzard'])

# Action: Call CEO Baller
def call_ceo_baller():
    log("Action: Call CEO Baller")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'CEO Vehicles', 'Baller LE LWB'])

# Action: Call CEO Turreted Limo
def call_ceo_turreted_limo():
    log("Action: Call CEO Turreted Limo")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'CEO Vehicles', 'Turreted Limo'])

# Action: Call CEO XLS
def call_ceo_xls():
    log("Action: Call CEO XLS")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'CEO Vehicles', 'XLS'])

# Action: CEO Retire
def ceo_retire():
    log("Action: CEO Retire")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'Retire'])

# Action: Resiger as CEO
def register_as_ceo():
    log("Action: Register as CEO")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'Register as Boss', 'SecuroServ CEO', 'Start an Organization'])

# Action: Register as MC President
def register_as_mc_president():
    log("Action: Register as MC President")
    InteractionMenu(offset()).navigate_to_menu(['CEO', 'Register as Boss', 'Motorcycle Club President', 'Start a Motorcycle Club'])

# Action: Call Mechanic
def call_mechanic():
    log("Action: Call Mechanic")
    Contacts('mechanic')

# Action: Call Mors Mutual
def call_mors_mutual():
    log("Action: Call Mors Mutual")
    Contacts('mors_mutual')

# Action: Call Pegasus
def call_pegasus():
    log("Action: Call Pegasus")
    Contacts('pegasus')

# Action: Call Merryweather
def call_merryweather():
    log("Action: Call Merryweather")
    Contacts('merryweather')

# Action: Call Assistant
def call_assistant():
    log("Action: Call Assistant")
    Contacts('assistant')

# Action: Call Lester
def call_lester():
    log("Action: Call Lester")
    Contacts('lester')

# Action: Call Pavel
def call_pavel():
    log("Action: Call Pavel")
    Contacts('pavel')

# Action: Call Paige
def call_paige():
    log("Action: Call Paige")
    Contacts('paige')

# Action: Call Emergency
def call_emergency():
    log("Action: Call Emergency")
    Contacts('emergency')

# Action: Toggle Personal Vehicle Context
def toggle_personal_vehicle_context():
    log("Action: Toggle Personal Vehicle Context")
    toggle_context('personal_vehicle')

# Action: Toggle VIP Context
def toggle_vip_context():
    log("Action: Toggle VIP Context")
    toggle_context('vip')

# Action: Toggle Indoor Context
def toggle_indoor_context():
    log("Action: Toggle Indoor Context")
    toggle_context('indoors')

# Action: Change Outfit
def change_outfit():
    log("Action: Change Outfit")
    InteractionMenu(offset()).navigate_to_menu(['Appearance', 'Outfit'])
    send_key('{Right}')
    send_key('{Enter}')
    send_key('m')

# Map the function keys and their combinations to their corresponding actions
hotkey_actions = {
    "f5": open_armor_menu,
    "f6": open_snack_menu,
    "f7": toggle_personal_vehicle,
    "f8": call_ceo_buzzard,
    "f9": call_ceo_baller,
    "f10": call_ceo_turreted_limo,
    "f11": call_ceo_xls,
    "f12": ceo_retire,
    "f13": register_as_ceo,
    "f14": register_as_mc_president,

    "shift+f5": call_mechanic,
    "shift+f6": call_mors_mutual,
    "shift+f7": call_pegasus,
    "shift+f8": call_merryweather,
    "shift+f9": call_assistant,
    "shift+f10": call_lester,
    "shift+f11": call_pavel,
    "shift+f12": call_paige,
    "shift+f13": call_emergency,

    "ctrl+f5": toggle_personal_vehicle_context,
    "ctrl+f6": toggle_vip_context,
    "ctrl+f7": toggle_indoor_context,

    "alt+f5": change_outfit,
    # Add more combinations as needed
}

# Function to send a single keystroke using AHK
def send_key(key):
    time.sleep(config['waits']['very_short'])
    ahk.send(key)

# Function to bind hotkeys
def bind_hotkeys():
    for key, action in hotkey_actions.items():
        keyboard.add_hotkey(key, action)

# Function to unbind hotkeys
def unbind_hotkeys():
    for key in hotkey_actions.keys():
        keyboard.remove_hotkey(key)

# Start a separate thread for the hotkey listener
def start_hotkey_listener():
    bind_hotkeys()
    print("Hotkey listener started.")
    keyboard.wait()  # Keep the listener running

# Function to update UI based on context
def update_ui():
    for key, (label, dot) in context_labels.items():
        color = "green" if context[key] else "red"
        dot.config(bg=color)

# Function to log messages to the UI
def log(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)

# Function to toggle context from the UI
def toggle_context_from_ui(key):
    toggle_context(key)
    update_ui()

# Function to toggle dark mode
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

# Function to apply the current theme
def apply_theme():
    bg_color = "#2e2e2e" if dark_mode else "#f0f0f0"
    fg_color = "#ffffff" if dark_mode else "#000000"
    for key, (label, dot) in context_labels.items():
        dot.config(bg="green" if context[key] else "red")
        frame = dot.master
        frame.config(bg=bg_color)
        label.config(bg=bg_color, fg=fg_color)
        frame.pack_configure(side=tk.TOP, anchor=tk.W, pady=2)
    root.config(bg=bg_color)
    context_frame.config(bg=bg_color)
    log_frame.config(bg=bg_color)
    log_text.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    toggle_button.config(bg=bg_color, fg=fg_color)

# Create the UI
root = tk.Tk()
root.title("GTA V Hotkey Manager")
root.geometry("500x400")

dark_mode = False

# Context Frame
context_frame = tk.Frame(root)
context_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

context_labels = {}
for key in context:
    frame = tk.Frame(context_frame)
    frame.pack(side=tk.TOP, anchor=tk.W, pady=2)
    dot = tk.Label(frame, text="   ", bg="green" if context[key] else "red", width=2)
    dot.pack(side=tk.LEFT)
    label = tk.Label(frame, text=key.capitalize(), width=20, anchor=tk.W)
    label.pack(side=tk.LEFT, padx=(0, 10))
    button = tk.Button(frame, text="Toggle", command=lambda k=key: toggle_context_from_ui(k))
    button.pack(side=tk.LEFT)
    context_labels[key] = (label, dot)

# Log Frame
log_frame = tk.Frame(root)
log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
log_text = ScrolledText(log_frame, state=tk.DISABLED, height=15)
log_text.pack(fill=tk.BOTH, expand=True)

toggle_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
toggle_button.pack(pady=10)

apply_theme()

# Start the hotkey listener in a separate thread
listener_thread = Thread(target=start_hotkey_listener)
listener_thread.daemon = True  # Allow thread to exit when the main program exits
listener_thread.start()

# Start the Tkinter main loop
root.mainloop()

# Ensure listener is stopped when the GUI exits
unbind_hotkeys()
print("Hotkey listener stopped.")
