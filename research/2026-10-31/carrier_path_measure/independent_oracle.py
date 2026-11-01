"""Independent combinatorial validation of the carrier path research prototype.

No import of carrier_path_measure. Uses spanning-tree/two-forest enumeration
in place of the Laplacian solver, and direct bitword enumeration in place of
Gaussian-Pascal recurrence. All arithmetic is exact.
"""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def two_forest_resistance(vertices, edges, source, sink):
    """Kirchhoff's exact spanning-tree / separating-two-forest formula."""
    edges = tuple((u, v, Fraction(c)) for u, v, c in edges)
    if not (0 <= source < vertices and 0 <= sink < vertices) or source == sink:
        raise ValueError("bad endpoints")

    def weight_if_forest(indices, target_components, separate):
        parent = list(range(vertices))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        weight = Fraction(1)
        for i in indices:
            u, v, c = edges[i]
            if c <= 0:
                raise ValueError("invalid conductance")
            ru, rv = root(u), root(v)
            if ru == rv:
                return Fraction(0)
            parent[ru] = rv
            weight *= c
        components = {root(v) for v in range(vertices)}
        if len(components) != target_components:
            return Fraction(0)
        if separate and root(source) == root(sink):
            return Fraction(0)
        return weight

    spanning_trees = sum((weight_if_forest(I,1,False)
                         for I in combinations(range(len(edges)),vertices-1)),Fraction(0))
    if not spanning_trees:
        raise ValueError("disconnected carrier")
    separating_two_forests = sum((weight_if_forest(I,2,True)
                                 for I in combinations(range(len(edges)),vertices-2)),Fraction(0))
    return separating_two_forests / spanning_trees


def direct_pascal_cyclotomic_zero(order):
    """Enumerate all 2^order bit paths; independent of q-binomial recursion.

    For a primitive 2^a root zeta, exact vanishing means that for each
    k=1..order-1 and each residue r<order/2, multiplicities of phases
    zeta^r and zeta^(r+order/2) agree.
    """
    if order < 2 or order & (order-1):
        raise ValueError("order must be a 2-power")
    histogram = [[0]*order for _ in range(order+1)]
    for word in product((0,1),repeat=order):
        ones = 0
        zeroes = 0
        area = 0
        for bit in word:
            if bit:
                ones += 1
                area += zeroes
            else:
                zeroes += 1
        histogram[ones][area % order] += 1
    for k in range(1,order):
        if sum(histogram[k]) != comb(order,k):
            return False
        if any(histogram[k][r] != histogram[k][r+order//2]
               for r in range(order//2)):
            return False
    return True


def run_oracle():
    results = {}
    for vertices, edges, a,b in (
        (3,[(0,1,1),(1,2,1)],0,2),
        (3,[(0,1,1),(1,2,1),(0,2,1)],0,2),
        (4,[(0,1,1),(1,2,1),(2,3,1),(3,0,1)],0,2),
        (4,[(0,1,2),(1,2,3),(2,3,4),(3,0,5),(0,2,7)],1,3),
    ):
        results[f"R_{vertices}_{a}_{b}_{len(edges)}"] = str(two_forest_resistance(vertices,edges,a,b))
    results["direct_Pascal16_all_interior_zero"] = direct_pascal_cyclotomic_zero(16)
    return results


if __name__ == "__main__":
    import json
    print(json.dumps(run_oracle(),indent=2,sort_keys=True))
