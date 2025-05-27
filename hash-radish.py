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
    currentMenu = MainMenu
    menuChoice = ''

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
                print("This functionality is still in the works.")
                continue

        # handle Algorithm Menu
        elif currentMenu == AlgMenu and menuChoice != 'x':
            if menuChoice == 'back':
                currentMenu = currentMenu.goBack()
            elif optionIndex >= 0:
                algorithm = ALGORITHMS[optionIndex]
                try:
                    hasher = Hasher(userInput, algorithm)
                    hash_value = hasher.hash()
                    print(f"\nInput: {userInput}")
                    print(f"Algorithm: {algorithm}")
                    print(f"Hash: {hash_value}\n")
                    currentMenu = MainMenu  # Return to main menu
                except ValueError as e:
                    print(f"[ERROR] {e}")
                    currentMenu = MainMenu
                except Exception as e:
                    print(f"[ERROR] Unexpected error: {e}")
                    currentMenu = MainMenu
if __name__ == '__main__':
    main()
