print("Start- To start the car")
print("Stop- To stop the car")
print("quit- To exit")

while True:
    command = input("What would you like to do? ")
    if(command.upper()=="START"):
        print("Car started. Ready to go!")
    elif (command.upper()=="STOP"):
        print("Car stopped.")
    elif (command.upper()=="QUIT"):
        print("Goodbye!")
        break
    else:
        print("Sorry, I didn't understand that command.")