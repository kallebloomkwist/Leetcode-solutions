# The isBadVersion API is already defined for you.
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        '''
        Finds first bad version in release sequence from 1 to n
        Time complexity: O(log n)
        Space complexity: O(1)
        :param n: number of versions
        :return: bad, number of the first bad version
        '''
        left, right = 1, n
        # Corner case
        if isBadVersion(left):
            return 1
        while left + 1 < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return right