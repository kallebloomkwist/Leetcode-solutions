class Solution:
    def searchInsert(self, nums, target):
        '''
        Finds index of element, equal to target, if it exists
        Otherwise, finds a position to insert it
        :param nums: sorted array of distinct ints
        :param target: integer value we want to find/insert
        :return: index of element, equal to target, if it exists
                 index of inserted target value otherwise
        Time complexity: O(log n)
        Space complexity: O(1)
        '''
        left, right = 0, len(nums) - 1
        while(left <= right):
            med = (left + right) // 2
            if (nums[med] == target):
                return med
            elif (nums[med] > target):
                right = med - 1
            else:
                left = med + 1
        return left