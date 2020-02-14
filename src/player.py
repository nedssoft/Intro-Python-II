 # Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap
class Player:
    def __init__(self, name, current_room, items =[]):
       self.name = name
       self.current_room = current_room
       self.items = items
    
    def __str__(self):
        room_info = f'Current room: {self.current_room.name}\nDescription: {self.print_description()}\n'
        if (len(self.current_room.items)):
           return  room_info + f'Room Items: {self.current_room}'
        else:
            return room_info

    
    def print_description(self):
        wrapper = textwrap.TextWrapper(width=50) 
    
        string = wrapper.fill(text=self.current_room.description) 
        return string

    def print_items(self):
        if (not len(self.items)):
            return f'{self.name} has no item at the moment'

        msg = f'{self.name} currently carries the following items:\n'
        count = 1
        for item in self.items:
            msg += f'[{count}]: {item}'
        return msg

