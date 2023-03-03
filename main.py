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


class SinlgeEndedExp(ADS1015VoltMeter):

    def get_reading(self)->float:
        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Or pick a different gain to change the range of voltages that are read:
        #  - 2/3 = +/-6.144V
        #  -   1 = +/-4.096V
        #  -   2 = +/-2.048V
        #  -   4 = +/-1.024V
        #  -   8 = +/-0.512V
        #  -  16 = +/-0.256V
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

        #gain = 2/3
        # value = self._adc.read_adc_difference(self._mode, gain)
        # print('gain:{gain}, {value}')

        gain = 2/3
        value = self._adc.read_adc_difference(self._mode, gain)
        print('gain:{gain}, {value}')

        # gain = 1
        # value = self._adc.read_adc_difference(self._mode, gain)
        # print('gain:{gain}, {value}')

        # gain = 2
        # value = self._adc.read_adc_difference(self._mode, gain)
        # print('gain:{gain}, {value}')

        # gain = 4
        # value = self._adc.read_adc_difference(self._mode, gain)
        # print('gain:{gain}, {value}')

        # gain = 8
        # value = self._adc.read_adc_difference(self._mode, gain)
        # print('gain:{gain}, {value}')

        # gain = 16
        # value = self._adc.read_adc_difference(self._mode, gain)
        # print('gain:{gain}, {value}')


        #value = self._adc.read_adc_difference(self._mode, self._gain)
        #return float(value)*self._lsb*self._multiplier + self._offset



def main():

    c = Controller()
    
    c.set_log_delay(0.3) # in sec
    #c.set_log_delay(0.5) # in sec
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

    c.add_sensor(LM35Temp_ADS1015(sensor_name='LM35 Temp (A0 0x49)', address=0x49, mode=0, lsb=2.0e-3, gain= (1.0)))
    
    # # c.add_sensor(LM35Temp_ADS1115(sensor_name='LM35 Temp (A0 0x48)', address=0x48, mode=0, lsb=2.0e-3))
    # # c.add_sensor(ADS1115VoltMeter(sensor_name='Raw (A0, 0x48)', address=0x48, mode=0, lsb=1.0))
    # # c.add_sensor(ADS1115VoltMeter(sensor_name='Raw (A1, 0x48)', address=0x48, mode=1, lsb=1.0))
    
    
    c.add_sensor(ADS1015DiffVoltMeter(sensor_name='Battery Voltage (A0-A1, 0x48)', address=0x4A, mode=0, multiplier=((15.355)*(10730.0/977.0)), offset=(32.54135225), gain=1.0))
    
    
    c.add_sensor(ADS1015VoltMeter(sensor_name='Battery Current (A2, 0x49)', address=0x49, mode=2, multiplier=((15.355)*(4000.0/79.0)), offset= ((-117.56674050632913)*(1.0)), gain=(1.0)))

    c.add_sensor(ADS1015VoltMeter(sensor_name='Line Current (A3, 0x49)', address=0x49, mode=3,multiplier=((15.355)*(4000.0/79.0)), offset= ((-115.43433544303798)*(1.0)), gain=(1.0)))
    
    #c.add_sensor(ACS758IP(sensor_name='Battery Current (A2 0x49)', address=0x49, mode=2, current_offset=0.0))
    #c.add_sensor(ACS758IP(sensor_name='Line Current (A3, 0x49)', address=0x49, mode=3, current_offset=0.0))
    c.add_sensor(KY003(sensor_name='KY003 Rev per sec'))

 
    c.run()

if __name__=='__main__':
    main()

