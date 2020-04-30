import wmi
c=wmi.WMI(namespace='wmi')
method = c.WmiMonitorBrightnessMethods()[0]
method.WmiSetBrightness(100,0) # change first part of value as you want