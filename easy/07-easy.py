class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        my_list = []
        max_value_list = []

        for i, value in enumerate(prices):
            buy = value
            for j in prices:
                my_list.append(buy - j)
                max_value_list.append(max(my_list))
                
            return my_list, max_value_list
            
            
        