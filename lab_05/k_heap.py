import math

class K_Heap:
    length = 0
    data = []

    def __init__(self, values, K):
        self.data = values
        self.length = len(values)
        self.k = K

    def build_heap(self):
        for i in range(self.length//self.k - 1, -1, -1):
            self.sink(i)

    def parent(self, i):
        return ((i + (self.k-1)) // self.k) - 1

    def children(self, i):
        return [self.k*i + j for j in range(1, self.k+1)]

    def sink(self, i):
        largest_known = i
        temp = self.children(i)
        for j in range(len(self.children(i))):
            if j < len(self.children(i)) and self.data[temp[j]] > self.data[i]:
                largest_known = i + j + 1
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)

