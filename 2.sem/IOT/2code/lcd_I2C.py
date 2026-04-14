import machine
import utime

DEFAULT_I2C_ADDR = 0x27

class I2CLcd:
    """Class to control LCD 16x2 via I2C."""

    def __init__(self, i2c, address=DEFAULT_I2C_ADDR):
        """Initialize LCD over I2C."""
        self.i2c = i2c
        self.address = address
        self.init_lcd()

    def send(self, data, mode=0):
        """Send data to the LCD (mode: 0 = command, 1 = character)."""
        high = (data & 0xF0) | mode | 0x08
        low = ((data << 4) & 0xF0) | mode | 0x08

        self.i2c.writeto(self.address,
                         bytes([high, high | 0x04, high,
                                low, low | 0x04, low]))
        utime.sleep_ms(1)

    def init_lcd(self):
        """Initialize LCD for 4-bit operation."""
        utime.sleep_ms(20)
        for cmd in [0x33, 0x32, 0x28, 0x0C, 0x06, 0x01]:
            self.send(cmd)

    def move_to(self, col, row):
        """Move cursor to a specific LCD position."""
        self.send(0x80 + (row * 0x40) + col)

    def putstr(self, text):
        """Write text to LCD."""
        for char in text:
            self.send(ord(char), 1)

    def clear(self):
        """Clear LCD screen."""
        self.send(0x01)
        utime.sleep_ms(2)

