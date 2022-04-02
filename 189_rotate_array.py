class Solution:
    def rotate(self, nums, k):
        '''
        Rotates list to the right with step k
        Time complexity: O(n)
        Space complexity: O(1)
        :param nums: list of numbers
        :param k: rotating step, integer, can't be negative
        :return: None
        '''
        def reverse_list(lst, left_border, right_border):
            '''
            Auxilary function, reverses part of this list in place
            :param lst: list of numbers
            :param left_border: left border of reversing interval
            :param right_border: right border of reversing interval, can't be less than left_border
            :return: None
            '''
            left, right = left_border, right_border - 1
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        length = len(nums)
        # In case k > len(nums)
        k = k % length
        # Reverse array
        reverse_list(nums, 0, length)
        # Reverse first k elements
        reverse_list(nums, 0, k)
        # Reverse remaining elements
        reverse_list(nums, k, length)
