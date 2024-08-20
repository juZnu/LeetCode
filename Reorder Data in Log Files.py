class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def isDigitLog(log):
            i = 0
            while log[i]!= ' ':
                i += 1
            return i,not (ord('a') <= ord(log[i+1]) <= ord('z'))

        digit_logs = []
        letter_logs = []

        for log in logs:
            i,cond = isDigitLog(log)
            if cond:
                digit_logs.append(log)
            else:
                log = (log[i+1:],log[:i+1])
                letter_logs.append(log)


        letter_logs.sort()
        letter_logs = [str2+str1 for str1,str2 in letter_logs]
        letter_logs.extend(digit_logs)
        
        return letter_logs
            

            