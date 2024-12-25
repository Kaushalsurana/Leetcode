class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mo = 10**9 + 7
        a =n// 2 
        b =n-a  
        var_odd =pow(4, a, mo)
        var_even =pow(5, b, mo)
        res =(var_odd * var_even) % mo
        return res