class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        """
        needed answer for this.

        i think the biggest lesson learned here is that i could only think of a O(n*m * log10(arr1_element) * log10(arr2_element)) and i felt that
        was trash. even tho i doint hate that i dont implement strats that i think are inefficient, i saw a hint where it was about find every single
        prefix of every number in arr1 and then comparing it with nums in arr2

        i thought that this approach was too slow and inefficient. worst case i calculated was that log10(arr[i]) = 8 and multiplied by n+m so the final
        compute operations would be 2*5*10^4 * 8 = 1*10^5 * 8 = 8*10^5. but now, i know that 10^5 and 10^6 is not crazy compute numbers for python. its 
        only crazy at 10^7 and above (except c++)

        185 ms runtime beats 87% O((n+m)*d)
        """
        
        prefixes = set()

        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10

        res = 0

        for num in arr2:

            while num > 0:
                if num in prefixes:
                    res = max(res, len(str(num)))
                    break
                num //= 10

        return res

            
