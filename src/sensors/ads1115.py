'''
reference code:
https://github.com/adafruit/Adafruit_Python_ADS1x15/blob/master/examples/
'''

from src.sensors.sensorinterface import SensorInterface
import Adafruit_ADS1x15


class ADS1115(SensorInterface):

    def __init__(self, address=0x48, gain=1, mode=0, lsb=125.0e-6, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('ADS1115 __init__')
        self._adc = Adafruit_ADS1x15.ADS1115(address=address, busnum=1)
        self._gain = gain
        self._mode = mode
        self._lsb = lsb


class ADS1115DiffVoltMeter(ADS1115):
    
    def get_reading(self)->float:
        value = self._adc.read_adc_difference(self._mode, self._gain)
        return float(value)*self._lsb


class ADS1115CurrentSensor(ADS1115DiffVoltMeter):

    def __init__(self, sense_resistance=0.05, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__sense_resistance = sense_resistance

    def get_reading(self) -> float:
        return super().get_reading()*self.__sense_resistance


class ADS1115VoltMeter(ADS1115):
    
    def get_reading(self)->float:
        value = self._adc.read_adc(self._mode, self._gain)
        return float(value)*self._lsb
        