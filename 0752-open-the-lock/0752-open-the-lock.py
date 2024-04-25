class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        rm = {str(k): str((k + 1) % 10) for k in range(10)}
        lm = {str(k): str((k - 1) % 10) for k in range(10)}
        q = ["0000"]
        h = set(deadends)
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                node = q.pop(0)
                for idx, s in enumerate(node):
                    l = lm[s]
                    r = rm[s]
                    l = node[:idx] + l + node[(idx + 1):]
                    r = node[:idx] + r + node[(idx + 1):]
                    if l == target or r == target:
                        return ans
                    if l not in h:
                        q.append(l)
                        h.add(l)
                    if r not in h:
                        q.append(r)
                        h.add(r)
        return -1