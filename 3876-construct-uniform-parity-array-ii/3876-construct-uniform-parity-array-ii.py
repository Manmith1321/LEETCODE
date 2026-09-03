class Solution:
    def uniformArray(self, nums1):
        minimum = min(nums1)

        # If minimum is odd, we can make all elements odd
        if minimum % 2 == 1:
            return True

        # If minimum is even, all elements must be even
        for x in nums1:
            if x % 2 == 1:
                return False

        return True