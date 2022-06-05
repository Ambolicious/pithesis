from abc import ABC, abstractmethod


class SensorInterface(ABC):

    def __init__(self, sensor_name='NO NAME'):
        self.__sensor_name = sensor_name

    @abstractmethod
    def get_reading(self)->float:
        pass

    def get_error_log(self, error:str):
        return 'ERROR in ' + self.__sensor_name + ' ' + str(error)

    def print_log_format(self, result):
        print(self.__sensor_name + ': ' + str(result))