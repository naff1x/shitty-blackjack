import sys
import os

if sys.platform == "darwin": #If the user's OS = MacOS...
    os.system('pip3 install --user arcade') #Installs files necessary for the 'Arcade' library.
    print("* Finished library install *")

if sys.platform == "win32": #If the user's OS = Windows...
    os.system('pip install --user arcade') 
    print("* Finished library install *")

import arcade

def openWindow():
    width = int(input("Enter window width (px): "))
    height = int(input("Enter window height (px): "))
    arcade.open_window(width,height,"Window") #This line causes MaxOS to generate a ApplePersistenceIgnoreState warning. Enter command 'defaults write org.python.python ApplePersistenceIgnoreState NO' to solve.
    arcade.run()
    
class GameWindow(arcade.Window):
    def __init__(self, width=800, height=600, title='Arcade Window', fullscreen=False, resizable=False, update_rate=1 /60, antialiasing=True):
        return super().__init__(width=width, height=height, title=title, fullscreen=fullscreen, resizable=resizable, update_rate=update_rate, antialiasing=antialiasing)

#   WRITE CODE ABOVE THIS LINE
if __name__ == "__main__": #Runs indented code if this file is regarded as "main"
    #import arcade #Imports 'Arcade' library so that we can actually use it in the file.
    print("* Using Arcade version",arcade.VERSION,"*")
    #openWindow()
    unit = GameWindow(700,400,"Shitty Blackjack",False,True)
    arcade.run()