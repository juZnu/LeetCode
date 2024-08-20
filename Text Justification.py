class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(str_array):
            if len(str_array) == 1:
                return str_array[0]+ (' ' * (maxWidth - len(str_array[0])))

            total_length = 0

            for ele in str_array:
                total_length += len(ele)

            space_length = maxWidth - total_length
            n = len(str_array) - 1
            i = 0
            res = ''
            for ele in str_array[:-1]:
                carry = space_length//n + (1 if space_length%n else 0)
                res += ele+ (' ' * carry)
                space_length -= carry
                n -= 1
            return res + str_array[-1]

        res = []
        carry = []
        count  = 0
        
        for word in words:
            if count + len(word) > maxWidth:
                res.append(justify(carry))
                count = 0
                carry = [word]
            else:
                carry.append(word)
            count += len(word)+1

        carry = ' '.join(carry)
        res.append(carry+ (' ' * (maxWidth - len(carry))))

        return res