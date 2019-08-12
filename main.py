import os.path
from os import path
import mainScreen
import startScreen

def main():

   #print ("file exist:"+str(path.exists('guru99.txt')))
   #print ("File exists:" + str(path.exists('career.guru99.txt')))
   #print ("directory exists:" + str(path.exists('myDirectory')))
   if(path.exists('folderLocation.txt')):
       mainScreen.runMainScreen()
   else:
       startScreen.runStartScreen()

if __name__== "__main__":
   main()
