# zeeshanjutt7055@gmail.com

import psutil

# Function to get threshold values from user
def system_health_check():
    cpu_threshold = int(input("Enter CPU threshold (%): "))
    memory_threshold = int(input("Enter Memory threshold (%): "))
    disk_threshold = int(input("Enter Disk threshold (%): "))

# Function to fetch system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    print("--- System Health Status ---")

# Function to compare metrics with thresholds
    if cpu_usage > cpu_threshold:
        print(f"CPU HIGH: {cpu_usage}%")
    else:
        print(f"CPU OK: {cpu_usage}%")

    if memory_usage > memory_threshold:
        print(f"Memory HIGH: {memory_usage}%")
    else:
        print(f"Memory OK: {memory_usage}%")

    if disk_usage > disk_threshold:
        print(f"Disk HIGH: {disk_usage}%")
    else:
        print(f"Disk OK: {disk_usage}%")

# call funtion
system_health_check()








