import time
from .base import TestSerialBase

BASE = 18.8
t = BASE + 3
FF = 4000

class TouchTestTool(TestSerialBase):

    def init(self):
        self.sends(self.reset())

    def touch(point):
        self.sends(xh(point))

    def finish():
        self.send("M84 X Y")

    def reset():
        r = ["G28 X Y Z", "G0 X0 Y0 Z%d" %(t, )]
        return r

    def xh(point):
        result = []
        s = "G0 F%d X%.3f Y%.3f Z%.3f" % (FF, point[0], point[1], t)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%.3f" % (FF, point[0], point[1], BASE)
        result.append(s)
        '''
        s = "G4 P0"
        result.append(s)
        '''
        s = "G0 F%d X%.3f Y%.3f Z%.3f" % (FF, point[0], point[1], t)
        result.append(s)
        s = "G4 P100"
        result.append(s)
        return result
