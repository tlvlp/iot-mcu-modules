from machine import Pin


class Relay:

    def __init__(self, pin_num: int, active_at: int, persist_path=None) -> None:
        """
        Relay control for the tlvlp.iot project

        Tested on ESP32 MCUs
        :param pin_num: digital output pin to control the relay
        :param active_at: the relay is either active at a HIGH(1) or LOW(0) Pin state
        :param persist_path: If a path is provided the relay's state will be persisted to and loaded from there.
        """
        self.state_str = "No state set"
        self.active_at = active_at
        self.persist_path = persist_path
        self.pin = Pin(pin_num, Pin.OUT, value=self.get_off_state())
        if persist_path is None:
            self.state_is_persisted = False
            self.relay_off()
        else:
            self.state_is_persisted = True
            self.load_state()

    def get_off_state(self) -> int:
        if self.active_at == 0:
            return 1
        else:
            return 0

    def get_state_str(self) -> str:
        """ Returns a string with the current relay state that is either 'on' or 'off' """
        return self.state_str

    def relay_on(self) -> None:
        """ Switches the relay on """
        if self.active_at == 1:
            self.pin.on()
        else:
            self.pin.off()
        self.state_str = "on"
        if self.state_is_persisted:
            self.persist_state()

    def relay_off(self) -> None:
        """ Switches the relay off """
        if self.active_at == 1:
            self.pin.off()
        else:
            self.pin.on()
        self.state_str = "off"
        if self.state_is_persisted:
            self.persist_state()

    def load_state(self) -> None:
        try:
            with open(self.persist_path) as state:
                loaded_state = state.readline()
            print("Relay - Loading state from path: {}".format(self.persist_path))
            if loaded_state == "on":
                self.relay_on()
            elif loaded_state == "off":
                self.relay_off()
            else:
                print("Error! Invalid state '{}' found on persist path: {}".format(loaded_state, self.persist_path))
                self.relay_off()
        except OSError:
            print("Relay - No persisted state exists yet at path: {}".format(self.persist_path))
            self.relay_off()

    def persist_state(self) -> None:
        with open(self.persist_path, "w+") as state:
            state.write(self.state_str)

