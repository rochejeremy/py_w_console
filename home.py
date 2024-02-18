import sys
import os 
from option_modules_1 import *
from option_modules_2 import *
from option_modules_3 import *
from option_modules_4 import *
from classes.utilityClasses import BgColors


menu_options = {
    1: 'Start Instance i-033182bde833796cb',
    2: 'Initialize Remote Command',
    3: 'Shutdown Instance i-033182bde833796cb',
    4: 'Update security groups on assets'
}
menu2_options = {
    5: 'update /etc/hosts',
    0: 'placeholder'
}




os.system('clear')

def print_menu():
    print("ISOLATED VM")
    for key in menu_options.keys():
        print (BgColors.MAINMENU + '[' + str(key) + '] - ' + BgColors.ENDC + BgColors.MAINMENU + str(menu_options[key]) + BgColors.ENDC )
    print("KALI")
    for key in menu_options.keys():
        print (BgColors.MAINMENU + '[' + str(key) + '] - ' + BgColors.ENDC + BgColors.MAINMENU + str(menu_options[key]) + BgColors.ENDC )
    print("JumpBox")
    for key in menu2_options.keys():
        print (BgColors.MAINMENU + '[' + str(key) + '] - ' + BgColors.ENDC + BgColors.MAINMENU + str(menu2_options[key]) + BgColors.ENDC )

def option1():
    exec_option1()
def option2():
    exec_option2()
def option3():
    exec_option3()
def option4():
    exec_option4()

if __name__=='__main__':
    while(True):
        print_menu()
        #text = '♠'
        #print(text)
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
           #os.system('clear')
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 0:
            os.system('clear')
            print('Thanks')
            os.system('clear')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
