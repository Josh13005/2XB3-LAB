# import random
# import timeit
# import math
# import Heap
#
# def create_random_list(n):
#     L = []
#     for _ in range(n):
#         L.append(random.randint(1, n))
#     return L
#
#
# def timetest(runs, length, sort):
#     total = 0
#     for _ in range(runs):
#         L = create_random_list(length)
#         heap = sort(L)
#         start = timeit.default_timer()
#         heap.build_heap1()
#         end = timeit.default_timer()
#         total += end - start
#     return total / runs
#
#
# # for i in range(10, 3000, 10):
# #     print(i, timetest(100, i, Heap))
#
# # for i in range(10, 5010, 10):
# #     print(i, timetest(10, i, Heap))
