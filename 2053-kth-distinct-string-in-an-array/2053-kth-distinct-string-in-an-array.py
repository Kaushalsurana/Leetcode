from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        c = 0
        for i in arr:
            if d[i] == 1:
                c += 1
                if c == k:
                    return i
        return ""
