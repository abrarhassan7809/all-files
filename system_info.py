import psutil
import platform

print(f"Computer cpu network name : {platform.node()}")
print(f"Machine type: {platform.machine()}")
print(f"Processor type: {platform.processor()}")
print(f"Platform type: {platform.platform()}")
print(f"Operating system: {platform.system()}")
print(f"Operating system release: {platform.release()}")
print(f"Operating system version: {platform.version()}")

print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
print(f"Current CPU frequency: {psutil.cpu_freq().current}")
print(f"Min CPU frequency: {psutil.cpu_freq().min}")
print(f"Max CPU frequency: {psutil.cpu_freq().max}")
print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}")
#Total RAM
print(f"Total RAM installed: ({round(psutil.virtual_memory().total/1000000000, 2)}) GB or ({round(psutil.virtual_memory().total/1024, 2)}) Mb")
print(f"Available RAM: ({round(psutil.virtual_memory().available/1000000000, 2)}) GB or ({round(psutil.virtual_memory().available/1024, 2)}) Mb")
print(f"Used RAM: ({round(psutil.virtual_memory().used/1000000000, 2)}) GB or ({round(psutil.virtual_memory().used/1024, 2)}) Mb")
print(f"RAM usage: {psutil.virtual_memory().percent}%")

def cpu_cores():
   not_logical_cores = psutil.cpu_count(logical=False)
   logical_cores = psutil.cpu_count(logical=True)
   print(f"non logical cores {not_logical_cores}")
   print("logical cores " + str(logical_cores))

cpu_cores()

