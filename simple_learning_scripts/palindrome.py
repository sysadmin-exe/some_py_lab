def solution(S):
    # write your code in Python 3.6
	if S.casefold() == S[::-1].casefold():
		return(S)
	else:
		return("NO")


solution("hannah") 