import psutil
partitions = psutil.disk_partitions()

for p in partitions:
    print(p.mountpoint, psutil.disk_usage(p.mountpoint).percent)
