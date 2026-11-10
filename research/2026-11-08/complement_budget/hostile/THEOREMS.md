# Complement-budget hostile theorems

**Status: PROVED PAPER for the stated finite identities and inequalities.**
These results delimit approximation mechanisms, not normality. The source is
the original four signed poles, literal `U0=0`, unwrapped recurrence and actual
prime principal parts. No global theorem, worldwide novelty or Lean authority
is claimed. PR1–8 are read at parent `95d9860de3a52ab76c1a0719e170b609759b17b9`.

## HCB1. The authenticated clean clock has an even number of repeats

For every prime `p=1 mod8`, put `m=ord_p(16)` and `L=(p-1)/4`.
Then `m | (p-1)/8`, so `q=L/m` is a positive even integer.

**Proof without an imported reciprocity theorem.** Write `p=8k+1`. The
least absolute representatives of `2,4,...,p-1` have absolute values that
permute `1,...,(p-1)/2`: two would collide only if their original indices
were equal or summed to p, and the latter is impossible. Exactly
`(p-1)/2-floor(p/4)=2k` representatives are negative. Multiplying and
cancelling the nonzero factorial gives `2^((p-1)/2)=1 modp`. Thus
`16^((p-1)/8)=1 modp`, and the multiplicative order divides this exponent.

The stronger PR1 selector gives no lower bound tending to infinity for q.
Finite eligible q=2 clocks exist (see receipt). An assertion of infinitely
many such selected clocks is **not** made. In particular, a folding argument
must not silently assume that its number of replicas grows.

## HCB2. A positive original-source floor for two-replica model error

Let p be a clean source prime with `L=2m`, `n0=L+1`, and h any nonzero integer.
Let `a_n=e(h[U_n]_p)` be the authenticated zero-source prime character on
`I={n0,...,n0+2m-1}`, and `b_n=e(hU_n)/a_n`. Its folded complement is

`B_r=(b_(n0+r)+b_(n0+r+m))/2`, `0<=r<m`.

The empirical L1 error of the zero predictor obeys the unconditional bound

```
mean_r |B_r| >= (m-1)/(17m)
 - pi |h|/(17m) * sum_(n=n0)^(n0+m-2) |r(n+m+1)-r(n+1)|.       (H1)
```

In particular,

```
mean |B| >= (1-1/m)/17 * (1-15 pi |h|/(8n0+1)^2).             (H2)
```

For fixed h this is `1/17-O(1/m+|h|/L²)`. The L2 error of zero is at
least the same positive lower bound. This is a finite source-forcing
restriction on an actual approximation error, **not** a signed Weyl lower
bound. It does not prevent accurate nonzero predictors.

**Proof.** Periodicity of a gives
`|B_r|=|1+v_(n0+r)|/2`, where `v_n=e(h(U_(n+m)-U_n))`. The literal recurrence
implies

`v_(n+1)=v_n^16 e(h(r(n+m+1)-r(n+1)))`.

For every unit z, factoring `1-z^16=(1+z)sum_(j=0)^15(-z)^j` gives
`|1-z^16|<=16|1+z|`. Since
`2<=|1-z^16|+|1+z^16|`, and `|e(t)-1|<=2pi|t|`, with `c_n=|1+v_n|`,

`2<=16c_n+c_(n+1)+2pi|h| |r(n+m+1)-r(n+1)|`.

Sum over the m-1 internal edges. The c terms are at most
`17 sum_(n=n0)^(n0+m-1)c_n`; divide by `34m` to obtain H1. No edge across
the next p-pole is used. The exact positive anchored decomposition

`r(n)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)]`, `a=8n-7`,

proves r is decreasing and `0<r(n)<15/(8n-7)^2`. Hence each forcing
difference in H1 is at most `15/(8n0+1)^2`, giving H2. Cauchy–Schwarz
gives the L2 claim. The proof is valid for every real seed if b is defined
using the same fixed authenticated local a; canonical rational principal
parts are asserted only for rational states, in particular literal zero.

**Controls and quantifiers.** The argument needs even radix 16. At odd radix
17, `v_n=-1` is dynamically consistent with zero forcing differences and
gives zero fold. At radix16, a synthetic constant `v_n=-1` requires forcing
phase increment 1/2; discarding that increment would invalidate H1. The
coherent same-forcing seed has v near1 and large fold, so is preserved.
H2 has asymptotic force along q=2 clocks if such clocks recur; this dossier
does not prove that recurrence. Each declared finite q=2 clock is certified.

## HCB3. Exact fits can erase the named resonance at a compulsory cost

Fix a proper nonempty subset `S` of `F_p`, of size m, and the character
`a(x)=e(hx/p)`. A subgroup coset from PR1 is one such subset. For any function
B on S, put `W=mean_S aB`. Extend B to F_p by

```
F(x)=B(x)                                      (x in S),
F(x)=-mW/(p-m) * e(-hx/p)                      (x not in S).
```

Its full additive Fourier coefficients are
`c_t=p^-1 sum_(x in F_p) F(x)e(-tx/p)`. Direct summation gives
`c_(-h)=0`; Fourier inversion gives the **exact** fit

`B(x)=sum_(t != -h modp) c_t e(tx/p)` on S.                    (H3)

Every atom in H3 has nonconstant reduced `hX+tX` of degree1 when m>1.
Thus this representation has both `rho=0` and `Rsig=0`, for every B. For
the coherent complement `B=e(-hx/p)`, it has `W=1`. Explicitly,

`c_t=(p-m)^-1 sum_(y in S)e(-(t+h)y/p)`, `t!=-h`.             (H4)

This is an exact counterexample to the shortcut “small approximation error
and small retained coefficient alone imply cancellation.” It preserves the
PR8 cost; it does not contradict PR8.

For a coset `S=xi<16>` with m>1, let `beta=min(1,sqrt(p)/m)`. PR6 implies
every representation of a coherent B with zero named resonance must satisfy

`rho + beta sum_t |c_t| >= 1`.                               (H5)

For exact H4, Parseval also gives

`sum_(t!=-h)|c_t|²=m/(p-m)`,
`sum_(t!=-h)|c_t|<=sqrt((p-1)m/(p-m))`.                       (H6)

The inequalities can both be useful: they exhibit an exact nonresonant
linear fit, and prove that its variation cannot enter the vanishing-cost
regime when the target is coherent. Merely recording degree1 is insufficient.

**Proof.** The extension was chosen to cancel exactly the Fourier coefficient
at -h. Inversion follows from `sum_t e(t(x-y)/p)=p 1_(x=y)`.
For coherent B, the coefficient formula follows from the zero complete sum
at every nonzero t+h. Its extension has modulus1 on S and m/(p-m) outside,
so Parseval yields H6's equality. Cauchy–Schwarz gives its inequality. Multiply
any proposed model by a, average on S and apply PR6 to each nonresonant atom;
the model residual contributes at most rho, proving H5.

**General representation ambiguity.** For every prescribed complex R, apply
H3 to `B-R e(-hx/p)` and then add the atom `R e(-hx/p)`. This represents the
same B exactly with retained coefficient R. Thus Rsig is a property of the
declared representation, not an intrinsic projection without a normalization.
Nevertheless two proposed representations with errors rho,rho' and costs E,E'
obey `|R-R'|<=rho+rho'+E+E'` by PR8 on the same complete clock. Accurate
representations of vanishing cost therefore have an asymptotically unique
retained coefficient, but this does not prove that coefficient tends to zero.

## HCB4. Convex dual witnesses for the actual approximation budget

Let the declared nonresonant dictionary on S be `u_j`, each with a proved
nonnegative arithmetic charge `w_j`. For any function psi on S satisfying
`max_x|psi(x)|<=1` and `|mean_S conjugate(psi) u_j|<=w_j` for every j,

```
mean |B-sum_j c_j u_j| + sum_j w_j |c_j|
 >= Re mean conjugate(psi) B.                               (H7)
```

If a resonance atom `a^-1` is free (uncharged), add the constraint
`mean conjugate(psi) a^-1=0`. If its coefficient is instead charged by |R|,
require only the already automatic modulus bound1. Proof is termwise
triangle inequality and the two stated constraints. No fit or independence
assumption is involved. A witness optimized using a restricted menu proves
only a lower bound for that same menu; enlarging the menu requires checking
all new inequalities. The witness `psi=conjugate(a)` gives H5 directly.

This theorem is a lower-bound instrument. A large dual lower bound refutes a
declared low-cost approximation mechanism without refuting normality. Neither
a dictionary fit nor successful learning is a source-selected cancellation
theorem.

## Inspected recent repository fronts

Read-only branch pins and the actual proof audit are in `REVIEW.md`.
The new golden finite-element transfer carries the signed target with
O_h(A^-2) error; the four-pole positive vector lift asymptotically carries
the same scalar W. Neither gives a bound on the original PR8 residual or
retained resonance. The Cayley/xi work belongs to RH and explicitly leaves
its own global extension/Jensen sign gate open. No cross-program theorem
is imported into HCB1–4.
