class Solution(object):
    def search(self, nums, target):
        '''
        Binary search realization
        Time complexity: O(log n)
        Space complexity: O(1)
        :param nums: array of integers, sorted in ascending order
        :param target: integer
        :return: index of target, if it exists in nums; -1 otherwise
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1



