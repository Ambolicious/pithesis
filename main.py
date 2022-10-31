from src.controller import Controller
from src.sensors.ads1115 import ADS1115DiffVoltMeter
from src.sensors.ads1115 import ADS1115CurrentSensor
from src.sensors.acs758ip import ACS758IP
from src.sensors.ky003 import KY003
from src.sensors.lm35temp import LM35Temp_ADS1015
from src.sensors.lm35temp import LM35Temp_ADS1115
from src.sensors.ads1115 import ADS1115VoltMeter
from src.sensors.ads1115 import ADS1015VoltMeter

from src.sensors.ads1115 import ADS1015DiffVoltMeter

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
    
    c.set_log_delay(0.3) # in sec
    #c.set_log_delay(1) # in sec
    #c.enable_debug()
    c.enable_phone_broadcast(broadcast_frequency=10)

    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A0, 0x48)', address=0x48, mode=0, lsb=1.0))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A1, 0x48)', address=0x48, mode=1, lsb=1.0))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A2, 0x48)', address=0x48, mode=2, lsb=1.0))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A3, 0x48)', address=0x48, mode=3, lsb=1.0))

    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A0, 0x49)', address=0x49, mode=0, lsb=1.0))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A1, 0x49)', address=0x49, mode=1, lsb=1.0))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A2, 0x49)', address=0x49, mode=2, lsb=1.0))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='ADS1015VoltMeter (A3, 0x49)', address=0x49, mode=3, lsb=1.0))

    c.add_sensor(LM35Temp_ADS1015(sensor_name='LM35 Temp (A0 0x49)', address=0x49, mode=0, lsb=2.0e-3))
    
    # # c.add_sensor(LM35Temp_ADS1115(sensor_name='LM35 Temp (A0 0x48)', address=0x48, mode=0, lsb=2.0e-3))
    # # c.add_sensor(ADS1115VoltMeter(sensor_name='Raw (A0, 0x48)', address=0x48, mode=0, lsb=1.0))
    # # c.add_sensor(ADS1115VoltMeter(sensor_name='Raw (A1, 0x48)', address=0x48, mode=1, lsb=1.0))
    
    
    c.add_sensor(ADS1015DiffVoltMeter(sensor_name='Battery Voltage (A0-A1, 0x48)', address=0x48, mode=0, multiplier=289.503009))
    
    #c.add_sensor(ADS1015VoltMeter(sensor_name='Battery Voltage (A0, 0x48)', address=0x48, mode=0, multiplier=14.15625927))
    #c.add_sensor(ADS1015VoltMeter(sensor_name='Battery Voltage (A1, 0x48)', address=0x48, mode=1, multiplier=14.15625927))
    
    c.add_sensor(ACS758IP(sensor_name='Battery Current (A2 0x49)', address=0x49, mode=2, current_offset=-72.5934))
    c.add_sensor(ACS758IP(sensor_name='Line Current (A3, 0x49)', address=0x49, mode=3, current_offset=-72.3164))
    c.add_sensor(KY003(sensor_name='KY003 Rev per sec'))

 
    c.run()

if __name__=='__main__':
    main()

