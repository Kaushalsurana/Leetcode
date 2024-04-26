class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic=defaultdict(list)
        for u,v in edges:
            dic[u].append(v)
            dic[v].append(u)
        vis=[0]*(n)
        def dfs(node):
            if node==destination:
                return True
            for n in dic[node]:
                if vis[n]==0:
                    vis[n]=1
                    if dfs(n)==True:
                        return True
            return False
        return dfs(source)