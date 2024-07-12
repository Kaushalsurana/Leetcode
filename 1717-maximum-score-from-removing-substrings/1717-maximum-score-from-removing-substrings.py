class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def k(s,sub,p):
            st=[]
            a=0
            for i in s:
                st.append(i)
                if len(st)>=2 and st[-2]+st[-1]==sub:
                    st.pop()
                    st.pop()
                    a+=p
            return ''.join(st),a
        if x>y:
            s,b=k(s,"ab",x)
            s,c=k(s,"ba",y)
        else:
            s,c=k(s,"ba",y)
            s,b=k(s,"ab",x)
        return b+c