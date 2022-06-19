from src.sensors.sensorinterface import SensorInterface
from time import sleep
from src.loggers.phonebroadcast import PhoneBroadcast
from src.loggers.csvlogger import CSVLogger

class Controller:

    def __init__(self):
        self.__broadcaster = None
        self.__logger = CSVLogger()
        self.__sensors = []
        self.__broadcast_freq = 10
        self.__log_count = 0
        
    def run(self):
        while True:
            self.__log_count += 1
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
            self.__log_reading(data_list)
            self.__broadcast_result(data_list)
            sleep(1)
            print()
        
    def add_sensor(self, sensor:SensorInterface):
        self.__sensors.append(sensor)
    
    def __log_reading(self, data_list:list):
        self.__logger.write_to_csv(data_list)
    
    def __broadcast_result(self, data_list:list):
        if self.__log_count > self.__broadcast_freq:
            return
        self.__log_count = 0
        if self.__broadcaster is not None:
            self.__broadcaster.broadcast(data_list)
    
    def enable_phone_broadcast(self):
        if self.__broadcaster is None:
            self.__broadcaster = PhoneBroadcast()
