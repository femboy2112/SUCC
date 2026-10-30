# Operation Frame-Reset Crucible — arithmetic source, normal systems, choice and selected transport

**Source scope:** original SUCC BBP source remains `R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)`, `r(n)=R(8n-7)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`. Main XVI and the research-only spacetime PRs #390–#393 are contextual, not mathematical authorities for the separate Stoneham source. Base-16 normality of π and RH remain **OPEN**. All new number-normality arguments below recover known classical results, not academic novelty.

## FR-01 — an exact arithmetic choice / observer / reset triple

Let the circle be `X=R/Z`, with deterministic radix map `T(x)={16x}`. The digit selected by an arithmetic point is `d(x)=floor(16x)`: unlike a random sampler, T has no unspecified choice once x is fixed. For a finite hexadecimal word w of length k, write its integer value as `[w]_16` and the half-open cylinder

```
C_w = [[w]_16 / 16^k, ([w]_16+1)/16^k).
```

The inverse-branch map `g_w(y)=([w]_16+y)/16^k` satisfies `T^k(g_w(y))=y` and the exact concatenation `g_u o g_v = g_(uv)`. For an observer measure mu with `mu(C_w)>0`, define the **chosen measurement and recentering**

```
R_w(mu) = (T^k)_*( mu|_(C_w) / mu(C_w) ).
```

This is epistemic conditioning plus coordinate reset, **not** an arithmetic operation that changes the selected number, and not the auxiliary BBP `mu_a` unless a coupling is explicitly declared. The observer's policy may select which word/partition to inspect; it cannot change the deterministic outcome of the source. A choice policy depending on n or information about future digits can strongly bias the selected sample, even when the number is normal.

For Haar m, `m(C_w)=16^-k` and `m(C_w intersection (T^k)^-1 I)=16^-k*|I|`, so `R_w(m)=m` exactly. For a deterministic normal α, the empirical laws `nu_N=N^-1 sum_(n=0)^(N-1) delta_(T^n α)` converge to Haar, and thus `R_w(nu_N)` converge to Haar **for each fixed w** (continuity sets, nonvanishing denominator). This does not guarantee uniformity in moving words of length growing with N.

### Reset-fixed-point theorem / countermodel

Assume a Borel probability measure mu gives positive mass to every finite cylinder and satisfies `R_w(mu)=mu` for every word w. Then for all words w,v,

```
mu(C_(wv)) = mu(C_w)*mu(C_v).
```

Indeed the left side divided by `mu(C_w)` is `R_w(mu)(C_v)=mu(C_v)`. Setting `p_d=mu(C_d)`, induction gives `mu(C_(d1...dk))=prod p_di`; hence mu is a full-support i.i.d. Bernoulli digit measure. Conversely every such product law is reset-invariant. It need NOT be Haar: e.g. `p_0=1/2`, `p_1=...=p_15=1/30` has exact reset invariance and is nonuniform. Invariance under *all* reset maps selects the Bernoulli class, not the uniform member.

## FR-02 — explicit Stoneham base-16 source

For c in {3,5}, define the classical known-normal Stoneham constant

```
alpha_(16,c) = sum_(p>=1) 1/(c^p*16^(c^p)),
x_n = {16^n alpha_(16,c)},
z_0=0,
z_n = {16 z_(n-1) + 1_(n=c^p)/c^p}.
```

Here z_n includes *only* impulses whose source birth index c^p is at most n. The full orbit x_n is deterministic and differs from z_n by an explicitly bounded positive future-pulse remainder; no random digit source is posited. At arithmetic stage `c^p<=n<c^(p+1)`, put `q=c^p`:

```
z_n = a_n/q,  a_n ≡1 (mod c),
a_(c^p+k) ≡16^k a_(c^p) (mod c^p).
```

The first congruence is exact because at the birth time n=c^p the newest contribution is `1/c^p`, and all earlier contributions, multiplied by c^p, are divisible by c. Since c|15=16-1 and `v_c(16-1)=1`, LTE gives

```
v_c(16^m-1)=1+v_c(m),
ord_(c^p)(16)=c^(p-1).
```

The orbit under multiplication by 16 therefore visits the whole residue subgroup `1 mod c` (of size `c^(p-1)`) once per period. This stage has length `(c-1)c^p = c(c-1)*c^(p-1)`; **each of those residues is visited exactly c(c-1) times**. For c=3 this is six traversals; c=5 twenty.

### Exact future-tail enclosure

For n in stage p, define the true-vs-surrogate circle displacement

```
delta_n = sum_(k>p) 16^(n-c^k)/c^k > 0.
```

Since `n<=c^(p+1)-1`, every term has radix factor `16^(n-c^k)<=1/16`, yielding the *uniform exact* bound

```
0<delta_n<=1/(16*(c-1)*c^p) =: epsilon_(c,p).
```

In particular `x_n={z_n+delta_n}`. This is an authenticated rational-conductor bridge between a **true** pure digit orbit and source arithmetic, not a fitted approximation to digit frequencies.

## FR-03 — all-horizon bounded-occupancy theorem (known normality recovered)

Let `A_N(I)=#{0<=n<N : x_n in I}` for any half-open circle interval I of length `ell`. For every N>c, let `P=floor(log_c(N-1))` (so `c^P<=N-1<c^(P+1)`). Then

```
A_N(I) <= c*N*ell + 3*c*(c-1)*P + c.       (BOUND-HS)
```

**Finite proof:** The first c indices contribute at most c. In any subsequent full or partial stage p, the z_n lie on the equally spaced circle grid `(1+c*j)/c^p`, j=0,...,c^(p-1)-1, with grid spacing `1/c^(p-1)`, and each possible grid point occurs at most `M=c(c-1)` times. If x_n enters I, z_n lies in the epsilon-neighborhood of I. That enlarged arc meets no more than `c^(p-1)*(ell+2 epsilon)+2` grid points; because `c^(p-1)*2epsilon=1/(8*c*(c-1))<1`, a convenient integer upper bound is `c^(p-1)*ell+3` points. Hence the stage contributes at most

```
M*(c^(p-1)*ell+3)=(c-1)c^p*ell+3c(c-1).
```

Sum stages p=1,...,P, including the possibly incomplete last one. Since `sum_(p=1)^P (c-1)c^p=c^(P+1)-c<=c*N`, BOUND-HS follows. This is uniform in I, N, and the position of I; only its length enters.

**Why coefficient c, not 1, is enough.** Define empirical probabilities `nu_N=N^-1 sum_(n<N)delta_(T^n alpha)`. Every weak-* subsequential limit nu is T-invariant (telescoping of the empirical measure under the circle map T). The uniform upper-bound BOUND-HS implies `nu<=c*m` as measures: approximate any nonnegative continuous test function from above by a finite step function on short intervals and let N→infinity. Hence `nu` has an L^infinity density. For each integer h,

```
nu_hat(h)=nu_hat(16h)=nu_hat(16^k h)  for all k>=0.
```

The Riemann–Lebesgue lemma for the L^1 density forces `nu_hat(h)=0` for h!=0. Thus nu=m. All subsequential limits are m, so nu_N→m; both constants `alpha_(16,3)` and `alpha_(16,5)` are normal to base16. This is a classical fact already proved by Bailey–Crandall; our elementary derivation is a **calibrated source-to-selection certificate**.

### A certified full-stage signed Fourier bound

The rational surrogate has the exact complete-stage character sum

```
Sum_(n=c^p)^(c^(p+1)-1) exp(2*pi*i*h*z_n)
  = (c-1)*c^p*exp(2*pi*i*h/c^p) * 1_[c^(p-1) divides h].
```

Proof: each residue `1+c*j` has multiplicity `c(c-1)`; the finite geometric character sum over j is zero unless its modulus divides h. For h not divisible by `c^(p-1)`, the rational surrogate sum is **exactly zero**, while the authentic infinite-orbit sum has absolute value at most

```
2*pi*|h| * sum_(stage p)delta_n
  <=2*pi*|h|*(c-1)c^p*epsilon_(c,p)=pi*|h|/8.
```

This source-specific bound controls **complete** conductor stages. Partial-stage Fourier sums can be large: the all-horizon BOUND-HS and invariant-density argument are what upgrade it to normality. A stagewise Fourier identity alone is insufficient.

## FR-04 — a matching nonnormal source grammar: conductor c=2

Take `alpha_(16,2)=sum_(p>=1)1/(2^p*16^(2^p))`. Exactly,

```
1/(2^p*16^(2^p)) = A_p / 16^(J_p),
J_p=2^p+ceil(p/4),  A_p=2^(4ceil(p/4)-p) in {1,2,4,8}.
```

The J_p strictly increase, so no digit overlap or carry occurs: the expansion has one isolated nonzero digit at each J_p, and the number of nonzero digits up to N is O(log N), density zero. This is **proved nonnormal** to base16. The same series grammar is normal for c=3 or5; the distinction lies in the modular unit/conductor action, not in the mere existence of source pulses or a local observer triangle. The prime 2 is not invertible modulo the radix 16; it cannot support the 3/5 subgroup argument.

**Source-signature caution:** 2,3,5 are also the exceptional reduction primes of the authentic BBP rational map, and `16-1=3*5=15=Q_BBP'(0)`. These are exact arithmetic equalities but **no theorem identifies Stoneham's conductor cycles with the original BBP prime passport or π's selected carry dynamics.** They are experimentally valuable comparison classes, not transported proofs.

## FR-05 — one-step reset is not enough (de Bruijn and biased Bernoulli)

The periodic order-two de Bruijn cycle on 16 digits has period 256 and each ordered digit pair `(d,e)` occurs exactly once per cycle. Therefore every digit d appears 16 times and, conditioned empirically on a *single* preceding digit d, all 16 possible next digits have exactly one occurrence: perfect one-step fair resetting. Yet only 256 three-digit cyclic blocks can appear out of 4096, so the periodic sequence is nonnormal. This is a precise finite-memory test of the 'one triangle should imply normality' overclaim.

The full-support biased Bernoulli measure from FR-01 passes **every-word** reset invariance despite having a biased first digit. This is an independent failure mode. Lastly the computable base-16 Champernowne concatenation is a known normal sequence, but an observer permitted to compute its next digit from n can choose only future zero positions and thereby produce a biased selected subsequence. Therefore the chosen observation policy, admissible memory, and any nonanticipation assumption must be declared. Normality of a fixed sequence does not mean algorithmic unpredictability or that arbitrary selection policies preserve normality.

## FR-06 — a portable certificate for SUCC's *selected* rational BBP carrier

**Grid-occupancy lemma (sufficient, not necessary).** Let `x_n={b^n alpha}` be a pure radix orbit. Partition all sufficiently large times into consecutive finite blocks B_k. Suppose there are source-authenticated surrogates z_n, uniformly spaced grids of size q_k (possibly translated), max visits M_k at each grid point during block k, and circle errors `dist(x_n,z_n)<=epsilon_k` on block k. Then for every arc I of length ell and any N,

```
A_N(I) <= initial_count + sum_(k touching [0,N))
                   M_k*( q_k*ell + 2*q_k*epsilon_k + 2 ).
```

If uniformly in N the total grid budget `sum M_k*q_k <= C*N` and the edge/error budget `sum M_k*(1+q_k epsilon_k) = o(N)`, then `A_N(I)<=C*N*ell+o(N)` for all arcs, and by the invariant-density argument the selected number alpha is b-normal.

Stoneham supplies these hypotheses **arithmetically**: `q_k=c^(k-1)`, `M_k=c(c-1)`, `epsilon_k=1/[16(c-1)c^k]`. This is exactly the certificate we have just calibrated, not an empirical estimate fitted to its digits.

For the genuine BBP selected orbit, the rational phases `z_n={U_n(0)}` are exact, and the known original source tail gives `dist({16^(n-1)pi}, z_n)<=T_n<(8n+1)^(-2)`. So the **arithmetic approximation/precision leg is already present**.

What is **not** present is an authenticated all-horizon family of grids/denominator stage packets with `sum M_k q_k=O(N)` and sublinear edge cost. Original rational `U_n` denominators vary with n, and source positivity/finite Gamma/Oily operators do not prove bounded visits for selected phases. A candidate π theorem requires deriving those budgets (or a genuinely stronger alternative) from the four signed poles and zero seed, not assuming the selected phases are random. The same-source coherent counterseed `s=-pi/16` must violate a claimed universal grid-occupancy theorem because its pure orbit is nonnormal.

The certificate is a **constructible pathway** and a proposed new SUCC interface. It is not a signed π Weyl estimate, does not prove π normality, and cannot be obtained from the positive virtual field alone. Its Stoneham and c=2 controls distinguish genuine arithmetic transport from source-blind cancellation.

## FR-07 — what the 'human T-action' means after calibration

There are three different typed maps, not one ambiguous 'choice':

1. **Arithmetic actualization:** the source/initial boundary determines an actual number and therefore its unique radix-digit path `x_n`, with `T(x_n)=x_(n+1)` for the pure orbit. There is no stochastic choice of digits just because an observer represents alternatives.
2. **Observer instrument/choice:** a policy chooses a cylinder, refinement, stopping rule, or statistic. The policy may itself depend on previously observed digits, current n, or a declared external input. This changes *what gets measured* and can introduce selection bias. An omniscient/predictive choice is not equivalent to a bounded-memory fixed-word observation.
3. **Epistemic conditioning and frame reset:** `R_w` pushes the conditional law to the new zero-relative coordinate. Haar is a fixed point, biased product laws are fixed points too, and a deterministic normal trajectory realizes Haar only in fixed-word, time-empirical limits.

Thus the 'zero-relative virtual field of the realized endpoint' is a **posterior chart**, while the arithmetic source supplies the realized endpoint. A new law gluing these must be source-derived. In a normal system, the observer may learn a specific digit while finding *zero change to the limiting recentered uniform law*; this is not zero information gain about history and is not quantum wavefunction collapse.

## Provenance and literature

- Bailey and Crandall, *Random Generators and Normal Numbers*, Experimental Mathematics 11 (2002): https://www.tandfonline.com/doi/abs/10.1080/10586458.2002.10504704 (normality of Stoneham `alpha_(b,c)` for coprime b,c).
- Bailey and Misiurewicz, *A Strong Hot Spot Theorem* (2006): https://escholarship.org/uc/item/2bp7q4b2 (normality ⇔ no arbitrarily concentrated orbit hot spot).
- Champernowne, *The Construction of Decimals Normal in the Scale of Ten* (1933), https://doi.org/10.1112/jlms/s1-8.4.254 (historical construction; base-16 analogue classical).
- Main XVI `docs/OPERATIONAL_TRIANGLE.md`; related but unmerged source research PRs #390–#393; SUCC `research/2026-10-29/OILY_STONEHAM_PATH_SHEET.md` (earlier base-2 Stoneham control).

**Claims inheritance firewall:** published external normality, elementary independently derived paper identities, exact finite checks, and hypothetical π transfers are different authority levels. No external originality or Lean authority is asserted. Main and historical proof contracts remain untouched.

### FR-06b — naive 'copy Stoneham's 3/5 conductor' transfer is refuted at finite depth

Original `U_n(0)` is an **exact rational** number at every n, but not the same source rational grid. As a deliberately hostile finite check, partition `[0,1)` into the `c^(p-1)` *equal bins* used by the respective Stoneham unit-subgroup grid and count the original BBP rational phases `frac U_n` at the corresponding stage times `c^p<=n<c^(p+1)`.

- For `c=3,p=2` (n=9..26), the three BBP bin counts are exactly `(9,7,2)`, versus Stoneham's `(6,6,6)` **residue** multiplicities.
- For `c=3,p=3` (n=27..80), the maximum BBP bin count is 13, versus Stoneham's exact residue multiplicity 6.
- For `c=5,p=2` (n=25..124), maximum BBP bin count is 23, versus Stoneham's exact residue multiplicity 20.

All counts are computed from the *unchanged four signed rational poles* with exact Fraction arithmetic. **This does not refute the possibility of future, different BBP grids or equidistribution;** it refutes the naive claim that the original selected carrier already inherits Stoneham's literal 3/5 modular stage multiplicities just because its resultant/discriminant involve 3 and 5. The calibration must lead to a source-derived new arithmetic certificate, not a presumed identification.
