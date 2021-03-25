from shape import *
import numpy as np

def GJK(s1, s2):
    # True if shapes s1 and s2 intersect
    # All vector points are "3D" ([x,y,0])
    global d
    d = normalize(s1.center - s2.center)
    simplex = [support(s1, s2, d)]
    d = ORIGIN - simplex[0]
    while True:
        A = support(s1, s2, d)
        if dot(A, d) < 0:
            return False
        simplex.append(A)
        if handleSimplex(simplex, d):
            return True

def handleSimplex(simplex, d):
    if len(simplex) == 2:
        return lineCase(simplex, d)
    return triangleCase(simplex, d)

def lineCase(simplex, d):
    B, A = simplex 
    AB, AO = B - A, ORIGIN - A
    ABperp = tripleProduct(AB, AO, AB)
    d = ABperp
    return False

def triangleCase(simplex, d):
    C, B, A = simplex
    AB, AC, AO  = B - A, C - A, ORIGIN - A
    ABperp = tripleProduct(AC, AB, AB)
    ACperp = tripleProduct(AB, AC, AC)
    if dot(ABperp, AO) < 0: #region AB
        simplex.remove(C)
        d = ABperp
        return False
    elif dot(ACperp, AO) < 0: #region AC
        simplex.remove(B)
        d = ACperp
        return False
    return True

def support(s1, s2, d):
    i = np.argmax([dot(point, d) for point in s1])
    j = np.argmax([dot(point, -d) for point in s2])
    return s1[i] - s2[j]

