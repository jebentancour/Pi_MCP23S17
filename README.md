# Pi_MCP23S17

This library is based on [RPi-MCP23S17](https://github.com/petrockblog/RPi-MCP23S17/blob/master/RPiMCP23S17/MCP23S17.py).

This library did not work for me, so I made some changes and created my own version.

Requirements:
```
sudo apt-get install python-dev python-pip
sudo pip install RPi.GPIO
sudo pip install spidev
```

To use it (it must be in the same directory):
```Python
from Pi_MCP23S17 import MCP23S17
```
