class Solution:
    def twoSum(self, nums, target):
        '''
        Finds indices of 2 elements, with sum equal to another element of list, there's always one solution
        Time complexity: O(n)
        Space complexity: O(n)
        :param nums: array of integers
        :param target: target integer, should be equal to another two elements of nums
        :return: indices of these two elements
        '''
        dic = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in dic:
                return [dic[dif], i]
            dic[num] = i
