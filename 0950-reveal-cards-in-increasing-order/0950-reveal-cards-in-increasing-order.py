class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque([])
        for c in deck[::-1]:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(c)
        return queue