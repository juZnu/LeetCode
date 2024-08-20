class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        hashmap ={}

        def nextDay(cells):
            num = 0
            res = [0]
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    res.append(1)
                    num |= (1<<i)
                else:
                    res.append(0)
            res.append(0)
            return res,num

        while n >0:
            next_day,num = nextDay(cells)
            
            if num in hashmap:
                current = hashmap[num]
                n  =  n % (len(hashmap) - (current))
                break

            hashmap[num] = len(hashmap)
            cells = next_day
            n -= 1

        while n>0:
            n -= 1
            cells,num = nextDay(cells)

        return cells

        