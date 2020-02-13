
class Item:
    def __init__(self, name, descritpion):
        self.name = name
        self.description = descritpion
    
    def on_take(self):
        print(f'You have picked up {self.name}')
    
    def on_drop(self):
        print(f'You have dropped {self.name}')