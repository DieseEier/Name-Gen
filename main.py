import random
import sys
from colorama import Fore, Back, Style
from os import system
import os

def println(WIEGEHTDAS):
    print(WIEGEHTDAS)

os.system('cls||clear')

banner = f'''{Fore.LIGHTCYAN_EX}
                ███╗   ██╗ █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗███╗   ██╗
                ████╗  ██║██╔══██╗████╗ ████║██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
                ██╔██╗ ██║███████║██╔████╔██║█████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║
                ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝╚════╝██║   ██║██╔══╝  ██║╚██╗██║
                ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝███████╗██║ ╚████║
                ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                
                                    Version: 100.0
                                    Developer: maquzo#6314
                                    Contributer: Bolusterbuster_710
                                    https://discord.gg/f4YcqekfBe                          
'''
println(banner)
title = "NAME-GENERATOR"
system("title "+title)

vowels = ["a", "e", "i", "o", "u"]

is_5_letter = random.getrandbits(1)
is_5_letter = bool(is_5_letter)

while True:
    input_str = input("Please enter 3 letters of you choice: ")
    if len(input_str) != 3:
            println("Error! Only 3 characters allowed!")
            sys.exit()

    random_letter = random.choice(vowels)


    if is_5_letter:
            random_5_letter = random.choice(vowels)
            println("Your name is: " + random_letter + input_str + random_5_letter)
            continue

    else:
            println("Your name is: " + input_str + random_letter)

