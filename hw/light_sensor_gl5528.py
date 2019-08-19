from machine import Pin
from machine import ADC
import uasyncio as asyncio


class LightSensorGl5528:

    def __init__(self, name: str, pin_num: int) -> None:
        """
        Analog light sensor GL5528 for the tlvlp.iot project

        Tested on ESP32 MCUs
        :param pin_num: Analog input pin number for reading measurements
        """
        self.reference = "gl5528|" + name
        self.sensor = ADC(Pin(pin_num, Pin.IN, Pin.PULL_DOWN))
        self.sensor.atten(ADC.ATTN_11DB)
        self.sensor.width(ADC.WIDTH_10BIT)

    async def read_percent(self, delay_ms=300) -> tuple:
        """
        :param delay_ms: a set delay before the reading is done
        :return: the percentage of the read value, using integer rounding
        """
        await asyncio.sleep_ms(delay_ms)
        analog_read = self.sensor.read()
        return self.reference, str(self.convert_to_percent(analog_read))

    def convert_to_percent(self, reading) -> int:
        return int((1023 - reading) / 10.23)

