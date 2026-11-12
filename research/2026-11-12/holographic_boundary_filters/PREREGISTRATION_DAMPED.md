# Follow-up contract: damped grade filters

2026-11-12, after the first constructor/adversary round. This is a
preregistered *continuation*, not a rewrite of the initial protocol.

The arithmetic audit found the fixed quadratic lower bound positive at
only nine midpoints in `2..257`. That test was an exploratory diagnostic,
not evidence for an all-midpoint theorem. The next object is a bounded-mass
histogram on arbitrary **integer** grades, observed through its Laplace
responses `F(t)=sum_h c_h t^h`.

Proposed theorem: for even `d>=2`, `0<t<=1/2`, let
`Q(z)=z product_(j=1)^(d-1)(z-t^j)/product_(j=1)^(d-1)(1-t^j)`.
Then `Q(1)=1`, `Q(t^h)=0` for `1<=h<d`, and for every integer `h>=d`,
`-t^[d(d+1)/2]<=Q(t^h)<=0`. If `Q(z)=sum_(r=1)^d a_r z^r`, its response
is a lower bound for `c_0`, its downward error is at most
`M*t^[d(d+1)/2]`, and `sum|a_r|<9` uniformly in `d,t`.

The universal proof must pay discrete grades, even degree, the `t<=1/2`
domain and a known finite mass. It must not require a finite grade ceiling.
The arithmetic application must retain the real `Omega` source. Measuring
the needed responses is a separate task, not a free oracle or a proved
speedup over direct primality.

Frozen finite arithmetic evaluation: midpoints `10,257,509,1021,2053,4099`,
degrees `2,4,6`, and `t=1/2`. Report every combination, including negative
bounds. Use no count-dependent degree tuning. Independent verification
should use a sieve for `Omega`/primality against the simple trial-factor
builder. Tests cover all small nonnegative histograms, arbitrarily higher
test grades, exact interval noise and count recovery.

Required falsifiers: odd degree claimed as lower bound; `t>1/2` with the
same alleged leakage; fractional grade between zero and one; absent mass
budget; omitted response uncertainty; claiming analytic estimates from
finite exact moment enumeration. These controls should fail the overclaim,
not the properly scoped theorem.

If true, this produces a stable approximate zero-sector projector and a
useful next bridge for the existing Borwein grade filters. If the new family
is already in the repository/literature, record its provenance and keep the
new quantitative comparison and validation only. No scholarly priority
claim. Goldbach and the BBP signed statistical obligations remain OPEN.
