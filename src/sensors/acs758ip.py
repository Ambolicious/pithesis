from src.sensors.ads1115 import ADS1115VoltMeter


class ACS758IP(ADS1115VoltMeter):

    def __init__(self, current_offset=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__current_offset = current_offset

    def get_reading(self) -> float:
        return ((super().get_reading() - (5.0/2.0)) / 0.04) - (self.__current_offset)
