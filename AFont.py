# <  A Note to the wonderful people seeing the code! :]  >
# If you attempt to dissect this code, then please know what you are doing.
# Not even I have the slightest idea of what is happening here.
# Still, I hope this makes your work easier! :D
# <  - Curious Adhvik  >

from SpritesheetMaker import launch1
from SplitSpritesheet import launch2
import time

print("""_______________________\n|                     |\n|  Welcome to AFont!  |\n|                     |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
print("Made by Curious Adhvik\nv1.0\n")

def tguh():

    choice = input("Type 'ready' to start.\nType 'help' for help.\nType 'exit' to exit.\nEnter: ")

    if choice.lower() == "ready":

        step = input("Choose a step:\n\nStep 1: Making the Spritehsheet\nStep 2: Splitting the Spritesheet\nStep 3: Editing in Glyphr Studio\nEnter (1/2/3): ")
        if step == "1":
            launch1()
        elif step == "2":
            launch2()
        elif step == "3":
            print("At the moment, there is no way to automate this process. Please see the video for more information.")

    elif choice.lower() == "help":

        print("This hasn't been implemented at the moment... :(")

    elif choice.lower() == "exit":

        print("Exiting...")
        exit()

    else:

        print("\nInvalid! Please try again.\n")
        tguh()

tguh()
