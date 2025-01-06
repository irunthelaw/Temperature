# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio
from analogio import AnalogIn

temp = AnalogIn(board.A0)

while True:
    maxxed = 65535
    vlt = temp.value / maxxed * 3.3
    temp_C = (vlt - .5) *100
    temp_F = (9/5) * temp_C +32
    
    print(temp_F)
    time.sleep(0.5)
