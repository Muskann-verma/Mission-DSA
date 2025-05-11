import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        dummy = ListNode(0)
        current = dummy

        while heap:
            smallest = heapq.heappop(heap)
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, smallest.next)

        return dummy.next
