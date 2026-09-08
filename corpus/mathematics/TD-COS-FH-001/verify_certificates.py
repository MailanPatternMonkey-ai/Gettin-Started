"""CC0-1.0 | Anonymous | Independent supplementary checks, 2026-09-08.

Exact rational enclosures for local witnesses, with outward rounding to a
rational grid after operations. No Monte Carlo, current cutoff, or replay.
The all-L/all-spacing theorem is analytical; these are finite certificates.
"""
from fractions import Fraction as F
from itertools import product, combinations
from functools import lru_cache
from math import comb
import json

GRID = 10**60
TERMS = 24


def floor_grid(x):
    return F((x.numerator * GRID) // x.denominator, GRID)


def ceil_grid(x):
    return -floor_grid(-x)


class Interval:
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo, self.hi = floor_grid(lo), ceil_grid(hi)

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Interval) else -F(other))

    def __mul__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        endpoints = [a*b for a in (self.lo, self.hi)
                     for b in (other.lo, other.hi)]
        return Interval(min(endpoints), max(endpoints))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        assert other.lo > 0
        return self * Interval(1/other.hi, 1/other.lo)

    def cap_one(self):
        return Interval(min(F(1), self.lo), min(F(1), self.hi))

    def record(self):
        return {"lower": str(self.lo), "upper": str(self.hi),
                "midpoint_display": float((self.lo+self.hi)/2),
                "width_upper_display": float(self.hi-self.lo)}


@lru_cache(None)
def normalized_bessel(n):
    # S_n = sum n!/[4^k k! (n+k)!]. The next-term ratios decrease.
    assert n >= 0
    term = total = F(1)
    for k in range(1, TERMS+1):
        term /= 4*k*(n+k)
        total += term
    rho = F(1, 4*(TERMS+1)*(n+TERMS+1))
    return Interval(total, total+term*rho/(1-rho))


@lru_cache(None)
def bessel_ratio(n, m):
    n, m = abs(n), abs(m)
    if n == m:
        return Interval(1)
    factor = F(1)
    for j in range(n+1, m+1):
        factor /= 2*j
    for j in range(m+1, n+1):
        factor *= 2*j
    return factor * (normalized_bessel(m)/normalized_bessel(n))


def cellulation(L):
    vertices = list(product(range(L), repeat=3))
    edges = [(v, a) for v in vertices for a in range(3)]
    faces = [(v, ab) for v in vertices for ab in combinations(range(3), 2)]
    edge_id, face_id = ({e:i for i,e in enumerate(cells)} for cells in (edges, faces))

    def shift(v, a):
        return tuple((x+1) % L if i == a else x for i,x in enumerate(v))

    boundaries = []
    for v, (a,b) in faces:
        boundaries.append({edge_id[v,a]: 1, edge_id[shift(v,a),b]: 1,
                           edge_id[shift(v,b),a]: -1, edge_id[v,b]: -1})
    cycles = []
    for a in range(3):
        cycles.append({edge_id[tuple(k if i == a else 0 for i in range(3)),a]:1
                       for k in range(L)})
    cubes = []
    for v in vertices:
        cube = set()
        for a in range(3):
            ab = tuple(i for i in range(3) if i != a)
            cube.update((face_id[v,ab], face_id[shift(v,a),ab]))
        assert len(cube) == 6
        cubes.append(cube)
    sheets = [{i for i,(v,ab) in enumerate(faces) if a not in ab and v[a] == cut}
              for a in range(3) for cut in range(L)]
    return vertices, edges, faces, boundaries, cycles, cubes, sheets, shift


def descriptors(L, geometry):
    _, _, faces, boundaries, cycles, cubes, sheets, _ = geometry
    V, B = L**3, 8*L**3+7
    moves = [("identity", F(V,B), {}, set(), 0)]
    moves += [("cube", F(1,B), {}, m, 0) for m in cubes]
    moves += [("sheet", F(1,3*L*B), {}, m, 0) for m in sheets]
    for i in range(len(faces)):
        for s in (-1,1):
            moves.append(("coupled",F(1,2*B),{e:s*c for e,c in boundaries[i].items()},{i},0))
            moves.append(("even_face",F(1,2*B),{e:2*s*c for e,c in boundaries[i].items()},set(),0))
    for a, cycle in enumerate(cycles):
        for s in (-1,1):
            moves.append(("even_cycle",F(1,2*B),{e:2*s for e in cycle},set(),0))
            moves.append(("unit_cycle",F(1,2*B),{e:s for e in cycle},set(),1<<a))
    assert sum((m[1] for m in moves), F(0)) == 1
    return moves


def validate(curr, membrane, q, L, geom):
    vertices, edges, _, boundaries, cycles, _, _, shift = geom
    divergence = {v:0 for v in vertices}
    residue = [i % 2 for i in curr]
    for (v,a), value in zip(edges,curr):
        divergence[v] += value
        divergence[shift(v,a)] -= value
    assert all(v == 0 for v in divergence.values())
    for face in membrane:
        for edge in boundaries[face]:
            residue[edge] ^= 1
    for a, cycle in enumerate(cycles):
        if q & (1<<a):
            for edge in cycle:
                residue[edge] ^= 1
    assert not any(residue)
    for a in range(3):
        cuts = [sum(curr[i] for i,(v,axis) in enumerate(edges)
                    if axis == a and v[a] == k) for k in range(L)]
        assert len(set(cuts)) == 1 and cuts[0] % 2 == ((q>>a)&1)


def acceptance(curr, delta, membrane_delta=0):
    bound = Interval(F(1,2)**membrane_delta)
    for edge, change in delta.items():
        bound = bound*bessel_ratio(curr[edge],curr[edge]+change)
    return bound.cap_one()


def local_certificate(N):
    L, B = 2, 71
    geom = cellulation(L)
    moves = descriptors(L,geom)
    start = tuple([2*N]*len(geom[1]))
    validate(start,set(),0,L,geom)

    @lru_cache(None)
    def stay(curr):
        # Only the unit-cycle family can change q. Membranes do not enter it.
        escape = Interval(0)
        for cycle in geom[4]:
            for s in (-1,1):
                escape += acceptance(curr,{e:s for e in cycle})*F(1,2*B)
        return Interval(1)-escape

    a1, a2 = stay(start), Interval(0)
    for _, probability, delta, membrane, q in moves:
        candidate = list(start)
        for e,c in delta.items():
            candidate[e] += c
        candidate = tuple(candidate)
        validate(candidate,membrane,q,L,geom)
        inverse = list(candidate)
        for e,c in delta.items():
            inverse[e] -= c
        assert tuple(inverse) == start
        a = acceptance(start,delta,len(membrane))
        # All rejected proposals stay at x_N. Accepted sector-changing
        # proposals are removed by D at the intermediate sampled endpoint.
        continuation = Interval(0) if q else stay(candidate)
        a2 += probability*((Interval(1)-a)*a1+a*continuation)
    ratio = a2/a1
    scaled = (ratio-F(139,142))/F(1,(4*N)**2)
    assert scaled.hi < 0
    return {"L":L,"N":N,"descriptors":len(moves),
            "proposal_mass":"1","invariants_and_inverse_currents":"PASS",
            "A1":a1.record(),"A2_over_A1":ratio.record(),
            "scaled_correction":scaled.record()}, ratio


def clock_certificate(L,d):
    B = 8*L**3+7
    # Integer path counts and derivative numerators, denominator (2B)^d.
    counts, derivs = [1]+[0]*7, [0]*8
    weights = {0:2*B-3, 1:1, 2:1, 4:1}
    changes = {0:-3, 1:1, 2:1, 4:1}
    for _ in range(d):
        counts, derivs = ([sum(counts[x^z]*weights[z] for z in weights) for x in range(8)],
                          [sum(derivs[x^z]*weights[z]+counts[x^z]*changes[z]
                               for z in weights) for x in range(8)])
    r, derivative = F(counts[0],(2*B)**d), F(derivs[0],(2*B)**d)
    character_r = sum((F(comb(3,j),8)*F(B-j,B)**d for j in range(4)),F(0))
    character_derivative = -F(d,8*B)*sum((comb(3,j)*j*F(B-j,B)**(d-1)
                                        for j in range(1,4)),F(0))
    assert r == character_r and derivative == character_derivative
    assert r > 0 and derivative < 0
    return {"L":L,"d":d,"B":B,"r0_exact":str(r),
            "derivative_exact":str(derivative),"exact_integer_walk_agrees":True}


if __name__ == "__main__":
    local = [local_certificate(n) for n in (10,100,1000)]
    assert local[0][1].hi < local[1][1].lo < local[1][1].hi < local[2][1].lo
    print(json.dumps({"scope":"Fresh finite supplementary certificates; analytical theorem separate",
                      "arithmetic":"Fraction with certified outward rational grid rounding",
                      "grid_denominator":str(GRID),"bessel_last_term":TERMS,
                      "local_certificates":[item[0] for item in local],
                      "local_ratio_intervals_pairwise_disjoint":True,
                      "clock_certificates":[clock_certificate(L,d) for L in (2,3,4)
                                            for d in (1,2,8*L**3+7)]},indent=2))
