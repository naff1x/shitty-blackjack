def basicImport():
    import os
    os.system('pip3 install --user arcade')
    print("* Finished library install *")
    import arcade
    print("* Using Arcade version",arcade.VERSION,"*")

if __name__ == "__main__": #Runs indented code if this file is regarded as "main"
    basicImport()