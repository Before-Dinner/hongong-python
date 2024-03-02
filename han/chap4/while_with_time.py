import time

time_set = time.time() + 5
value = 1
while time.time() < time_set:
    value += 1
    
print(value)