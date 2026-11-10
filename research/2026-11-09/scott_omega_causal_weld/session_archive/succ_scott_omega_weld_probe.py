"""Exact finite SUCC + omega-indexed two-path / circle weld controls.

This tests finitely indexed consequences. Equality of dcpo limits is proved
separately in the companion mathematical note, not inferred from testing.
No GitHub interactions or external dependencies.
"""
from fractions import Fraction as Q


def distance_circle(a, b):
    d = abs(a-b) % 1
    return min(d, 1-d)


def phase(x):
    return x % 1


def prefixes(n):
    assert n >= 1
    e=Q(1,16**n)
    return (Q(1)-e,Q(0))


def interval_prefixes(n):
    e=Q(1,16**n)
    return (Q(1)-e,Q(1)),(Q(0),e)


def omega_leftmost_length(k, steps):
    assert k>=2 and steps>=0
    return 2 + steps * (k-2)


def test():
    seen=0
    for k in range(2,11):
        for n in range(100):
            assert omega_leftmost_length(k,n+1) - omega_leftmost_length(k,n) == k-2
            seen+=1
    for n in range(1,101):
        a,b=prefixes(n)
        e=Q(1,16**n)
        assert a != b
        assert phase(a)!=phase(b)
        assert distance_circle(phase(a),phase(b))==e
        (left_a,right_a),(left_b,right_b)=interval_prefixes(n)
        assert left_a==a and right_a==1 and left_b==b and right_b==e
        assert right_b < left_a  # disjoint as real compact sets, n>=1
        if n>1:
            (old_a,old_end),(old_b,old_eps)=interval_prefixes(n-1)
            assert old_a < left_a and right_a == old_end
            assert old_b==left_b and right_b < old_eps
        seen+=1
    for n in range(1,25):
        for m in range(1,25):
            # Arcs q([1-e_n,1]) and q([0,e_m]) are opposite sides
            # of the seam, so their circular Hausdorff distance is
            # max(e_n,e_m); unlike 0 until both counters diverge.
            en=Q(1,16**n); em=Q(1,16**m)
            assert max(en,em)>0
            assert distance_circle(phase(1-en),phase(0))==en
            assert distance_circle(phase(0),phase(em))==em
            seen+=1
    # Even after q identifies the limit endpoints, a lift still carries
    # a nonzero integer deck difference.
    assert phase(Q(1))==phase(Q(0))
    assert Q(1)-Q(0)==1
    # Source-independent control: same limiting circle readout need not
    # mean equal histories or identical underlying reals.
    assert Q(1)!=Q(0)
    print(f"PASS: {seen} exact finite checks; two never-equal finite paths; ")
    print("      circle defect 16^-n; distinct line limits; equal quotient limits.")
    print("The equal-limits and Scott-continuity theorems are in the note.")


if __name__=="__main__":
    test()
