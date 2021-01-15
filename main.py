#imports
from os import system
from os import getuid
from sys import exit
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Style

try:

#colors
    global green
    global cyan
    global black
    global light_cyan
    global yellow
    global magenta
    global red
    global light_green
    global light_red
    global reset

    #colors
    green = Fore.GREEN
    cyan = Fore.CYAN
    black = Fore.BLACK
    light_cyan = Fore.LIGHTCYAN_EX
    yellow = Fore.YELLOW
    magenta = Fore.MAGENTA
    red = Fore.RED
    light_green = Fore.LIGHTGREEN_EX
    light_red = Fore.LIGHTRED_EX
    reset = Style.RESET_ALL

    #sudo control
    if getuid() != 0:
        system("clear")
        custom_fig = Figlet(font="banner")
        print(cyan + custom_fig.renderText("O O P S"))
        print(green + "Please Run This Script As A Root.")
        sleep(2.5)
        system("clear")
        exit()
    
    

    

except KeyboardInterrupt:
    system("clear")
    print(cyan + "\nGörüşmek üzere :)")
    print(reset)
    sleep(1)
    system("clear")
    exit()
