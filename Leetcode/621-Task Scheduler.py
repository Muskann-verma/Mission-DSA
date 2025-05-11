from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        max_count = max(count.values())
        
        # Count how many tasks have the maximum frequency
        num_max = sum(1 for task in count.values() if task == max_count)
        
        part_count = max_count - 1
        part_length = n - (num_max - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_count * num_max
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles
