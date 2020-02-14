from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms

outside_items = [Item('ocat', 'This is an outside room cat cat'), Item('odog', 'This is an outside room dog')]
foyer_items = [Item('fcat', 'This is a foyer cat'), Item('fdog', 'This is a foyer dog')]
overlook_items = [Item('vcat', 'This is an overlook cat'), Item('vdog', 'This is an overlook dog')]
narrow_items = [Item('ncat', 'This is a narrow cat'), Item('ndog', 'This is a narrow dog')]
treasure_items = [Item('tcat', 'This is a treasure cat'), Item('tdog', 'This is a treasure dog')]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", outside_items ),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", foyer_items),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", overlook_items),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", narrow_items),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", treasure_items),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player('Ned', room['outside'])


valid_commands = ['n','s','e', 'w', 'q', 'i', 'inventory']


# Write a loop that:
#

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

def main():
    command = ''
    while command != 'q':
        print(player)
        command = input('1. Enter either n, s, e or w to move to a cardinal direction\n2. Enter take [item name] or drop [item name] to add or remove item\n3. Enter q to quit: ')
        
        cmd = command.split(' ')
        if (len(cmd) == 1):
            if not command in valid_commands:
                print('You have entered an invalid command')
                exit()
            elif cmd[0] in ['i', 'inventory']:
                print(player.print_items())
            else:
                direction = command+'_to'
                for key,value in room.items():
                    if hasattr(value, direction):
                        player.current_room = getattr(value, direction)
        else:
            verb, obj, *args = cmd
            if verb in ['take', 'get']:
                for i, item in enumerate(player.current_room.items):
                    if item.name == obj:
                        player.current_room.items.pop(i)
                        player.items.append(item)
                        item.on_take()
                        break
                else:
                    print('The item does not exist in the current player\'s room')
            elif verb == 'drop':
                for i, item in enumerate(player.items):
                    if item.name == obj:
                        player.current_room.items.append(item)
                        player.items.pop(i)
                        item.on_drop()
                        break
                else:
                    print('The item does not exist in the current player\'s items')
    print('Bye ✌️')
    exit()

main()
# If the user enters "q", quit the game.