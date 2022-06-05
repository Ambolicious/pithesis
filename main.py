from src.controller import Controller
from src.sensors.ads1115 import ADS1115DiffVoltMeter
from src.sensors.ads1115 import ADS1115CurrentSensor
from src.sensors.acs758ip import ACS758IP
from src.sensors.ky003 import KY003
from src.sensors.lm35temp import LM35Temp

from src.sensors.ads1115 import ADS1115VoltMeter


def main():

    c = Controller()

    #  mode values for differential
    #  - 0 = Channel 0 minus channel 1
    #  - 1 = Channel 0 minus channel 3
    #  - 2 = Channel 1 minus channel 3
    #  - 3 = Channel 2 minus channel 3

    c.add_sensor(ADS1115VoltMeter(sensor_name='A0 0x49', address=0x49, mode=0))
    c.add_sensor(ADS1115VoltMeter(sensor_name='A1 0x49', address=0x49, mode=1))
    c.add_sensor(ADS1115VoltMeter(sensor_name='A2 0x49', address=0x49, mode=2))
    c.add_sensor(ADS1115VoltMeter(sensor_name='A3 0x49', address=0x49, mode=3))

    c.add_sensor(ADS1115VoltMeter(sensor_name='A0 0x48', address=0x48, mode=0))
    c.add_sensor(ADS1115VoltMeter(sensor_name='A1 0x48', address=0x48, mode=1))
    c.add_sensor(ADS1115VoltMeter(sensor_name='A2 0x48', address=0x48, mode=2))
    c.add_sensor(ADS1115VoltMeter(sensor_name='A3 0x48', address=0x48, mode=3))

    # c.add_sensor(LM35Temp(sensor_name='motor_temperature', address=0x48, mode=2))
    # c.add_sensor(ADS1115DiffVoltMeter(sensor_name='supply_voltage', address=0x49, mode=0))
    # c.add_sensor(ACS758IP(sensor_name='motor_line_current', address=0x48))
    # c.add_sensor(ADS1115CurrentSensor(sensor_name='supply_current', sense_resistance=0.05, address=0x49))
    # c.add_sensor(KY003(sensor_name='motor_speed', gpio_pin=4))

    c.run()

if __name__=='__main__':
    main()
