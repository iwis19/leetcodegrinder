class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        """
        erm calm 34 mins on this question im highkey dum (music ddoes NOT hgelp in the backlground)

        all thought process are laid out besiddes last step debugging, lowkey loved this quesrion

        20 ms runtime beats 80%
        """
        
        """
        case 1:
            all elements in the arr alr fit the condition, no element moved so return largest element in there

        case 2:
            not organized, so count the amt of unorganized numbers and add it with the last organized #
            
        """

        """
        1,1,2,2,2

        1,100,1000

        1,2,3,4,5

        1,2,2,5,6,7
        """

        arr.sort()
        arr[0], res = 1, 1
        n = len(arr)

        """
        because arr[i] can solely decrease and not increase, i must set a cap on it before it just returns n

        if arr[i] <= i - 1, then arr[i] is achievable

        i = 0, arr[0] = 1

        i = 1, arr[1] = 2

        arr[i] <= i+1

        arr[i] = 3, i = 2
        """
        for i in range(1, n):

            # this would pass no matter what
            # if arr[i] <= i - 1:
            #     res = arr[i]
            # else:
            #     res += 1


            if arr[i] - arr[i-1] <= 1:
                res = arr[i]

            else:
                
                res += 1
                arr[i] = res  # help place the arr[i] back on track

        return res
