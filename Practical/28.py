class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        if isinstance(item, Item):
            self.menu.append(item)
            print(f"Item '{item.name}' added to the menu.")
        else:
            print("Only items of type 'Item' can be added to the menu.")

    def remove_item(self, item_name):
        for item in self.menu:
            if item.name == item_name:
                self.menu.remove(item)
                print(f"Item '{item_name}' removed from the menu.")
                return
        print(f"Item '{item_name}' not found in the menu.")

    def display_menu(self):
        if self.menu:
            print(f"Menu for {self.name}:")
            for item in self.menu:
                print(f" - {item.name}: {item.price}")
        else:
            print(f"The menu for {self.name} is empty.")
