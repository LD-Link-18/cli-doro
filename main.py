#Imports
import time

#Classes
class inputs_class():
    def __init__(self):
        # Get the necessary inputs
        self.work_time = int(float(input("How long would you like a session to be? (in munites)\n"))*60)
        self.break_time = int(float(input("\nHow long would you like a break to be? (in munites)\n"))*60)
        self.reps = input("\nHow much repetitions do you want?\n")
        self.start_input = input("Type 'start' to start.\n")

#Funnctions
def progress_bar(progress,total):
    #Create percentage based on the values given
    percent = 100 * (progress / float(total))
    #Create the bar according to the percentage
    bar = "█" * int(percent) + "-" * (99-int(percent))
    #Print the progress bar itself
    print(f"\r|{bar}| %{percent:.2f}", end="\r")

def timer(wt,bt,rps,rp,timer_type):
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
                progress_bar(time_diff,wt)
            else:
                print(f"\nFinished session {rp}/{rps}.")
                print(f"Taking a break for {float(bt/60)} munites.")
                break       
    elif timer_type == "break":
        #Same thing as the previous if statement
        starting_time = time.time()
        while True:
            time_now = time.time()
            time_diff = time_now - starting_time
            if time_diff < bt:
                progress_bar(time_diff,bt)
            else:
                print(f"\nFinished break.")
                break 

def main_loop():
    print("Welcome to cli-doro.")

    #Get inputs
    inputs = inputs_class()

    if inputs.start_input == "start":
        for i in inputs.reps:
            timer(inputs.work_time,inputs.break_time,inputs.reps,i,"work")
            timer(inputs.work_time,inputs.break_time,inputs.reps,i,"break")
        print("Congratulations you have finished your goal.")

if __name__ == "__main__":
    main_loop()