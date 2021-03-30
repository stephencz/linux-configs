import shutil
import psutil

output = ''

disk_usage = str(round(float(shutil.disk_usage('/')[2]) / (1024 * 1024 * 1024), 1)) + 'GB'
used_ram = str(round(float(psutil.virtual_memory()[3]) / (1024 * 1024 * 1024), 1)) + 'GB'
cpu_temp = str(psutil.sensors_temperatures()['coretemp'][0][1]) + '°C'

output += disk_usage + ' ' + used_ram + ' ' + cpu_temp

print(output)
print(output)
