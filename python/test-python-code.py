import time

# Prints numbers without forcing flush, output may be delayed
for i in range(5):
    print(i, end=' ', flush=False)
    time.sleep(1)


