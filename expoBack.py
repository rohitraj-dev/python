import time

wait_time = 1
max_retires = 5
attempts = 0

while attempts < max_retires:
    print("attempt", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2