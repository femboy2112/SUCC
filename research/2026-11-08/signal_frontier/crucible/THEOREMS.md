# All-order authentic phase calibration and its critical bandwidth

**Status: PROVED PAPER, finite exact checks. Pi base-16 normality: OPEN.
RH: OPEN.** Pinned parent `86327467191420d2157eeae5f4cfa1c2c62810da`.
No worldwide novelty is claimed. This develops an effective source instrument;
it does not claim a new original-zero signed cancellation estimate.

The preceding GQ2 gives the authentic tail integral and its first two
asymptotic terms. Here a special simplification of that very kernel yields
integer all-order coefficients, signed rational enclosures, and an extra
power of accuracy for cross-time phases. These are useful when choosing an
observer's precision and spectral bandwidth before attempting cancellation.

## SC1. Integer source jets and signed rational tail enclosures

Preserve the original four-pole forcing and every unwrapped state:

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U_0(s)=s, U_n(s)=16 U_(n-1)(s)+r(n),
X_n(s)=16^n(s+pi/16), T_n=X_n(s)-U_n(s).
```

Only s=0 is the authenticated selected source. For every n>=1, the inherited
Green identity and positive integral representation give

```
T_n = integral_0^1 x^(8n)(1-x) f(x) dx,
f(x) = (x^2+2)(x^2+2x+2)/(16-x^8)
     = 1/[(2-x^2)(x^2-2x+2)].                         (SC1)
```

Cancellation in this rational function is an exact kernel identity; the four
forcing poles in the recurrence remain unchanged. On [0,1] all derivatives
of f are nonnegative, and they are strictly positive on (0,1]. Indeed the original quotient expands as the
nonnegative power series `sum_(k>=0) Q(x)x^(8k)/16^(k+1)`, whose radius of
convergence exceeds1; every derivative has a positive term on (0,1].

Let `a_j=f^(j)(1)/j!`, with `a_j=0` for negative j. Then

```
a_0=1,    a_j=2 a_(j-1)+2 a_(j-3)+a_(j-4)  (j>=1),
(a_0,...,a_6)=(1,2,4,10,25,60,144).                   (SC2)
```

**Proof.** At x=1+v, the denominator is
`(1-2v-v^2)(1+v^2)=1-2v-2v^3-v^4`. Multiply its Taylor series by that of f
and equate coefficients. In particular every a_j is a positive integer.
This identity does not assert convergence of the series throughout [0,1];
only its finite Taylor formula is used below.

Write `B(u,v)=integral_0^1 x^(u-1)(1-x)^(v-1) dx`. For integer m>=-1 put

```
t_m(n) = sum_(j=0)^m (-1)^j a_j B(8n+1,j+2),
D_m(n) = a_(m+1) B(8n+1,m+3),
R_m(n) = T_n-t_m(n),                                 (SC3)
```

where the sum is0 for m=-1. These are explicit rational numbers because
`B(8n+1,j+2)=(j+1)! / product_(q=1)^(j+2)(8n+q)`.
For every n>=1 and every finite m>=-1,

```
0 < (-1)^(m+1) R_m(n) < D_m(n).                       (SC4)
```

Thus even truncations are upper bounds, odd truncations are lower bounds,
and the next signed term encloses the exact tail. The statements remain valid
even if a high-order lower bound happens to be negative.

**Proof.** For m>=0 Taylor's integral remainder about1 is

```
f(x)-sum_(j<=m) a_j(x-1)^j
 = (-1)^(m+1)/m! * integral_x^1 f^(m+1)(u)(u-x)^m du.
```

The signed remainder is positive for x<1 and strictly below
`a_(m+1)(1-x)^(m+1)`, since the derivative is strictly increasing. Multiply
by the positive weight x^(8n)(1-x), integrate, and use the beta integral.
For m=-1 use `0<f(x)<f(1)=1` on [0,1). This proves SC4 for all finite m
without an unjustified exchange of an infinite Taylor series and integral.

## SC2. Cross-time calibration gains one power, with a sharp constant

For every integer lag ell>=1,

```
0 < (-1)^(m+1)[R_m(n)-R_m(n+ell)]
  < 8 ell a_(m+1) B(8n+1,m+4) =: E_m(n,ell).           (SC5)
```

**Proof.** The signed Taylor remainder is a fixed positive function of x,
independent of n. Subtract the two integrals, multiply it by
`x^(8n)(1-x)(1-x^(8ell))`, and use
`0<1-x^(8ell)<=8ell(1-x)` on (0,1). The bound SC4 for the integrand then
gives SC5. This retains the exact temporal comparison; it does not discard
the forced phase in `U_(n+ell)=16^ell U_n+F_ell(n)`.

For each fixed m and ell, both orders and constants are asymptotically sharp:

```
c_m = a_(m+1)(m+2)! / 8^(m+3),
lim_(n->infinity) n^(m+3) (-1)^(m+1) R_m(n) = c_m,
lim_(n->infinity) n^(m+4) (-1)^(m+1)
                     [R_m(n)-R_m(n+ell)] = (m+3)ell c_m. (SC6)
```

**Proof.** Taylor expansion one order further makes the signed integrand
remainder `a_(m+1)(1-x)^(m+1)+O((1-x)^(m+2))`, uniformly on [0,1].
In the difference, also use
`1-x^(8ell)=8ell(1-x)+O((1-x)^2)` for fixed ell. Integrate each term and use
`B(8n+1,k) ~ (k-1)!/(8n)^k`. The next beta integral has one lower power.
This also establishes uniform versions on x=n/A in any fixed compact subset
of (0,infinity), by the same explicit remainder bounds.

The uncorrected case is especially simple:

```
0<T_n-T_(n+ell)<16ell/[(8n+1)(8n+2)(8n+3)]<ell/(32n^3). (SC7)
```

No exponential-in-ell error is paid. This compares source and completed
*lag phases*; it does not identify them with the uncorrected enlarged-frequency
character of U_n. That latter comparison has a different forced-phase cost.

## SC3. Uniform transport of signed observations, with declared bandwidth

Let `e(t)=exp(2pi i t)`, `V_n^(m)(s)=U_n(s)+t_m(n)`. Exactly

```
V_n^(m)(s)=X_n(s)-R_m(n).
```

For any integer h, any finite probability weights mu_n on n>=A>=1,
and every seed s,

```
|sum_n mu_n e(h V_n^(m)(s))-sum_n mu_n e(h X_n(s))|
 <=2pi|h| D_m(A).                                    (SC8)
```

For any integer ell>=1,

```
|sum_n mu_n e(h[V_(n+ell)^(m)-V_n^(m)])
       -sum_n mu_n e(h[X_(n+ell)-X_n])|
 <=2pi|h| E_m(A,ell).                                (SC9)
```

The same bounds hold with arbitrary complex test weights w_n and an added
factor `sum |w_n|`; positive weights are not needed for signed transport.
They hold uniformly in s. The proof is the pointwise Lipschitz estimate
`|e(u)-e(v)|<=2pi|u-v|` and SC4/SC5. Thus, for each fixed m, the single-time
transport is o(1) when `|h_A|=o(A^(m+3))`; the lag transport is o(1) when
`|h_A| ell_A=o(A^(m+4))`. The latter condition is sufficient for arbitrary
positive integer ell_A, without fixing the lag.

For a triangular lag statistic with weights
`w_ell=2(H-ell)/H^2`, 1<=ell<H, the transport error is at most

```
16pi|h| a_(m+1) B(8A+1,m+4) * (H^2-1)/(3H).          (SC10)
```

This follows from `sum w_ell ell=(H^2-1)/(3H)`. It applies directly to
signed lag aggregates, preserving their signs and all cross terms. It is a
precision lemma for those aggregates, not an upper bound on their value.
For m=-1, it is `<pi|h|(H^2-1)/(48H A^3)`.

For a finite multi-time character with integer coefficients h_j and times
n_j>=A, its absolute transport error is at most
`2pi D_m(A) sum_j |h_j|`. If repeated coefficients sum to0, no improvement
is claimed without a bound on the actual time separations.

## SC4. Critical chirps show the bandwidth cannot be silently enlarged

Take the coherent same-forcing seed `s*=-pi/16`. Then X_n=0 and
`V_n^(m)=-R_m(n)`. Fix lambda!=0, choose integers h_A with
`h_A/A^(m+3)->lambda`, and average on A<=n<2A. SC6 and Riemann sums give

```
mean e(h_A V_n^(m))
 -> integral_1^2 e(-lambda (-1)^(m+1)c_m/x^(m+3)) dx.   (SC11)
```

The completed mean is1. The limiting integral has modulus strictly less
than1: equality in the triangle inequality for a unit-valued continuous
function would force it to be constant, whereas its displayed phase is
nonconstant on every interval. Thus a blanket vanishing transport error at
the critical frequency scale is false even for an exact same-forcing orbit.
For a fixed positive ell and `h_A/A^(m+4)->lambda`, the corresponding lag
mean instead tends to

```
integral_1^2 e(lambda (-1)^(m+1)(m+3)ell c_m/x^(m+4)) dx, (SC12)
```

again of modulus<1. Both are fixed-seed controls; only the spectral probe
h_A changes. They do not refute a claim about the authentic zero seed.

## SC5. Gamma is a calibratable constant; its residual has its own bandwidth

In the preceding GQ notation put

```
L_N=sum_(n<=N)nT_n-(log N)/64,
L_infinity=C+gamma/64,    delta_N=L_N-L_infinity.
```

The inherited result gives `0<delta_N<11/(512N)`. Moreover

```
lim N delta_N = 11/512.                              (SC13)
```

**Proof.** GQ2 proves `N(C_N-C)->7/512`. The elementary harmonic remainder
obeys `N(H_N-log N-gamma)->1/2`: use
`log(1+1/k)-1/(k+1)=1/(2k^2)+O(k^-3)` and sum over k>=N. Since
`delta_N=(C_N-C)+(H_N-log N-gamma)/64`, the constants add to11/512.

For any unit or bounded sequence z_N and any probability weights supported
on N>=A, multiplying it by the fully dephased gamma product
`g_N(h)=e(-h delta_N)` changes its mean by at most

```
11pi |h|/(256A).                                     (SC14)
```

At fixed h this tends to0, so this gamma correction preserves both decay
and nondecay of the original signed statistic. It cannot manufacture
cancellation. At critical h_A/A->lambda!=0 and z_N=1, its epoch mean tends
to `integral_1^2 e(-11lambda/(512x)) dx`, of modulus<1. Treating the gamma
product as an N-independent phase is therefore unsafe at that bandwidth.
The constant `e(-h[C+gamma/64])` by itself is a global unit gauge and never
changes the magnitude of a signed mean.

This is a positive calibration result, not a dismissal of the gamma signal:
it tells exactly how accurately that known part may be divided out, and
where its remaining deterministic chirp must still be retained. The
remaining arithmetic question is whether the source-selected phase left
behind has signed covariance decay for every fixed h and all epochs A.
No theorem here identifies that covariance with L_N or its gamma constant.

## Claim and failure ledger

| ID | Verdict | Scope / receipt | Remaining debt |
|---|---|---|---|
| SC1–2 | PROVED PAPER | Source-specific integer jets, signed rational enclosures, sharp lag gain | No distributional claim |
| SC3 | PROVED PAPER | Explicit all-epoch signed transport and bandwidth | Bounds calibration error, not signed mean |
| SC4 | REFUTED shortcut | Coherent fixed seed disproves unqualified critical-bandwidth constant-gauge approximation | Does not refute zero-source normality |
| SC5 | PROVED PAPER | Sharp gamma residual scale11/512 and covariance-gauge robustness | No gamma-to-covariance cancellation bridge |
| Generic Abel/Cesaro gate | INHERITED | analytic_exile AE07 already proves/imports it | No duplicate result counted |
| Zero-source signed covariance decay | OPEN | Same literal U0=0, same original poles | Source-derived signed estimate still required |

## Provenance and verification

SC1's integral and the Green identity come from the pinned quotient_signal
GQ2 and original selected_orbit source. The all-order Taylor recurrence and
finite-order beta enclosures are derived here. Classical Taylor remainder,
beta integrals and Riemann sums are proved/applied at their stated domains;
no external theorem is needed for the new claims. For the explicitly excluded
already-known Abel/Cesaro result, the repository's primary source is
[Ponce, Theorems10–11](https://mat.uc.cl/prepublicaciones/download/36).

The independent oracle in this directory reconstructs the original four-pole
source directly and encloses the positive16-adic tail without using the
Taylor approximants. Its tail bound follows independently from
`r(k)=integral x^(8k-8)(1-x)Q(x) dx <=15/[(8k-7)(8k-6)]<1/k^2`
for k>=2: the final inequality is `49k^2-104k+42>0`. Thus truncation after L
terms costs at most `16^(-L)/[15(n+L+1)^2]`. It checks the latter against those enclosures, and
separately verifies the polynomial identities by exact convolution. It does
not use pi or gamma values to construct phases. Finite tests corroborate the
implementation and falsifiers; the all-n statements rely on the proofs above.
No Lean/kernel certificate or external scholarly referee review is claimed.
