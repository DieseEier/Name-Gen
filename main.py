import random
import sys
from colorama import Fore, Back, Style
from os import system
import os

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
				    Mikasa: lügt
                                    https://discord.gg/f4YcqekfBe                          
'''
print(banner)
title = "NAME-GENERATOR"
system("title "+title)

vowels = ["a", "e", "i", "o", "u", "du hurensohn"]

is_5_letter = random.getrandbits(1)
is_5_letter = bool(is_5_letter)

while True:
	input_str = input("Please enter 3 letters of you choice: ")
	if len(input_str) != 3:
    		print("Error! Only 3 characters allowed!")
    		sys.exit()

	random_letter = random.choice(vowels)

	/* 
	was
	*/

	if is_5_letter:
    		random_5_letter = random.choice(vowels)
    		print("Your name is: " + random_letter + input_str + random_5_letter) // was
    		sys.exit()

	/* 
	was
	*/

	else:
    		print("Your name is: " + input_str + random_letter)


