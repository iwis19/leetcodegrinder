class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        """
        very interesting daily problem, needed some help but it was good learning about cycles...

        altthough idk about this runtime (optimal tho i think)

        1064 ms runtime beats 70%
        """
        
        pairs = []
        n = len(nums)

        for i, num in enumerate(nums):
            pairs.append((digit_sum(num), num, i))

        pairs.sort(key=lambda x: x[:2])

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle_len = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pairs[j][2]
                cycle_len += 1

            swaps += cycle_len - 1
                
        return swaps

def digit_sum(n: int) -> int:
    s = 0
    while n:
        s += n%10
        n //= 10
    return s
