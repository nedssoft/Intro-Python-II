# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        if (not len(self.items)):
            return f'There is no item in {self.name} room'
        else:
            output = f'{self.name} has the following items\n'
            item_count = 1
            for item in self.items:
                output += f'[{item_count}]: {item}\n'
                item_count += 1
            return output

