import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import threading
import socket
from socket import SHUT_RDWR

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def sendData(data,conn,s):
    try:
        conn.send(data.encode())
    except Exception as e:
        print(str(e))
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.shutdown(SHUT_RDWR)
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            print(str(addr))
        except Exception as ee:
            pass
        
def get_scale(values,val):
    scale = (float(values[val])/32767)
    return scale

def saveLineToFile(newLine):
    file = open("/home/pi/data.txt","a")
    file.write(newLine)
    file.close

class UpdateTask(threading.Thread):
    def __init__(self,):
        threading.Thread.__init__(self)

    def run(self):
        global temperature
        global voltage
        global batteryCurrent
        global motorVoltage
        global speed
        global adc
        global conn
        global s
        while True:
            values = [0]*4
            for i in range(4):
                values[i] = adc.read_adc(i, gain=2/3)
            voltage = (get_scale(values,0) * 6.144)
            temperature = ((get_scale(values,2) * 6144))/10
            batVs = float(((get_scale(values,1)*6.144))-float(0.500*5.000)+0.007)
            batteryCurrent = float(batVs / float(40.00 / 1000.00)) + 15.22
            motorVoltage = (get_scale(values,3) * 6.144)
            #print("Batt: "+str(voltage)+'\n')
            #print("analog: "+str(values[3])+'\n')
            #print("Temp: "+str(temperature))
            data = str( "{:.2f}".format(temperature)) + ","\
                   + str( "{:.2f}".format(voltage))+ "," \
                   + str( "{:.2f}".format(batteryCurrent))+ ","\
                   + str( "{:.2f}".format(motorVoltage))+ "," + str( "{:.2f}".format(speed)) +"\n"
            print(data)
            sendData(data,conn,s)
            #saveLineToFile(data)
            time.sleep(0.005)

class SpeedTask(threading.Thread):
    def __init__(self,):
        threading.Thread.__init__(self)

    def run(self):
        global revs
        global speed
        currentMillis = int(time.time() * 1000)
        previousMillis = currentMillis
        while True:
            currentMillis = int(time.time() * 1000)
            if (currentMillis-previousMillis) > 1000:
                speed= float(revs/1.0000)
                revs=0
                previousMillis=currentMillis
                #print(speed)
            
def active(null):
    global revs
    revs = revs + 1


def test():
    conn=None
    addr=None
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print(str(addr))
    except Exception as e:
        print('Error in Socket')

    while True:
        data = ','.join(['xxx' for _ in range(5)]) + '\n'
        print(data)
        sendData(data,conn,s)
    
def main():
    temperature=0
    voltage=0
    batteryCurrent=0
    motorVoltage=0
    speed=0
    revs = 0
    speed=0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(4, GPIO.FALLING, callback=active) 
    adc = Adafruit_ADS1x15.ADS1115()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print(str(addr))
    except Exception as e:
        pass
    #while True:
    #    a="hello"
     #   conn.send(a.encode() + b'\n')
     #   time.sleep(1)
    speedtask = SpeedTask()
    speedtask.start()
    updatetask = UpdateTask()
    updatetask.start()

if __name__ == '__main__':
    test()