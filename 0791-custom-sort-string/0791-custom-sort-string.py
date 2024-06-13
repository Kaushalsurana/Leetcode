class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count=Counter(s)
        order_count=Counter(order)
        ans=""
        for i in order:
            ans+=i*s_count[i]
        for i in s:
            if i not in order_count:
                ans+=i
        return ans    