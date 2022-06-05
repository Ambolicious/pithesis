from src.sensors.sensorinterface import SensorInterface
from random import randint


class DummySensor(SensorInterface):

    def get_reading(self) -> float:
        return float(randint(1, 5))