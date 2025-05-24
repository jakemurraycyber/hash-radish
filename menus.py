# Class definition for Main and sub-menus for Hash Radish Program

class Menu:

    def __init__(self, title: str, options: list[str] = []) -> None:
        self.title = title
        self.options = options

    def displayMenu(self) -> None:
        # Prints Menu title with same-length line break
        lineBreak = '-' * len(self.title)
        print(f"\n{self.title}")
        print(lineBreak)
        for option in self.options:
            print(option.title())

    def addOption(self, option: str) -> None:
        self.options.append(option)


class SubMenu(Menu):
    def __init__(self, parent: object, title: str, options: list[str] = []) -> None:
        super().__init__(title, options)
        self.parent = parent

    # return to previous/parent menu
    def goBack(self):
        return self.parent


mainOptions = [
    '1. user input',
    '2. file input',
    '3. line input'
    ]

# TESTING
mainMenu = Menu('Main Menu', mainOptions)
mainMenu.addOption(('"x" to exit'))
currentMenu = mainMenu
currentMenu.displayMenu()

algOptions = ["1. SHA512"]
algMenu = SubMenu(mainMenu, "Algorithm Menu", algOptions)
currentMenu = algMenu
currentMenu.displayMenu()
