"""
Compare two instances of the same dataclasses, or regular classes in most cases, to identify any differences betwen attributes.

Useful to compare what in an endpint has changes between two calls e.g.

if fresh_endpoint != stored_endpoint:
    find_differences(fresh_endpoint, stored_endpoint)
"""

from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str


def find_differences(obj1, obj2):
    return set([x[0] for x in obj1.__dict__.items() ^ obj2.__dict__.items()])


# All matching
user1 = User("test_first_name", "test_last_name", "test_email")
user2 = User("test_first_name", "test_last_name", "test_email")

print(f"{find_differences(user1, user2)=}")

# 1 difference
user3 = User("test_first_name", "test_last_name_1", "test_email")
user4 = User("test_first_name", "test_last_name", "test_email")

print(f"{find_differences(user3, user4)=}")

# No matching
user5 = User("test_first_name_1", "test_last_name_1", "test_email_1")
user6 = User("test_first_name", "test_last_name", "test_email")

print(f"{find_differences(user5, user6)=}")
