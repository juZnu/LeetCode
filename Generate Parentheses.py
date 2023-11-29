def generateParenthesis(n):
    result = []
    def recParenthesis(string,close,open):
        if close == n and open == n:
            result.append(string)
        elif close == open:
            recParenthesis(string+'(',close,open+1)
        elif close < open :
            if open != n:
                recParenthesis(string+'(',close,open+1)
                recParenthesis(string+')',close+1,open)
            else:
                recParenthesis(string+')',close+1,open)
    recParenthesis('',0,0)
    return result