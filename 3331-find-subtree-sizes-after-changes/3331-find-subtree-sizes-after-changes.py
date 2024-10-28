class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        from collections import defaultdict
        n=len(parent)
        t=defaultdict(list)
        for i in range(1,n):
            t[parent[i]].append(i)
        new=list(parent)
        def find(node,char):
            cur=parent[node]
            while cur!=-1:
                if s[cur]==char:
                    return cur
                cur=parent[cur]
            return None
        for node in range(1,n):
            ancestor = find(node, s[node])
            if ancestor is not None:
                new[node] = ancestor
                t[parent[node]].remove(node)
                t[ancestor].append(node)     
        answer = [0] * n
        def dfs(node):
            size = 1
            for child in t[node]:
                size += dfs(child)
            answer[node] = size
            return size
        
        dfs(0) 
        
        return answer