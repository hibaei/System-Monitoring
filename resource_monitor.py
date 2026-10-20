import psutil
import time
def get_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return {
            'CPU Usage (%)': cpu_usage,
            ' memory Usage (%)': memory_usage,
            'Disk Usage (%)': disk_usage
            }
if __name__ == "__main__":
        while True:
            resources = get_system_resources()
            print("\nResource Dashbord")
            print("-----------------")
            for key, value in resources.items():
                print(f"{key}: {value}")
                time.sleep(5)
