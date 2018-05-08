#!/usr/bin/python

from Pi_MCP23S17 import MCP23S17

try:
    mcp1 = MCP23S17(ce=1)
    mcp1.open()

    for x in range(0, 16):
        mcp1.setDirection(x, mcp1.DIR_INPUT)
        mcp1.setPullupMode(x, mcp1.PULLUP_ENABLED)

    old_btn = 1

    print "Starting reading pin A0 (CTRL+C to quit)"
    while (True):
        new_btn = mcp1.digitalRead(0)
        if new_btn != old_btn:
            if new_btn == 0:
                print "Button pressed!"
            else:
                print "Button released!"

        old_btn = new_btn

finally:
    mcp1.close()
