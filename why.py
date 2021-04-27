import clr
import os
import time
clr.AddReference(r'OpenHardwareMonitor')
from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True
c.GPUEnabled = True
c.Open()
while True:
    for a in range(0, len(c.Hardware[1].Sensors)):
        if "/nvidiagpu/0/temperature/0" in str(c.Hardware[1].Sensors[a].Identifier):
            temp = c.Hardware[1].Sensors[a].get_Value()
            print('Gpu Temp = '+str(temp))
            if(temp > 80):
                os.system("shutdown /s /t 1")
            time.sleep(2)
            c.Hardware[1].Update()
            