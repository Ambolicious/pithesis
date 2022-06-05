from src.sensors.ads1115 import ADS1115VoltMeter


class ACS758IP(ADS1115VoltMeter):

    def get_reading(self) -> float:
        voltage_reading = super().get_reading()
        return voltage_reading