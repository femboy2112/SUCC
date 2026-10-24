# Joint observer interactions and trimmed BBP collision bounds

**Date:** 2026-10-24. **Parent:** draft #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
**Authority:** elementary paper proofs and exact finite calibration. No new
Lean declaration, external refereeing, or proof of pi normality.

This dossier keeps every joint interaction, allows a vanishing exceptional
set of actual source positions, and proves the resulting finite entropy
budget. It extends the inherited [SCE-02 entropy bridge](PI_SOURCE_COLLISION_ENTROPY.md)
without treating a selected subset as a stationary orbit.

Code: [joint_observer_entropy.py](../../observational_succ/joint_observer_entropy.py).
Tests: [test_joint_observer_entropy.py](../../tests/test_joint_observer_entropy.py).
Probe: [joint_observer_entropy_probe.py](../../scripts/joint_observer_entropy_probe.py).
Receipt: [PI_JOINT_OBSERVER_ENTROPY_RECEIPT.json](PI_JOINT_OBSERVER_ENTROPY_RECEIPT.json).

## 1. The exact joint quantity

Let P be a probability on length-d words over b symbols. Let P_k(v) be
its prefix marginal and set

$$
C_k=b^k\sum_{|v|=k}P_k(v)^2,\qquad C_0=1.
$$

For P_k(v)>0, define the actual conditional law and collision-weighted
prefix law

$$
q_v(a)=\frac{P_{k+1}(va)}{P_k(v)},\qquad
\xi_k(v)=\frac{P_k(v)^2}{\sum_uP_k(u)^2}.
$$

**Exact factorization.** Direct expansion gives

$$
\frac{C_{k+1}}{C_k}
=b\sum_v\xi_k(v)\sum_aq_v(a)^2
=1+\mathbb E_{\xi_k}\chi^2(q_v\Vert u_b).
$$

Therefore

$$
\boxed{\log C_d=\sum_{k=0}^{d-1}
\log\!\left(1+\mathbb E_{\xi_k}\chi^2(q_v\Vert u_b)\right).}
$$

Every term is nonnegative. A subexponential collision bound means that the
mean of these conditioned defects tends to zero. The law used to weight a
prefix is its squared mass, normalized; replacing it by a uniform prefix
or by a product of separate observer marginals changes the statement.

This is a precise interpretation of using all observers together. It is
not an independence premise. Actual earlier observations remain in each
conditional law.

### A correlated reference is allowed

Let R be any probability on the same history space with P absolutely
continuous with respect to R. Define

$$
M_k=\sum_v\frac{P_k(v)^2}{R_k(v)},\qquad
\zeta_k(v)=\frac{P_k(v)^2}{R_k(v)M_k}.
$$

Terms with P_k(v)=0 are omitted. Expanding one further level gives

$$
\boxed{\frac{M_{k+1}}{M_k}
=1+\mathbb E_{\zeta_k}
\chi^2\!\left(P(\cdot\mid v)\Vert R(\cdot\mid v)\right).}
$$

Here R may itself have Pascal, Lucas, prime, or other coherent dependencies.
No product reference is silently substituted. If a proved finite decoder F
maps observer histories to carries, fiberwise Cauchy--Schwarz gives

$$
\sum_c\frac{(F_*P)(c)^2}{(F_*R)(c)}
\le\sum_v\frac{P(v)^2}{R(v)}.
$$

Indeed, on each fiber,

$$
\left(\sum_{F(v)=c}P(v)\right)^2
\le\left(\sum_{F(v)=c}R(v)\right)
\left(\sum_{F(v)=c}\frac{P(v)^2}{R(v)}\right).
$$

If F_*R is the uniform carry law, this bounds the carry collision excess.
The actual observer-to-carry map, its reference pushforward, and the joint
bound still have to be established for the BBP source. The identity is not
that missing arithmetic estimate.

### Hostile controls

A uniform even-parity law on four bits has every one-, two-, and three-bit
coordinate marginal uniform, but C_4=2. Its conditional ratios are
`(1,1,1,2)`. Independent repetitions of this four-bit law have
C_(4r)=2^r. Thus an interaction invisible to every proper within-block
marginal can accumulate at a positive density of levels.

The held-out base-5 law on triples a+b+c=0 modulo 5 has all two-coordinate
marginals uniform, C_3=5, and conditional ratios `(1,1,5)`. A deliberately
false product-of-marginals calculation returns 1 and is rejected by the
exact tests.

These are laws on declared finite words, not counterfeit claims about the
authentic BBP source. Their purpose is to distinguish full joint information
from separate marginal information.

## 2. A trimmed finite entropy bridge

Take an infinite word on b symbols and N consecutive starting positions
`0,...,N-1`. Its length-d block law uses the actual d-1 future digits after
the last start. Let G be any nonempty subset of those starting positions,
and let

$$
\delta=1-\frac{|G|}{N},\qquad
q_d(w)=\frac1{|G|}\#\{n\in G:\text{the d-block at n is w}\},
\qquad C_G=b^d\sum_wq_d(w)^2.
$$

Write p_(N,k) for the k-block law on **all N original starts**. Put
q=floor(d/k), t=d/N, and assume 1<=k<=d and t<=1/2. Then

$$
\boxed{
D(p_{N,k}\Vert u_{b^k})
\le
\frac{\delta d\log b+(1-\delta)\log C_G}{q}
+h_2(t)+t\log(b^k-1).
}
$$

All logarithms are natural and h_2 is binary entropy. A max-mass estimate
`max_w q_d(w)<=A b^-d` permits replacing log C_G by log A.

### Proof, with the original window retained

The full d-block law decomposes as

$$
p_{N,d}=(1-\delta)q_d+\delta r_d.
$$

If delta=0 the second component can be any law. Concavity and nonnegativity
of entropy, followed by Shannon/Renyi comparison, give

$$
H(p_{N,d})\ge(1-\delta)H(q_d)
\ge(1-\delta)(d\log b-\log C_G).
$$

Now split each **full-window** random d-block into q adjacent k-blocks and
a remainder. At internal offset jk, the short-block law differs from
p_(N,k) by total variation at most jk/N<=d/N: the two consecutive start
windows differ only at their ends. Entropy continuity and subadditivity give

$$
H(p_{N,d})\le qH(p_{N,k})
+q[h_2(t)+t\log(b^k-1)]+(d-qk)\log b.
$$

Combining proves the displayed inequality. **No shift-invariance statement
was made about G.** An arbitrary retained subset can have a completely
different short-block law; the implementation returns the original-window
law and tests this explicitly.

Pinsker's inequality then bounds the fixed k-block total-variation defect
by the square root of half the displayed right side.

### Sufficient asymptotic condition and its precise strength

If, through every large N,

$$
d(N)\to\infty,\quad d(N)=o(N),\quad
\delta(N)\to0,\quad \frac{\log C_{G_N}}{d(N)}\to0,
$$

the original word is normal. If q_d is an empirical law on at most N
positions, its diagonal gives C_G>=b^d/N. The collision premise then
forces d<=(1+o(1))log_b N, so the explicit d=o(N) condition is automatic.

This is a sufficient counting criterion. At an unspecified source-adapted
slow depth it recovers an equivalence to normality; at a prescribed growing
depth it has additional quantitative content. SCE-03 already proves that
a normal word need not satisfy an untrimmed collision estimate at a fixed
logarithmic depth. No new normality theorem is obtained until a source
estimate supplies the premise.

### Rare hotspots separate Shannon information from L2 collision

For d>=2 consider the finite law

$$
p_d=(1-1/d)u_{b^d}+(1/d)\delta_{0^d}.
$$

Discarding mass 1/d leaves the exactly uniform law. Its normalized Shannon
entropy deficit is at most (log b)/d. Nevertheless its untrimmed collision is

$$
C(p_d)=1+\frac{b^d-1}{d^2},\qquad
\frac{\log C(p_d)}d\to\log b.
$$

Thus trimmed collision control is materially less demanding than untrimmed
diagonal collision control in the presence of a vanishing rare concentration.
This is a family of finite laws, with an exact receipt, not a claim of a
single consistent infinite process with this formula at every depth.

## 3. Authentic BBP transport costs only a factor two

Keep the literal BBP source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad y_n=\{U_n\}.
$$

For alpha=pi/16 the inherited positive-tail theorem gives

$$
x_n=\{16^n\alpha\}=y_n+T_n\pmod1,\qquad
0<T_n<B_n=\frac1{(8n+1)(8n+2)}.
$$

Partition the circle into M=16^d equal cells and retain only positions with
B_n<=1/M. On the retained source law, let a_j be the mass staying in cell j
and b_j the mass advancing from j to j+1. The strict tail bound means no
other destination is possible. Indices are cyclic. Thus

$$
q_j=a_j+b_j,\qquad p_j=a_j+b_{j-1},
$$

and

$$
\boxed{M\sum_jp_j^2
\le2M\sum_j(a_j^2+b_j^2)
\le2M\sum_jq_j^2.}
$$

The reverse factor-two inequality follows by viewing each target cell's
mass as split between at most two source cells. The forward bound is the
one used here. It preserves circular wrap and the positive displacement
lift. Merely comparing the endpoints modulo one does not authorize a
larger physical displacement.

The bound is sharp: two equal masses from neighboring cells can coalesce
into one cell. If shifts across two cells are allowed, three equally
weighted cells can coalesce, giving collision ratio 3; the exact instrument
rejects that changed hypothesis.

### An exact deterministic trimming cutoff

Let

$$
L_d=\min\{n\ge0:(8n+1)(8n+2)\ge16^d\}.
$$

It satisfies

$$
L_d=\max\!\left(0,
\left\lceil\frac{\sqrt{1+4\cdot16^d}-3}{16}\right\rceil\right)
=O(16^{d/2}).
$$

The implementation computes the minimum with integer square root and an
exact final inequality, avoiding floating-point threshold decisions.

For a prefix of N authentic positions, take G within `{L_d,...,N-1}`,
possibly discarding additional positions of vanishing density. If the
source collision is C_source, the true d-block collision on G is at most
2 C_source. The finite entropy bound becomes

$$
D(p_{N,k}^{\pi}\Vert u_{16^k})
\le\frac{\delta d\log16+(1-\delta)\log(2C_{\rm source})}
{\lfloor d/k\rfloor}
+h_2(d/N)+(d/N)\log(16^k-1).
$$

Consequently a subexponential bound for the retained authentic source
collision suffices. Its diagonal forces d<=(1+o(1))log_16 N, and then the
mandatory initial trimming has size N^(1/2+o(1)), hence vanishing density.
Neither the factor two nor this cutoff requires a conjecture about carries.
The missing estimate is the retained **actual source collision** itself.

## 4. Verification and what remains open

The tests check exact correlated-reference chains, decoder contraction,
proper-marginal parity countermodels, rare-hotspot formulas, arbitrary
retained subsets, original-window entropy bounds by integer powers of
rationals, one-cell transport with weights and wrap, a two-cell mutation,
and exact minimal BBP cutoffs. The independent probe also reconstructs
literal BBP rational states and certifies true-cell labels from a rational
Machin enclosure, preserving the tail and carry domains.

The finite code checks are calibrations of these paper lemmas. They do not
test all asymptotic horizons or prove a rate for the authentic source.
In particular, no conditional independence of Pascal/Lucas/prime observers
has been established. The conditioned joint defects and retained source
collision bounds remain OPEN.
