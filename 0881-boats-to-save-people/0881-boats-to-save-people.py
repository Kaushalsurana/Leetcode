class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        a=0
        b,c=0,len(people)-1
        while b<=c:
            a+=1
            if people[b]+people[c]<=limit:
                b+=1
            c-=1
        return a
            
