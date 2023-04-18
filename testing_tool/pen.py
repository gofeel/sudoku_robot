import time
from .base import TestSerialBase

BASE = 5
t = BASE + 5
FF = 2000

class PenTestTool(TestSerialBase):

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
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0], point[1], t)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0]-5, point[1]-5, t)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0]-5, point[1]-5, BASE)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0]+5, point[1]+5, BASE)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0]-5, point[1]+5, t)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0]-5, point[1]+5, BASE)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0]+5, point[1]-5, BASE)
        result.append(s)
        s = "G0 F%d X%.3f Y%.3f Z%d" % (FF, point[0], point[1], t)
        result.append(s)
        return result
