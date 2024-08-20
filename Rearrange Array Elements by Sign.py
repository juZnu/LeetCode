class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        post = []
        neg = []
        res = []

        for i in nums:
            if i >0:
                post.append(i)
            else:
                neg.append(i)

        for i in range(len(post)):
            res.append(post[i])
            res.append(neg[i])
        
        return res
