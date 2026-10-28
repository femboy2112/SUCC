# Operation Dual SUCC: BBP endpoint jets, critical arithmetic and chiral gauge rigidity

**2026-10-27 — RESEARCH DRAFT / NO NORMALITY CLAIM.** Source context: SUCC #333, #335, #336 and #337. Exact starting research parent: PR #336, `dc59810de9dd0b97d07ad48be8e045fe6756b082`. Neither the original signed four-pole source, its zero seed, historical proof receipts, nor `main` is to be modified. All claims below are over the rationals unless an explicit finite-field specialization is stated. No RH, base-16 normality of pi, positive Weil form, independence, or selected Weyl cancellation is inferred.

## Steelman and typed definitions

Use the dual-number algebra `R[eps]/(eps^2)` for a commutative rational algebra `R`; `a+b eps` is **value plus tangent**, not a complex phase or an ordered tiny real. For any polynomial/rational expression at a point where its denominator is a unit, `f(x+eps)=f(x)+eps f'(x)`. For a Taylor coefficient of order two or three, use `R[t]/(t^3)` or `R[t]/(t^4)` rather than incorrectly reusing first-order dual numbers. Character phase, carry floor, rational source, chiral transport, finite-field reduction and analytic Gamma are different observation types.

Primary external background: Cornell [automatic differentiation lecture](https://www.cs.cornell.edu/~bindel/nmds/01-Fund1d/04-AutoDiff.html) and Baydin et al., [AD in Machine Learning survey](https://jmlr.org/papers/v18/17-468.html). Internal ancestors: [rank-two Gaussian source #333](https://github.com/femboy2112/SUCC/pull/333), [source-sensitive Mellin/Gamma #335](https://github.com/femboy2112/SUCC/pull/335), [chiral target and two-clock filters #336](https://github.com/femboy2112/SUCC/pull/336), and [Furstenberg safeguard #337](https://github.com/femboy2112/SUCC/pull/337). No external priority claimed.

## DJ-1 (exact): the BBP time-source derivative has additional critical arithmetic

The *authentic* source is

```
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2) = A(n)/D(n)
A(x) = 120*x^2 - 89*x + 16
D(x) = (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3).
```

Let `W=A'D-AD'`. Direct integer expansion gives

```
W(x) = -122880*x^5 + 259584*x^4 - 215040*x^3
       + 87800*x^2 - 17744*x + 1427.
```

Consequently `r(n+eps)=r(n)+eps W(n)/D(n)^2` wherever `D(n)` is invertible. Exact Sylvester determinants (reproducible with integer Bareiss elimination) yield

```
Res(A,D) = -2^15 * 3^2 * 5^2
Disc(D)  =  2^24 * 3^2 * 5^2
Res(W,D) = -2^48 * 3^4 * 5^4
Disc(W)  =  2^49 * 3^5 * 5^2 * 52497217.
```

`52497217` is prime (trial division up to sqrt suffices). It is an **additional critical-point collision prime**, not a new denominator-pole prime: modulo `p=52497217` the residue `x=22168154` satisfies `D(x)!=0`, `W(x)=W'(x)=0` and `W''(x)!=0`. The local Hasse/Taylor expansion has the exact coefficients

```
(A(x+t)/D(x+t)) mod (p,t^4)
    = 34082935 + 0*t + 0*t^2 + 5987934*t^3.
```

For `p=7`, at good (non-pole) residues `x=1` and `x=5`, the **first** derivative vanishes while the **second** does not. The respective local coefficients modulo seven through order three are `(5,0,4,5)` and `(1,0,1,6)`. Thus first-order dual observations can be locally blind even at a prime outside the original `{2,3,5}` exceptional set. A third-order jet distinguishes the extra-prime double critical point. This is a source-fingerprint / local etale-locus diagnostic, **not** a global inverse, orbit distribution theorem, or proof of normality. It cannot be evaluated modulo a prime at a residue that is a pole.

## DJ-2 (exact): endpoint jets explain the chiral cancellation and source decay

From PR #333, the complete eight-tap shell polynomials `P=P_+ + P_-` have coefficient vectors

```
P    : (4,0,0,-2,-1,-1,0,0)
P_+  : (4,2,0,-1,-1,-1/2,0,1/4)
P_-  : (0,-2,0,-1,0,-1/2,0,-1/4).
```

The exact Mellin formula is `r(n)=int_0^1 x^(8(n-1)) P(x) dx`; apply this separately to the chiral channels. The endpoint dual jets are

```
P(1+eps)   = 0 - 15*eps
P_+(1+eps) = 15/4 - 23*eps/4
P_-(1+eps) = -15/4 - 37*eps/4.
```

**Endpoint-jet decay lemma.** Let `P` be a rational polynomial and `q>=0` be the exact order of vanishing at `x=1`. Then, for `n` tending to infinity,

```
int_0^1 x^(8(n-1)) P(x) dx
 = (-1)^q P^(q)(1) / (8^(q+1) n^(q+1)) + O(n^(-q-2)).
```

Proof: Taylor-expand at 1; the first nonzero term is `(-1)^q P^(q)(1)(1-x)^q/q!`, and the beta integral `int_0^1 x^M (1-x)^q dx = M!q!/(M+q+1)!` has leading term `q! M^(-q-1)` for `M=8(n-1)`. Bound the finite polynomial remainder by the next beta integral. For the total BBP shell, `q=1`, giving `r(n)=15/(64n^2)+O(n^-3)`; each chiral shell has `q=0`, giving `r_+(n)=15/(32n)+O(n^-2)` and `r_-(n)=-15/(32n)+O(n^-2)`. This recovers the #333 chiral pole cancellation through a **single endpoint jet certificate**. Higher truncated jet rings expose further decay powers. This is source cancellation, not signed Weyl cancellation.

The log moments are equally exact: `d/dn r(n)=8 int_0^1 x^(8(n-1)) log(x) P(x) dx`, obtained by differentiating the Mellin exponent (the finite polynomial permits differentiation under the integral). In Gamma language, `Gamma(1+eps)=1-gamma*eps`; the Euler-Mascheroni constant appears through Gamma differentiation, but the rational BBP Mellin derivative does not automatically acquire an extra uncancelled gamma term. The two original chiral harmonic finite parts already cancel as recorded in #335.

## DJ-3 (exact): infinitesimal rigidity of the authentic eight-step carrier

Use the rational source-selected chiral matrix from #333 in the basis (even real, even imaginary, odd coordinate 1, odd coordinate 2), and its fixed input/readout:

```
T = [[1/2,-1/2,0,0], [1/2,1/2,0,0],
     [0,0,0,1], [0,0,1/2,0]]
b = (1,0,1,0)^T ; ell = (4,0,0,-4).
```

Then `T^4=diag(-1/4,-1/4,1/4,1/4)=-J/4`, `T^8=I/16`, the first eight `ell T^m b` are exactly the original taps and `det[ell T^(i+j)b]_(0<=i,j<4)=4`. The minimal polynomial is `(t^2-t+1/2)(t^2-1/2)`, with four distinct roots over the algebraic closure.

For any rational 4x4 `B`, perturb `T_eps=T+eps B`. Then

```
T_eps^8 = I/16 + eps * H(B)
H(B) = sum_(k=0)^7 T^(7-k) B T^k.
```

**Clock tangent theorem.** `H(B)=0` if and only if `B=[X,T]` for some rational 4x4 `X`. Proof: in an eigenbasis, for distinct eigenvalues lambda_i, lambda_j, the multiplier on `B_ij` is `(lambda_i^8-lambda_j^8)/(lambda_i-lambda_j)=0`, whereas on the diagonal it is `8 lambda_i^7 != 0`. The kernel is exactly the off-diagonal space, dimension `4*3=12`. That is precisely the image of the commutator map. Rational solutions exist by rational linear algebra. This shows that preserving the clock to first order alone yields *coordinate gauge*, not genuinely new carrier structure.

**Source-anchored tangent theorem.** Keep `b` and `ell` fixed. The three independent source variations for `m=1,2,3` are `dc_m(B)=sum_(k=0)^(m-1) ell T^(m-1-k) B T^k b`. The exact ranks in the full 16-dimensional rational matrix space are:

```
rank(H)=4; rank(dc_1,dc_2,dc_3)=3;
rank(H,dc_1,dc_2,dc_3)=7.
```

Hence preserving *both* eight-step holonomy and every source tap has dimension 9, not 12. These nine are precisely `B=[X,T]` with `Xb=0` and `ell X=0`: that subspace of `X` has dimension `16-(4+4-1)=9`, and commutation with `T` plus `Xb=0` forces `X=0` because the controllability matrix `[b,Tb,T^2b,T^3b]` has determinant `1/8`. The matching dimension and inclusion prove equality. The readout observability determinant is `32` and the Hankel determinant is `4`.

**Hostile controls:** choose `X=E_11` in zero-based matrix indices: `B=[X,T]` is nonzero but all eight source variations vanish. Choose instead `X=E_01`: `B=[X,T]` still preserves the clock but changes the first three taps by `(2,2,1)`. The clock therefore cannot authenticate the original four-pole forcing on its own. This is a precise first-order gauge/source separation; it is not a universal finite-deformation, uniqueness, or nonlinear-realization theorem.

## DJ-4 (exact, mostly inherited #336): the two-clock filter becomes a jet test

Let `E` act by a forward time shift, and `F_n=P_+(E)U_n^+ + P_-(E)U_n^-`. Put `D=P_+-P_-`. By the authentic endpoint gauge #336, `T_n^+=a_n+R_n^+`, `T_n^-=-a_n+R_n^-`, `a_n=1/[4(8n+1)]`, with `R_n^+~1/(256n^2)`, `R_n^-~3/(256n^2)`. For fixed integer polynomials,

```
P_+(E)T_n^+ + P_-(E)T_n^-
 = D(1)/(32n)
 + ( -D'(1)/32 - D(1)/256
     + [P_+(1)+3P_-(1)]/256 )/n^2 + O_P(n^-3).
```

`D(1)=0` is the inherited cancellation of the 1/n chiral gauge; `D(16)=0` removes the log2 carrier. Under `D(1)=0`, with `p=P_+(1)=P_-(1)`, the further `n^-2` cancellation criterion is **`D'(1)=p/2`**. As one exact example, choose `P_-(X)=-30`, `P_+(X)=X^2-17X-14`. Then `D=(X-1)(X-16)` and all three conditions hold. The raw filtered Green defect is `O(n^-3)` and the pi carrier coefficient is `P_+(16)=-30`, not zero.

**Firewall:** #336 already establishes that such fixed neutral filters collapse to an ordinary authentic-orbit filter plus a summably small source difference. Better tail order is not a new signed normality rate. The condition is an explicitly computable source-jet certificate; it is *not* permission to promote pi normality.

## DJ-5 (exact): causal age susceptibility, and a decisive carry obstruction

Differentiate the authentic zero-seeded recurrence in a formal gain `lambda=16+eps`, keeping the four-pole source unchanged:

```
U_0(lambda)=0;
U_n(lambda)=lambda*U_(n-1)(lambda)+r(n).

U_n(16) = sum_(s=1)^n 16^(n-s)*r(s)
dU_n/dlambda|_16 = sum_(s=1)^n (n-s)*16^(n-s-1)*r(s).
```

The `(n-s)` factor is the exact causal age/echo weight; equivalently the tangent recurrence is `V_n=16 V_(n-1)+U_(n-1)`, `V_0=0`. This is a deterministic Green susceptibility. It is not a posterior probability, stochastic collapse or new independence assumption, and the expanding gain can make unnormalized sensitivities grow rapidly.

**Decisive one-jet no-go at digit cuts.** The real families `x_+(t)=1/16+t^2` and `x_-(t)=1/16-t^2` have identical first-order dual jets at `t=0`, namely `1/16+0eps`; for every sufficiently small positive real `t` they have different first hexadecimal digits (`1` and `0`). Thus no method using *only* the first jet of a real phase can recover all carry decisions. A phase character `exp(2*pi*i*x)` is smooth but the digit/carry map `floor(16x)` is discontinuous at radix boundaries. Higher finite jets also miss real flat perturbations if no margin or analytic-class assumption is supplied. SUCC's real-circle/adic joint gate must retain boundary distances, source history and signed arithmetic.

## Research verdict, claim status and next discriminating probe

- **DJ-1 — DISCLOSED (exact local arithmetic):** rational derivative polynomial, resultants, critical collision prime and finite Hasse jets. The additional prime has no demonstrated normality implication.
- **DJ-2 — DISCLOSED (paper derivation):** the endpoint-jet/Mellin decay lemma, with original two-channel masses and derivative. This recovers inherited source cancellations via a sharper organizing instrument; external novelty unverified.
- **DJ-3 — DISCLOSED over Q for the stated 4D linear representation:** 12 clock tangents, 9 source-invisible gauge tangents, and three authenticated-source directions. No global representation rigidity inferred.
- **DJ-4 — DISCLOSED conditional on the #336 source-tail formulas:** order-2 tail coefficient and exact example. Prior filter collapse blocks a normality promotion.
- **DJ-5 — DISCLOSED:** gain/age response and discontinuous digit-boundary counterexample.
- **UNVERIFIED frontier:** use modular critical classes and source-changing tangent perturbations as hostile controls for an *actual*, source-selected signed innovation / Weyl cancellation estimate. The preferred test must distinguish authentic `U_0=0` from changed-source, changed-seed, and rational nonnormal controls at all fixed Fourier frequencies. A differentiable carrier description alone cannot do so.

### Validation boundary

Accompanying pure-standard-library exact module: `observational_succ/bbp_dual_jets.py`; 12 focused Python tests in `tests/test_bbp_dual_jets.py` passed in an isolated local package shim on 2026-10-27. Exact arithmetic also independently crosschecked in SymPy for W, the discriminant and projective-source polynomial. This is NOT full native SUCC validation, a Lean proof, a PR-head CI pass or peer review. Re-run source-provenance and native tests against a real checkout before integration. No automatic merge, tag, release, rewriting history or assertion of pi normality/RH.