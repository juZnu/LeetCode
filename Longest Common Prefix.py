def longestCommonPrefix(strs):
        result = strs.pop()
        while strs:
            element = strs.pop()
            i = 0
            while i < len(element) and i < len(result):
                if element[i] != result[i]:
                    break
                i += 1
            result = result[:i]
        return result