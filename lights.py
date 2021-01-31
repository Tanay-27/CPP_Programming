import RPi.GPIO as GPIO
import time
# Pin Setup:
gpiolst = [27,29,31,33]
for pin in gpiolst:
    GPIO.setup(pin,GPIO.OUT)

def get_command():
    URL = "http://103.87.173.236:44572/Api/Getlight"
    PARAMS = {'aps':'Pl123456'} 
    r = requests.get(url = URL,params = PARAMS) 
    return r.text

def time_1min():
    stringlist = get_command()
    lst = stringlist.split(',')
    print(lst)

def setlights(lst):
    for i in range(4):
        if lst[i]==1:
            GPIO.output(gpiolst[i],GPIO.HIGH)
        elif lst[i]==0:
            GPIO.output(gpiolst[i],GPIO.LOW)
        time.sleep(60)
