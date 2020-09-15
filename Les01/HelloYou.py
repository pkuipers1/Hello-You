import time
from datetime import datetime

def mijnprogramma():

    #datum en tijd
    datumentijd = datetime.now()

    #intro van het programma
    print('Hello You!, I am Patricia.')
    time.sleep(1.5)
    naam = input("Who are you?\n")

    #wacht op user input
    time.sleep(1.5)
    print("Hello",naam,"!","The date and time is",datumentijd)

    #opnieuw? - heeft nog geen loop voor ongeldige invoer
    restart = input("Do you want to restart the program? Type 'Y' for yes or 'N' for no.\n")
    if restart == 'y' or restart == 'Y':
        print('Restarting...\n')
        time.sleep(1.5)
        mijnprogramma()
    elif restart == 'n' or restart == 'N':
        print('Bye!')
    else:
        print('Invalid input')

mijnprogramma()
