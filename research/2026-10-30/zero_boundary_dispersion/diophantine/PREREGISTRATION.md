# Diophantine front: preregistration

Pinned starting head: `5f350af7808532e55d74e80c948c02bb385c6e70` (PR #403).
Owned scope: this directory. Original source and zero seed are not edited.

Candidates declared before execution:

| ID | Precise candidate | Prediction / fail / ambiguous |
|---|---|---|
| DP-01 | The #403 no-wrap mechanism holds uniformly for `1<=abs(h)<=A^3/6` once A exceeds one constant, not a separate h-dependent threshold. | Prove with one published Diophantine constant and exact cubic tail. Fresh authentic exact windows A=19,37,61 and h at low, middle, and top of the band must contain a distance >=1/20. Any finite failure is evidence about thresholds only, not an asymptotic refutation. |
| DP-02 | Simultaneously allow lag `1<=ell<=A/26`, `abs(h)*ell<=A^3/6`, using the same [A,8A) window and threshold. | Derive exact denominator/time tradeoff. Test longer lags on fresh A=53,79,107. Falsify algebra with direct rational lag calculations. |
| DP-03 | beta_m=sum_{j>=0}16^(-m^j), every integer m>=3, has exact irrationality exponent m and total lag-energy O(log N), including after original BBP Green-tail transport. | Prove elementary rational separation and summable digit contributions. Exact intervals m=3,4,5, N=3^j or fresh mixed horizons should show sparse slips. Any derived bound failure kills the stated constant; finite success cannot prove irrationality exponent. |
| DP-04 | A finite family of frequencies/lags or rational periodic targets cannot force superlogarithmic slip count from finite exponent plus Green correction alone. | Use the same DP-03 countermodel and rational affine translations. Check all h=1,3,7,11, ell=1,2,5 simultaneously. Normal controls need not fail. |
| DP-05 | Sparse finite-exponent controls can have unbounded coherent windows of length proportional to their start, despite logarithmic global energy. | Produce exact rational enclosures strictly below 1/20 for declared m=3/4/5 windows. Failure refutes that window specification, not finite-mu theorem. |
| DP-06 | The integer no-wrap core admits a small Lean 4 proof without axiomatizing the conclusion. | Run actual available compiler. If no real/analytic library is available, formalize only denominator-cleared finite integer lemma and label its narrower scope. No asserted formalization of irrationality input or infinite theorem. |

Independent computations must not import the primary probe module. Same-model proof review is not an independent referee. The published input is Zeilberger–Zudilin 2020, not 2026 claims. Primary sources and full proof boundaries go in THEOREMS.md.

## Added before Kempner execution

DP-08: Reconstruct Shallit's published 1979 folding law for
`B(u,v)=sum_(j=0)^v u^(-2^j)`. For u>=3, predict exact equality between the
folding construction and an independent Euclidean continued fraction; for
v>=2 all partial quotients after a0 lie in `{u-2,u-1,u,u+2}`. Declare u=3,5,16,19
and v=2,...,10 as fresh checks. A mismatch refutes the implementation or stated
fold; finite success is not the universal theorem. At u=16 the published
bounded-partial-quotient result gives mu(beta_2)=2. The analytic digit budget
then predicts O(log N) deviation despite this strongest finite irrationality
exponent. Certify all-index coherent windows j=5,8,11 separately. No pi
exponent-two claim is assumed.
