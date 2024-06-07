class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0) + 1
        count = 0
        carry = 0
        for k,v in hashmap.items():
            if not v%2:
                count += v
            else:
                count += v-1
                carry += 1
        return count + (1 if carry else 0)

        