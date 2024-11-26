class ItemManager:

    def __init__(self):
        self.items = []

    def add_item_to_database(self, item):
        self.items.append(item)

    def get_all_items_from_database(self):
        return self.items

    def remove_item_from_database(self, item):
        if item in self.items:
            return self.items.remove(item)
        else:
            return "Cannot remove item. item does not exist."

    def find_item_in_database(self, identifier):
        index = 0
        if isinstance(identifier, int):
            for item in self.items:
                if identifier == item["id"]:
                    return self.items[index]
                index += 1
            return "item Not Found"
        else:
            for item in self.items:
                if identifier == item["name"]:
                    return self.items[index]
                index += 1
            return "item Not Found"

    def update_item_in_database(self, item, edited_item):
        index = self.items.index(item)
        self.items[index] = edited_item
