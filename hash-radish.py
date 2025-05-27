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

def getMenuChoice() -> str:
    menuChoice: str = str(input('\n>> ').lower().strip())
    return menuChoice

def main():
    # Initialize Menus and Constants
    # List of available hash algorithms
    
    MAINTITLE = 'Hash Radish - Main Menu'
    MAINOPTIONS = ['User Input', 'File Input']

    MainMenu = Menu(MAINTITLE, MAINOPTIONS)

    ALGTITLE = 'Algorithm Menu'
    ALGORITHMS = [
            'sha224',
            'sha256',
            'sha384',
            'sha512',
            'sha3-224',
            'sha3-256',
            'sha3-384',
            'sha3-512'
    ]
    AlgMenu = SubMenu(MainMenu, ALGTITLE, ALGORITHMS)

    # Set initial user choice, active menu, and start program loop
    currentMenu: 'Menu' = MainMenu
    menuChoice: str = ''
    userInput: str | None = None # stores user input or filepath
    isFile: bool = False # tracks if user input is a filepath

    while menuChoice != 'x':
        currentMenu.displayMenu()
        menuChoice = getMenuChoice()

        # get index number of user choice
        optionIndex = currentMenu.getOptionIndex(menuChoice)

        # Handle exit
        if menuChoice == 'x':
            print('Goodbye.')
            continue

        # Handle return to main menu
        elif menuChoice == 'b':
            currentMenu = MainMenu
            userInput = None
            isFile = False
            continue
        
        # Handle Main Menu
        if currentMenu == MainMenu and menuChoice != 'x':
            if optionIndex == 0: # index of 'User Input'
                userInput = str(input("What would you like to hash?\n>> ")).strip()
                if not userInput:
                    print("[ERROR] No input provided.")
                    continue
                currentMenu = AlgMenu
            elif optionIndex == 1: # File input not implemented yet
                filePath = str(input("Enter the file path to hash:\n>> ")).strip()
                if not filePath:
                    print("[ERROR] No file path provided.")
                    continue
                if not os.path.isfile(filePath):
                    print("[ERROR] Invalid file path or file does not exist.")
                    continue
                userInput = filePath
                isFile = True
                currentMenu = AlgMenu

        # handle Algorithm Menu
        elif currentMenu == AlgMenu and menuChoice != 'x':
            if menuChoice == 'back':
                currentMenu = currentMenu.goBack()
            elif optionIndex >= 0:
                algorithm = ALGORITHMS[optionIndex]
                try:
                    hasher = Hasher(userInput, algorithm, isFile)
                    hash_value = hasher.hash()
                    if isFile:
                        print(f"\nFile: {userInput}")
                    else:
                        displayInput = userInput if len(userInput) < 50 else userInput[:47] + '...'
                        print(f"\nInput: {displayInput}")
                    print(f"Algorithm: {algorithm}")
                    print(f"Hash: {hash_value}\n")
                    currentMenu = MainMenu  # Return to main menu
                    userInput = None
                    isFile = False
                except FileNotFoundError:
                    print("[ERROR] File not found. Please check the path.")
                    currentMenu = MainMenu
                    userInput = None
                    isFile = False
                except PermissionError:
                    print("[ERROR] Permission denied. Unable to access file.")
                    currentMenu = MainMenu
                    userInput = None
                    isFile = False
                except ValueError as e:
                    print(f"[ERROR] {e}")
                    currentMenu = MainMenu
                    userInput = None
                    isFile = False
                except Exception as e:
                    print(f"[ERROR] Unexpected error: {e}")
                    currentMenu = MainMenu
                    userInput = None
                    isFile = False
if __name__ == '__main__':
    main()
