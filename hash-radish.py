##########################
#
# Hash Radish
# Version: 1.0.0
#
# By: Jake Murray
#
##########################
from hasher import Hasher
from menus import Menu, SubMenu
import os


def get_menu_choice() -> str:
    menu_choice = input('\n>> ').lower().strip()
    return menu_choice


def main():
    # Initialize Menus and Constants

    MAIN_MENU_TITLE = 'Hash Radish - Main Menu'
    MAIN_MENU_OPTIONS = ['User Input', 'File Input']

    main_menu = Menu(MAIN_MENU_TITLE, MAIN_MENU_OPTIONS)

    ALGORITHM_MENU_TITLE = 'Algorithm Menu'
    HASH_ALGORITHMS = [
            'sha224',
            'sha256',
            'sha384',
            'sha512',
            'sha3-224',
            'sha3-256',
            'sha3-384',
            'sha3-512'
    ]
    algorithm_menu = SubMenu(main_menu, ALGORITHM_MENU_TITLE, HASH_ALGORITHMS)

    # Set initial user choice, active menu, and start program loop
    current_menu: Menu = main_menu
    menu_choice: str = ''
    user_input: str | None = None  # stores user input or filepath
    is_file: bool = False  # tracks if user input is a filepath

    while menu_choice != 'x':
        current_menu.display_menu()
        menu_choice = get_menu_choice()

        # get index number of user choice
        option_index = current_menu.get_option_index(menu_choice)
        if option_index == -1 and menu_choice not in ('x', 'b'):
            print("[ERROR] Invalid option selected."
                  "Please choose a valid option.")
            continue
        # Handle exit
        if menu_choice == 'x':
            print('Goodbye.')
            continue

        # Handle return to main menu
        elif menu_choice == 'b':
            current_menu = main_menu
            user_input = None
            is_file = False
            continue

        # Handle Main Menu
        if current_menu == main_menu and menu_choice != 'x':
            if option_index == 0:  # index of 'User Input'
                user_input = str(input
                                 ("What would you like to hash?\n>> ")).strip()
                if not user_input:
                    print("[ERROR] No input provided.")
                    continue
                current_menu = algorithm_menu
            elif option_index == 1:
                file_path = str(input
                                ("Enter the file path to hash:\n>> ")).strip()
                if not file_path:
                    print("[ERROR] No file path provided.")
                    continue
                if not os.path.isfile(file_path):
                    print("[ERROR] Invalid file path or file does not exist.")
                    continue
                user_input = file_path
                is_file = True
                current_menu = algorithm_menu

        # handle Algorithm Menu
        elif current_menu == algorithm_menu and menu_choice != 'x':
            if menu_choice == 'b':
                current_menu = current_menu.go_back()
            elif option_index >= 0:
                algorithm = HASH_ALGORITHMS[option_index]
                try:
                    hasher = Hasher(user_input, algorithm, is_file)
                    hash_value = hasher.compute_hash()
                    if is_file:
                        print(f"\nFile: {user_input}")
                    else:
                        display_input = user_input if len(user_input) < 50 \
                            else user_input[:47] + '...'
                        print(f"\nInput: {display_input}")
                    print(f"Algorithm: {algorithm}")
                    print(f"Hash: {hash_value}\n")
                    current_menu = main_menu  # Return to main menu
                    user_input = None
                    is_file = False
                except FileNotFoundError:
                    print("[ERROR] File not found. Please check the path.")
                    current_menu = main_menu
                    user_input = None
                    is_file = False
                except PermissionError:
                    print("[ERROR] Permission denied. Unable to access file.")
                    current_menu = main_menu
                    user_input = None
                    is_file = False
                except ValueError as e:
                    print(f"[ERROR] {e}")
                    current_menu = main_menu
                    user_input = None
                    is_file = False
                except Exception as e:
                    print(f"[ERROR] Unexpected error: {e}")
                    current_menu = main_menu
                    user_input = None
                    is_file = False


if __name__ == '__main__':
    main()
