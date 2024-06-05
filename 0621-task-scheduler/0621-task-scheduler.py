class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for ch in tasks:
            count[ord(ch) - ord('A')] += 1
        count.sort()
        mxVal = count[25] - 1
        idle = mxVal * n
        for i in range(24, -1, -1):
            idle -= min(count[i], mxVal)
        return idle + len(tasks) if idle > 0 else len(tasks)