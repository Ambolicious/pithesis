'''
reference code:
https://github.com/adafruit/Adafruit_Python_ADS1x15/blob/master/examples/
'''

from src.sensors.sensorinterface import SensorInterface
import Adafruit_ADS1x15

class ADS1x15(SensorInterface):

    def __init__(self, gain=1, mode=0, lsb=125.0e-6, multiplier=1.0, offset=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._adc = Adafruit_ADS1x15.ADS1115(address=address, busnum=1)
        self._gain = gain
        self._mode = mode
        self._lsb = lsb
        self._multiplier = multiplier
        self._offset = offset


class ADS1115(ADS1x15):

    def __init__(self, address=0x48, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('ADS1115 __init__')
        self._adc = Adafruit_ADS1x15.ADS1115(address=address, busnum=1)


class ADS1015(ADS1x15):

    def __init__(self, address=0x48, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('ADS1115 __init__')
        self._adc = Adafruit_ADS1x15.ADS1015(address=address, busnum=1)


class ADS1115DiffVoltMeter(ADS1115):
    
    def get_reading(self)->float:
        value = self._adc.read_adc_difference(self._mode, self._gain)
        return float(value)*self._lsb*self._multiplier + self._offset


class ADS1115CurrentSensor(ADS1115DiffVoltMeter):

    def __init__(self, sense_resistance=0.05, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__sense_resistance = sense_resistance

    def get_reading(self) -> float:
        return super().get_reading()*self.__sense_resistance


class ADS1115VoltMeter(ADS1115):
    
    def get_reading(self)->float:
        value = self._adc.read_adc(self._mode, self._gain)
        # print("Raw value {}".format(value))
        return float(value)*self._lsb*self._multiplier + self._offset
        

class ADS1015VoltMeter(ADS1015):
    
    def get_reading(self)->float:
        value = self._adc.read_adc(self._mode, self._gain)
        # print("Raw value {}".format(value))
        return float(value)*self._lsb*self._multiplier + self._offset
        