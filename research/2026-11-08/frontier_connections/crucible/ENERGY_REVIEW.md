# Hostile audit of root RE1–4

Reviewed `../ENERGY_THEOREMS.md` independently of the root implementation.
The proof is accepted for its stated scope; no original-zero cancellation
estimate follows. This is an internal separate-agent review, with shared
model family and source files, not external scholarly refereeing.

RE1: Differentiation gives exactly the two stationary families stated.
The competing family has value at least `-(b-1)`, strictly above the proposed
minimum by `pi^2/(2(b+1))<2`. The two equality points are swapped by the even
multiplier, so invariant probability weights on the minimizing support must
be equal. The parity counterexample at theta=pi is valid.

RE2: Summing over **m-1**, not m, interior transitions leaves
`Re v_0+16Re v_(m-1)`. Its lower bound -17 gives the sharpened boundary factor
`(1-1/m)sin^2(pi/34)`. The forcing difference starts at n0+1, and the bound
`15/(8n0+1)^2` uses the correct smallest denominator. The original p-pole
clock is not extended beyond its clean interval. No claim that q=2 clocks
exist infinitely often is made.

RE3: Direct expansion gives the upper defect
`34(E-s2)+17(1-c)/m+mean eta`. The same endpoints have the correct sign.
The compact set away from the two equality points has a strictly positive
minimum; the result is a concentration theorem at an extremal two-cycle,
not at Haar measure.

RE4: The normality proof is uniform inside each stage. For fixed word length
j, errors accumulated from completed stages and the current partial stage
are `O_j(sum_(i=j)^k 16^i+k)`, while even the earliest time in stage k is
`N_(k-1)=4*16^((k-1)^2)`. Their ratio tends zero. Stage joins contribute only
O(j) each, and any exceptional first stages give a fixed finite error.

For k>=2, `N_(k-1)<2m_k`, so every digit compared from2m_k+1 through4m_k
belongs to stage k. The divisibility `16^k | 16^(k^2)` makes the two tails
equal for `3m_k-n` digits, including the case n=3m_k-1 where precisely one
digit is guaranteed. The bound `16^(-(3m_k-n))` is correct even when a tail
later uses the extreme digits0 or15. Its geometric sum is less than1/15.
Thus the fixed-h lag correlation tends1 although alpha is normal. The stated
restriction to prescribed temporal lags, rather than prime-clock orders,
is essential and correctly retained.

`energy_review.py` supplies a separate Hierholzer construction and exact
word counts for bases2,4,16 and orders1,2,3. It checks periodic alignment and
rational tail-sum bounds. These finite checks test the mechanism; they are
not presented as the proof of infinite normality.
