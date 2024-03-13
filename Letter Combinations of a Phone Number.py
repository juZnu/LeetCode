from typing import List


def letterCombinations(digits: str) -> List[str]:
        numberToLetter = {
            "2":"abc",
            "3":"def",
            "4":'ghi',
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        results = []
        def combiantion(word,digit):
            if not digit:
                results.append(word)
                return
            for i in numberToLetter[digit[0]]:
                combiantion(word+i,digit[1:])
        combiantion("",digits)
        return results

print(letterCombinations(digits = "23"))