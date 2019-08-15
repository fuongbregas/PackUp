import os.path
from os import path
import mainScreen
import startScreen

def main():
   if(path.exists('folderLocation.txt')):
       mainScreen.runMainScreen()
   else:
       startScreen.runStartScreen()

if __name__== "__main__":
   main()
