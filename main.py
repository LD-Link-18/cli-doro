#Imports
import os
import time
import tqdm

#Classes
class inputs_class():
    def __init__(self):
        # Get the necessary inputs
        self.work_time = int(float(input("How long would you like a session to be? (in munites)\n"))*60)
        self.break_time = int(float(input("\nHow long would you like a break to be? (in munites)\n"))*60)
        self.reps = int(input("\nHow many repetitions do you want?\n"))
        self.start_input = input("[S] Start\n")

#Funnctions

def main_loop():
    cls()
    logo()
    #Get inputs
    inputs = inputs_class()

    if inputs.start_input.lower() == "s":
        for i in range(int(inputs.reps)):
            timer(inputs.work_time,inputs.break_time,inputs.reps,i,"work")
            timer(inputs.work_time,inputs.break_time,inputs.reps,i,"break")

        print("Congratulations you have finished your goal.\n")
        print("[M] Return to the main menu")
        print("[Q] Exit application")
        #Return the user to main menu or exit the app
        return_to_menu = input()

        if return_to_menu.lower() == "m":
            cls()
            main_menu()
        elif return_to_menu.lower() == "q":
            cls()
            os.system("exit")

def progress_bar(t):
    #Run tqdm with some bar formating
    for i in tqdm.tqdm(range(t),bar_format='{l_bar}{bar}| {remaining}'):
        time.sleep(1)

def timer(wt,bt,rps,rp,timer_type):
    cls()
    logo()

    if timer_type == "work":
        #Record the starting time
        starting_time = time.time()
        print(f"Starting a session for {float(wt/60)} munites.")
        
        while True:
            #Record the current time
            time_now = time.time()
            time_diff = time_now - starting_time
            #Compare the difference between time_now and starting_time
            #As long as the difference is less than the number user selected update the progress bar
            if time_diff < wt:
                progress_bar(wt)
            else:
                print(f"\nFinished session {rp+1}/{rps}.")
                cls()
                logo()
                print(f"Taking a break for {float(bt/60)} munites.")
                break       
    elif timer_type == "break":
        #Same thing as the previous if block
        starting_time = time.time()
        while True:
            time_now = time.time()
            time_diff = time_now - starting_time
            if time_diff < bt:
                progress_bar(bt)
            else:
                print(f"\nFinished break.")
                cls()
                logo()
                break 
       
def logo():
    print("      __   _____ _      _____      _____   ____  _____   ____   __     ")
    print("     / /  / ____| |    |_   _|    |  __ \ / __ \|  __ \ / __ \  \ \   ")
    print("    / /  | |    | |      | |______| |  | | |  | | |__) | |  | |  \ \   ")
    print("   / /   | |    | |      | |______| |  | | |  | |  _  /| |  | |   \ \  ")
    print("  / /    | |____| |____ _| |_     | |__| | |__| | | \ \| |__| |    \ \ ")
    print(" /_/      \\_____|______|_____|    |_____/ \\____/|_|  \\_\\\\____/      \\_\\")
    print("")

def main_menu():
    cls()
    logo()
    print("[P] Pomodoro")
    print("[Q] Exit")

    menu_input = input()
    if menu_input.lower() == "p":
        main_loop()
    elif menu_input.lower() == "q":
        os.system("exit")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main_menu()