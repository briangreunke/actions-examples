import random

with open("random-number", "w") as f:
    random_number = str(random.randint(0, 1000000))
    f.write(random_number)
