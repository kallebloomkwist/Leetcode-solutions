class Solution:
    def validPalindrome(self, s):
        '''
        Checks, is string a palindrome after deleting at most 1 symbol
        Time complexity: O(n)
        Space complexity: O(1)
        :param s: input string
        :return: True - if string can be transformed into palindrome this way, False otherwise
        '''

        def check_palindrome(s, left, right):
            '''
            Aux function, checks is part of string between two pointers a palindrome
            :param s: input string
            :param left: left border
            :param right: right border
            :return: True, if required interval is a palindrome, False otherwise
            '''
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # We should try to delete either top left or top right symbol to get palindrome
                # If it's impossible either way, we need more than 1 deletion, so function returns False
                return check_palindrome(s, left, right - 1) or check_palindrome(s, left + 1, right)
            left += 1
            right -= 1
        return True
