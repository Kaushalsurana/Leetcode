class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        sorte=sorted(count,key=count.get,reverse=True)
        result=''
        for i in sorte:
            result+=i*count[i]
        return result
