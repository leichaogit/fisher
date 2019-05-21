import random
from collections import deque

a = [random.randint(1, 40) for i in range(20)]


def Last_number(ls):
    """
    实现搜索过程的代码和搜索结果的代码解耦
    :param ls:
    :return:
    """
    for i in range(len(ls)):
        yield ls[i]


for i in Last_number(a):
    print(i, end='、')
print()
for i in Last_number(a):
    print(i, end='、')
print()

# 使用双端队列来保存最后maxlen=N的元素
b = deque(maxlen=5)
for i in range(len(a)):
    b.append(a[i])
print(b)
