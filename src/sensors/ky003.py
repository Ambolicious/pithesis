from src.sensors.sensorinterface import SensorInterface
import RPi.GPIO as GPIO
from time import time


class KY003(SensorInterface):

    def __init__(self, gpio_pin=4, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_time_stamp = self.__get_time()
        self.__rev_per_sec = 0.0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.add_event_detect(4, GPIO.FALLING, callback=self.__on_event)

    def get_reading(self) -> float:
        return self.__rev_per_sec
    
    def __on_event(self, _):
        new_time_stamp = self.__get_time()
        delta = new_time_stamp - self.__old_time_stamp
        self.__rev_per_sec = 1.0 / delta
        self.__old_time_stamp = new_time_stamp
    
    def __get_time(self)->float:
        return time()

