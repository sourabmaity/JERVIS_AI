import psutil
b = psutil.sensors_battery()
print(b.percent) # battery parsentage
print(b.power_plugged) # charging or not using cable