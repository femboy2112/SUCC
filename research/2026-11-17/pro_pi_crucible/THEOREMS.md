# Exact objects and theorem ledger

## 1. Immutable source and target

Every original-source assertion uses, for integer n>=1,

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Set x=pi/16 and

\[
T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,\qquad U_n+T_n=16^nx.
\]

The last evaluation is the imported classical BBP identity. The positive
decreasing source integral gives T_n<r(n+1)/15. No substitute source or
random prime clock is an input to an original-source assertion.

For each integer B>=1,

\[
\mathcal R_B=\frac1B\sum_{k=1}^B\|U_{2B}/16^k\|_{\mathbb T}^2,\qquad
\widehat\mu_B=\frac1B\sum_{k=1}^B\delta_{\{U_{2B}/16^k\}}.
\]

Let D_B,J_B be the inherited last-B hexadecimal non-extreme digit and direct
0/F transition counts in floor(U_(2B)). The #657/#662 identities imply

\[
\mathrm{R0}\iff\liminf_B\mathcal R_B>0
\iff\liminf_B(D_B+J_B)/B>0.
\]

For L(t)=162/289 (||t||_T-1/18)_+^2 and Haar probability m, put

\[
\widehat\Delta_B=\|L*\widehat\mu_B-256/7803\|_\infty.
\]

Full base-16 pi normality is equivalent to its zero limit. #663 supplies
the equivalent rational squared-kernel energy gate. These are inherited
equivalences; none of the desired limits is established here.

## 2. New original-source arithmetic

| ID | Universal statement | Full proof |
|---|---|---|
| EPS-01 | If p divides L_n, p>7, p^2>8n and p^2>=19*32^K for K=floor((8n-2)/p), then v_p(U_n)=-1. | [Prime survival](EFFECTIVE_PRIME_SURVIVAL.md), sections 2--4 |
| EPS-02 | For each A>20 log 2, all born primes p>=A n/log n survive for every sufficiently large n, with an effective threshold. | Same, section 5 |
| EPS-03 | Q_n divides L_n and log(L_n/Q_n)=O(n/log n), with the explicit finite Y-bound. | Same, section 6 |

L_n is the LCM of the four native odd lanes; Q_n is the reduced denominator.
All four signed chronological contributions are retained. Nonzero rational
coefficients are not presumed nonzero modulo p: the numerator-height bound
pays that step. Small primes, higher powers and cancellations are charged.

**Authority:** Disclosed within the stated domain by paper proof, checked by
a separate same-model derivation and two exact implementations. Neither
external priority nor formal verification is claimed.

**Novelty boundary:** CG-01 already gives rate-6 denominator growth and
fixed-epsilon prime survival. The new growing packet-depth height estimate
lowers the cutoff to order n/log n. It does not restrict floor(U_n) modulo
radix powers. This is auxiliary arithmetic, not category D/E for coercivity.

## 3. Quantitative swept-filter instrument

For any circle probability mu, put nu=mu-m, g=L*nu and Delta=||g||_infinity.
Let tau be the half-turn and P convolution by the uniform probability on the
arc of radius 1/18 centered at the antipode. Then

\[
(I+P/8)\nu=-\frac{289}{288}\tau g'',\qquad
\nu=-\frac{289}{288}\sum_{j\ge0}(-P/8)^j\tau g''.
\]

The series converges in signed-measure total variation. For h!=0,

\[
\frac{63}{289\pi^2h^2}\le|\widehat L(h)|
\le\frac{81}{289\pi^2h^2},\qquad
\operatorname{sgn}\widehat L(h)=(-1)^h.
\]

For every probability mu,

\[
D_{\rm arc}(\mu)\le\min\{1,(34/7)\sqrt\Delta\}.
\]

Exponent 1/2 is optimal; optimality of the constant is not claimed.
The densities 1+cos(2 pi Ht) prove sharpness and disprove a continuous
inverse from swept supremum norm into total variation.

For the actual completed BBP shell mu_B, the original positive tail gives

\[
D_{\rm arc}(\mu_B)^2
\le\frac{1156}{49}\left(\widehat\Delta_B+
\frac{16r(2B+1)}{7225B}\right).
\]

This exact rational right side bounds the square of every word-frequency
error at a chosen shell. Full proofs, including atomic limits, are in
[BORWEIN_INVERSE.md](BORWEIN_INVERSE.md).

**Novelty tax:** instrument identity/stability (A) and finite certificate
(C when evaluated). The factor 1/8 acts in origin space, not chronological
time. #663 already has an L2-energy all-word certificate; the measure inverse
and sharp supremum-to-interval bound are distinct refinements.

For V=integral |g|^2 the additional direct estimate is

\[
D_{\rm arc}(\mu)^5\le\frac{144324288}{16807}V.
\]

Exponent 1/5 is optimal. Moving a centered interval of mass epsilon into a
point gives discrepancy epsilon and energy O(epsilon^5). The proof uses
semiconcavity, the mean-zero Lipschitz tent and the exact inverse, with no
Erdős--Turán import. For any rational q_B>=0 with q_B^2>=Vhat_B, it gives

\[
D_{\rm arc}(\mu_B)^5
\le\frac{144324288}{16807}(q_B+\epsilon_B)^2.
\]

See [BORWEIN_ENERGY_STABILITY.md](BORWEIN_ENERGY_STABILITY.md). This improves
the V^(1/6) static stability rate stated in pinned #663, without estimating
the authentic energy as B grows. It remains instrument mathematics.

## 4. Hostile theorems and exact quantifiers

**GSC.** For each fixed M>=1 there are positive completely monotone rational
sources f_B with zero seed, converging to r, whose completed Hankel forms
obey a relative 1+O_M(16^-B) comparison simultaneously at every degree.
They retain the original four residues, every weighted shift-orbit obstruction
and all but eight Gamma activation values. Nonetheless at their selected shell,

\[
D_B(f_B)=J_B(f_B)=0,\quad
\mathcal R_B(f_B)<16^{-2B}/(255B),\quad
\widehat J_B^{f_B}(0)=0,\quad\widehat\Delta_B(f_B)>3/40.
\]

See [GAMMA_POSITIVE_SOURCE_SHELL_CLONE.md](GAMMA_POSITIVE_SOURCE_SHELL_CLONE.md).
This refutes a locally uniform neighborhood bridge. The source varies with
B; a fixed-counterfeit all-late-shell conclusion is not claimed. Extra
shifted poles disclose the source change.

**H-01--04.** For each arbitrary finite prefix length M, a finite rational
algorithm constructs one positive decreasing rational-valued zero-seeded
source r_tilde, equal through M, with

\[
|\widetilde r(n)-r(n)|
<\frac{17}{1024}16^{-n^2}(r(n)-r(n+1)).
\]

Its completed endpoint belongs to Z[1/16], every late terminal suffix is
all-F, and its norm is asymptotic to 1/(16711680 B^5). An entire interpolant
preserves exactly the four finite clock poles/principal parts and every
real-axis asymptotic derivative. It does not preserve the original rational
function or global complex growth. An exact high-order negative alternating
difference rejects a positive Hausdorff moment representation for the
concrete M=0 counterfeit.

See [SUPEREXPONENTIAL_LOCKED_SOURCE.md](SUPEREXPONENTIAL_LOCKED_SOURCE.md).
The simultaneous all-order match and radix lock strengthen the inspected
CAT-12/13 and TW-07 constructions. Do not combine incompatible properties
of this counterfeit and GSC.

**GG-01.** A single integer gauge of the authentic full history preserves
the completed pi orbit and all fractional states while erasing every raw
even-terminal suffix. Its large transformed tail invalidates the original
small-tail comparison in that gauge. See [CRUCIBLE.md](CRUCIBLE.md).

## 5. Failed bridges

- Complete fractional prime data do not determine integer winding: GG-01
  and the inherited cofactor clone retain them.
- Uniformly close all-degree Gamma moment geometry does not give locally
  uniform source-neighborhood coercivity: GSC.
- All real asymptotic coefficients and finite clock poles do not imply R0
  in the broader meromorphic class: H-01--03.
- The flat locked counterfeit fails the full positive moment cone: H-04.
- A spatial Neumann inverse does not mix periodic measures in time.

No RH, zeta value, Gamma positivity, prime coincidence or numerical trend
was converted into a normality claim.
