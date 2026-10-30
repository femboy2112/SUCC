# Positive-slip cylinder probe

**Predeclared before execution.** Extend CT8 from zero slips to at most K
strict slips (distance greater than delta), retaining every source increment.
Fresh native starts: p1153,b145 and p1201,b151, h=1,5; prefix lengths6,8,10;
delta=1/20; K=1. These are short prefixes, not complete SC-06 windows.

Partition the initial centered lag coordinate x in [-1/2,1/2] according to
the exact affine maps y_j=16^j x+g_j, g_(j+1)=16g_j+f_j. At each stage the
closed good strips [m-delta,m+delta] cost zero; the closed complementary
strips [m+delta,m+1-delta] cost one. Intersect their inverse images with
the surviving rational intervals, discard paths costing more than K,
and merge overlapping intervals of the same cost. Closing both strips
produces a conservative endpoint cover: every point with at most K strict
slips is retained. Points on thresholds receive the favorable zero cost.
The affine coordinate is global, so merging equal-cost intervals loses no
future information. This is an exact finite algorithm, not sampling.

Pass: direct rational propagation and interval membership agree at all
declared rational grid points that avoid thresholds; authentic zero-seed
coordinate is outside and has more than K strict slips. Fail: preserve any
disagreement or surviving authentic coordinate. Coherent-source tail control
is checked via a rational Green-prefix coordinate and a certified error.
An interval-boundary touch is reported, not treated as exclusion.

The probe attacks the positive-slip union directly. Thin Lebesgue measure
still says nothing about the selected point without the exact membership
calculation, and finite membership exclusions do not prove the uniform
all-prime positive-density assertion. Larger L and K proportional to L need
controlled branch complexity and then an arithmetic argument, not extrapolation.

**Executed result:** all12 rows passed;1,548 rational forward-grid membership
checks passed. The authentic phases have more than one strict slip, and the
rigorously bounded coherent coordinates lie inside. At length10 the computed
union measure is223/687194767360 in all four declared (p,h) cases. This is
OBSERVED finite equality, not a claimed formula for all sources or windows.
Raw rational outputs and command metadata are `receipts/cylinder-union.*`.
