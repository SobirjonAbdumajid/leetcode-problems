class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # Step 1: Sort robots and factories by their positions
        robot.sort()
        factory.sort()

        # Step 2: Define the number of robots and factories
        n = len(robot)
        m = len(factory)

        # Step 3: Initialize DP table with infinity
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # Step 4: Fill the DP table
        for j in range(1, m + 1):  # Iterate over each factory
            dp[0][j] = 0  # No robots to assign results in zero distance
            for i in range(1, n + 1):  # Iterate over each robot
                # Carry over the minimum distance from the previous factory
                dp[i][j] = dp[i][j - 1]
                
                # Assign up to 'limit' robots to the current factory
                limit = factory[j - 1][1]
                total_distance = 0
                for k in range(1, min(i, limit) + 1):
                    # Calculate the distance for assigning k robots to this factory
                    total_distance += abs(robot[i - k] - factory[j - 1][0])
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)

        # Step 5: Return the minimum distance for all robots and all factories
        return dp[n][m]
