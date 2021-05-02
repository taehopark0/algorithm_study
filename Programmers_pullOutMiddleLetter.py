def solution(s):


    if len(s) == 1:
        return s
    else:
        if len(s)%2 == 1:
            return s[int((len(s)-1)/2)]
        if len(s)%2 == 0:
            return s[int(len(s)/2-1)]+s[int(len(s)/2)]

#s="abcde" return ="c"
#s="qwer" return = "we"