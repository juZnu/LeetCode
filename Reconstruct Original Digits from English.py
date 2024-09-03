class Solution:
    def originalDigits(self, s: str) -> str:
        hashmap = collections.Counter(s)
        result = ['' for _ in range(10)]
        
        if hashmap.get('z',0):
            count = hashmap['z']
            result[0] = '0' * count
            for ele in 'zero':
                hashmap[ele] -= count

        if hashmap.get('w',0):
            count = hashmap['w']
            result[2] = '2' * count
            for ele in 'two':
                hashmap[ele] -= count
        
        if hashmap.get('x',0):
            count = hashmap['x']
            result[6] = '6' * count
            for ele in 'six':
                hashmap[ele] -= count
        
        if hashmap.get('g',0):
            count = hashmap['g']
            result[8] = '8' * count
            for ele in 'eight':
                hashmap[ele] -= count
        
        if hashmap.get('t',0):
            count = hashmap['t']
            result[3] = '3' * count
            for ele in 'three':
                hashmap[ele] -= count
        
        if hashmap.get('s',0):
            count = hashmap['s']
            result[7] = '7' * count
            for ele in 'seven':
                hashmap[ele] -= count
        
        if hashmap.get('r',0):
            count = hashmap['r']
            result[4] = '4' * count
            for ele in 'four':
                hashmap[ele] -= count
        
        if hashmap.get('v',0):
            count = hashmap['v']
            result[5] = '5' * count
            for ele in 'five':
                hashmap[ele] -= count
        
        if hashmap.get('o',0):
            count = hashmap['o']
            result[1] = '1' * count
            for ele in 'one':
                hashmap[ele] -= count
        
        if hashmap.get('i',0):
            count = hashmap['i']
            result[9] = '9' * count
            for ele in 'nine':
                hashmap[ele] -= count
            
        return ''.join(result)
        