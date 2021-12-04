"""
Used on the raspberry pi to control the adafruit MCP 3008.
Then sends the data to the server via the socket.
"""
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import client

CHANMAXV = 65472
CONSTMAXV = 3.2968276493476765

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

while True:
    hydration = (1-chan.value/CHANMAXV)*100
    print(hydration)
    client.main(hydration)
    time.sleep(1)
