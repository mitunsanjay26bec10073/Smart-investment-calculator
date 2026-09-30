import math

def getSip(self, amt, te, pe, Display):
    P = amt
    i = float(pe / 12)
    n = te * 12

    M = int(P * ((pow((1 + i), n) - 1) / i) * (1 + i))
    N = int(amt * n)
    print(M, N)

    Display(self, M, N)

def getLump(self, lsamt, te, pe, Display):
    P = lsamt
    M = math.ceil(P * (pow(1 + pe, te)))
    print(M, P)

    Display(self, M, P)