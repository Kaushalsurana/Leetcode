class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        a = [[] for _ in range(n)]
        b = defaultdict(list)
        for c, d in edges:
            b[d].append(c)
        
        def dfs(node):
            s = [node]
            t = set()
            
            while s:
                curr = s.pop()
                for i in b[curr]:
                    if i not in t:
                        a[node].append(i)
                        s.append(i)
                        t.add(i)

        for i in range(n):
            dfs(i)

        for i in a:
            i.sort()
        
        return a