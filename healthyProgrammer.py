from pygame import init, mixer
from datetime import date, datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__  == '__main__':
    init_water = time()
    init_eye = time()
    init_ex = time()
    print("Enter Time Gaps in term of Minutes")
    watersecs = 60*int(input("Enter the time interval of drinking water \n Generally, Drinking Glass Of 200ml at every 28 Minute is Benificial "))
    exsecs = 60*int(input("Enter the time interval of exersice \n Generally, 45 Minute Gap For Physical Activity is Good"))
    eyesecs = 60*int(input("Enter the time interval of eyecare \n Generally, After every 40 Minute you Shoud Give Your Eyes Rest or Relaxation "))


    while True:
        if time() - init_water > watersecs:
            print("water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank water at ")

        if time() - init_eye > eyesecs:
            print("eye care time. Enter 'doneEye' to stop the alarm.")
            musiconloop('eye.wav', 'doneEye')
            init_eye = time()
            log_now("Eyes Relaxed at ")

        if time() - init_ex > exsecs:
            print("Physical activity time. Enter 'donePhy' to stop the alarm.")
            musiconloop('exersice.mp3', 'donePhy')
            init_ex = time()
            log_now("Extersice Done at ")
