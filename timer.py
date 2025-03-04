import winsound
import time


def breaksound():
    duration=100
    freq=2000
    for i in range(0,3):
        winsound.Beep(freq,duration)


start = input("Would you like to begin Timing? (y/n): ")

def timer():
    
    print("This is the timer")
    if start == "y":
        timeloop=True
    # Variables to keep track and display
    Min = int(input("enter the minutes"))
    Sec=int(input("enter the seconds")) 
        
    # Begin Process
    while timeloop:
        
        print(str(Min) + " Mins " + str(Sec) + " Sec ")
        time.sleep(1)
        if Sec==0:
            if Min==0:
                breaksound()
                
                break
            Min-=1
            Sec=59
        else:
         
            Sec-=1
timer()