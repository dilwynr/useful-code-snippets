"""
Generate a random strings with variable lengths.

Do not sure if you require true randomness for cryptographic or secure use
"""

import random
import string

def random_printable(length=10):
    return "".join(random.choice(string.printable) for _ in range(length))


print(f"{random_printable()=}")

def random_number(length=10):
    return "".join(random.choice(string.digits) for _ in range(length))

print(f"{random_number()=}")


def random_ascii(length=10):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

print(f"{random_ascii()=}")