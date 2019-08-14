from machine import Pin
from machine import ADC
import uasyncio as asyncio


class SoilMoistureSensor:

    def __init__(self, name: str, read_pin_num: int, power_pin_num=None) -> None:
        """
        Analog capacitive soil moisture sensor for the tlvlp.iot project

        Tested on ESP32 MCUs
        :param read_pin_num: Analog input pin number for reading measurements
        :param power_pin_num: Optional digital output pin number for controlling power to the sensor.
        """
        self.reference = "somo|" + name
        self.power_control = False
        if power_pin_num is not None:
            self.power_control = True
            self.power = Pin(power_pin_num, Pin.OUT, value=0)
        self.sensor = ADC(Pin(read_pin_num, Pin.IN, Pin.PULL_DOWN))
        self.sensor.atten(ADC.ATTN_11DB)
        self.sensor.width(ADC.WIDTH_10BIT)

    async def read_percent(self, delay_ms=300) -> tuple:
        """
        :param delay_ms: a set delay before the reading is done
        :return: the percentage of the read value, using integer rounding
        """
        if self.power_control:
            self.power.on()
        await asyncio.sleep_ms(delay_ms)
        analog_read = self.sensor.read()
        if self.power_control:
            self.power.off()
        return self.reference, self.convert_to_percent(analog_read)

    def convert_to_percent(self, reading) -> int:
        return int((1023 - reading) / 10.23)

