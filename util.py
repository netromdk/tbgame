# -*- Coding: utf-8 -*-
from constants import CONSOLE

def getInt(msg, default = None, signed = True, zeroable = False, allowed = None,
           disallowed = None, min = None, max = None):
    if default != None:
        msg += " [" + str(default) + "]"    
    while True:
        print(msg, end=" ")
        data = input(CONSOLE)
        try:
            res = int(data)
            if signed and res < 0: res *= -1
            if not zeroable and res == 0: continue
            if allowed != None and not res in allowed: continue
            if disallowed != None and res in disallowed: continue
            if min and res < min: continue
            if max and res > max: continue
            return res
        except:
            if default != None and data == "":
                return default
