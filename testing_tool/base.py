import serial
import time

BASE = 18.8
t = BASE + 3
FF = 4000

class TestBase:

    def __init__(self):
        pass

    def init(self):
        pass

    def touch(self):
        pass

    def finish(self):
        pass


class TestSerialBase(TestBase):

    def __init__(self, serial):
        super().__init__()
        self.serial = serial

    def send(self, string):
        self.serial.write(bytes(string + "\n", "utf-8"))
        while True:
            response = self.serial.readline().decode().strip()
            if response == 'ok':
                break

    def sends(self, strings):
        for string in strings:
            self.serial.write(bytes(string + "\n", "utf-8"))
            time.sleep(0.3)
            while True:
                response = self.serial.readline().decode().strip()
                if response == 'ok':
                    break
