import sys
import os

if sys.platform == "darwin": #If the user's OS = MacOS...
    os.system('pip3 install --user arcade') #Installs files necessary for the 'Arcade' library.
    print("* Finished library install *")

if sys.platform == "win32": #If the user's OS = Windows...
    os.system('pip install --user arcade') 
    print("* Finished library install *")

import arcade

#arcade.open_window(width,height,"Window") #This line causes MacOS to generate a ApplePersistenceIgnoreState warning. Enter command 'defaults write org.python.python ApplePersistenceIgnoreState NO' to solve.

class GameWindow(arcade.Window):
    def __init__(self, width=800, height=600, title='Shitty Blackjack', fullscreen=False, resizable=False, update_rate=1 /60, antialiasing=True):
        return super().__init__(width=width, height=height, title=title, fullscreen=fullscreen, resizable=resizable, update_rate=update_rate, antialiasing=antialiasing)

#   WRITE CODE ABOVE THIS LINE
if __name__ == "__main__": #Runs indented code if this file is regarded as "main"
    #import arcade #Imports 'Arcade' library so that we can actually use it in the file.
    print("* Using Arcade version",arcade.VERSION,"*")
    #openWindow()
    unit = GameWindow()
    arcade.run()