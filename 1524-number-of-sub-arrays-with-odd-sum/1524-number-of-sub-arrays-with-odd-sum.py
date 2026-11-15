
class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        even = 1
        odd = 0
        ans = 0
        parity = 0

        for num in arr:
            parity = (parity + num) % 2

            if parity == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD
