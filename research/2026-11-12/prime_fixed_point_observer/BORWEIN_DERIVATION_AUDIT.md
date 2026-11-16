# Borwein cylinder ratchet: derivation and boundary audit

**Date:** 2026-11-12. **Scope:** real uniform convolutions, exact rational support events, and a separately declared stochastic rectifier. **Academic priority:** UNVERIFIED. This note extends the repository's October Borwein dossiers; it does not replace their provenance or promote a prime-distribution claim.

The useful distinction is between three objects: a Borwein window mass, a deterministic record of support thresholds, and an actual rectified trajectory. Their equations are related, but they have different state, direction, and information requirements. In particular, a tiny positive deficit is an exact support certificate; it is not itself a preferred direction of motion.

## 1. Prior-work map

| Existing result | Established location | Treatment here |
| --- | --- | --- |
| Normalized radius-one Borwein mass; inclusion–exclusion CDF; first simplex deficit; classical first failure at the factor `sinc(x/15)` | [Borwein delta prime-clock dossier](../../2026-10-19/BORWEIN_DELTA_PRIME_CLOCK.md), BDW-01; [claim supplement](../../../docs/CLAIM_SUPPLEMENT_BORWEIN_DELTA.md) | Retained and independently recalibrated. General radius and shifted cap formulas are made explicit. |
| Odd-prime reciprocal widths first leave the radius-one plateau when 29 is included; this is not a residue test on an integer input | Same dossier, BDW-02–03 | Preserved boundary. Genuine arithmetic gates require their source labels. |
| Finite rational gated walks; support growth distinguished from typical symmetric trajectories | Same dossier, BDW-04–05; [implementation](../../../observational_succ/borwein_prime_clock.py) | Used as the existing exact CDF oracle. No duplicate implementation is introduced by this audit. |
| Factorial prime-power cardinal carrier; variance increment zero exactly at prime successor stages; stable source-clock lift | [Factorial Borwein hologram dossier](../../2026-10-19/FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md), FBH-01–07; [claim supplement](../../../docs/CLAIM_SUPPLEMENT_FACTORIAL_BORWEIN_HOLOGRAM.md) | These prime signatures already exist. A ratchet proposal must add transport or state, not rename FBH-03. |
| Summable repeated-prime-power widths and their limiting protected plateau | Same factorial dossier, FBH-01/06; [implementation](../../../observational_succ/factorial_borwein_hologram.py) | Cannot produce infinitely many fixed-unit support releases without a further clock, reset, or rescaling. |

The classical sinc/convolution provenance is D. Borwein and J. M. Borwein, *Some Remarkable Properties of Sinc and Related Integrals*, Ramanujan Journal **5** (2001), 73–89, especially Theorem 1 and its convolution proof ([primary paper](https://gwern.net/doc/math/humor/2001-borwein.pdf)). The finite-range random-walk interpretation is developed by S. N. Majumdar and E. Trizac, *When random walkers help solving intriguing integrals*, Physical Review Letters **123**, 020201 (2019), equations (3)–(6) ([primary preprint](https://arxiv.org/abs/1906.04545), [PDF](https://arxiv.org/pdf/1906.04545)). Their whole-line integral convention and the half-line convention below differ by a factor of two.

## 2. Shifted, normalized window theorem

**Status: PROVED LOCAL derivation, with classical Fourier/convolution ingredients.**

Fix a positive integer \(m\), positive real half-widths \(a_1,\ldots,a_m\), a window radius \(b>0\), and a shift \(c\in\mathbb R\). Let \(U_j\) be independent uniforms on \([-a_j,a_j]\), and put

\[
S_m=\sum_{j=1}^m U_j,\qquad A_m=\sum_{j=1}^m a_j,
\qquad \operatorname{sinc}(x)=\begin{cases}\sin(x)/x,&x\ne0,\\1,&x=0.\end{cases}
\]

Define the **dimensionless window mass**

\[
\boxed{
M_{b,m}(c)=\frac{2b}{\pi}\int_0^\infty
\operatorname{sinc}(bx)\cos(cx)
\prod_{j=1}^m\operatorname{sinc}(a_jx)\,dx
=\Pr\{|S_m+c|\le b\}.
}
\]

There are at least two sinc factors, so the integral is absolutely convergent: its integrand is bounded near zero and is bounded by a constant times \(x^{-(m+1)}\) away from zero.

**Derivation.** The characteristic function of \(S_m\) is \(\prod_j\operatorname{sinc}(a_jx)\). Independently convolve its law with a uniform on \([-b,b]\). The resulting continuous density at \(-c\) equals both

\[
\frac1{2b}\Pr\{|S_m+c|\le b\}
\quad\text{and}\quad
\frac1{2\pi}\int_{\mathbb R}e^{icx}
\operatorname{sinc}(bx)\prod_j\operatorname{sinc}(a_jx)\,dx.
\]

Symmetry cancels the imaginary part and halves the integral to the positive axis. Multiplication by \(2b\) proves the identity. The endpoint choices of the uniform densities do not affect their laws.

The density of \(S_m\) is positive on the interior \((-A_m,A_m)\), and its law has no atoms. Consequently the exact endpoint statements are

\[
\boxed{M_{b,m}(c)=1\iff A_m+|c|\le b,}
\qquad
\boxed{M_{b,m}(c)=0\iff |c|\ge A_m+b.}
\]

In all other cases, \(0<M_{b,m}(c)<1\). The non-strict inequalities are deliberate. At \(A_m+|c|=b\), the shifted support merely touches the window boundary and there is no lost mass. At \(|c|=A_m+b\), the supports only touch at one point, which has probability zero. Positivity on the support interior gives the converse implications.

### Degenerate inputs

The theorem assumes \(m\ge1\), positive widths, and \(b>0\). Zero widths can be deleted before applying it. If all widths are deleted, \(S_0=0\) has an atom: the single-sinc improper integral gives 1 for \(|c|<b\), 0 for \(|c|>b\), and **one half** for \(|c|=b\). The closed-window probability at that last point is 1. Thus the empty-bank endpoint must not be silently passed through the atomless theorem. A zero-radius window is outside the stated normalization and is not used.

For positive rational inputs, rescaling gives an implementation identity with the existing exact module:

\[
M_{b,m}(c;a_1,\ldots,a_m)
=M_{1,m}(c/b;a_1/b,\ldots,a_m/b).
\]

This preserves its declared finite resource budget; it does not remove the exponential cost of full subset enumeration.

## 3. Exact CDF and the shifted first-cap formula

**Status: PROVED LOCAL derivation; exact rational evaluation when the inputs are rational.**

For \(x_+=\max(x,0)\), the uniform-sum CDF is

\[
F_m(x)=\frac{1}{2^m m!\prod_{j=1}^m a_j}
\sum_{T\subseteq\{1,\ldots,m\}}(-1)^{|T|}
\left(x+A_m-2\sum_{j\in T}a_j\right)_+^m.
\]

To derive it, translate each uniform to \([0,2a_j]\). The unconstrained nonnegative simplex under a sum threshold has volume \(t_+^m/m!\); inclusion–exclusion subtracts the portions beyond each upper face. Division by \(\prod_j2a_j\) normalizes the rectangular density. Atomlessness then gives

\[
M_{b,m}(c)=F_m(b-c)-F_m(-b-c).
\]

Set

\[
\delta_+=A_m+c-b,\qquad
\delta_-=A_m-c-b,\qquad a_{\min}=\min_j a_j.
\]

If both \((\delta_+)_+\) and \((\delta_-)_+\) are at most \(2a_{\min}\), then

\[
\boxed{
1-M_{b,m}(c)=
\frac{(\delta_+)_+^m+(\delta_-)_+^m}
{2^m m!\prod_j a_j}.
}
\]

**Proof.** The upper tail \(S_m+c>b\) becomes
\(\sum_j(a_j-U_j)<\delta_+\). Its coordinates are independent uniforms on \([0,2a_j]\). At depth at most \(2a_{\min}\), this cap is a single corner simplex with volume \((\delta_+)_+^m/m!\). The lower tail gives the corresponding opposite corner with depth \(\delta_-\). The two events are disjoint because \(b>0\), so their probabilities add. At depth exactly \(2a_{\min}\), the simplex first touches a further face only on a set of zero volume; equality is therefore allowed. Beyond the declared depths, use the complete CDF rather than extrapolating the cap formula.

For the centered window, write \(\delta=A_m-b\). The result reduces to

\[
1-M_{b,m}(0)=\frac{\delta^m}{2^{m-1}m!\prod_j a_j}
\quad\text{when }0<\delta\le2a_{\min},
\]

with zero deficit when \(\delta\le0\).

## 4. Every first tooth has an exact simplex certificate

**Status: PROVED LOCAL. The support-threshold construction extends the earlier fixed-radius examples; no academic novelty is claimed.**

Let \((a_j)_{j\ge1}\) be a nonincreasing sequence of positive widths, and assume

\[
A_m=\sum_{j=1}^m a_j\longrightarrow\infty.
\]

For each positive integer tooth \(k\), define

\[
\tau_k=\min\{m\ge1:A_m>k\}.
\]

The divergence assumption makes every \(\tau_k\) finite. The window theorem identifies the same event as the **first departure from the radius-\(k\) plateau**:

\[
M_{k,m}(0)=1\text{ for }m<\tau_k,
\qquad M_{k,\tau_k}(0)<1.
\]

Write \(\delta_k=A_{\tau_k}-k\). Minimality gives

\[
0<\delta_k\le a_{\tau_k}
=\min_{j\le\tau_k}a_j.
\]

Thus **every first crossing automatically lies in the valid single-simplex regime**, and

\[
\boxed{
1-M_{k,\tau_k}(0)
=\frac{\delta_k^{\tau_k}}
{2^{\tau_k-1}\tau_k!\prod_{j=1}^{\tau_k}a_j}.
}
\]

The theorem does not assert that the next several stages remain in that regime. Monotonicity of the widths is used to identify the last width with the minimum; it must not be removed without replacing that step by a valid cap-depth check.

### Strict releases, equality, and a finite program

At stage \(m\), the exact number of released positive-integer teeth is

\[
\boxed{
L_m=\#\{k\in\mathbb Z_{>0}:k<A_m\}
=\max\{0,\lceil A_m\rceil-1\}.
}
\]

It is nondecreasing. **Using \(\lfloor A_m\rfloor\) instead is incorrect at positive integer values of \(A_m\)**: when \(A_m=k\), the radius-\(k\) integral is still on its plateau. For a nonnegative rational \(A_m=u/v\) with positive denominator, exact integer arithmetic evaluates the release count as

```python
released = max(0, (u - 1) // v)
```

If the width sequence has a finite rational-generating program, the state update `A += next_width` and this strict comparison give a finite-program event enumerator. Each requested tooth is found after finitely many updates, as proved above. No tiny integral has to be resolved by floating-point quadrature. Program size is finite; elapsed work and rational-state size are not asserted to be uniformly bounded. No completed traversal of infinitely many stages is represented as an executed computation.

This is a record of an expanding **possible-displacement support**. Its direction comes from the monotone budget and remembered release state. It does not say that an unbiased random trajectory drifts around a cylinder. An angular coordinate such as \(e^{2\pi iA_m}\) can be attached to that state, but it adds no new arithmetic discrimination.

### Choice of bank matters

For \(a_j=1/(2j+1)\), the budget diverges, since \(a_j\ge1/(3j)\). All teeth therefore release. The odd-prime reciprocal bank also has divergent total width by the classical divergence of the prime reciprocal sum, but generating it already requires authentic prime sources.

The repository's repeated-factorial prime-power bank is different. Its total twice-half-width is uniformly less than \(11/12\), and its limiting width sum is finite. Its protected central plateau is designed to survive. That unchanged bank cannot realize the all-tooth hypothesis above. A reset, rescaling, or separate divergent budget would be an additional declared construction.

## 5. Exact finite calibration and first three teeth

**Status: OBSERVED exact finite execution on 2026-11-12, supported by the displayed algebra. These receipts do not replace the universal proof in Section 4.**

For \(a_j=1/(2j+1)\), exact `Fraction` accumulation gives:

| Tooth \(k\) | First stage \(\tau_k\) | Last denominator | Exact certificate |
| --- | ---: | ---: | --- |
| 1 | 7 | 15 | \(A_6<1<A_7\) |
| 2 | 56 | 113 | \(A_{55}<2<A_{56}\) |
| 3 | 418 | 837 | \(A_{417}<3<A_{418}\) |

The following are **strict rational brackets**, not uncertified decimal approximations. In each table cell, the stated integer is a lower numerator \(q\), with the certificate \(q/10^{15}<A<(q+1)/10^{15}\).

| Tooth | Lower numerator for \(A_{\tau_k-1}\) | Lower numerator for \(A_{\tau_k}\) |
| --- | ---: | ---: |
| 1 | 955133755133755 | 1021800421800421 |
| 2 | 1994437501289942 | 2003287058812066 |
| 3 | 2999495848508641 | 3000690591638868 |

For the first tooth, the complete small rational data are

\[
A_6=\frac{43024}{45045},\qquad
A_7=\frac{46027}{45045},\qquad
\delta_1=\frac{982}{45045}<\frac1{15}.
\]

The normalized deficit is

\[
\boxed{
1-M_{1,7}(0)
=\frac{6879714958723010531}
{467807924720320453655260875000}
\approx1.4706281350056343375\times10^{-11}.
}
\]

Accordingly,

\[
\int_0^\infty\operatorname{sinc}(x)
\prod_{j=1}^7\operatorname{sinc}\!\left(\frac{x}{2j+1}\right)dx
=\frac\pi2
\frac{467807924713440738696537864469}
{467807924720320453655260875000}.
\]

The audit executed the independently written simplex expression, the existing full inclusion–exclusion CDF through `borwein_window_mass`, and the existing `first_boundary_leak` helper. All three returned the same exact rational deficit. The two legacy APIs share their repository provenance; their agreement is not three independent witnesses. The direct corner-simplex derivation and the full CDF are the two different mathematical decompositions checked here.

Reproduce the finite calibration from the repository root:

```python
from fractions import Fraction as F
from math import factorial, prod
from observational_succ.borwein_prime_clock import (
    borwein_window_mass, first_boundary_leak,
)

widths = tuple(F(1, 2*j + 1) for j in range(1, 8))
delta = sum(widths, F()) - 1
simplex = delta**7 / (2**6 * factorial(7) * prod(widths))
assert simplex == F(
    6879714958723010531, 467807924720320453655260875000
)
assert simplex == 1 - borwein_window_mass(widths)
assert simplex == first_boundary_leak(widths)

expected = {7: (1, 955133755133755, 1021800421800421),
            56: (2, 1994437501289942, 2003287058812066),
            418: (3, 2999495848508641, 3000690591638868)}
A = F()
D = 10**15
for m in range(1, 419):
    before = A
    a = F(1, 2*m + 1)
    A += a
    if m in expected:
        k, before_lo, after_lo = expected[m]
        assert before <= k < A
        assert 0 < A - k <= a
        assert F(before_lo, D) < before < F(before_lo + 1, D)
        assert F(after_lo, D) < A < F(after_lo + 1, D)
```

The stage counts use only exact support arithmetic, so the legacy module's 11-width CDF budget is not exceeded to evaluate stages 56 or 418. No numerical integral at those stages was asserted to have been measured.

## 6. A mass score is not automatically a ratchet

**Status: PROVED LOCAL inequalities and exact counterexamples.**

The density of a sum of centered uniform variables is symmetric and nonincreasing with distance from zero. This follows inductively: averaging a symmetric unimodal density \(f\) over \([x-a,x+a]\) has, almost everywhere for \(x>0\), derivative proportional to \(f(x+a)-f(x-a)\le0\).

For a centered window, let

\[
h(u)=\int_{-b}^b f(y-u)\,dy.
\]

It is even and satisfies \(h'(u)=f(b+u)-f(b-u)\le0\) for \(u\ge0\), wherever the derivative exists. Hence adding an independent centered uniform cannot increase the centered mass: its new value is \(\mathbb E h(U)\le h(0)\). This gives non-strict monotonicity, not a release at every step.

Two exact hostile controls were executed against the existing CDF:

| Proposed overclaim | Counterexample, with radius \(b=1\) |
| --- | --- |
| Every added nonzero width strictly decreases centered mass | Width `(3,)` has mass \(1/3\); `(3,1/2)` also has mass \(1/3\). |
| Shifted mass always decreases as widths accumulate | At shift \(c=9/4\), width `(1,)` has mass 0; adding the smaller width \(1/2\) raises it to \(1/64\). |

Moreover, the centered increment characteristic function \(\prod_j\operatorname{sinc}(a_jt)\) is even and contains no preferred orientation. The product is unchanged by reordering the widths. An arithmetic label or a directed update rule must be retained explicitly if the construction is supposed to observe more than this symmetric convolution.

## 7. Optional actual rectification: a separate stochastic model

**Status: PROVED LOCAL probability theorem under independent increments and deterministic positive widths. This is an ideal mathematical rectifier, not an inferred physical mechanism.**

Let \(U_j\sim\mathrm{Unif}[-a_j,a_j]\) be independent as above, and explicitly change the increment law to

\[
Y_j=\max(U_j,0),\qquad X_m=\sum_{j=1}^m Y_j.
\]

The law of \(Y_j\) has an atom of mass \(1/2\) at zero and density \(1/(2a_j)\) on \((0,a_j)\). Therefore

\[
\boxed{
\mathbb E e^{itY_j}
=\frac12+\frac12e^{ita_j/2}\operatorname{sinc}(ta_j/2),
\qquad
\mathbb E Y_j=\frac{a_j}{4},
\qquad
\operatorname{Var}(Y_j)=\frac{5a_j^2}{48}.
}
\]

The characteristic function follows by integrating \(e^{ity}\) on \([0,a_j]\). Direct integration gives \(\mathbb E Y_j^2=a_j^2/6\), so the stated variance is \(a_j^2/6-a_j^2/16\). The complex phase in this characteristic function comes from the explicitly positive increments; it was not present in the symmetric sinc law.

### Exact divergence criterion

For every deterministic sequence of positive widths,

\[
\boxed{
X_m\longrightarrow\infty\ \text{almost surely}
\iff \sum_{j=1}^\infty a_j=\infty.
}
\]

If the width sum is finite, \(0\le X_m\le\sum_j a_j\) on the bounded-increment sample space, so divergence is impossible.

For the converse, fix \(s>0\), and write \(\ell_j=\mathbb E e^{-sY_j}\). Because \(\Pr(Y_j\ge a_j/2)=1/4\),

\[
1-\ell_j
=\mathbb E(1-e^{-sY_j})
\ge\frac14(1-e^{-sa_j/2})
\ge c_s\min(a_j,1),
\quad
c_s=\frac{1-e^{-s/2}}4>0.
\]

The last inequality follows from concavity on \([0,1]\) and monotonicity beyond 1. If \(\sum_j a_j=\infty\), then \(\sum_j\min(a_j,1)=\infty\). Independence and \(1-u\le e^{-u}\) yield

\[
\mathbb E e^{-sX_m}=\prod_{j=1}^m\ell_j
\le\exp\left(-\sum_{j=1}^m(1-\ell_j)\right)
\longrightarrow0.
\]

Since \(X_m\) increases to an extended nonnegative random variable \(X_\infty\), bounded convergence gives \(\mathbb E e^{-sX_\infty}=0\), with \(e^{-s\infty}=0\). Thus \(X_\infty=\infty\) almost surely. No square-summability hypothesis was needed for this divergence proof.

This model supplies genuine unbounded monotone displacement. For any fixed period \(h>0\), its winding record \(\lfloor X_m/h\rfloor\) is unbounded almost surely. Thresholds can be overshot; exact visits to every real boundary are not asserted. Its individual event times are random, and they are different from the deterministic support times \(\tau_k\).

For the unrectified odd-reciprocal walk, \(\sum_j a_j^2<\infty\) and centered independent increments instead give almost-sure convergence, as already distinguished in BDW-05. The same divergent support budget therefore permits a convergent symmetric trajectory and an unbounded explicitly rectified trajectory. Which process is meant must be declared.

Specifying a probability law by a finite program does not specify every random sample path with finite information. Neither model furnishes primality information that was absent from its width sources and gates.

## 8. Claim ledger and next discriminators

| Claim | Verdict and boundary | Next useful discriminator |
| --- | --- | --- |
| Shifted normalized mass and exact endpoint rules | **PROVED LOCAL**, \(m\ge1,a_j>0,b>0\); empty-bank boundary isolated | Test radius rescaling and both support-touch equalities with exact rational inputs. |
| Two shifted shallow caps | **PROVED LOCAL** within both depth bounds | Mutate a cap beyond \(2a_{\min}\); the full CDF must reject the extrapolated shortcut. |
| Every tooth of a decreasing divergent bank has a first-simplex certificate | **PROVED LOCAL** for all positive integer teeth | Remove width monotonicity or divergence and exhibit the failed hypothesis. |
| Strict release count | **PROVED LOCAL** with equality convention explicit | Mutation `floor(A)` must fail at every positive integer support budget. |
| First three odd-reciprocal tooth indices and first deficit | **OBSERVED exact finite computations**, with exact inequalities and reproducible derivation | Independent arithmetic implementation; use source prefixes beyond the fitted three stages. |
| Symmetric sinc convolution supplies directed trajectory drift | **REFUTED as an inference**; even increment law and convergent square-summable-width walks are concrete controls | State and test the actual directional update before assigning it a current. |
| Positive-part rectifier diverges almost surely exactly for divergent total widths | **PROVED LOCAL** under independent, deterministic-width increments | Audit independence if widths become feedback-dependent; the product proof then needs replacement. |
| These support or rectification results prove a new prime correlation theorem | **UNVERIFIED**; no such implication has been derived | Retain authentic arithmetic gates and derive a new source-sensitive uniform estimate. |

The demonstrated gain is an exact, indefinitely extensible event clock and a separately proved way to add directed motion. The remaining arithmetic burden lies in the source-sensitive coupling: a width-only release schedule cannot distinguish integers whose residue or factor data were never supplied to it.

## 9. Integration review of the cylinder-ratchet dossier

**Status: mathematical review of [BORWEIN_RATCHET.md](BORWEIN_RATCHET.md), 2026-11-12. Same-model review is not independent external refereeing.** The all-tooth theorem, source lift, finite non-star coefficient filter, and observation-error model survive the following checks. Two explicit domain/normalization corrections were requested from the owner of that document.

**Resolution observed:** a subsequent read of the dossier confirms the unit correction to `B(C)+(1/2)E_11` and an explicit switch to the full positive-integer carrier before applying multipliers to `e_1`. Its centered-series convergence argument is now also included directly. The two requested mathematical corrections are resolved in that reviewed version.

### Required correction: fixing the unit

On the full positive-integer carrier, the canonical functional-calculus filter has

\[
T=B(N_\Omega-I)=\tfrac12P_0+P_1+\tfrac12P_2,
\qquad P_0=E_{11}.
\]

Thus \(Te_1=e_1/2\). Adding \(E_{11}\) to this canonical extension gives eigenvalue \(3/2\), so it does **not** fix the unit. The correct prime-and-unit variant is

\[
\boxed{T_{\mathrm{unit}}=T+\tfrac12E_{11}
=P_0+P_1+\tfrac12P_2.}
\]

If a zero extension from \(\ell^2(\{2,3,\ldots\})\) is chosen instead, adding \(E_{11}\) works, but that intermediate extension must be stated: it is not \(B(N_\Omega-I)\) on the unit. Likewise, changing the coefficient filter to fix the identity multiplier would change its fixed-space statement; the unmodified commutator condition \([N_\Omega,X]=X\) does not fix the identity.

### Required clarification: multiplier carrier

The finite multipliers \(V_d\) are linearly independent on either positive-integer carrier. On \(\ell^2(\{2,3,\ldots\})\), apply a finite linear relation to \(e_2\), obtaining distinct vectors \(e_{2d}\). Applying it to \(e_1\) requires first switching explicitly to \(\ell^2(\mathbb N_{>0})\). This is a domain correction, not a failure of the coefficient-filter theorem. On the declared finite non-star algebra,

\[
[N_\Omega,V_d]=\Omega(d)V_d
\]

and the scalar gate equals one exactly for \(\Omega(d)=1\). Hence its fixed space is precisely the finite span of prime multipliers. No extension to arbitrary operators, adjoints, or positive coefficient maps follows.

### Deadline and asymptotic checked

For a dyadic block \(r\le j\le2r-1\),

\[
\sum_{j=r}^{2r-1}(2j+1)=3r^2,
\qquad
\sum_{j=r}^{2r-1}\frac1{2j+1}\ge\frac13.
\]

Cauchy–Schwarz is strict for \(r>1\), since the denominators are then unequal. There are \(3k\) such blocks in \(1\le j\le8^k-1\), including a strict block for every \(k\ge1\). Therefore \(A_{8^k-1}>k\), proving the stated deadline \(\tau_k\le8^k-1\).

The exact identity

\[
A_m=H_{2m+1}-\tfrac12H_m-1
=\tfrac12\log m+\log2+\tfrac\gamma2-1+o(1)
\]

and the first-crossing bound \(0<A_{\tau_k}-k\le1/(2\tau_k+1)\to0\) give

\[
\tau_k\sim\frac{e^{2-\gamma}}4e^{2k}.
\]

The overshoot estimate is the step that transfers the harmonic-sum asymptotic to the first-crossing index. No uniform numerical accuracy for small \(k\) is implied by this asymptotic.

### Lift and observation interface checked

For \(n-1=Lh+r\), multiplication gives
\(dn-1=d(Lh+r)+d-1\). Quotient and remainder by \(L\) therefore yield the stated affine lift, including its necessary \(d-1\). Direct substitution gives \(V_dS=S^dV_d\). The retained pair \((h,r)\) recovers \(n\); the angular residue alone does not.

Under arbitrary report errors bounded in absolute value by \(\epsilon\), masses \(1\) and \(1-\lambda\) permit overlapping reports exactly when \(2\epsilon\ge\lambda\). Thus \(\epsilon<\lambda/2\) is the correct guarantee for the specified interval-error interface. It is not a lower bound for an observer supplied with exact source widths or a different oracle.

### Additional leakage decimals recalculated

Using exact `Fraction` support sums and products, then evaluating the resulting rational with 30-digit `Decimal` arithmetic, the three first-release deficits were

```text
1.47062813500563433751188711782e-11
1.48487080919097812273873474842e-138
2.87721670250524992479296682188e-1320
```

These agree with the dossier's illustrative decimals. The first scratch calculation incorrectly initialized the product accumulator to zero and raised `ZeroDivisionError`; it produced no leakage values. Initializing it to `Fraction(1)` corrected that audit script. The rerun produced all three values above. No repository implementation was changed in this check.

## 10. Centered rectified displacement: the missing maximal-inequality argument

**Status: PROVED LOCAL, under the independent deterministic-width model of Section 7 and the additional condition \(\sum_j a_j^2<\infty\).** Put

\[
Z_m=X_m-\tfrac14A_m=\sum_{j=1}^m(Y_j-a_j/4),
\qquad \sigma_j^2=5a_j^2/48.
\]

Independence gives \(\mathbb E|Z_N-Z_M|^2=\sum_{j=M+1}^N\sigma_j^2\). Hence the partial sums are Cauchy in \(L^2\), and completeness supplies an \(L^2\) limit.

For almost-sure convergence, the elementary maximal inequality for independent mean-zero partial sums gives

\[
\Pr\!\left(\max_{M<n\le N}|Z_n-Z_M|>\eta\right)
\le\eta^{-2}\sum_{j=M+1}^N\sigma_j^2.
\]

To verify the inequality, partition its event by the first threshold-crossing index \(n\). That event depends only on increments through \(n\), and the later increment sum has conditional mean zero. The expected final square on that event is therefore at least the expected square at the crossing, which is at least \(\eta^2\) times the event probability. Sum over the disjoint crossing events and bound by the unconditional final second moment.

Choose an increasing sequence \(M_q\) with \(\sum_{j>M_q}\sigma_j^2\le2^{-4q}\). Apply the inequality with \(\eta=2^{-q}\), and let \(N\) tend to infinity. The probability that any later partial sum differs from \(Z_{M_q}\) by more than \(2^{-q}\) is at most \(2^{-2q}\). These bounds are summable, so the elementary first Borel–Cantelli argument shows that eventually every such tail stays within that radius. The full partial-sum sequence is consequently Cauchy almost surely. Its almost-sure limit agrees with its \(L^2\) limit by uniqueness of limits in probability. Thus

\[
\boxed{X_m-\tfrac14 A_m\longrightarrow Z
\quad\text{almost surely and in }L^2.}
\]

For the odd reciprocal widths, square summability holds. The same argument with centered increments \(U_j\) and variances \(a_j^2/3\) proves convergence of the unrectified walk. The two opposite displacement conclusions are therefore supported within one explicitly declared model, rather than inferred from support geometry.
