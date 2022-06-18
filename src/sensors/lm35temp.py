from src.sensors.ads1115 import ADS1115VoltMeter
from src.sensors.ads1115 import ADS1015VoltMeter


class LM35Temp_ADS1015(ADS1015VoltMeter):

    def get_reading(self) -> float:
        voltage_reading = super().get_reading()
        return voltage_reading/.010

class LM35Temp_ADS1115(ADS1115VoltMeter):

    def get_reading(self) -> float:
        voltage_reading = super().get_reading()
        return voltage_reading/.010