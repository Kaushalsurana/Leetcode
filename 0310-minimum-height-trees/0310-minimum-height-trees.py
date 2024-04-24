class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        a = defaultdict( set )

        for src_node, dst_node in edges:
            a[src_node].add( dst_node )
            a[dst_node].add( src_node )

        q = deque()
        for i in range(n):
            if len(a[i]) == 1:
                q.append(i)

        while n > 2:
            k = len(q)
            n -= k
            while k:
                node = q.popleft()
                pN = a[node].pop()
                a[pN].remove(node)
                del a[node]

                if len(a[pN]) == 1:
                    q.append(pN)
                k -= 1

        return list(q)