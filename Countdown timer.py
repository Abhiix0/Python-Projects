import time
# Countdown timer
my_time = int(input("Enter the time in seconds for countdown: "))

for i in range(my_time, 0, -1):
    sec = i % 60
    min = (i // 60) % 60   
    hour = i // 3600
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("Time's up!")