#Imports
import time


#Funnctions
def progress_bar(progress,total):
    #Create percentage based on the values given
    percent = 100 * (progress / float(total))
    #Create the bar according to the percentage
    bar = "█" * int(percent) + "-" * (100-int(percent))
    #Print the progress bar itself
    print(f"\r|{bar}| {percent:.2f}", end="\r")

def main_loop():
    print("Welcome to Cli-doro.") #Greet the user.

    study_time = input("How long would you like a session to be? (in munites)\n")
    break_time = input("\nHow long would you like a break to be? (in munites)\n")