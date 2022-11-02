#Time_Complexity: O(m*n) 
#Space_Complexity : O(m*n)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)] # creating dp matrix
        
        for j in range(1,amount+1): 
            dp[0][j] = amount+1 # assigning amount+1 to dp array
        
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                if j < coins[i-1]: # if jth value is less than coins
                    dp[i][j] = dp[i-1][j] 
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]]) # assigning min value between dp value and dp of coins
                    
        if dp[-1][-1] == amount+1: # if dp of last is equal to amount+1
            return -1
        return dp[-1][-1] # returning last value in matrix
