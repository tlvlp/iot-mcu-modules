import uasyncio as asyncio
from machine import Pin
import onewire
import ds18x20


class TempSensorDS18B20:

    def __init__(self, pin_num: int) -> None:
        """
        Digital temp sensor DS18B20 for the tlvlp.iot project

        Tested on ESP32 MCUs
        :param pin_num: Digital input pin number for reading measurements
        """
        one_wire = onewire.OneWire(Pin(pin_num))
        self.channel = ds18x20.DS18X20(one_wire)

    async def read_first_celsius(self, delay_ms=750) -> float:
        """
        :param delay_ms: a set delay before the reading is done
        :return: readings from the first sensor on the pin
        The order is not guaranteed so works best with only one sensor
        """
        readings = await self.read_all_celsius(delay_ms)
        return readings[0]

    async def read_all_celsius(self, delay_ms=750) -> list:
        """
        :param delay_ms: a set delay before the reading is done
        :return: readings for all the sensors on the same channel/pin
        """
        sensors = self.channel.scan()
        print("IS SENSORS EMPTY?", sensors)
        self.channel.convert_temp()
        await asyncio.sleep_ms(delay_ms)
        readings = []
        for sensor in sensors:
            readings.append(self.channel.read_temp(sensor))
        return readings

