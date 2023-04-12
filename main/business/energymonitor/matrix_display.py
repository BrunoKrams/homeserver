from luma.core.legacy import text
from luma.core.legacy.font import CP437_FONT
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219

from main.business.energymonitor.logic import Display


class MatrixDisplay(Display):
    FONT = CP437_FONT
    MATRIX_SIDE_LENGTH = 8
    SCROLL_DELAY = 0.03
    Y_OFFSET = 1

    def __init__(self, device:max7219):
        self.device = device

    def update(self, energy_in_mw: int):
        energy_in_w  = energy_in_mw // 1000
        self.__show_message(str(energy_in_w))

    def clear(self):
        self.device.clear()

    def __textsize(self, txt):
        src = [c for ascii_code in txt for c in self.FONT[ord(ascii_code)]]
        return len(src)

    def __show_message(self, msg):
        fps = 1.0 / self.SCROLL_DELAY
        regulator = framerate_regulator(fps)
        w = self.__textsize(msg)

        x = self.device.width
        virtual = viewport(self.device, width=w + x + 8, height=self.device.height)

        with canvas(virtual) as draw:
            text(draw, (x, self.Y_OFFSET), msg, font=self.FONT, fill="white")

        i = 0
        while i <= w + self.MATRIX_SIDE_LENGTH - 1:
            with regulator:
                virtual.set_position((i, 0))
                i += 1
