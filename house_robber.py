class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def rob(self, nums):
      
    if not nums:
    	return 0

   	n = len(nums)

    if n < 2:
      return nums[0]

   	dp = {}
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])


    for i in range(2, n):
      dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    return dp[n-1]
