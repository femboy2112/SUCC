# Preserved red scratch probes — NOT quietly discarded

## RED-1: anticipated wrong-carry detection failed

Initial finite test in triangle_tests, before the repair:

    a2,b2,d2=overlaps(v,c+flip,x,Q)
    assert (a2+d2-3*b2)%Q != 0
    AssertionError

This expectation is mathematically FALSE. Exact algebra yields A+D−3B=2(V−C−x), and a carry mutation by flip=Q/2 yields a defect −Q, hence zero modulo Q. The corrected test now DEMANDS equality to zero for the spoof and detects the missing bit modulo 2Q. THEOREMS TS2 includes the repaired scope; the original failure is crucial evidence of a real 2-adic certificate gap.

## RED-2: wrong test helper used on H shadow

An initial signed-shell scratch invocation reused energy(xs,[0]*N,Q,M) for the non-original rational shadow H(n)=n/(2n−1)^4. That helper enforces a **BBP V(n)** relabeling check, which is wrong for H. The run failed:

    assert all(len(group)==M for group in state_groups.values())
    AssertionError

This was a misapplied oracle, NOT evidence against the shadow. It was repaired by independently computing the unlabelled progression energy for arbitrary rational phase sequences. The corrected H-shadow controls pass, with R near 1.

Both red tests preceded successful 10/10 finished unit tests. Failures are included because they distinguish source-specific invariants from generic models and prevent false theorem promotion.
