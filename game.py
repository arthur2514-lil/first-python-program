command = ''

while True:
    # Get user input
    command = input('Enter a command:'). lower()

    if command =='quit':
      print("Extiting the game")
      break

    elif command == 'start':
     print("Car Started")

    elif command == "stop":
      print(" CarStoped")

    elif command == 'help':
      print(""""
     start - to start the car
     stop - to stop the car
     quit - to quit the car
     help - to show all command
             """)

    else:
     print("command invalid")