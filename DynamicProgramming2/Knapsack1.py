#Time_Complexity: O(m*n) 
#Space_Complexity : O(m*n)
def knapsack(val,wt,c,n):
    dp = [[ 0 for i in range(c+1)] for j in range(n+1)] # creating dp matrix with value 0
    for i in range(1,n+1):
        for j in range(c+1):
            if j<wt[i-1]: # if jth isterative value is less than weight
                dp[i][j] = dp[i-1][j] # assigning to dp martix
            else:
                dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i-1][j-wt[i-1]]) # finding max between previous and weight value + dp array and assigning to dp matrix
    return dp[-1][-1]

val = [2,4,6,8]
wt = [1,2,3,4]
c=7
n=len(val)
print(knapsack(val,wt,c,n))
