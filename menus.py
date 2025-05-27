# Class definition for Main and sub-menus for Hash Radish Program

class Menu:

    def __init__(self, title: str, options: list[str] = []) -> None:
        self.title = title
        self.options = options

    def displayMenu(self) -> None:
        # Prints Menu title with same-length line break
        lineBreak = '-' * len(self.title)
        optionCounter = 1
        print(f"\n{self.title}")
        print(lineBreak)
        for option in self.options:
            print(f"{str(optionCounter)}. {option.title()}")
            optionCounter += 1
        print('"exit" to terminate program')

    def addOption(self, option: str) -> None:
        self.options.append(option)

    def getOptionIndex(self, choice: str) -> int:
        # This is the method that maps user input ("1") to one of the menu items
        # if the input is invalid, it returns -1
        index = int(choice) -1
        if 0 <= index < len(self.options):
            return index
        else:
            return -1


class SubMenu(Menu):
    def __init__(self, parent: 'Menu', title: str, options: list[str] = []) -> None:
        super().__init__(title, options)
        self.parent = parent

    # return to previous/parent menu
    def goBack(self) -> 'Menu':
        return self.parent
    
__all__ = ['SubMenu', 'Menu']

'''
# TESTING
mainOptions = [
    '1. user input',
    '2. file input',
    '3. line input'
    ]

mainMenu = Menu('Main Menu', mainOptions)
mainMenu.addOption(('"x" to exit'))
currentMenu = mainMenu
currentMenu.displayMenu()

algOptions = ["1. SHA512"]
algMenu = SubMenu(mainMenu, "Algorithm Menu", algOptions)
currentMenu = algMenu
currentMenu.displayMenu()
'''
