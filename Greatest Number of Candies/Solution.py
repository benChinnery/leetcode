class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = [False] * len(candies)
        most = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= most:
                output[i] = True
        return output