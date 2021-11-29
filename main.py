# Add your Python code here. E.g.
from microbit import *
import utime

dict = {}
timp = 1
isArmed = False

    
def addUser(user, parola):
    if len(dict) < 4:
        if len(parola) < 4:
            print( "Could not save profile. Invalid pin.")
        else:
            if user in dict:
                up_dict = {user : parola}
                dict.update(up_dict)
            else:
                dict[user] = parola
                print("Profile added.")
    else:
        print("Could not save profile. Limit exceeded.")
    
def deleteUser(user):
    if user in dict:
        del dict[user]
        print("Profile deleted.")
    else:
        print("Could not delete profile. Profile {} does not exist.".format(user))
        
def armed(timp):
    global isArmed
    image = Image("99999:""99999:""99999:""99999:""99999")
    slp = timp * 60000
    currentTime = utime.ticks_ms()
    stop = utime.ticks_ms() + slp
    while currentTime < stop:
        display.show(image)
        if button_a.is_pressed() and button_b.is_pressed():
            isArmed = False
            pinCode()
        if currentTime > stop:
            display.show(Image.HAPPY)
        if isArmed == True:
            if accelerometer.was_gesture("shake"):
                while isArmed == True:
                    display.show(image)
                    display.show(Image())
                    speaker.on()
                    audio.play(Sound.YAWN)
                    if button_a.is_pressed() and button_b.is_pressed():
                        isArmed = False
                        pinCode()                       
        
def pinCode():
    val = -1
    res = ''
    global isArmed
    while True:
        if button_a.is_pressed():
            val += 1
            sleep(500)
            if val > 9:
                val = 0
        elif button_b.is_pressed():
            val -= 1
            sleep(500)
            if val < 0:
                val = 9
        display.show(val)
        if pin_logo.is_touched():
            res += str(val)
            sleep(500)
            if len(res) == 4:
                display.clear()
                res = int(res)
                for value in dict.values():
                    if int(value) == res:
                        isArmed = True
                        display.show(Image.HAPPY)
                        utime.sleep(3)
                        armed(timp)
                    else:
                        display.show(Image.SAD)
                        utime.sleep(3)
                        res = ''                        

uart.init(115200)
conn = False

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        if conn == False:
            pinCode()                
            
    if uart.any() == True:
        conn = True
    else:
        conn = False
    if conn == True:
        line = input("alarm cmd> ")
        parsed = line.split()
        if(parsed[0] == "exit"):
            conn = False
        elif(parsed[0] == "profile"):
            if(parsed[1] == "add"):
                addUser(parsed[2], parsed[3])
            elif(parsed[1] == "delete"):
                deleteUser(parsed[2])
            elif(parsed[1] == "print"):
                print(dict)
        elif(parsed[0] == "arm" and parsed[1] == "time"):
            timp = int(parsed[2])