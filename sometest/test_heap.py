# 第N小/大的元素，最小/大的N个元素，分析使用heap
# 大顶堆，小顶堆
import heapq

num = [-1, -34, 56, -9, -34, 67]
max_n = heapq.nlargest(4, num)
min_n = heapq.nsmallest(4, num)
print(max_n)
print(min_n)
# 在大顶堆中获取第N大的元素
max_nm_n = max_n.pop()
print(max_nm_n)


min_nm_n = min_n.pop()
print(min_nm_n)
print(sorted(num))
