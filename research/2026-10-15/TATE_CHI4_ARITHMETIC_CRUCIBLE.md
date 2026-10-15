# The ramified chi4 Tate test and its complete theta reconstruction

**Date:** 2026-10-15. **Status:** CLASSICAL, DERIVED with exact finite source
interfaces and adversarial certificates. **RH/GRH proved: NO.**

This note reconstructs a primitive odd Dirichlet character through the actual
adelic Schwartz–Bruhat and idelic Mellin maps. Its analytic results are classical
Tate/Hecke theory. The contribution to SUCC is the commuting source interface,
including the ramified place that an Euler product alone cannot expose, and
the explicit distinction between exact finite witnesses and analytic estimates.

The source functions below have declared mathematical provenance. They are not
new physical measurements. No nontrivial zero locations are inputs.

## 1. Dependencies, conventions and the object being reconstructed

We use the rational adeles and full Schwartz–Bruhat Poisson theorem proved from
ordinary real Poisson in `ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md`, AS-04–06.
Additive Haar measures are Lebesgue at infinity and vol(Z_p)=1 at finite places.
The Fourier convention is

\[
 \widehat f(y)=\int f(x)\psi(xy)\,dx,\qquad
 \psi_\infty(x)=e^{2\pi ix},\quad
 \psi_p(x)=e^{-2\pi i\{x\}_p}.
\]

Both signs may be reversed consistently; reversing only one changes the
arithmetic pairing. Multiplicative measures are

\[
 d^\times x_\infty=\frac{dx}{|x|},\qquad
 d^\times x_p=(1-p^{-1})^{-1}\frac{dx_p}{|x_p|_p}.
 \tag{1.1}
\]

In particular vol(Z_p^×)=1. The idelic measure is the restricted product of
these measures relative to Z_p^×. The exact implementations reuse
`PadicBall`, the rational valuation/factorization maps, `character_four`, and
the existing outward rational pi/exponential machinery; no competing p-adic
or interval implementation is introduced.

**Primary provenance.** Tate's original thesis [T], §§2.2–2.5 and 4.2–4.5,
provides the local characters/measures, special zeta tests and global
Poisson/Mellin method. We compute the chi4 specialization below rather than
import an unexplained completed-L-function oracle. NIST DLMF [D],
25.15.1–2 and 25.15.5–6, supplies an independent official formula comparison
for the Dirichlet series, Euler product, functional equation and Gauss sum.
The formula signs below are fixed by our own declared additive characters.

## 2. The genuine Hecke character, including its ramified component

Let chi=chi4 be 0 on even integers, 1 on 1 mod 4 and -1 on 3 mod 4. Set

\[
 \omega_\infty(x)=\operatorname{sgn}(x),\qquad
 \omega_p(x)=\chi(p)^{v_p(x)}\quad(p\ne2),\qquad
 \omega_2(2^ku)=\chi(u\bmod4)\quad(u\in\mathbb Z_2^\times).
 \tag{2.1}
\]

The map omega_2 is a multiplicative character on Q_2^×; in particular
omega_2(2)=1, **not** chi(2)=0. These two uses of a character must not be
confused. Its conductor is 4Z_2: it is trivial on 1+4Z_2 but not on
1+2Z_2, since omega_2(3)=-1. The positive integer conductor is therefore 4.

**Proposition C4-01 (CLASSICAL, DERIVED).** The product omega of (2.1) is a
continuous unitary idelic character, trivial on diagonal Q^×.

**Proof.** Only finitely many unramified factors differ from 1 on any idele,
so the product is defined and continuous in the restricted-product topology.
Write a diagonal rational as
q=epsilon 2^k product_(p odd) p^{k_p}, where epsilon=±1 and only finitely
many k_p are nonzero. Its 2-adic unit has character
chi(epsilon) product chi(p)^{k_p}=epsilon product chi(p)^{k_p}.
Multiplying this by omega_infinity(q)=epsilon and by all odd factors gives
epsilon² product chi(p)^{2k_p}=1. Negative exponents cause no difficulty
because chi(p)=±1. ∎

The source method `diagonal_hecke_receipt` executes this factorization for
each rational input. The proof quantifies over every rational; the finite
regressions are controls of the implementation, not its universal proof.

## 3. The ramified Schwartz–Bruhat vector and exact local Fourier map

Define, for t>0,

\[
 \varphi_{\infty,t}(x)=x e^{-\pi t x^2/4},\qquad
 \varphi_2(x)=\omega_2(x)\mathbf1_{\mathbb Z_2^\times}(x)
 =\mathbf1_{1+4\mathbb Z_2}(x)-\mathbf1_{3+4\mathbb Z_2}(x),
 \qquad \varphi_p=\mathbf1_{\mathbb Z_p}\ (p\ne2).
 \tag{3.1}
\]

Extend phi_2 by zero at zero. The real function is Schwartz and the finite
functions are compactly supported locally constant. Their restricted tensor
Phi_t is an honest Schwartz–Bruhat function on A, since all but one finite
factor are standard integer indicators. The finite factor is also exactly
the rational-coset combination

\[
 \varphi_f=\mathbf1_{1+4\widehat{\mathbb Z}}
             -\mathbf1_{3+4\widehat{\mathbb Z}}.
 \tag{3.2}
\]

Indeed multiplication by 4 is a unit at every odd place, so each displayed
coset has odd-prime coordinate Z_p. Thus the *same* rational-coset generators
used in the reconstructed global Poisson proof apply here directly.

**Proposition C4-02 (CLASSICAL, DERIVED).** In the declared convention,

\[
 \widehat\varphi_2(y)=-\frac i2\varphi_2(4y),\qquad
 \widehat\varphi_{\infty,t}(y)
   =2i\,t^{-3/2}\varphi_{\infty,1/t}(4y),\qquad
 \boxed{\widehat\Phi_t(a)=t^{-3/2}\Phi_{1/t}(4a)}.
 \tag{3.3}
\]

Here 4a means multiplication at **every** place, not just the real one.
Phi_1 is Fourier-invariant up to rational dilation; it is not asserted to be
literally self-dual.

**Proof.** Each finite coset has additive volume 1/4. Its transform is its
volume times psi_2(ay) times the indicator of (1/4)Z_2. Subtracting a=3
from a=1 gives

\[
 \widehat\varphi_2(y)=\frac14
   \left(\psi_2(y)-\psi_2(3y)\right)
       \mathbf1_{(1/4)\mathbb Z_2}(y).
 \tag{3.4}
\]

It vanishes for v_2(y)>-2 and v_2(y)<-2. For y=u/4 with u a 2-adic
unit, let u=1 or 3 modulo 4: the two differences are respectively -2i and
2i. Hence (3.4) is -i chi(u)/2, exactly the first formula in (3.3).
This is also the finite Gauss identity tau(chi)=i-(-i)=2i under the
positive Gauss-sum convention. The usual odd root number is therefore
tau(chi)/(i sqrt(4))=1.

For the real transform, differentiation of the Gaussian transform gives
F_+[x e^(-pi a x²)](y)=i y a^(-3/2)e^(-pi y²/a). Take a=t/4 to
obtain 8i y t^(-3/2)e^(-4pi y²/t), the second formula in (3.3).
At each odd prime the standard indicator is self-dual and unchanged by
multiplication by 4. The two exceptional constants multiply to
(2i)(-i/2)=1, proving the full tensor identity. ∎

**Exact source implementation.** `Chi4TateSource(source_id, epoch)` is
immutable and builds the two signed `PadicBall` atoms with the same source
identity and epoch. `ramified_fourier` evaluates the atoms through the
pre-existing local Fourier map; `ramified_fourier_closed` independently
evaluates the conductor formula. Their rational-frequency agreement is
tested, including zero and unsupported frequencies. Finite-minus phase and
the Haar amplitude 1/4 are visible in each atom.

## 4. The complete idelic Mellin integral

For Re(s)>1 define

\[
 Z(\Phi_1,\omega,s)=\int_{\mathbb A^\times}
    \Phi_1(a)\omega(a)|a|^s\,d^\times a.
 \tag{4.1}
\]

**Proposition C4-03 (CLASSICAL, DERIVED).** Its local factors are

\[
 Z_p(s)=(1-\chi(p)p^{-s})^{-1}\quad(p\ne2),\qquad
 Z_2(s)=1,\qquad
 Z_\infty(s)=\left(\frac4\pi\right)^{(s+1)/2}
               \Gamma\left(\frac{s+1}{2}\right).
 \tag{4.2}
\]

Consequently

\[
 \boxed{Z(\Phi_1,\omega,s)=\Lambda_4(s)
 =\left(\frac4\pi\right)^{(s+1)/2}
   \Gamma\left(\frac{s+1}{2}\right)L(s,\chi_4)}
 \qquad (\Re s>1).
 \tag{4.3}
\]

**Proof.** At an odd prime, each p^k Z_p^× has multiplicative mass 1 and
the support requires k>=0. The integral is the geometric series with ratio
chi(p)p^(-s), absolutely convergent locally for Re(s)>0. At 2 only units
occur, and phi_2 omega_2=1 there. Under (1.1), each residue 1 or 3 mod 4
has mass 1/2, so Z_2=1 for every s. The real integrand reduces to
|x|^s e^(-pi x²/4) dx; substituting u=pi x²/4 in twice the positive
half-line integral gives (4.2), locally for Re(s)>-1.

For sigma>1, the integral of the absolute value is finite: its real factor
is finite, its ramified factor is 1, and its remaining shell factors are
bounded by the absolutely convergent product of (1-p^(-sigma))^(-1).
Fubini on the restricted product therefore factors (4.1). Unique prime
factorization and absolute convergence expand the product to
sum_(n>=1) chi(n)n^(-s), giving (4.3). ∎

The factor 4 in the real Gaussian is deliberate. It moves the conductor
scaling into the Mellin Gamma factor and is tied by (3.3) to the genuinely
ramified finite vector. One cannot change that scaling while retaining
the same modular equation. The completion convention in (4.3) is exactly
the one in the requested mission; conventions differing by a fixed
nonzero constant describe the same functional equation.

## 5. Full odd theta, analytic continuation, zero modes and root number

On diagonal rationals, the finite support of Phi_t consists precisely of
odd integers. Thus its theta sum is

\[
 \Theta_4(t)=\sum_{q\in\mathbb Q}\Phi_t(q)
    =\sum_{n\in\mathbb Z}n\chi(n)e^{-\pi n^2t/4}
    =2\sum_{n\ge1}n\chi(n)e^{-\pi n^2t/4}.
 \tag{5.1}
\]

**Proposition C4-04 (CLASSICAL, DERIVED).** For t>0,

\[
 \boxed{\Theta_4(t)=t^{-3/2}\Theta_4(1/t)}. \tag{5.2}
\]

**Proof.** Apply the full adelic Poisson theorem to Phi_t. Its Fourier
sum is t^(-3/2) sum_(q in Q) Phi_(1/t)(4q) by (3.3). Multiplication
by 4 permutes Q, proving (5.2). Absolute convergence follows either from
the Schwartz–Bruhat Poisson theorem or directly from the Gaussian sums. ∎

An independent route is ordinary real Poisson separately on 1+4Z and
3+4Z, then the four-term Gauss transform of chi. This is precisely the
rational-coset route (3.2); both routes share real Gaussian Fourier
analysis and hence are not independent axiomatic foundations.

**Proposition C4-05 (CLASSICAL, DERIVED).** Lambda_4 extends to an entire
function, with no zero-mode poles, and obeys Lambda_4(s)=Lambda_4(1-s).
For all complex s its source integral is

\[
 \boxed{\Lambda_4(s)=\frac12\int_1^\infty\Theta_4(t)
       \left(t^{(s-1)/2}+t^{-s/2}\right)dt.} \tag{5.3}
\]

**Proof.** Initially for Re(s)>1, termwise Gaussian Mellin integration gives
Lambda_4(s)=(1/2)int_0^infinity Theta_4(t)t^((s-1)/2)dt.
Absolute interchange reduces to sum n^(-sigma). Transform the interval
(0,1) using t=1/u and (5.2); the power becomes u^(-s/2), proving (5.3).
Gaussian decay at infinity dominates every real power and every power of
log t uniformly for s in any compact vertical strip. Hence (5.3) is
entire by differentiation under the integral and agrees with (4.3) in
its original half-plane. Its two powers are interchanged by s -> 1-s.
There are no source pole terms: Phi_t(0)=0 and Phi_t-hat(0)=0. ∎

This proof does not continue an Euler product term by term into its region
of divergence. It continues the genuine absolutely convergent Mellin germ
through the reconstructed Poisson interface. The odd Gamma factor's poles
are canceled in the completed entire function; importing the zeta poles at
0 and 1 would contradict (5.3).

## 6. Exact logarithmic source and the half-density interface

Absolute locally uniform convergence for Re(s)>1 permits logarithmic
differentiation of the Euler product:

\[
 -\frac{L'}L(s,\chi_4)
 =\sum_p\sum_{k\ge1}\chi(p)^k\log p\,p^{-ks}
 =\sum_{n\ge1}\chi(n)\Lambda(n)n^{-s}. \tag{6.1}
\]

Thus the true signed source at n=p^k is chi(p)^k log p; no independent
impulse occurs at n=6. At the ramified place all coefficients are zero.
At p=3 the signs alternate: -log3,+log3,-log3,... . This is not a positive
prime measure. `logarithmic_source_tape` retains prime-power provenance and
checks the two independent forms chi(p)^k and chi(n).

The completed derivative is

\[
 \frac{\Lambda_4'}{\Lambda_4}(s)
 =\frac12\log\frac4\pi+
   \frac12\psi\!\left(\frac{s+1}{2}\right)
   +\frac{L'}L(s,\chi_4). \tag{6.2}
\]

Equation (6.1) is an absolutely convergent series only in its stated
half-plane. A later contour transport may use (6.2), but may not evaluate
(6.1) on Re(s)=1/2 as an ordinary convergent sum. In the logarithmic test
coordinate, F(x)=x^(-1/2)h(log x) gives the Mellin transform
int h(u)e^((s-1/2)u)du. Replacing -1/2 by -1/2+delta creates exact real
drift delta at Re(s)=1/2. Existing `critical_mellin_character` checks this
interface; it does not assert positive definiteness of the signed Weil form.

## 7. Quantified approximation: what the numerical experiments certify

Let Theta_(4,N) truncate (5.1) to |n|<=N. For t>0 and 3tN²>=2,

\[
 |\Theta_4(t)-\Theta_{4,N}(t)|
 \le\frac4{3t}e^{-3tN^2/4}. \tag{7.1}
\]

Indeed pi>3, and x exp(-3tx²/4) is decreasing for x>=N under the stated
condition. Bound the positive tail by its integral from N to infinity;
the factor 2 from the signed theta gives (7.1). The exponential is bounded
rationally by (M/(M+x))^M for x>=0, with M=128 in the code. Finite terms
use the existing certified rational pi and exponential intervals.

For t>=1, the same integral estimate starting at 1 gives

\[
 |\Theta_4(t)|\le 2\left(1+\frac2{3t}\right)e^{-3t/4}
             \le\frac{10}3 e^{-3t/4}. \tag{7.2}
\]

For a declared strip a<=Re(s)<=b, put
B=max(0,ceil((b-1)/2),ceil(-a/2)). Let the approximation to (5.3)
use Theta_(4,N), integrated on [1,T]. Its r-th s derivative, r>=0, has
absolute error at most

\[
 E_r\le2^{-r}\left[
  \frac43\int_1^\infty t^{B+r}e^{-3N^2t/4}dt
 +\frac{10}3\int_T^\infty t^{B+r}e^{-3t/4}dt\right]. \tag{7.3}
\]

For the mode tail use (7.1) and weaken t^(-1)<=1; for the integration tail
use (7.2). The half in (5.3) cancels the two-power bound, and the r-th
derivative costs (log t/2)^r<=t^r/2^r. Each integral in (7.3) is an
integer-degree exponential moment, evaluated by repeated integration by
parts and an outward exponential bound. `completed_theta_error` implements
this for 0<=r<=2 and bounded input resources. The bound is uniform in all
imaginary ordinates in the strip. It excludes finite quadrature error,
which must be certified separately before reporting a full L-value interval.

At t=4 the executable probe certifies the following approximate displays
of rational interval endpoints (decimals here are illustrative only):

| Source | Direct enclosure | Transformed enclosure | Verdict |
|---|---:|---:|---|
| q=4, root=+1 | [0.0864278365167, 0.0864278365321] | [0.0864278198767, 0.0864278534364] | Consistent |
| q=4, root=-1 | same positive interval | negative interval | Refuted |
| q=1, root=+1 | approximately 0.00000697468 | approximately 0.11334595690 | Refuted |

Passing overlap is not the proof of (5.2); the proof is §5. Disjoint outward
rational intervals are decisive finite certificates against the specified
mutations, because the omitted tails are proved bounds.

## 8. Hostile crucible and exact failure receipts

| Mutation | Receipt | Instrument and scope |
|---|---|---|
| Reverse only finite phase | fhat_2(1/4) becomes +i/2 instead of -i/2; full tensor multiplier -1 | Exact finite fourth roots; wrong theta root also interval-refuted |
| Reverse both Fourier signs | Full multiplier remains +1 | Valid convention change, not an error |
| Drop multiplicative Haar normalization at 2 | Unit integral becomes 1/2 instead of 1 | Exact residue masses |
| Omit ramified place because its Euler factor is 1 | Character on diagonal -1 becomes -1 | Exact Hecke reciprocity failure |
| Omit p=3 Euler place | At s=2, local factor 9/10 becomes 1 | Exact rational Euler shell witness |
| Declare primitive conductor 2 | 1 and 3 are equal mod 2 but chi values differ | Exact residue witness |
| Declare primitive conductor 8 | Character already factors through mod 4 | Exact non-minimal conductor witness |
| Replace conductor 4 by 1 in completion/theta | Wrong t=4 modular identity has disjoint intervals | Rigorous analytic tail estimate required |
| Use even real Gaussian with odd character | Real Mellin integrand is odd; unweighted theta pairs cancel | Exact parity/integrability argument |
| Set root number to -1 | Contradicts tau/(i sqrt4)=1 and certified nonzero theta | Exact Gauss sum plus analytic nonzero certificate |
| Insert standalone log-Euler impulse at 6 | 6 has distinct prime factors and is absent from the prime-power tape | Exact finite factorization |
| Non-Euler tape with a9=-1, a3=-1 | a9 != a3²; witness (3,3,-1,1) | Exact coherence failure, independent of fake composite 6 |
| Completely multiplicative counterfeit a_n=1 | Coherence passes; a2=1 != chi4(2)=0 | Exact source-fidelity failure |
| Shift half-density by delta=1/8 | Real log-clock drift is 1/8 at Re(s)=1/2 | Exact coordinate identity |
| Import zeta pole contributions | Both source zero modes vanish and (5.3) is entire | Exact local witness plus analytic entire-continuation proof |

The finite tape validator explicitly separates coherence from authenticity.
Neither agreement up to a cutoff nor a symbolic descriptor authenticates a
physical source or proves a universal formula for an arbitrary unknown tape.

## 9. Verdict, ledger-ready claims and failure boundary

**SURVIVES — CLASSICAL, DERIVED:** C4-01–05 reconstruct the genuine primitive
odd Hecke source, its ramified finite test, the complete idelic Mellin factor,
the root/conductor/odd theta transform, and the entire functional equation.
The source Fourier equation is an actual identity of Schwartz–Bruhat
functions, not merely agreement of a chosen numeric covariance.

**SURVIVES — PROVED BOUND / TESTED MODEL:** (7.1)–(7.3) certify finite theta
tails and split-integral truncation errors. The source implementations have
22 focused tests; exact phase and tape witnesses and outward interval
mutation rejections are separately scoped.

**REFUTED, with receipts:** omitting ramified structure while retaining only
its Euler factor; wrong one-sided Fourier phase; non-Euler prime-square
coefficients; wrong conductor/root/parity and imported zeta zero modes.

**UNVERIFIED:** no unconditional positivity theorem for the complete signed
chi4 Weil form follows. Conductor/root correctness and analytic continuation
do not produce such a theorem. No claim of GRH, novelty of Tate's theorem,
or universal execution over all completed adelic points is made.

The executable finite carrier handles rational residues, source words,
prime factorization and certified truncation. The full idelic character,
Poisson theorem and analytic continuation admit finite mathematical proofs
under their classical hypotheses, but are not the outcome of infinitely
many physically executed prime experiments. A field classification must
declare target, proof theory and allowed experiment model before assigning
SimpleField/IdealHardField/FuckedField. None is assigned to RH merely because
its proof is currently unknown.

**Integration in this checkpoint:** [the complete signed Weil transport](TATE_TO_WEIL_DISTRIBUTION.md)
now carries this source identity, conductor 4, parity 1, absent poles, and
signed prime coefficients to every compact smooth log test. The remaining
consequential probe is a source-specific positive representation on arbitrary
convolution autocorrelations, with a uniform error bound and matched non-Euler
controls. Identification alone supplies no sign theorem.

## References and validation

[T] J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*,
Princeton thesis (1950), §§2.2–2.5, 4.2–4.5. Original thesis scan inspected:
<https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf>.

[D] NIST Digital Library of Mathematical Functions, §25.15, equations
25.15.1, 25.15.2, 25.15.5, 25.15.6:
<https://dlmf.nist.gov/25.15>. Formula comparison only; no zero data used.

Implementation: `observational_succ/tate_chi4.py`.
Focused validation: `python -m unittest tests.test_tate_chi4 -v` — 22 passed
in the execution environment. Full repository/provenance and remote CI
status are recorded separately in `CARRIER_TATE_WEIL_VALIDATION.json` and the
stacked draft PR; focused tests alone do not certify them.

RH PROVED: NO
