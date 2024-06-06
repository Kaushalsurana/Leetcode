class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        c=Counter(hand)
        for i in hand:
            if c[i]==0:
                continue
            for j in range(groupSize):
                if c[i+j]>0:
                    c[i+j]-=1
                else:
                    return False
        return True