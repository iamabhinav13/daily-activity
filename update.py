import datetime
import random
import time

for _ in range(random.randint(10, 20)):
    with open("activity.log", "a") as f:
        f.write(str(datetime.datetime.now()) + "\n")
    time.sleep(random.randint(1, 120))