import os
import shutil
from termcolor import colored, cprint

commands = {
    "1": "Help",
    "2": "Make dir",
    "3": "Remove dir",
    "4": "Add file",
    "5": "Remove file",
    "6": "Rename file/dir",
    "7": "Exit"
}
def help():
    for command in commands:
        print(f"{command}: {commands[command]}")

def make_dir():
    input_name = input(colored("Enter your dirname: ", "blue"))
    os.mkdir(input_name)
    cprint("Successfully created!", "green")

def remove_dir():
    input_name = input(colored("Enter your dirname: ", "blue"))
    if os.path.isdir(input_name):
        shutil.rmtree(input_name)
        cprint("Successfully deleted!", "green")
    else:
        cprint("No such directories like this...", "red")
def make_file():
    file_name = input(colored("Enter your filename: ", "blue"))
    os.mknod(file_name)
    cprint("Successfully created!", "green")

def remove_file():
    file_name = input(colored("Enter your filename: ", "blue"))
    if os.path.exists(file_name):
        os.remove(file_name)
        cprint("Successfully removed!", "green")
    else:
        cprint("No such files like this...", "red")
def rename_file():
    file_name = input(colored("Enter your filename: ", "blue"))
    rename_input = input(colored("Rename file name: ", "blue"))
    if os.path.exists(file_name):
        os.rename(file_name, rename_input)
        cprint("Successfully renamed!", "green")
    else:
        cprint("No such file/directory... ", "red")
help()
input_command = ''
while input_command != "7": 
 input_command = input(colored("Enter command: ", "blue"))

 if input_command == '1':
    help()
 elif input_command == '2':
     make_dir()
 elif input_command == '3':
     remove_dir()
 elif input_command == '4':
     make_file()
 elif input_command == '5':
     remove_file()
 elif input_command == '6':
     rename_file()
 elif input_command == "7":
     break
 else:
     cprint("I don't understand you...", "red")