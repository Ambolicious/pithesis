from src.sensors.sensorinterface import SensorInterface
from src.loggers.phonebroadcast import PhoneBroadcast
from time import sleep

class Controller:

    def __init__(self):

        # self.__broadcaster = PhoneBroadcast()
        self.__logger = None
        self.__sensors = []
        
    def run(self):
        while True:
            data_list = []
            for sensor in self.__sensors:
                reading = None
                try:
                    reading = sensor.get_reading()
                    sensor.print_log_format(reading)
                except Exception as e:
                    reading = sensor.get_error_log(e)
                    print(reading)
                data_list.append(reading)
            # self.__log_reading(data_list)
            # self.__broadcast_result(data_list)
            sleep(1)
            print()
        
    
    def add_sensor(self, sensor:SensorInterface):
        self.__sensors.append(sensor)
    
    def __log_reading(self, data_list:list):
        print('todo: __log_reading')
    
    def __broadcast_result(self, data_list:list):
        __data_list = ','.join([str(x) for x in data_list])
        self.__broadcaster.broadcast(__data_list+'\n')