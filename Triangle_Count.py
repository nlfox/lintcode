class Solution:
    # @param S: a list of integers
    # @return: a integer
    def twoSum2(self, nums, target):
        # Write your code here
        left, right = 0, len(nums) - 1
        c = 0
        while left < right:
            if nums[left] + nums[right] > target:
                c += (right - left)
                right -= 1
            else:
                left += 1
        return c

    def triangleCount(self, S):
        # write your code here
        S.sort()
        left, right = 0, len(S) - 1
        c = 0
        r = 0
        for i in xrange(len(S)):
            r = self.twoSum2(S[:right], S[right])
            c += r
            right -= 1
        return c