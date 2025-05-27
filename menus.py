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
        if isinstance(self, SubMenu):
            print('"b" to go back to Main Menu')
        print('"x" to quit Hash Radish')

    def addOption(self, option: str) -> None:
        self.options.append(option)

    def getOptionIndex(self, choice: str) -> int:
        '''
        This is the method that maps user input ("1") to one of the menu items
        if the input is invalid, it returns -1
        '''
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.options):
                return index
            else:
                return -1
        except ValueError:
            return -1


class SubMenu(Menu):
    def __init__(self, parent: 'Menu', title: str,
                 options: list[str] = []) -> None:
        super().__init__(title, options)
        self.parent = parent

    # return to previous/parent menu
    def goBack(self) -> 'Menu':
        return self.parent


__all__ = ['SubMenu', 'Menu']
