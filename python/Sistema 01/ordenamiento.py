def sortOne(a,b,c):
    if a < b:
        if a < c:
            if b < c:
                return a,b,c
            else:
                return a,c,b
        else:
            return c,a,b
    else:
        if a < c:
            return b,a,c
        else:
            if b < c:
                return b,c,a
            else:
                return c,b,a

def sortTwo(a,b,c):
    if a <= b:
        if a <= c:
            if b<=c:
                return a,b,c
            else:
                return a,c,b
        else:
            return c,a,b
    else:
        if a <= c:
            return b,a,c
        else:
            if b<=c:
                return b,c,a
            else:
                return c,b,a




