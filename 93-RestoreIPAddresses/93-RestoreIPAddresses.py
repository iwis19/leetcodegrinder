class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        """
        beauty sol gotta start doing more in da morning

        1 ms runtime beats 63%
        """
        
        ans = []
        n = len(s)

        def dfs(arr, index):

            """
            in each dfs call, im aiming to get one WHOLE number done. and then i move on to next stage
            only get ones that are 0<=x<=255

            if len of arr meets 4 after appending, i do ans.append(".".join(arr))
            """
            if len(arr) == 4:
                if index == n:
                    ans.append(".".join(arr))
                return

            curr = 0
            i = index

            while i < n:

                curr = curr*10 + int(s[i])  # also need handlign from leading zero, come back to this
                if not 0<=curr<=255:
                    break 
                arr.append(str(curr))
                dfs(arr, i+1)
                arr.pop()

                if s[i] == "0" and i == index:
                    break

                i += 1

        dfs([], 0)
        return ans
