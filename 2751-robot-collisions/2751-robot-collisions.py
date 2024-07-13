class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        st = []
        for i in sorted(range(len(positions)), key = lambda i: positions[i]):
            if directions[i] == 'R':
                st.append(i)
            else:
                while st and healths[st[-1]] < healths[i]:
                    healths[i] -= 1
                    healths[st.pop()] = 0
                if st:
                    if healths[st[-1]] == healths[i]:
                        healths[st.pop()] = 0
                    else:
                        healths[st[-1]] -= 1
                    healths[i] = 0
        a=[]
        for i in healths:
            if i:
                a.append(i)
        return a