from ctypes import addressof
from types import MemberDescriptorType
from src.controller import Controller
from src.sensors.ads1115 import ADS1115DiffVoltMeter
from src.sensors.ads1115 import ADS1115CurrentSensor
from src.sensors.acs758ip import ACS758IP
from src.sensors.ky003 import KY003
from src.sensors.lm35temp import LM35Temp_ADS1015
from src.sensors.lm35temp import LM35Temp_ADS1115

from src.sensors.ads1115 import ADS1115VoltMeter

from src.sensors.ads1115 import ADS1015VoltMeter


# Battery Current: ACS758, A2, 0x48
# Line Current: ACS758, A3, 0x48


# Speed: gpio 4
# LM35: A0,0x49
# Battery Voltage: A0-A1, 0x48

# 0x48 -> 16bit
# 0x49 -> 12bit (ads1015)


#  mode values for differential
#  - 0 = Channel 0 minus channel 1
#  - 1 = Channel 0 minus channel 3
#  - 2 = Channel 1 minus channel 3
#  - 3 = Channel 2 minus channel 3

#  mode values for single ended
#  - 0 = Channel 0
#  - 1 = Channel 1
#  - 2 = Channel 2
#  - 3 = Channel 3



def main():

    c = Controller()
    c.add_sensor(ADS1115DiffVoltMeter(sensor_name='Battery Voltage (A0-A1, 0x48)', address=0x48, mode=0, multiplier=15.28))
    c.add_sensor(LM35Temp_ADS1015(sensor_name='LM35 Temp (A0 0x49)', address=0x49, mode=0, lsb=2.0e-3))
    c.add_sensor(KY003(sensor_name='KY003 Rev per sec'))
    c.add_sensor(ACS758IP(sensor_name='Battery Current (A2 0x48)', address=0x48, mode=2, current_offset=-3.5))
    c.add_sensor(ACS758IP(sensor_name='Line Current (A3, 0x48)', address=0x48, mode=3, current_offset=-3.5))
    c.run()

if __name__=='__main__':
    main()

