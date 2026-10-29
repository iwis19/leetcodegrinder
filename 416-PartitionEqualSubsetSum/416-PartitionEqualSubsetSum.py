class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        total = sum(nums)

        if total%2:
            return False

        target = total // 2

        """
        what needs to happen is: outputs loop + curr num + before edit outputs

        3 3 6 8 16 16 16 18 20

        0 3 (add 3 to it) -> 3 6 + prev -> ***0 3 6*** (use a set)

        0 3 6 (add 6 to it) -> 6 9 12 + 0 3 6 -> ***0 3 6 9 12***

        0 3 6 9 12 (add 8 to it) -> 8 11 14 17 20 + 0 3 6 9 12 -> ***0 3 6 8 9 11 12 14 17 20***

        bro i dont know why my sets werent working earlier i needa figure it out
        - bruh i was editing the reference like a dumbass

        core idea is just to keep track of all possible sums and target is exactly half the entire sum.
        once the possible sum includes that, then its possible to make a subset w sum, and hte remaining nums also a subset
        """

        outputs = [set([0])]
        n = len(nums)

        for i in range(n):
            prev = outputs[-1]
            new = set()
            for item in prev:
                pos = item + nums[i]
                if pos == target:
                    return True
                new.add(pos)
            prev.update(new)
            outputs.append(prev)

        return False
        


        
