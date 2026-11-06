# Pointed cocategory / virtual support: BBP gauge transport and its exact boundary

**2026-11-05. Research-only, strictly additive child of draft PR #508**
(head `61cdf240d0c2e75afe934dde6c98ce71a783a832`).
No edits to canonical source, archived proofs, contracts, Lean, main, or workflows.
**The base-16 normality of pi, its selected signed Weyl gate, and RH remain OPEN.**
All claims below are classical/elementary algebra in the declared domain or
new *representations* of previously authenticated SUCC identities. No novelty
or physical realization is asserted.

## 1. Steelman, then the precise obstruction

Intuition: the information apparently lost in the Haar integral may survive as
the *relation/parallel transport between two reference frames*. "Virtual field"
is a **proposed mathematical metaphor for preserved gluing or connection data**,
not an independently identified physical field, a quantum energy fluctuation,
or a claim that every categorical arrow is a null geodesic.

The pointwise claim `f(s+theta)=f(s)` is generally false except at symmetries,
but translation-invariance of Haar measure gives
`int f(s+theta) ds = int f(s) ds` for **all** theta.
This scalar projection is noninjective, and theta cannot be recovered from
that scalar *alone*: no-go by equal input to any prospective reconstruction.
A *different, coupled observation* can retain theta:
`int e(s+theta) conjugate(e(s)) ds = e(theta)`,
where `e(t)=exp(2 pi i t)`.

This is a pathway repair, not an extra metaphysical dimension.
One must preserve the cross-frame arrow before quotienting by it.

## 2. Source and domains (exact)

Let `b>=2` be an integer, `r(j)` any declared real source sequence, and
`U_0=0, U_(n+1)=b U_n+r(n+1)` **unwrapped**. Set
`T=R/Z`, `h in Z\{0}`, `n>=0`, and `s,theta in T`.
Choose real lifts for algebra, then take phases modulo integers. Define

```text
x_n(s) = U_n + b^n s (mod 1)
z_n(s;h) = e(h (U_n + b^n s)).
T_theta(s) = s+theta.
```

For SUCC's *authentic* BBP case, `b=16` and

```text
r(j) = 4/(8j-7) - 2/(8j-4) - 1/(8j-3) - 1/(8j-2)
     = (120j^2-89j+16)/((2j-1)(4j-1)(8j-7)(8j-3)).
```

The exact integer/rational carry lift remains a **separate source object**:
circle characters alone see `r(j) mod 1`, not its integer part.

## 3. PT-1 — cross-frame covariance and retained displacement [EXACT / CLASSICAL]

For all declared `n,s,theta,h`,

```text
z_n(s+theta;h) / z_n(s;h) = e(h b^n theta).
C_n(theta;h) = int_T z_n(s+theta;h) conjugate(z_n(s;h)) ds
             = e(h b^n theta).
C_(n+1)(theta;h) = C_n(theta;h)^b.
```

Proof: subtract the two exponents; the integrand in `C_n` is independent
of `s`. The `b`th-power law follows by multiplication.
At `n=0,h=1`, the correlation determines `theta` exactly mod 1.
At `n>0` it only determines theta mod `1/b^n` (and with general
`h`, mod `1/(abs(h)b^n)`), so the earlier pointed clock is needed to
avoid torsion aliases. The unpaired Haar marginals do not distinguish shifts.

The square `T_(b^(n+1) theta) o F_(n+1) =
F_(n+1) o T_(b^n theta)`, where `F_(n+1)(x)=b x+r(n+1)`,
**commutes on the circle**. This is *time-indexed* equivariance, not the
time-independent intertwiner forbidden in the categorical observer atlas.

## 4. PT-2 — a pointed source link and anchored selected character [EXACT]

Define the temporal link and source-pointed observable:

```text
L_n(s;h) = z_(n+1)(s;h) conjugate(z_n(s;h))^b
         = e(h r(n+1)).
B_n(s;h) = z_n(s;h) conjugate(z_0(s;h))^(b^n)
         = e(h U_n).
```

These are exact for every `s`; `B_0=1` and

```text
B_(n+1) = B_n^b L_n,
B_n = product_(j=1)^n L_(j-1)^(b^(n-j)).
S_N^U(h) = sum_(n=0)^(N-1) B_n(s;h)
         = sum_(n=0)^(N-1) e(h U_n).
```

The selected BBP signed Weyl sum is the **pointed/transported observable**,
not the unpaired Haar marginal. The familiar `n=1,...,N` convention differs
by endpoint terms and does not change a little-o gate.

CRITICAL SCOPE: for a hypothetical orbit with arbitrary `U_0=t`,
the same anchored construction returns `e(h(U_n-b^n t))`, the zero-boundary
*formal response to the same forcing*. This does **not** prove that an
external process realized `t=0`. Within SUCC's declared exact arithmetic
source `U_0=0` is an axiomatically selected initial condition, not a new
ontological debt.

Circle phases alone are not fully source faithful: replacing `r(j)` by
`r(j)+k_j` with arbitrary integers `k_j` leaves *all* integer-character
links unchanged. Preserve the exact unwrapped forcing and literal carry
labels in `integer_bbp_carrier` and other existing source modules.

## 5. PT-3 — sharp first unbalanced Haar resonance [EXACT / CLASSICAL]

For `N>=2` define `P_N(s)=sum_(n=0)^(N-1) z_n(s;h)`.
Character orthogonality gives

```text
int_T P_N(s)^b conjugate(P_N(s)) ds
       = sum_(m=1)^(N-1) e(-h r(m)).
```

Proof: a term with `b` positive factors at indices `n_1,...,n_b`
and one negative at `m` survives precisely when
`sum_i b^(n_i)=b^m`. Let `k=min n_i`. Modulo `b^(k+1)`,
the number of indices equal to `k` must be a positive multiple of `b`;
there are exactly `b` indices, so *all* equal `k=m-1`.
The remaining phase is `e(h (b U_(m-1)-U_m))=e(-h r(m))`.

For `p,q>=0` and `p+q<b+1`, every nonzero Haar moment
`int P_N^p conjugate(P_N)^q` is source-blind: the exponent balance cannot
have a radix carry because each side has fewer than `b` digits when both
sides are nonempty. If `p=q`, identical index multisets cancel their
source phases; if `p!=q`, there is no equality. Consequently degree
`b+1=17` is the first **source-sensitive unbalanced moment** of this
particular single-frequency polynomial. It does not distinguish initial
seeds, because shifting the seed merely translates `s` in a Haar integral.
This is an *exact identity*, not signed `o(N)` cancellation.

## 6. PT-4 — the virtual support can be the changing frame itself [EXACT]

Let `theta_n` be a declared sequence of real frame offsets. Observing

```text
w_n(s) = e(h (U_n + b^n(s+theta_n)))
```

changes the temporal link by the exact deformation term:

```text
w_(n+1) conjugate(w_n)^b
    = e(h [r(n+1) + b^(n+1)(theta_(n+1)-theta_n)]).
```

For a fixed theta, the extra term vanishes and the source link persists.
For arbitrary time-varying frames, the apparent source can be altered at will
unless the frame path and its provenance are retained. Thus a chart can
flatten the dynamics without destroying their *connection data*.

In particular choose the **source-comoving frame**

```text
theta_0=0,
theta_n= -sum_(j=1)^n r(j)/b^j = -U_n/b^n,
theta_(n+1)-theta_n= -r(n+1)/b^(n+1).
```

Then `U_n+b^n theta_n=0` **exactly for every n** and
`w_n(s)=e(h b^n s)`. The entire original forcing has migrated into the
frame transition sequence. Calling it "lost" after forgetting `theta_n`
is a failure of source transport, not a theorem of ontological absence.

For authentic BBP the classical identity
`sum_(j>=1) 16^(-j) r(j) = pi/16` gives

```text
theta_n -> theta_infinity = -pi/16.
Z_n = sum_(k>=1) 16^(-k) r(n+k).
U_n + 16^n theta_infinity = -Z_n.
```

This identifies SUCC's **coherent wrong seed `-pi/16` as the limit of the
exact finite comoving gauge**. The true source and the coherent counterseed
are therefore two different *pointings of the same forcing*.

A useful rigorously explicit bound needs no real-pi numerical oracle.
For `j>=1`, positivity of `120j^2-89j+16`, the numerator bound
`120j^2-89j+16<=120j^2`, and the four denominator estimates
`2j-1>=j`, `4j-1>=3j`, `8j-7>=j`, `8j-3>=5j` give

```text
0 < r(j) <= 8/j^2;
0 < Z_n <= 8 / (15 (n+1)^2);
0 < theta_n - theta_infinity <= 8 / (15*16^n*(n+1)^2).
```

Therefore `U_n+16^n(-pi/16)=-Z_n ->0` on the circle. The coherent
counterseed is manifestly **not normal**, despite having exactly the same
forcing and flat frame-transport squares. This is the concrete hostile
counterexample to "a coherent virtual/transport field implies mixing."

## 7. PT-5 — flatness, invariants, and the still-open signed gate

The frame-time commutator/plaquette is identically trivial:

```text
[z_(n+1)(s+theta)/z_(n+1)(s)] /
[z_n(s+theta)/z_n(s)]^b = 1.
```

This is a **flat circle-valued equivariant connection** in the declared
coordinate system. A nonzero curvature, physical null-ray propagation,
quantum virtual-particle interpretation, Lorentzian geometry, or completed
Weil positivity would require additional maps and sourced structure.
They cannot be inferred from the commuting square.

The missing result remains, for every fixed nonzero integer `h`,

```text
sum_(n=1)^N e(h U_n) = o_h(N).
```

The pointed correlation gives an exact formula for its summands, not a
nontrivial upper bound. Neither the comoving gauge nor the `17`th Haar
moment closes this open estimate. The #508 trilinear route is another
representation of this same source-selected difficulty.

## 8. Probe ledger, adversarial cases, next verdict-changing experiment

- **EXACT PAPER / local algebra**: covariance, temporal link, pointed readout,
  flat square, base-16 degree-17 moment, comoving gauge, coherent-seed tail.
- **OBSERVED**: `tests/test_pointed_cocategory_transport.py` contains exact
  Fraction probes for the original four signed poles, gauge changes, wrong
  anchor power, `+1/7` source mutation, `+1` integer-carry-invisible
  mutation, first resonances at bases 2/3/4/16, time-varying frames, and
  finite coherent-seed tails. Tests are finite probes, not authority for the
  infinite theorems. Full hosted suite is not claimed.
- **REFUTED (by exact counterexample)**: *Haar scalar carries the seed*;
  *source-character links authenticate the unwrapped integer forcing*;
  *flatness or time-dependent frame equivalence guarantees normality*.
- **UNVERIFIED**: any signed source-specific saving from these correlators,
  a nonflat common-basis cycle using the real-circle/16-adic/prime-Frobenius
  clocks, or a realization in physical causal light-ray transport.

**Next discriminating probe:** start with the existing source-labelled
`operational_yoneda_descent`, `prime_clock_yoneda`, and #508 delayed cubic
observer. Form an actual square of *two genuinely independent source actions*
(radix successor and a typed prime-clock/lift action); retain the original
integer carry and a common orientation. Calculate a signed plaquette defect
*before* Haar or quotienting, and compare (a) genuine `U_0=0`,
(b) `s_*=-pi/16`, (c) integer forcing mutants, and (d) same-forcing
alternative seeds. Either identify a nonzero source-dependent defect with
a proved quantitative bound, or show the square is another flat tautology.
A new `o(N)` statement needs a genuinely source-selected signed estimate,
not just a new representation.

**Provenance:** main `AGENTS.md`, `docs/CATEGORICAL_OBSERVER_ATLAS.md`,
`docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`; stacked drafts #499–#508,
especially #507/#508. Their results are inherited context, **not independent
validation** of the present algebra or a normality claim.
