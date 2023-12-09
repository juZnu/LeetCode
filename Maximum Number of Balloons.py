def maxNumberOfBalloons(text):
    ballon ={
        'b':0,
        'a':0,
        'l':0,
        'o':0,
        'n':0
    }
    for i in text:
        if ballon.get(i,-1) != -1:
            ballon[i] +=1
    ballon['l'] = ballon['l']//2
    ballon['o'] = ballon['o']//2
    output = float('inf')
    for key , value in ballon.items():
        if value < output:
            output = value
    return output
