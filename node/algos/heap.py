"""
Use heapq module via "import heapq"

This file is just a quick tutorial on how heapq module works
https://www.ashatutorials.com/python_heapq.html
"""
import heapq

# heapify(x)
# Transform given list x in to a min-heap, in-place, in linear time.
extList = [15, 2, 5, 11, 7, 3, 9, 1, 6, 8]
print('\nheapify() example:')
print('Before :', extList)
heapq.heapify(extList)
print('After  :', extList)

# heappush(heap, e)
# Adds an element to the heap maintaining heap property.
minHeap = []

heapq.heappush(minHeap, 15)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 11)
heapq.heappush(minHeap, 7)
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 9)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 6)
heapq.heappush(minHeap, 8)
print('\nheappush() example:')
print("From empty list using heappush : {}".format(minHeap))


# heappop(heap)
# Remove and return smallest element from heap maintaining heap property.
minHeap = [1, 2, 3, 6, 7, 5, 9, 11, 15, 8]

print('\nheappop() example:')
print('Before :', minHeap)
print('heappop() :', heapq.heappop(minHeap))
print('After  :', minHeap)

# heappushpop(heapList, e)
# Pushes element 'e' to the heap and pop() the smallest element from the heap.
# It runs efficiently compare to heappush() executed followed by heappop().
minHeap = [1, 2, 3, 6, 7, 5, 9, 11, 15, 8]

print('\nheappushpop() example:')
print('Before :', minHeap)
print('heappushpop() :', heapq.heappushpop(minHeap, 10))
print('After  :', minHeap)


# heapreplace(heapList, e)
# Pops the smallest element and then pushes element 'e' to heap. It runs efficiently compare to heappushpop() followed by heappush().
minHeap = [1, 2, 3, 6, 7, 5, 9, 11, 15, 8]

print('Before :', minHeap)
print('heapreplace() :', heapq.heapreplace(minHeap, 0))
print('After  :', minHeap)


# nlargest(n, iterable, key=None)
# Returns list of n largest elements after sorting given iterable by key. Equivalent to sorted(iterable, key=key, reverse=True)[:n]
n1 = [1, 2, 3, 6, 7, 5, 9, 11, 15, 8]
print(heapq.nlargest(3, n1))