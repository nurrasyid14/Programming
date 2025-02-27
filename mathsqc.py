def fibonacci(u):
    rawfib = [0, 1]
    for i in range(2, u):
        rawfib.append(rawfib[-2] + rawfib[-1])
    return rawfib[-1]

def Sn_fibonacci(u):
    rawfib = [0, 1]
    for i in range(2, u):
        rawfib.append(rawfib[-2] + rawfib[-1])
    return sum(rawfib)

def arithmetic (bas,a, dif):
    rawarit = [0, bas]
    for i in range(1, a):
        rawarit.append(rawarit[-1] + dif)
    return rawarit[-1]

def Sn_arithmetic (bas,a, dif):
    rawarit = [0, bas]
    for i in range(1, a):
        rawarit.append(rawarit[-1] + dif)
    return sum(rawarit)

def geometric (bas, a, multiplier):
    rawgeom= [0, bas]
    for i in range(1, a):
        rawgeom.append(rawgeom[-1] * multiplier)
    return rawgeom[-1]

def Sn_geometric (bas, a, multiplier):
    rawgeom= [0, bas]
    for i in range(1, a):
        rawgeom.append(rawgeom[-1] * multiplier)
    return sum(rawgeom)

def geom_power (bas, u, power):
    rawexgeom = [0, bas]
    for i in range (1,u):
        rawexgeom.append(rawexgeom[-1] ** power)
    return rawexgeom[-1]

def Sn_geom_power (bas, u, power):
    rawexgeom = [0, bas]
    for i in range (1,u):
        rawexgeom.append(rawexgeom[-1] ** power)
    return sum(rawexgeom)