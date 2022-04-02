class Solution:
    def sortedSquares(self, nums):
        '''
        Transforms sorted list into sorted list of squared values in initial list
        Time complexity: O(n)
        Space complexity: O(n)
        :param nums: sorted list of integer values
        :return: sorted list of squared values in initial list
        '''
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1]
