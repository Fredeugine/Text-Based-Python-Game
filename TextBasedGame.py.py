# Name: Fred Eugine Adomako
inventory = []


# Function to display instructions
def show_instructions():
    # print a main menu and the commands
    print("Student Escape Text Adventure Game\n"
          "Collect 6 items to win the game or remain hostage at the kidnapper's house\n"
          "Move commands: South, North, East, West\n"
          "To take an item: get 'item name'\n"
          "\n")


# Function for everything that occurs at the Gym Room
def gym_room():
    # What to print whenever the user enters this room
    print('You are in the Gym room')
    print('Valid commands in this room:', room_commands['Gym Room'])
    print('Inventory:', inventory)
    user_input = input('Enter your move\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Gym Room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Gym Room'])
        user_input = input('Enter your move\n')
    # A while loop when user retrieves and item, leaves this room and comes back again to take the already retrieved
    # item
    while user_input == room_commands['Gym Room'][2] and 'Shoes' in inventory:
        print('You have already taken your snack')
        user_input = input('Enter a command\n')
        while user_input not in room_commands['Gym Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Gym Room'])
            user_input = input('Enter your move\n')
    # A while loop when user wants to retrieve an item
    while user_input == room_commands['Gym Room'][2] and 'Shoes' not in inventory:
        print('Shoes retrieved!')
        inventory.append('Shoes')
        print('Your inventory now:', inventory)
        # An if statement when user collects the last item in this room
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and escaped the kidnapper! Thanks for playing the '
                  'game. Hope you enjoyed it.')
            break
        user_input = input('Enter your move\n')
        while user_input == room_commands['Gym Room'][2]:
            print('You have already taken your shoes')
            user_input = input('Enter a different command\n')
        while user_input not in room_commands['Gym Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Gym Room'])
            user_input = input('Enter your move\n')
            while user_input == room_commands['Gym Room'][2]:
                print('You have already taken your shoes')
                user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Gym Room'][1]:
        living_room()
    elif user_input == room_commands['Gym Room'][0]:
        playroom()


# Function for everything that occurs at the Play room
def playroom():
    # What to print whenever the user enters this room
    print('You are in the Playroom')
    print('Valid commands in this room:', room_commands['Play Room'])
    print('Inventory:', inventory)
    user_input = input('Enter your move\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Play Room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Play Room'])
        user_input = input('Enter your move\n')
    # A while loop when user retrieves and item, leaves this room and comes back again to take the already retrieved
    # item
    while user_input == room_commands['Play Room'][2] and 'Drawing tools' in inventory:
        print('You have already taken your Drawing tools')
        user_input = input('Enter a command\n')
        while user_input not in room_commands['Play Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Play Room'])
            user_input = input('Enter your move\n')
    # A while loop when user wants to retrieve an item
    while user_input == room_commands['Play Room'][2] and 'Drawing tools' not in inventory:
        print('Drawing tools retrieved!')
        inventory.append('Drawing tools')
        inventory.sort()
        print('Your inventory now:', inventory)
        # An if statement when user collects the last item in this room
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and escaped the kidnapper! Thanks for playing the '
                  'game. Hope you enjoyed it.')
            break
        user_input = input('Enter your move\n')
        while user_input == room_commands['Play Room'][2]:
            print('You have already taken your drawing tools ')
            user_input = input('Enter a different command\n')
        while user_input not in room_commands['Play Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Play Room'])
            user_input = input('Enter your move\n')
            while user_input == room_commands['Play Room'][2]:
                print('You have already taken your Drawing tools ')
                user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Play Room'][1]:
        library_room()
    elif user_input == room_commands['Play Room'][0]:
        gym_room()


# Function for everything that occurs at the Library room
def library_room():
    # What to print whenever the user enters this room
    print('You are in the Library room')
    print('Valid commands in this room:', room_commands['Library Room'])
    print('Inventory:', inventory)
    user_input = input('Enter a command\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Library Room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Library Room'])
        user_input = input('Enter a different command\n')
    # A while loop when user retrieves and item, leaves this room and comes back again to take the already retrieved
    # item
    while user_input == room_commands['Library Room'][3] and 'Books' in inventory:
        print('You have already taken your Books')
        user_input = input('Enter a command\n')
        while user_input not in room_commands['Library Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Library Room'])
            user_input = input('Enter a different command\n')
    # A while loop when user wants to retrieve an item
    while user_input == room_commands['Library Room'][3] and 'Books' not in inventory:
        print('Books retrieved!')
        inventory.append('Books')
        print('Your inventory now:', inventory)
        # An if statement when user collects the last item in this room
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and escaped the kidnapper! Thanks for playing the '
                  'game. Hope you enjoyed it.')
            break
        user_input = input('Enter a command\n')
        while user_input == room_commands['Library Room'][3]:
            print('You have already taken your books')
            user_input = input('Enter a different command\n')
        while user_input not in room_commands['Library Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Library Room'])
            user_input = input('Enter your move\n')
            while user_input == room_commands['Library Room'][3]:
                print('You have already taken your books')
                user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Library Room'][2]:
        laundry_room()
    elif user_input == room_commands['Library Room'][1]:
        playroom()
    elif user_input == room_commands['Library Room'][0]:
        print('You have awaken the kidnapper. Game over!.  Thanks for playing the game. Hope you enjoyed it.')


# Function for everything that occurs in the Living room
def living_room():
    # What to print whenever the user enters this room
    print('You are in the Living room')
    print('Valid commands in this room:', room_commands['Living Room'])
    print('Inventory:', inventory)
    user_input = input('Enter a command\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Living Room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Living Room'])
        user_input = input('Enter a different command\n')
    # A while loop when user retrieves and item, leaves this room and comes back again to take the already retrieved
    # item
    while user_input == room_commands['Living Room'][3] and 'Money' in inventory:
        print('You have already taken your Money')
        user_input = input('Enter a command\n')
        while user_input not in room_commands['Living Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Living Room'])
            user_input = input('Enter a different command\n')
    # A while loop when user wants to retrieve an item
    while user_input == room_commands['Living Room'][3] and 'Money' not in inventory:
        print('Money retrieved!')
        inventory.append('Money')
        print('Your inventory now:', inventory)
        # An if statement when user collects the last item in this room
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and escaped the kidnapper! Thanks for playing the '
                  'game. Hope you enjoyed it.')
            break
        user_input = input('Enter a command\n')
        while user_input == room_commands['Living Room'][3]:
            print('You have already taken some money ')
            user_input = input('Enter a different command\n')
        while user_input not in room_commands['Living Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Living Room'])
            user_input = input('Enter your move\n')
            while user_input == room_commands['Living Room'][3]:
                print('You have already taken some money ')
                user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Living Room'][2]:
        kitchen()
    elif user_input == room_commands['Living Room'][1]:
        gym_room()
    elif user_input == room_commands['Living Room'][0]:
        print('You have awaken the kidnapper. Game Over!.  Thanks for playing the game. Hope you enjoyed it.')


# Function for everything that occurs at the Laundry room
def laundry_room():
    # What to print whenever the user enters this room
    print('You are in the Laundry room')
    print('Valid commands in this room:', room_commands['Laundry Room'])
    print('Inventory:', inventory)
    user_input = input('Enter a command\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Laundry Room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Laundry Room'])
        user_input = input('Enter a different command\n')
    # A while loop when user retrieves and item, leaves this room and comes back again to take the already retrieved
    # item
    while user_input == room_commands['Laundry Room'][2] and 'Uniform' in inventory:
        print('You have already taken your Uniform')
        user_input = input('Enter a command\n')
        while user_input not in room_commands['Laundry Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Laundry Room'])
            user_input = input('Enter a different command\n')
    # A while loop when user wants to retrieve an item
    while user_input == room_commands['Laundry Room'][2] and 'Uniform' not in inventory:
        print('Uniform retrieved!')
        inventory.append('Uniform')
        print('Your inventory now:', inventory)
        # An if statement when user collects the last item in this room
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and escaped the kidnapper! Thanks for playing the '
                  'game. Hope you enjoyed it.')
            break
        user_input = input('Enter a command\n')
        while user_input == room_commands['Laundry Room'][2]:
            print('You have already taken your uniform.')
            user_input = input('Enter a different command\n')
        while user_input not in room_commands['Laundry Room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Laundry Room'])
            user_input = input('Enter your move\n')
            while user_input == room_commands['Laundry Room'][2]:
                print('You have already taken your uniform.')
                user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Laundry Room'][0]:
        main()
    elif user_input == room_commands['Laundry Room'][1]:
        library_room()


# Function for everything that occurs at the Kitchen
def kitchen():
    # What to print whenever the user enters this room
    print('You are in the Kitchen')
    print('Valid commands in this room:', room_commands['Kitchen room'])
    print('Inventory:', inventory)
    user_input = input('Enter a command\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Kitchen room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Kitchen room'])
        user_input = input('Enter a different command\n')
    # A while loop when user retrieves and item, leaves this room and comes back again to take the already retrieved
    # item
    while user_input == room_commands['Kitchen room'][2] and 'Snack' in inventory:
        print('You have already taken your snack')
        user_input = input('Enter a command\n')
        while user_input not in room_commands['Kitchen room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Kitchen room'])
            user_input = input('Enter your move\n')
    # A while loop when user wants to retrieve an item
    while user_input == room_commands['Kitchen room'][2] and 'Snack' not in inventory:
        print('Snack retrieved!')
        inventory.append('Snack')
        print('Your inventory now:', inventory)
        # An if statement when user collects the last item in this room
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and escaped the kidnapper! Thanks for playing the '
                  'game. Hope you enjoyed it.')
            break
        user_input = input('Enter a command\n')
        while user_input == room_commands['Kitchen room'][2]:
            print('You have already taken your snack ')
            user_input = input('Enter a different command\n')
        while user_input not in room_commands['Kitchen room']:
            print('Command is invalid')
            print('Valid commands in this room:', room_commands['Kitchen room'])
            user_input = input('Enter your move\n')
            while user_input == room_commands['Kitchen room'][2]:
                print('You have already taken your snack')
                user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Kitchen room'][1]:
        main()
    elif user_input == room_commands['Kitchen room'][0]:
        living_room()


# The main function
def main():
    global room_commands
    room_commands = {'Storage Room': ['West', 'South', 'East'],
                     'Gym Room': ['West', 'North', 'get Shoes'],
                     'Play Room': ['East', 'North', 'get Drawing tools'],
                     'Library Room': ['East', 'South', 'North', 'get Books'],
                     'Living Room': ['West', 'South', 'North', 'get Money'],
                     'Laundry Room': ['East', 'South', 'get Uniform'],
                     'Kitchen room': ['South', 'West', 'get Snack']
                     }
    # Print statements whenever user enters the Storage room
    print('You are in the Storage room')
    print('Valid commands in this room:', room_commands['Storage Room'])
    print('Inventory:', inventory)
    user_input = input('Enter a command\n')
    # A while loop for invalid commands
    while user_input not in room_commands['Storage Room']:
        print('Command is invalid')
        print('Valid commands in this room:', room_commands['Storage Room'])
        user_input = input('Enter a different command\n')
    # If statements, when user makes a move command
    if user_input == room_commands['Storage Room'][0]:
        laundry_room()
    elif user_input == room_commands['Storage Room'][2]:
        kitchen()
    # elif statement, when user awakens the kidnapper
    elif user_input == room_commands['Storage Room'][1]:
        print('You have awaken the kidnapper. Game over!.  Thanks for playing the game. Hope you enjoyed it.')


show_instructions()
main()
