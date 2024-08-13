class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, item_name):
        self.item.append(item_name)

    def remove_item(self, item_name):
        if item_name in self.item:
            self.item.remove(item_name)
        else:
            print('item not found')
    
    def display_items(self):
        for item in self.item:
            print(item)
