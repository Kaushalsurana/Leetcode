from collections import defaultdict,deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        a=defaultdict(list)
        b=defaultdict(list)
        for i,j in invocations:
            a[i].append(j)
            b[j].append(i)
        def ran(k):
            q=set()
            p=deque([k])
            while p:
                y=p.popleft()
                if y not in q:
                    q.add(y)
                    for i in a[y]:
                        if i not in q:
                            p.append(i)
            return q
        sus=ran(k)
        for i in sus:
            for j in b[i]:
                if j not in sus:
                    return list(range(n))
        rem=[i for i in range(n) if i not in sus]
        return rem