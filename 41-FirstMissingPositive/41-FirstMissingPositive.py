class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        """
        damn first hard

        i feel like a good starting point was that i knew i had to use a hashtable, but now i learned a technique about simulating a hashtable using the array indices and 
        positive/negative values indicators

        for hards, i should definitely click on topics and maybe get a hint and see how it may tell me how to solve a problem

        60 ms runtime beats 22%
        """
        
        n = len(nums)

        # make numbers that are negative or out of bounds invalid, by setting them to such as n+1
        for i in range(n):
            num = nums[i]
            if num < 1 or num > n:
                nums[i] = n + 1  # slipped up and did num = n+1 since num = nums[i] is just a value copy
        
        # we go thru all numbers in here that are VALID, and set seen ones's corresponding index in the array to negative
        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num-1] = -abs(nums[num-1])

        # since all numbers are labelled pos neg in indices, we return the first is positive
        for i in range(n):
            if nums[i] > 0:
                return i+1  # accidentally returned nums[i] + 1 since nums[i] is an unassociated value

        return n+1 # this is the case where all values is 1 2 3 4 5 6 ... so i have to use the next value thats not included
