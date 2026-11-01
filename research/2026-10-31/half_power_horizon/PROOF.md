# Half-power horizon: true 2-adic ramification, joint 2×3 successor, and source pole costs

**2026-10-31, research only.** Parent SUCC draft PR #428 at 91e06fd21b2e301d5d73df4415d6cf60ec9d79cd, Main XVII main e8598cfa5d32fd1de8e94a3e458a366a0850d59e. Original four signed BBP poles and U_0=0, frozen archives, production, formal and workflows unchanged. π base-16 normality, RH, source-to-selected-Haar transfer, and an RH→π-normality implication remain **OPEN**. These results are elementary/classical proofs plus new-to-SUCC source-aware synthesis; no new academic priority claimed.

## 0. Steelman, object, and the exact location of the half exponent

The proposal: because the positive finite sums 1+2+4+... possess a negative completion, the negative unit, the ordinary successor +1, and the half-power x^(1/2) might all be carried by finite-to-global arithmetic presentations. The strongest coherent version distinguishes:
(1) finite N snapshots; (2) a continued rational generating function; (3) actual 2-adic/3-adic series convergence; (4) adjoining algebraic fractional powers; (5) the selected real BBP law.

For m≥0, define S_(b,m)=Σ_(j=0)^(m-1)b^j=(b^m−1)/(b−1). Every term and sum is ordinary N arithmetic. As a rational generating function, (1−z)^(-1) analytically continues to z=b≠1 and evaluates to 1/(1−b). The ordinary real series diverges when b≥2. No zeta(-1) summation is involved: that is continuation in the exponent of n^(-s), not continuation in the geometric ratio z.

## HP-01 — the negative unit and a UNIFORM p-adic successor (PROVED LOCAL, classical)

For a prime p and integer b≥2, Σ_(j≥0)b^j converges in Q_p **iff p divides b**; then its sum is 1/(1−b). Proof: a convergent series requires b^m→0, equivalent to v_p(b)>0, and finite geometric telescoping gives the limit.

For every integer m,
\[
\boxed{x-(b-1)\sum_{j=0}^{m-1}b^j=x+1-b^m.}\tag{HP01}
\]
Thus if p|b, the finite all-N operation on the left converges **uniformly for all x∈Z_p** to successor x↦x+1, with exact error |b^m|_p=p^(-m v_p(b)). For P∈Z_p[X], polynomial factorization P(u)−P(v)=(u−v)Q(u,v), Q∈Z_p[u,v], gives
\[
|P(x+1-b^m)-P(x+1)|_p\le|b^m|_p.
\]
This rigorously realizes every *integral polynomial* combination of successor as cancellation of finite N-series inside its lawful p-adic completion. Division, poles, infinite products and all-scale phase laws require separate hypotheses; the construction does not make every operation scheme-independent.

At b=2: Σ_(j≥0)2^j=−1 in Z₂, so x−Σ2^j=x+1. At b=6: Σ_(j≥0)6^j=−1/5 in BOTH Z₂ and Z₃, so
\[
\boxed{-5\sum_{j\ge0}6^j=+1\quad\text{in }\mathbb Z_2\times\mathbb Z_3.}\tag{HP01b}
\]
This is a single 6-adic/joint-profinite successor presentation, not two separately prescribed random laws. At p=3 the base-2 prefix does **not** converge since |2^m|_3=1 for every m.

The rational error e_m=b^m obeys the classical product formula ∏_(v≤∞)|e_m|_v=1. Specifically
\[
\boxed{|6^m|_\infty\,|6^m|_2\,|6^m|_3
=6^m\,2^{-m}\,3^{-m}=1.}\tag{HP01c}
\]
So the SAME finite integer residual grows at the Archimedean place while shrinking in both local places. This is a genuine common-source relation. It does **not** mean finite integer addition must physically pass through R, nor that all completions identify the same limit.

## HP-02 — finite square-root ghosts and authentic infinite branches (PROVED LOCAL)

For m≥3, the roots of X²=1 modulo 2^m are exactly
\[
\boxed{1,\ -1,\ 1+2^{m-1},\ -1+2^{m-1}\quad(\bmod\,2^m).}\tag{HP02}
\]
Proof: if x²≡1 mod 2^m, x is odd and the consecutive even numbers x−1,x+1 have gcd exactly 2. One has v₂=1, the other v₂≥m−1. Conversely the four listed residues square to 1 modulo2^m. Only the ±1 residues admit a lift to a root of that **same fixed polynomial at the next precision**; the others are finite ghost roots. In the integral domain Z₂ the equation X²=1 has only ±1.

The mod-2 fiber of X²−1 equals (X−1)², and the polynomial discriminant is 4. This identifies non-étaleness of the split quadratic Z₂-algebra at p=2; it does NOT itself construct a nontrivial quadratic FIELD extension.

## HP-03 — an actual half-power with a finite error certificate (PROVED LOCAL)

For t∈Z₂, use the generalized binomial coefficient (1/2 choose k)=(Γ(3/2))/(Γ(k+1)Γ(3/2−k)) as an algebraic expression at finite k, without treating Gamma as a p-adic measure. Define the 2-adic series
\[
\boxed{B(t)=\sum_{k=0}^{\infty}{1/2\choose k}(8t)^k.}\tag{HP03}
\]
For k≥1, every numerator factor 1−2j is odd, hence
\[
v_2\!\left({1/2\choose k}8^k\right)
=2k-v_2(k!)\ge k+1.
\]
Therefore B converges uniformly on Z₂; truncation before k=M gives error valuation at least M+1. Formal binomial multiplication and completeness prove B(t)^2=1+8t. Moreover B(t)≡1 mod4, selecting one unique root in 1+4Z₂; its negative selects the other.

At t=1, B(1)²=9 and B(1)≡1 mod4, hence
\[
\boxed{B(1)=-3\quad\text{in }\mathbb Z_2,}
\]
whereas the usual positive REAL square root of 9 is +3. The algebraic equation has the same two roots; the completions and branch conventions select different ones. The real binomial Taylor series around 1 is outside its convergence disk at increment 8, so termwise real and 2-adic evaluations are not being equated.

## HP-04 — a moving target realizes a finite ghost root (PROVED LOCAL)

Take the finite negative of the dyadic geometric snapshot:
\[
a_m=-S_{2,m}=1-2^m\qquad (m\ge3).
\]
Because a_m≡1 mod8, the selected 2-adic root r_m=B(−2^(m−3)) exists, r_m≡1 mod4. From
\[
(r_m-1)(r_m+1)=-2^m,\quad v_2(r_m+1)=1,
\]
deduce \(v_2(r_m-1)=m-1\), i.e.
\[
\boxed{r_m\equiv1+2^{m-1}\pmod{2^m}.}\tag{HP04}
\]
This residue is a **nonlifting ghost for the fixed equation X²=1**, yet it is the reduction of a genuine infinite 2-adic square root of the **moving equation X²=1−2^m**. As m→∞ the root r_m→+1 in Z₂.

Our first exact local test erroneously expected r_m≡1 mod2^m. It FAILED at m=3 (observed 5). The corrected congruence passed all m=3..21. The failure is a calibrated discriminating probe, not erased history. This is the cleanest distinction between a selected changing boundary and a fixed polynomial lifting claim.

The UNNEGATED positive finite sum S_(2,m)=2^m−1≡7 mod8 is never a square in Q₂ for m≥3. The order of the outside minus and the half-power is mathematically load-bearing.

## HP-05 — TRUE ramified quadratic extension from the half-power (PROVED LOCAL)

The completed geometric sum L=Σ_(j≥0)2^j is the 2-adic integer −1. Therefore
\[
\sqrt{-L}=\sqrt{+1}\in\mathbb Q_2\quad(\text{roots }\pm1),
\]
but \(\sqrt L=\sqrt{-1}\notin\mathbb Q_2\), because odd squares are 1 mod4. Adjoining i with i²=−1 produces Q₂(i). Put u=1+i. Then u²=2i, and u obeys
\[
\boxed{u^2-2u+2=0.}
\]
This polynomial is Eisenstein at 2. Consequently [Q₂(i):Q₂]=2 is totally ramified, with uniformizer 1+i, and 2 is a unit multiple of (1+i)².

At the THREE-adic place, X²+1 has no root mod3 and is a separable irreducible polynomial mod3, so Q₃(i)/Q₃ is instead an **unramified** quadratic extension. This contrast concerns the algebraic target −1; Σ2^j itself does NOT converge in Q₃.

A distinct power-law caveat: \(G_s(z)=(1-z)^{-s}\). For s=1, the geometric power series at z=2 converges 2-adically to −1. At s=1/2, its formal z=2 terms are
\[
\binom{2k}{k}2^{-k},\qquad
v_2=\operatorname{popcount}(k)-k,
\]
and along k=2^j their valuations are 1−2^j→−∞. Thus the fractional-power SERIES does not converge even after extending the p-adic field. The algebraic half-power requires a separately declared algebraic/analytic continuation with branch and extension. There is NO legitimate interchange of continuation in s with evaluating the original infinite series.

## HP-06 — a single finite real/2-adic/3-adic half-root source (PROVED LOCAL)

Let \(a_m=1-6^m\), m≥3. The SAME rational integer lies in three completed places:
- Real: a_m<0, so there is **no real square root**;
- 2-adic: a_m≡1 mod8, so choose the root r_(2,m)≡1 mod4;
- 3-adic: a_m≡1 mod3, so Hensel gives unique root r_(3,m)≡1 mod3.

Taking factorizations \( (r_{p,m}-1)(r_{p,m}+1)=-6^m\) gives
\[
\boxed{v_2(r_{2,m}-1)=m-1,\qquad
v_3(r_{3,m}-1)=m.}\tag{HP06}
\]
The difference of ONE unit of local valuation is a real, source-derived half-power branch effect. Consequently,
\[
r_{2,m}\equiv1+2^{m-1}\pmod{2^m},
\quad r_{3,m}\equiv1\pmod{3^m}.
\]
Both roots tend to 1 at their respective local places even while the real target tends to −infinity. Neither a real limit nor a common real square root is asserted. Exact Fraction/binomial and integer Hensel probes certify these statements on finite holdouts m=3..16.

## HP-07 — original BBP forcing pays a new 3-adic pole cost (PROVED LOCAL)

Retain original four signed poles, rationally valid for all integer n:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{A(n)}{D(n)},
\]
\(A(n)=120n^2-89n+16,\ D(n)=(2n-1)(4n-1)(8n-7)(8n-3)\).
For every integer n and m≥1 set y=n+1, x=y−6^m.
The inherited source divided-difference/unit proof over Z₂ gives EXACT
\[
\boxed{v_2(r(x)-r(y))=m.}\tag{HP07a}
\]
Thus using the common **6-adic finite successor presentation** inside the actual unchanged BBP source has no dyadic precision loss.

For p=3, let \(d=v_3(D(y))\). The pole denominator may be nonunit; this is exactly the source-level obstruction not present in the simple 3-adic clock. If m>d, polynomial congruence D(x)≡D(y) mod3^m ensures v₃(D(x))=d. Since A,D∈Z[X], the difference
\[
r(x)-r(y)=
\frac{(A(x)-A(y))D(y)-A(y)(D(x)-D(y))}
{D(x)D(y)}
\]
has numerator divisible by x−y=−6^m. Therefore
\[
\boxed{v_3(r(x)-r(y))\ge m-2d,\quad m>d.}\tag{HP07b}
\]
This is a genuinely original-BBP-source finite↔local bound at EVERY integer n, but it is **not uniform in n**, because d can grow arbitrarily along residue classes approaching genuine 3-adic denominator zeros. For y=1 the exact denominator has d=1; for y=2, d=3. Missing source 3-adic pole budgets cannot be replaced by the uniform joint time clock of parent #427.

The statement authenticates the four-pole **forcing law**, not a new estimate on real BBP Weyl sums or π-normality. The initial U0=0 is preserved but not a load-bearing input for this standalone source-function lemma.

## HP-08 — separated Euler/Gamma/half-density and RH scope

The classical half-density dilation on L²(R₊,dx) is \(D_af(x)=\sqrt a\,f(ax)\), which is unitary. This exponent 1/2 comes from the Jacobian, and appears in completed zeta/Weil representations. \(\Gamma(1/2)=\sqrt\pi\) is likewise a genuine Archimedean identity. These facts do NOT identify the algebraic 2-adic half-power from HP-03 with RH's critical-line condition Re(s)=1/2. The latter is about zeta zero locations and the full completed signed Weil functional.

For π normality, SUCC still needs actual original zero-selected signed real-phase cancellation, or a source-derived ×3-invariance plus componentwise entropy. The common geometric successor and algebraic field extension appear for many other sources and seeds; their presence cannot certify the unique selected BBP orbit.

## Claims, prior provenance, and next falsifier

- **PROVED LOCAL / CLASSICAL:** HP-01 through HP-07 with the quoted domains, complete derivations and exact finite checks, including the discriminating finite ghost-root correction. Academic novelty UNVERIFIED.
- **REFUTED:** real ordinary convergence of Σ2^n; 3-adic convergence of the same series; extraction of a 2-adic √−1 without extension; termwise 2-adic evaluation of G_(1/2)(2); lifting a moving-source ghost as a root of the fixed polynomial X²−1; uniform 3-adic BBP pole-free isometry; automatic π-normality/RH transfer.
- **UNVERIFIED / OPEN:** selected π-phase source-to-full Weil positivity, normality, RH and an RH→normality theorem.
- **Next probe:** combine original four-pole denominator valuations d(n), 6-adic finite successor, and the **selected zero-boundary** BBP real circle/triangular φ observables. Determine whether a finite source-weighted cancellation bound is created that is not shared by the coherent changed-seed control. If none, retain this as an exact arithmetic/interface result, not false proof progress.

Primary references: Keith Conrad, Hensel notes https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf ; product formula https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf ; SUCC pre-existing Operation SUMMATION SNAPSHOT ARROWS, DYADIC EXPOSURE, BDC square-root work, PI_DYADIC_SOURCE_ISOMETRY, and draft PRs #427–428. All references are leads and classical provenance, not independent confirmation of the new SUCC interface.
