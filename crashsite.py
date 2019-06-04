def basicImport():
    import os
    os.system('pip3 install --user arcade') #Installs files necessary for the 'Arcade' library.
    print("* Finished library install *") 

def openWindow():
    width = int(input("Enter window width (px): "))
    height = int(input("Enter window height (px): "))
    arcade.open_window(width,height,"Test") #This line causes MaxOS to generate a ApplePersistenceIgnoreState warning. Enter command 'defaults write org.python.python ApplePersistenceIgnoreState NO' to solve.
    arcade.run()

if __name__ == "__main__": #Runs indented code if this file is regarded as "main"
    #basicImport()
    import arcade #Imports 'Arcade' library so that we can actually use it in the file.
    print("* Using Arcade version",arcade.VERSION,"*")
    openWindow()
