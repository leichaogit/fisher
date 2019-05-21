# a = ["well", "unlike", "banana", 'cat']
# a.sort(key=lambda o: len(o))
# print(a)
# print("-" * 40)
# a.sort(key=lambda o: len(o), reverse=True)
# print(a)
# print("-" * 40)
# a.sort(key=lambda o: o.lower())
# print(a)
from collections import defaultdict


def log_missing():
    print("Key added")
    return 0


current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9)
]
result = defaultdict(log_missing, current)
print(result)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))

