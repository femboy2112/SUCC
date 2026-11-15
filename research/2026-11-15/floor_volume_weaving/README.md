# A sharp maximum-law bridge to the BBP carry gate

**Parent:** draft [#647](https://github.com/femboy2112/SUCC/pull/647),
`fec5cdda24ca36328e123b0b367a0628491e1eb8`.
**Status:** exact finite inequalities, explicit probability constructions, and
source-attached integral identities. The original positive carry-density
estimate and pi normality remain **OPEN**.

The user's `11,11,3,3 = 7 +/- 4` and `sqrt(U) = max(U1,U2)` observations led to
a useful positive result. A square-root maximum law can leave orientation
undetermined and still force enough of the required orientation to prevent
the fourth-root carry gate from locking. The key is to attach the law to the
correct source coordinates and retain one cofactor marginal.

## 1. Main finite theorem: three masses suffice

For any random labels `J,K in {0,1,2,3}`, define

\[
d=\Pr((J-K)\bmod4\in\{1,2\}),\quad
F_1=\Pr(J=K=0),\quad F_2=\Pr(J<2,K<2),\quad c_1=\Pr(K=1).
\]

Then, with no independence or marginal assumptions,

\[
\boxed{d\ge F_1+c_1-F_2.}
\]

This is an exact sixteen-cell indicator inequality. Therefore

\[
F_1=1/16,\quad c_1=1/4,\quad F_2=1/4
\quad\Longrightarrow\quad d\ge1/16.
\]

If `X,Y` have uniform marginals and `max(X,Y)` has the law of `sqrt(U)`,
these three conditions hold for `J=floor(4X),K=floor(4Y)`. Independence is
unnecessary. The lower bound is sharp even under the **full continuous**
maximum law: an explicit absolutely continuous joint density attains it.
Under those full hypotheses the exact attainable interval is
`1/16 <= d <= 7/8`. Thus the same radial law permits different signed
carry responses while excluding total lock.

The robust version is equally finite:

\[
F_1\ge1/16-\eta_1,\quad c_1\ge1/4-\kappa,\quad
F_2\le1/4+\eta_2
\quad\Longrightarrow\quad
d\ge1/16-\eta_1-\kappa-\eta_2.
\]

See [the elementary proof and slack identity](THREE_MASS_ANTI_LOCK.md) and
[the sharp continuous controls](MAX_GATE_CERTIFICATE.md).

### Literal source attachment

Keep the authentic original recurrence

\[
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\]

and `U_n=C_n+y_n`, with `C_n=floor(U_n)`. The inherited source clock gives

\[
J_n=n\bmod4,\qquad K_n=[y_n]_4,\qquad C_n\equiv J_n-K_n\pmod4.
\]

Here `[y_n]_4` is reduction of the **odd-denominator rational** cofactor in
the dyadic ring. It is not `floor(4y_n)`. Apply the finite theorem to the
empirical distribution on any integer shell `[B,2B)`:

\[
\boxed{\frac1B\#\{B\le n<2B:C_n\bmod4\in\{1,2\}\}
\ge F_{1,B}+c_{1,B}-F_{2,B}.}
\]

Proving an eventual positive lower bound for the right side would prove the
current anti-lock target. Its three source estimates have **not** been proved.
This criterion requires neither all-depth carry Haar nor a Markov law for BBP.

## 2. The algebra of the period-four pattern

Put `s(n)=(-1)^floor(n/2)`. For every integer `n`,

\[
s(n)=(-1)^{n(n-1)/2}=\Re((1-i)i^n),\qquad
s(m+n)=s(m)s(n)(-1)^{mn}.
\]

The source's derivative residue is represented by `d(n)=7+4s(n)`, namely
11 or 3. The real carry sign is `w(C)=s(C+1)=(-1)^(C(C+1)/2)`.
These are respectively Clifford **reversion** and **conjugation** grade
signs. They are Walsh characters under bitwise XOR and quadratic phases
under ordinary integer addition. The carry changes the addition law.

On the source clock/cofactor labels,

\[
w(C_n)=s(J_n+1)s(K_n)(-1)^{J_nK_n}.
\]

The bilinear factor retains the joint coupling. See
[period-four algebra and source transport](PERIOD_FOUR_NOTES.md).

## 3. A constructive weave, with its orientation exposed

Draw independent uniform `U,V`, set `R=sqrt(U)` and `L=RV`, then use a fair
coin to orient `(R,L)`. The result is two independent uniforms, with maximum
equal to `sqrt(U)` **pathwise in that construction**. Radius, ratio, and
orientation specify the whole pair.

More generally, `U^(1/d)` is the maximum of `d` independent uniforms in law.
It is also the radial norm of a uniformly sampled point in the unit ball of
**any norm on R^d**, because that ball's radius-r volume is `r^d` times its
unit volume. If that volume is `V`, radial integration gives

\[
\int_{\mathbb R^d}e^{-\|x\|^p}\,dx
=dV\int_0^\infty r^{d-1}e^{-r^p}\,dr
=V\Gamma(1+d/p),\qquad p>0.
\]

This is an explicit volume-to-Gamma mechanism. The radial law alone does not
specify the direction or ordered coupling of the underlying vector.

For the quarter signs `a=(++--)`, `c=(+--+)`, define

\[
G(x,y)=a(x)c(y)-c(x)a(y),\qquad
p_\epsilon(x,y)=1+\epsilon G(x,y),\quad |\epsilon|\le1/2.
\]

A conditional orientation coin realizes this density. Every symmetric pair
observable has the same law as for independent uniforms, but

\[
\mathbb E G=2\epsilon,\quad \mathbb E G^2=2,\quad
\mathbb E w(\lfloor4X\rfloor-\lfloor4Y\rfloor)=-\epsilon.
\]

Its stationary Markov realization has `phi=a+ic`, `P phi=i epsilon phi`,
so its ordered lag response contains exactly
`epsilon^k (-1)^floor(k/2)`. This is a declared classical construction.
The source transport `i^C = conjugate(phi(J))*phi(K)/2` is exact, but the
Markov transition law has not been assigned to BBP. See
[ordered weaving and calibrated controls](WEAVING_ADVERSARY_NOTES.md).

## 4. The floor/Gamma integral is explicit and source-attached

The inherited positive source factorization gives, for `a=8n-7`,

\[
r(n)=\sum_{j=0}^4q_j\mathrm B(a+j,2)
=\sum_{j=0}^4q_j\frac{\Gamma(a+j)}{\Gamma(a+j+2)},
\qquad(q_j)=(4,4,4,2,1).
\]

Each normalized branch has the exact construction
`Beta(k,2) = V1^(1/k) V2^(1/(k+1))` in distribution: its negative logarithm
is the sum of independent exponential waiting times with rates `k,k+1`.
The `+2` is a Gamma-argument shift; arithmetic `n -> n+1` shifts `a` by eight.
In the logarithmic coordinate, the maximum construction is a parallel race:
`-log(max(U1,U2))=min(E1,E2)`, an exponential clock of rate two. The Beta
branch uses serial waits `Exp(k)+Exp(k+1)`. Its scaled limit is Gamma(2).
Thus the rule coupling the two components determines which integral law emerges.
Two positive branches individually have 2-adic valuation `-1`; their sum has
odd denominator. A valid carrier model must retain that reassembly.

Floor is an integral against an atomic counting measure. For the actual gate
`A(x)=1_{floor(x) mod4 in {1,2}}`, interval integration gives

\[
\int_0^\infty e^{-tx}A(x)\,dx=\frac1{2t\cosh t},\qquad t>0.
\]

Its exponential-probe probability is `p(t)=1/(2 cosh t)`, with

\[
\int_0^\infty t^{s-1}p(t)\,dt=\Gamma(s)\beta(s),\quad\Re s>0;
\qquad \int_0^\infty p(t)\,dt=\pi/4.
\]

Here `beta=L(s,chi_4)` is Dirichlet beta. Its odd character parity differs
from zeta's. Applying this mask to the original normalized four-pole
log-source yields the explicit formula in
[VOLUME_CONSTRUCTOR_NOTES.md](VOLUME_CONSTRUCTOR_NOTES.md), V14. Its native
Gamma(2) limiting gate probability is
`2 exp(-1)/(1+exp(-2))^2`, approximately `0.57080431`, rather than `1/2`.
That auxiliary source law must not replace the deterministic orbit law.

## 5. Evidence, novelty, and next step

- [Independent exact audit](independent_audit.py) and
  [machine-readable receipt](receipts/independent_audit.json): no production
  imports, exact rational/polynomial certificates and mutation controls.
- The inherited 32,768 certified carries are reanalyzed, not presented as
  newly generated digits. An independent original-rational recurrence checks
  the first 512 residues. On the last shell `[16384,32768)`, the new
  three-mass lower bound is exactly `1/16`; the actual selected fraction is
  `4089/8192`. This is finite evidence, not an eventual source estimate.
- [Validation](VALIDATION.md), [provenance and prior art](PROVENANCE.md), and
  [claim ledger](CLAIM_LEDGER.json) distinguish exact theorems, inherited
  identities, finite observations, controls, and open source estimates.
- [Next source obligation](NEXT.md): prove a uniform eventual one-sided
  defect budget below `1/16` for the three declared empirical masses.

The positive kernel, Beta product identities, and earlier floor integration
are inherited or classical. The central result of this round is the **sharp
maximum-law anti-lock certificate**, its minimal source attachment, and the
explicit controls showing both what the radial law forces and what it leaves
undetermined. No academic-priority claim is made.
