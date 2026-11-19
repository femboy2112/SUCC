# Hole contract: retain the boundary, then prove a signed source margin

## 1. Frozen object and success predicate

For every integer `n>=1`, retain exactly

```math
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
```

Let `x=pi/16`, `T_n=sum_(j>=1)16^-j r(n+j)`, and
`z_n={U_n+T_n}={16^n x}`. For every integer `B>=1`, define

```math
W_B(h)=B^{-1}\sum_{n=B}^{2B-1}e(hz_n),\qquad
\mathcal A_B=B^{-1}\sum_{n=B}^{2B-1}(1-\cos(2\pi z_n)).
```

**Weak target R0 (OPEN):** there exist `eta>0` and `B0` such that
`A_B>=eta` for every integer `B>=B0`. Full normality additionally requires
`W_B(h)->0` for every fixed nonzero integer h. No statement in this dossier
proves either target.

The existing terminal norm `B^-1 sum_(k=1)^B ||U_(2B)/16^k||_T^2` is an
equivalent R0 instrument after its inherited tail payment. Restating its
positive lower bound would be a reformulation, not a new proof step.

## 2. Cave map

| Field | Current object |
|---|---|
| Primary object | The original ordered rational BBP history and its completed real phases |
| Observable | Local prime registers, causal boundary state, cyclic source filters, and signed real Fourier averages |
| Mechanism | Exact rational recurrence, finite integer operator algebra, Mellin source factorization |
| Success predicate | A positive uniform all-integer-shell real anti-lock margin, then all fixed Fourier modes |
| Residual | Local heights, local Haar and positive filter energies coexist with real phase locking in admissible controls |
| Closure obstruction | Dropping the incoming state or quotient residual changes the object; retaining them still does not estimate the selected signed joining |

The obstruction is a **pathway gap** for the source-selected signed estimate.
There is now a decisive probe for the previously ambiguous boundary issue:
`H(S_8)K(S_8)=15I` versus `H(L_8)K(L_8)=16I`.

## 3. Candidate dependency cuts

Scores range from 0 to 5 and express research judgment, not truth probabilities.

| Candidate | Orthogonality | Falsifiability | Intrinsic value | Bridge potential | Verdict |
|---|---:|---:|---:|---:|---|
| Causal source filter with retained boundary and sharp local inverse cost | 4 | 5 | 4 | 3 | Selected; local theorem proved |
| Exact original 3-adic denominator growth | 2 | 5 | 3 | 2 | Already proved in repo; rederive and use for a new window corollary |
| Collatz valuation-word transport to a driven ternary register | 4 | 5 | 4 | 3 | Classical affine theorem plus sharp interface; no direct BBP theorem transfer |
| Declare real tripling invariance from local joint Haar | 1 | 5 | 1 | 1 | Refuted by inherited decoder/joining controls |
| Positive cyclic-filter energy forces real anti-lock | 1 | 5 | 1 | 1 | Refuted by the constant-phase control |

The selected object survives deletion of the current pi-normality strategy:
it is an independently meaningful theorem about causal versus cyclic
realizations of the same integer filter. It changes boundary conditions,
observable, and local inverse geometry. It is not equivalent to normality.
Its contribution is an exact interface/prohibition, not a claimed closure of
the asymptotic dependency edge.

## 4. The exact next signed joining obligation

Use the inherited unique primary decomposition in `Q/Z`. Put
`a_n=lambda_3(U_n)`, `b_n=[U_n]-a_n`, and `e(t)=exp(2 pi i t)`.
For each shell, define

```math
M_{3,B}=\mathbb E_B e(a_n),\quad M_{c,B}=\mathbb E_B e(b_n),\quad
\Gamma_B=\mathbb E_B[e(a_n)e(b_n)]-M_{3,B}M_{c,B}.
```

Then, exactly,

```math
\mathbb E_B e(U_n)=M_{3,B}M_{c,B}+\Gamma_B.
```

The original positive tail pays

```math
|W_B(1)-\mathbb E_B e(U_n)|
\le {2\pi\over B}\sum_{n=B}^{2B-1}T_n
\le {2\pi\over15B}\sum_{n=B}^{2B-1}r(n+1)=O(B^{-2}).
```

A sufficient, strictly stronger-than-R0 route would prove some fixed
`delta>0`, `B0`, and `epsilon_B->0` with

```math
|M_{3,B}|\le1-\delta,\qquad
|\Gamma_B|\le\delta/2+\epsilon_B
\quad(B\ge B_0).
```

It would imply `|W_B(1)|<=1-delta/2+o(1)` and hence R1 and R0. **Both source
estimates are OPEN.** Neither the height law nor the causal inverse theorem
proves them. The covariance identity is inherited elementary decomposition;
its novelty tax is unpaid as a new normality strategy. Its role here is to
name exactly which signed information the new observer must preserve.

The arithmetic variables `a_n,b_n` are synchronized components of one rational
state. They are not independent draws. The four-pole chronology, literal zero
seed, and incoming state must remain in any derivation of these bounds.
Extending this route to full normality requires all fixed h, not a growing
or selected finite set of frequencies.

## 5. Discriminating probes and receipts

### A. Causal record versus cyclic closure

**Inputs:** the exact coefficient polynomials H,K; nilpotent and cyclic
eight-dimensional shifts. **Predictions:** a boundary-free identification
predicts the same inverse arithmetic; the boundary-retaining frame predicts
16 versus 15. Integer matrix multiplication confirms the latter. Mutation:
change the final coefficient of H; the source and determinant certificates
must reject it.

### B. Original memory versus zero-initialized recent window

**Inputs:** authentic rational states and an exact trailing source window.
**Predictions:** uniform forgetting at both local places would make both
errors small; the proved transfer gives binary contraction and ternary error
`d3(U_(n-L))>(4/9)(n-L)` when `n-L>=1`. The full-history window is the null
control. Retaining the boundary is the positive reconstruction control.

### C. Local precision versus signed source authentication

A last-pole sign mutation preserves the observed denominator heights through
64, but fails the prescribed leading ternary unit at n=1. Height alone is
therefore an inadequate discriminator. The mutation is not the authentic
source and is never substituted for it.

### D. Constant real phase

For a constant channel vector, `H(S_m)1=15*1` and `Q(S_m)1=0`.
Invertibility/large H-energy therefore coexists with perfectly locked phase.
This kills the proposed inference from positive filter energy alone to R0.

### E. Finite local seed alias

Fix nonnegative K,L. Rational seeds
`s=2^K 3^L a/5^j`, with a integer, are dense in R. For every n,
`U_n(s)-U_n(0)=16^n s` has binary valuation at least K and ternary valuation
at least L. They are indistinguishable to those fixed-depth local difference
probes for all times. For any finite horizon M and real epsilon>0, density
allows `|x+s|<epsilon*16^-M`, giving completed phases within epsilon of zero
through M. This does not claim the rationally shifted endpoint is globally
nonnormal. It demonstrates finite locking and why the literal zero seed must
be authenticated separately. In particular, no p-adic value of irrational
pi is invented by this construction.

### F. Chronology in the Collatz comparison

The actual orbits `11->17->13` and `9->7->11` have valuation words `(1,2)`
and `(2,1)`, respectively. Equal totals and equal slopes coexist with distinct
terminal residues modulo9. The last-m theorem provides the positive control;
the all-ones infinite word (limit -1 in Z2) tests the positive-integer boundary.

### G. Exact cycle complexity versus real shadowing

Write `U_n=A_n/B_n` in lowest terms. Its autonomous radix-16 period is
`ord_(B_n)(16)>4n/27`. But `z_n=1/B_n` has the identical full denominator
and identical autonomous period while tending to zero, with shell anti-lock
energy at most `81*pi^2/(8B^2)`. This is an explicitly altered-forcing
zero-seeded sequence. It refutes the shortcut from denominator or exact
period growth alone to real anti-lock; it does not refute a theorem using
the complete original signed four-pole chronology.

## 6. What would change the verdict

The next successful step must produce an original-source inequality for the
signed joining, or another bound with a checked implication to R0, that
rejects the retained altered-forcing and local-alias controls. A new cyclic
factorization, a larger finite sample, or a better local height bound by
itself does not change the asymptotic verdict.

Before any subsequent attack: reread the live frontier, this operation's
source audit, and the donor #664 counterfeit receipts. Keep the canonical
source and actual forward boundary, declare the exact signed observable and
all-B quantifiers, pre-register the cheapest control that can kill it, and
work on one missing inequality. If it fails, preserve its counterexample.
