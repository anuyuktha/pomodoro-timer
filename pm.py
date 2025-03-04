import winsound
import time
# this is a pomodoro timer

def breaksound():
    duration=100
    freq=2000
    for i in range(0,3):
        winsound.Beep(freq,duration)
def worksound():
    duration=2000
    freq=3000
    winsound.Beep(freq,duration)

        
start = input("Would you like to begin Timing? (y/n): ")
def timer(a,b):
    print("This is the timer")
    if start == "y":
        timeloop=True
    # Variables to keep track and display
    Sec = b
    Min = a
    # Begin Process
    while timeloop:
        
        print(str(Min) + " Mins " + str(Sec) + " Sec ")
        time.sleep(1)
        if Sec==0:
            if Min==0:
                
                break
            Min-=1
            Sec=59
        else:
         
            Sec-=1
def stop():
    print("WATER BREAK!!")
    timer(5,3)
    breaksound()
def pomodoro():
    cycle=int(input("How many pomodoro cycles are required? Each cycle includes 25 minutes along with a 5 minute break.  :"))
    for i in range (1,cycle+1):
        print("WORK TIMEEEE")
        timer(25,0)
        worksound()
        stop()
        print("GREAT WORK!!")
for i in range(1,5):
    pomodoro()
    print("LONG BREAK! GREAT JOB!!")
    timer(30,00)
pomodoro()




