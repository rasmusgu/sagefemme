import time
import random
import mysql.connector
5
from modules import *
#from story import *
#from commands import *

hpbar = 50

#mahdollistaa pelin häviämisen/restartaamisen
def restart():
    input("When '>>' appears on screen, press enter to continue"  +"\n"+ ">> ")
    print("When '>' appears, you are free to enter commands. Type 'help' if lost")

    chapter1()

    def storymode():
        print("\n"+">>>>Täs kohtaa kävelet sinne, muttei onneks tartte ny")
        input(">> ")
        chapter2()
        return

    #testing purposes
    #storymode()

    #parser
    while hpbar > 0:
        commands()
    if hpbar < 0:
        print("You died.")
    else:
        print("Bye")
    db.rollback()
    db.close()
    print("thank you, se you soon, by")
    input(">> ")
    return

#pyörittää koko peliä
restart()
