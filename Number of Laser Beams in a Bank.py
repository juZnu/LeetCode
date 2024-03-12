def numberOfBeams( bank):
        count = 0
        prev = 0
        for ele in bank:
            pres = 0
            for one in ele:
                pres += int(one)
            count += prev * pres
            prev = pres if pres else prev
        return count
    
print(numberOfBeams(bank = ["011001","000000","010100","001000"]))