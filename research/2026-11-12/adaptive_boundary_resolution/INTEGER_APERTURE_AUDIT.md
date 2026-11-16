# Independent audit of integer information and adaptive aperture

**2026-11-12. Verdict: the mathematical claims survive after one
normalization clarification, which the root constructor applied and I
reread.** This is an adversarial review by a separately tasked agent in
the same model family and session. It is not an external referee report,
formal verification, or independent-source corroboration.

I read `INTEGER_INFORMATION.md`, `integer_information.py`,
`test_integer_information.py`, and `ADAPTIVE_APERTURE.md`. I did not
modify those files. The only artifact written by this audit is this note.
The audit covers the supplied fixed-base integer packet and the stated
moving-node recovery rule; it does not audit every source-acquisition
interface or establish a new arithmetic estimate.

## 1. Finding and correction: the normalizing mass must be known

The initial aperture wording allowed a known upper bound
Σc_h≤M, then referred to a response normalized by total mass. If the
actual normalization mass m is unknown, an absolute integer count cannot
in general be reconstructed from F(s)/m, even at zero noise.

The exact counterexample is the pair of histograms `(1)` and `(2)`.
Both obey the same upper bound M=2 and both report F(s)/m=1 at every
node, but their zero counts are one and two. This is an access-model
ambiguity, not a defect in the unnormalized coefficient-isolation proof.

I notified the root immediately. The revised paragraph now specifies
normalization by the **known bound M**, or by a separately supplied
actual normalization mass m≤M. I reread that correction. Normalizing
by a positive actual mass presupposes m>0; a zero mass determines the
zero histogram and needs no response, as the note separately explains.

For a normalized interval of width 1/(2M), rescaling by known M gives
width 1/2; rescaling by known positive m≤M gives width at most 1/2.
The original aperture interval proof consequently applies. The defect
is closed in the audited snapshot.

## 2. Integer kernel: all finite supports and exact mass equality

Let c,c′ be nonnegative integer histograms with the same exact mass M,
and let P=F_c−F_c′. Finite integer mass forces finite support, even
though no shared support ceiling is given. Equal mass gives P(1)=0;
equal damped responses give P(b⁻ʳ)=0 for r=1,...,d.

The claimed integer factorization is sound. To divide P by 1−kz,
with integer k≥1 and P(1/k)=0, recursively set q_0=p_0 and
q_j=p_j+kq_{j−1}. Every q_j is integral, and the terminal condition
q_H=k^H P(1/k)=0 proves that the final remainder vanishes. Distinct
roots survive subsequent divisions. Thus

\[
P(z)=A_{b,d}(z)Q(z),\quad Q\in\mathbb Z[z],\qquad
A_{b,d}(z)=(1-z)\prod_{r=1}^d(1-b^rz).
\]

For a nonzero difference, orient its leading coefficient positively.
It is an integer multiple of B_d=b^{d(d+1)/2}, hence at least B_d.
Let S be the positive coefficient mass. P(1)=0 gives equal positive
and negative masses, and cancellation of common histogram mass gives
S≤M. If the leading coefficient were the only positive coefficient,
then P(x)<0 for every 0<x<1: all negative terms have lower degree and
their coefficients sum in magnitude to the leading coefficient.
This contradicts the root x=1/b. For d≥1 there is at least one further
positive integer coefficient, so S≥B_d+1.

This argument excludes every nonzero difference at M≤B_d, including
differences whose constant coefficient is zero. Therefore **entire
histogram uniqueness**, over arbitrary finite support, is justified.
The proof does not supply a fast decoder. The strict extra unit uses
d≥1; the zero-channel exception is correctly separated in the note.

Exact mass equality is load-bearing. With only a common upper bound
M=2, `(1,0)` and `(0,2)` have the same response at 1/2 but different
zero counts and different masses. They do not contradict the theorem,
because the packet also contains the exact mass. The code's witness
verifier rejects this unequal-mass pair.

## 3. A witness is not the exact minimum

Splitting the positive and negative coefficients of A_{b,d} gives equal
mass U_d=∏_{r=1}^d(b^r+1), because A(1)=0 and its coefficients
alternate in sign. Its constant is one, so its target gap is one.
Adding the same units at grade one preserves both the observations and
that target gap, proving ambiguity at every integer mass M≥U_d.

An exact characterization that makes the quantifiers explicit is

\[
M_{\min}(b,d)=
\min_{\substack{Q\in\mathbb Z[z]\\Q(0)\ne0}}
\frac12\|A_{b,d}Q\|_1.
\]

Every such multiple supplies twins by taking coefficientwise signs;
every pair of twins supplies such a multiple, with no greater mass
after cancelling common mass. This identity does not solve the infinite
optimization over polynomial degree.

In particular, the constructor correctly avoids promoting Q=1 to an
optimum. At b=2,d=2, multiplication by 1+z changes the product witness
from mass 15 to mass 14:

\[
(1+z)A(z)=1-6z+7z^2+6z^3-8z^4.
\]

The equal responses of `(1,0,7,6,0)` and `(0,6,0,0,8)` are
7/2 and 49/32. The established interval is 9≤M_min(2,2)≤14;
no exact minimum at d≥2 is established by this audit or the note.
At d=1, lower and upper bounds do coincide at b+1.

The uniform product estimate is also correct: the first four factors
of C_2 are 2295/1024, the tail logarithm is less than 1/16, and
exp(1/16)<16/15. Hence C_b≤C_2<153/64. This compares the stated
sufficient uniqueness threshold with the explicit witness threshold,
not with an unproved exact minimizer.

## 4. Channel bounds, endpoint and comparison with the previous rule

For positive mass, the computed upper bound K is the least integer
d≥1 with B_d≥M. The lower bound L is one plus the largest prefix
length whose product witness can be padded to mass M. Both definitions
match the implementation's integer loops, including equality endpoints.

To check the one-channel gap independently, for j≥1 use

\[
U_j=\prod_{r=1}^j(b^r+1)
<\prod_{r=1}^j b^{r+1}
=B_jb^j<B_{j+1};
\]

the j=0 case is U_0=1<B_1. If K≥2, minimality gives
B_{K−1}<M, whence U_{K−2}<M and L≥K−1. If K=1, then
1≤M≤b and U_1=b+1>M, so L=1. The two bounds therefore differ
by zero or one. They need not determine the undecided channel.

The asymptotic N_b(M)=sqrt(2 log_b M)+O_b(1) follows for each
**fixed** base. This is a lower bound for the prescribed prefix packet,
not arbitrary node selection, bit complexity, or a source-restricted
arithmetic family. The exact mass is a separately supplied observation.

For the old even-degree rule, if E≥4 is the least even degree with
B_E>M, then B_{E−2}≤M and U_{E−3}<B_{E−2}≤M. Thus
N_b(M)≥E−2, while that reconstruction rule gives N_b(M)≤E.
The small E=2 case is handled separately. The claimed two-channel
comparison is justified.

The endpoint comment is correct as well. At M=B_d and even d,
the old damped filter applied to mass concentrated at grade d gives
B=−1 and c_0=0. Unmodified ceil(B) is wrong there, but
max(0,ceil(B)) is correct: if c_0≥1 the leakage is strictly less
than one, and if c_0=0 the clipping handles B∈[−1,0]. This does
not invalidate the earlier rule, whose stated condition was strict.

## 5. Deterministic noise: interval overlap and the factor of two

The normalized witnesses have the same **known exact positive mass**.
The unit-transfer pair has coordinate gaps (1−b⁻ʳ)/M; the largest
is at r=d. The midpoint is a common admissible report at radius
(1−b⁻ᵈ)/(2M). This is exact adversarial indistinguishability, not
an inference about random errors.

The last-channel witness is likewise correct: the degree-(d−1)
annihilator vanishes at all earlier sample nodes and has value
κ_{b,d}=∏_{j=1}^d(1−b⁻ʲ) at the final node. Common grade-one
padding cancels from the difference. The final normalized separation
is κ_{b,d}/M, so the common midpoint radius is half that value.

The sufficient noise comparison also pays the right factor. If each
normalized error is at most η, the unnormalized filtered-response
error is E<9Mη. A coarse valid integer interval has width at most
ε_dM+2E. Thus ε_dM≤1/2 and η<1/(36M) make its width strictly
less than one. The genuine integer target then makes it a singleton.
The two appearances of E are not interchangeable with one E.

The resulting statement concerns the least accuracy required to guarantee
recovery in this noise model: an inverse-mass absolute error scale,
or log₂M+O(1) precision bits at a suitable channel count. It is not
a bound on exact rational representation length when grades are unbounded,
and it gives no full-histogram stability theorem.

## 6. Moving aperture: what the one-channel result actually proves

Under nonnegative grade masses, integer c_0, and a known upper bound
Σc_h≤M, the elementary inequality

\[
0\le F(s)-c_0\le s(M-c_0)\le Ms
\]

is valid without integrality of the other masses. Therefore Ms<1
implies c_0=floor F(s). A moving node s=1/(M+1) suffices. This
changes the measurement family and is entirely compatible with the
fixed-base lower bound.

For an authentic interval [l,u], the weaker but valid bracket

\[
\max(0,\lceil l-Ms\rceil)\le c_0
\le\min(M,\lfloor u\rfloor)
\]

has exactly one integer if u−l+Ms<1. At s=1/(4M) and width
u−l≤1/2, the width bound is 3/4. Width and radius must not be
confused: an interval of width 1/2 corresponds to midpoint error at
most 1/4. The normalization qualification is addressed in section 1.

The signed lower response is safe even with an upper bound M:

\[
\frac{F(s)-sM}{1-s}\le c_0.
\]

If c_0=0 then F(s)≤sM; if c_0≥1 and Ms<1 then
F(s)≥1>sM. This proves the stated equivalence between its positivity
and a positive integer zero count. Substitution of the genuine Goldbach
source yields an equivalent pointwise criterion, not an estimate proving it.

The following exact mutations delimit the rule:

- At Ms=1, `(c_0,c_1)=(0,M)` has F(s)=1 and its floor is wrong.
- For c_0=1/2 and no tail, flooring cannot recover the noninteger target.
- For a genuine count-one source, the authentic interval [4/5,1]
  recovers one with M=1,s=1/4, while flooring its midpoint gives zero.
- Knowing only the normalizing mass upper bound cannot undo the
  absolute-count ambiguity of `(1)` versus `(2)`.

The production one-sample helper makes a conditional assertion: the
caller must authenticate the response and the chosen node. Its range
check 0≤value≤M is necessary, but it is not a complete source-feasibility
test. This is consistent with its docstring and the note's access caveat.

## 7. Executed checks and reproduction

I observed the constructor suite pass **13 tests**. Those tests are
the constructor's tests; running them again is not an independent method.

I additionally ran a separate in-memory exact checker with these totals:

| Check family | Cases | Independent calculation |
|---|---:|---|
| Integer annihilator multiples | 72 | Evaluate roots by homogeneous integer sums, avoiding the production Fraction response routine; check equal sign masses and leading divisibility. |
| Channel-bound endpoints | 108 | Check masses immediately around B_d and U_d against integer inequalities and both channel gaps. |
| Authentic aperture intervals | 1,620 | Independently apply rational floor/ceiling to upper-bound sources, fractional tails, three grades and three allowed interval placements. |
| Designed contract mutations | 5 | Unequal mass, unknown normalizer, strict aperture endpoint, noninteger target, and noisy-center flooring. |

All completed without a failed assertion. These are finite calibrations,
not the proof of an arbitrary-support or asymptotic statement. The
polynomial cases use witnesses generated by the implementation under
audit, then check them by a different arithmetic route; that dependence
is explicit.

The following compact reproduction covers the three counted families;
the five mutations are displayed explicitly in the preceding sections.
Run it from the dossier directory.

~~~python
from fractions import Fraction as F
from math import prod, ceil, floor
import integer_information as ii

counts = [0, 0, 0]
for b in (2, 3, 5):
    for d in range(1, 7):
        B = b**(d*(d+1)//2)
        for multiplier in ((1,), (1, 1), (1, -1), (2, 0, -1)):
            w = ii.twins(b, d, multiplier=multiplier)
            p = [a-c for a, c in zip(w.left, w.right)]
            while p[-1] == 0:
                p.pop()
            H = len(p)-1
            assert sum(p) == 0
            for r in range(1, d+1):
                k = b**r
                assert sum(c*k**(H-h) for h, c in enumerate(p)) == 0
            assert p[-1] % B == 0 and abs(p[-1]) >= B
            assert sum(max(c, 0) for c in p) == w.mass >= B+1
            assert sum(max(-c, 0) for c in p) == w.mass
            assert w.zero_gap == multiplier[0]
            counts[0] += 1

for b in (2, 3, 7):
    for d in range(1, 7):
        B = b**(d*(d+1)//2)
        U = prod(b**r+1 for r in range(1, d+1))
        for M in (B-1, B, B+1, U-1, U, U+1):
            lo, hi = ii.channel_bounds(b, M)
            assert hi-lo in (0, 1)
            assert b**(hi*(hi+1)//2) >= M
            if hi > 1:
                assert b**((hi-1)*hi//2) < M
            assert prod(b**r+1 for r in range(1, lo)) <= M
            assert prod(b**r+1 for r in range(1, lo+1)) > M
            assert 0 <= ii.prior_even_channels(b, M)-hi
            assert ii.prior_even_channels(b, M)-lo <= 2
            counts[1] += 1

for M in range(1, 13):
    s = F(1, 4*M)
    for c0 in range(M+1):
        for h in (1, 2, 7):
            for tail in (F(M-c0), F(M-c0, 2)):
                value = c0 + tail*s**h
                for offset in (F(0), F(1, 4), F(1, 2)):
                    l, u = value-offset, value-offset+F(1, 2)
                    assert (max(0, ceil(l-M*s)), min(M, floor(u))) == (c0, c0)
                    counts[2] += 1
assert counts == [72, 108, 1620]
print(counts)
~~~

## 8. Snapshot and residual boundaries

The following SHA-256 hashes were read after the normalization
clarification was present:

| File | SHA-256 |
|---|---|
| INTEGER_INFORMATION.md | `04352e2d36b92dea24a1e2afba9e30a9df7e36af8b86edc16381930b3e545c04` |
| integer_information.py | `3de86c94ea1df547f55733037a647b0a7f8c4534a81ec3194e5a67325b3e81e7` |
| test_integer_information.py | `d5a6540369e28dae61e822708dd662887394a588f30cf4cf9acf8f9db5d18181` |
| ADAPTIVE_APERTURE.md | `270e5554fb8704222129eb905e56e237b80cc2280d7edb1ba9e84082fc298320` |

No unresolved mathematical blocker was found in this snapshot. The
unresolved exact minimum, the possible one-channel gap, optimal noise
constants, efficient decoding, and authentic arithmetic acquisition
remain unresolved as stated. The audit does not certify later edits,
full repository CI, a formal proof, a globally new theorem, or a
pointwise Goldbach result.
