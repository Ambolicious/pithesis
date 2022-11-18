#from src.sensors.ads1115 import ADS1115VoltMeter
from src.sensors.ads1115 import ADS1015VoltMeter


class ACS758IP(ADS1015VoltMeter):

    def __init__(self, current_offset=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__current_offset = current_offset

    def get_reading(self) -> float:
        return (((super().get_reading()*3.0) - (5.0/1.5)) / 0.04) - (self.__current_offset)
        #return (super().get_reading())
        

# for experiment
        #def get_reading(self)->float:
            #gain = 2.0/3.0
            #value = self._adc.read_adc_difference(self._mode, gain)
            #return value
            #return float(value)*self._lsb*self._multiplier + self._offset
