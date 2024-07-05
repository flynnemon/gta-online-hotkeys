# GTA V Hotkey Manager

## Overview

GTA V Hotkey Manager is a Python-based tool that allows you to manage various in-game actions using predefined hotkeys. It provides a user-friendly interface to monitor the state of different contexts and logs actions performed.

## Features

- Manage vehicle and character actions in GTA V with hotkeys.
- Toggle contexts such as personal vehicle, VIP, and indoor status.
- Call various contacts (e.g., Mechanic, Mors Mutual, Pegasus) in the game.
- Display a user interface with status indicators and action logs.

## Requirements

- Python 3.8 or higher
- `keyboard` library
- `ahk` library
- `tk` library (for the UI)

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```sh
   python main.py
   ```

2. The UI will display the current context statuses and log the actions performed via hotkeys.

## Hotkey Actions

### Function Keys

- **F5**: Open Armor Menu
- **F6**: Open Snack Menu
- **F7**: Toggle Personal Vehicle
- **F8**: CEO calls a Buzzard
- **F9**: CEO calls a Baller
- **F10**: CEO calls a Turreted Limo
- **F11**: CEO calls an XLS
- **F12**: CEO Retires
- **F13**: Register as a CEO
- **F14**: Register as an MC President

### Shift + Function Keys

- **Shift + F5**: Call Mechanic
- **Shift + F6**: Call Mors Mutual
- **Shift + F7**: Call Pegasus
- **Shift + F8**: Call Merryweather
- **Shift + F9**: Call Assistant
- **Shift + F10**: Call Lester
- **Shift + F11**: Call Pavel
- **Shift + F12**: Call Paige
- **Shift + F13**: Call Emergency

### Ctrl + Function Keys

- **Ctrl + F5**: Toggle Personal Vehicle Context
- **Ctrl + F6**: Toggle VIP Context
- **Ctrl + F7**: Toggle Indoor Context

### Alt + Function Keys

- **Alt + F5**: Change Outfit

## Configuration

Modify the `config.py` file to customize the contacts, wait times, and interaction menu paths.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Acknowledgements

This project uses the `keyboard`, `ahk`, and `tk` libraries for hotkey management and UI.