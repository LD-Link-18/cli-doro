#Imports
import time
import tqdm

#Classes
class inputs_class():
    def __init__(self):
        # Get the necessary inputs
        self.work_time = int(float(input("How long would you like a session to be? (in munites)\n"))*60)
        self.break_time = int(float(input("\nHow long would you like a break to be? (in munites)\n"))*60)
        self.reps = int(input("\nHow much repetitions do you want?\n"))
        self.start_input = input("Type 'start' to start.\n")

#Funnctions
def progress_bar(t):
    #Run tqdm with some bar formating
    for i in tqdm.tqdm(range(t),bar_format='{l_bar}{bar}| {remaining}'):
        time.sleep(1)

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
                progress_bar(wt)
            else:
                print(f"\nFinished session {rp+1}/{rps}.")
                print(f"Taking a break for {float(bt/60)} munites.")
                break       
    elif timer_type == "break":
        #Same thing as the previous if statement
        starting_time = time.time()
        while True:
            time_now = time.time()
            time_diff = time_now - starting_time
            if time_diff < bt:
                progress_bar(bt)
            else:
                print(f"\nFinished break.")
                break 

def main_loop():
    print("Welcome to cli-doro.")

    #Get inputs
    inputs = inputs_class()

    if inputs.start_input == "start":
        for i in range(int(inputs.reps)):
            timer(inputs.work_time,inputs.break_time,inputs.reps,i,"work")
            timer(inputs.work_time,inputs.break_time,inputs.reps,i,"break")
        print("Congratulations you have finished your goal.")

if __name__ == "__main__":
    main_loop()