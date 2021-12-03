# November 2021 - v0.1
# Python code to connect to get the input from RPI GPIO pins working with
# the MCP3008 analog to digital converter
# @author Team 2

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration (no spi enabling needed)
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, miso=MISO, mosi=MOSI)

# Hardware SPI configuration
# SPI_PORT = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print("Reading mcp3008 values, press Ctrl-C to quit")
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)

# Main loop
while True:
    values = [0]*8
    for i in range(8):
        values = mcp.read_adc(1)
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
        time.sleep(1)