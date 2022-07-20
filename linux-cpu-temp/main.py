def get_cpu_temp():
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp) / 1000 

ctemp = get_cpu_temp()
print(ctemp)
