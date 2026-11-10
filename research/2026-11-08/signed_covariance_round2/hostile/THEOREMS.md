# Signed lag gates, exact transport, and the normality quantifiers

**Status:** proved paper reductions and hostile controls. The original-zero
signed estimate is **OPEN**. These results do not replace that estimate with
an assumption that has already been proved. A separate narrow Lean certificate
checks integer recurrence transport only; the analytic reductions remain paper proofs.

The source is exactly

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Write e(t)=exp(2 pi i t). Expectations below average over time, not over seeds.
PE1--PE9 from the pinned previous dossier supply p=p_A, m=ord_p(16), and

\[
\rho_A=p_A^{-\gamma}+\varepsilon_A\to0,\qquad
\left|E_{n\in[A,2A)}e(k[U_n]_p)\right|\le\rho_A
\quad(p\nmid k).
\tag{H0}
\]

Here p_A~4A, m>p_A^(1/3), and [U_n]_p is the original rational principal
part. PNT/AP and Bourgain--Konyagin remain declared classical inputs. The
covariance is bilinear, Cov(a,b)=E(ab)-(Ea)(Eb), with no conjugation.

## H1. An exact signed energy with its finite-window cost

Fix A,H>=1 and complex f_0,...,f_(A-1), |f_r|<=1, extended by zero to all
integers. Define

\[
W=A^{-1}\sum_r f_r,\quad
C_\ell=A^{-1}\sum_{r=0}^{A-1-\ell}f_{r+\ell}\overline{f_r},\quad
q=A^{-1}\sum_r|f_r|^2,
\]

where C_ell=0 for ell>=A. Then

\[
E_H=\frac1{AH^2}\sum_{t\in\mathbb Z}
 \left|\sum_{j=0}^{H-1}f_{t+j}\right|^2
=\frac qH+\frac2H\sum_{\ell=1}^{H-1}
 (1-\ell/H)\operatorname{Re}C_\ell,
\tag{H1a}
\]

\[
0\le E_H\le q\le1,\qquad
|W|^2\le\frac{A+H-1}{A}E_H.
\tag{H1b}
\]

**Proof.** Expanding each squared moving sum counts each pair at displacement
ell precisely H-|ell| times, which proves H1a. Positivity is literal. For the
upper bound, the l2 norm of a mean of H translates of f is at most the l2 norm
of f by the triangle inequality. The nonzero moving sums occupy A+H-1 positions
and their total is H sum f. Cauchy--Schwarz over those positions gives H1b.
No absolute value is applied to the signed off-diagonal terms in H1a. QED.

For fixed 1<=K<=H, write H=q_0 K+r_0 with 0<=r_0<K. Decomposing the H-term
sum into q_0 K-term blocks and r_0 individual terms gives the useful bound

\[
\sqrt{E_H}\le\frac{q_0K}{H}\sqrt{E_K}
                 +\frac{r_0}{H}\sqrt q
\le\sqrt{E_K}+K/H.
\tag{H1c}
\]

This follows by the l2 triangle inequality on Z, where translating a whole
zero-extended block preserves its norm. It does not require stationarity,
independence, or a probability model. In particular, if for each fixed ell>=1
C_ell(A)->0 and q(A)=1, then E_(H(A))->0 for **every** H(A)->infinity: first
hold K fixed in H1c, use E_K(A)->1/K, and then let K->infinity.

## H2. Exact causal forcing transport allows a polynomial aperture

Now f_r=e(h U_(A+r)), h a fixed nonzero integer. For every ell>=1 put

\[
k_\ell=h(16^\ell-1),\qquad
F_\ell(n)=\sum_{j=1}^{\ell}16^{\ell-j}r(n+j).
\]

The unwrapped recurrence, with all four poles and integer carries retained,
gives the exact identity

\[
U_{n+\ell}-U_n=(16^\ell-1)U_n+F_\ell(n).
\tag{H2a}
\]

On the full actual epoch J=[A,2A) define

\[
a_{\ell,n}=e(k_\ell[U_n]_p),\quad
v_{\ell,n}=e\bigl(k_\ell(U_n-[U_n]_p)+hF_\ell(n)\bigr),
\]

\[
\Gamma_{A,h}(\ell)=\operatorname{Cov}_{J}(a_\ell,v_\ell),
\qquad
R_{A,h}(H)=\frac2H\sum_{\ell=1}^{H-1}
 (1-\ell/H)\operatorname{Re}\Gamma_{A,h}(\ell).
\tag{H2b}
\]

These use the same operational phase reference. F_ell is kept exactly;
independently rotating either factor changes the statistic. If p does not
divide h and 1<=H<=m, then p does not divide any k_ell for 1<=ell<H, so H0
and |Ev_ell|<=1 imply

\[
\boxed{\left|E_H-\frac1H-R_{A,h}(H)\right|
\le (1-1/H)\rho_A+\frac{H^2-1}{3HA}.}
\tag{H2c}
\]

Consequently

\[
\boxed{|W_A(h;0)|^2\le
\frac{A+H-1}{A}\left[
\frac1H+R_{A,h}(H)+(1-1/H)\rho_A+
\frac{H^2-1}{3HA}\right].}
\tag{H2d}
\]

**Proof.** The product a_ell,n v_ell,n is exactly
e(h(U_(n+ell)-U_n)). Its full-J mean differs from Gamma by the product of
its two marginal means, of modulus at most rho_A. Its truncated mean C_ell
omits at most ell terms, giving error at most ell/A (also valid for ell>=A).
Sum these errors with the nonnegative weights in H2b. Their total is
1-1/H and their ell-weighted total is (H²-1)/(3H), respectively. Substitute
into H1a, whose q=1, and then H1b. QED.

The restriction is H<=m, not H<m: the largest shift is H-1. At ell=m the
local character becomes trivial, and H0 is not applicable. There is no
restriction that the integers k_ell be smaller than p; their nonzero residues
are what H0 requires. There is also no exponential error in H in H2c.
The exact forced phase must be supplied, however large its unwrapped value.
Computational precision cost is a separate resource.

Take H_A=max(1,floor(A^(1/4))). For every sufficiently large A, H_A<=m_A,
because m_A>p_A^(1/3) and p_A~4A. Thus H_A->infinity and H_A/A->0, and

\[
|W_A(h;0)|^2\le R_{A,h}(H_A)+o_h(1).
\tag{H2e}
\]

This creates a concrete one-sided target:

\[
\forall h\ne0,\quad\limsup_{A\to\infty} R_{A,h}(H_A)\le0.
\tag{SIGNED-GATE-OPEN}
\]

Its implication to the original Weyl gate is proved; its truth for literal
zero is **not** proved. Exact causal transport is the new feature relative
to the untwisted logarithmic version below. This is a supporting reduction,
not an asymptotic cancellation saving for the complementary phase.

## H3. The prescribed-aperture signed gate is equivalent to normality

More generally fix any deterministic integer H_A with H_A->infinity,
H_A=o(A), and H_A<=m_A eventually. The following are equivalent:

1. pi is normal to base16.
2. W_A(h;0)->0 for every fixed integer h!=0 and all integer A->infinity.
3. E_(H_A)(A,h)->0 for every fixed integer h!=0.
4. R_(A,h)(H_A)->0 for every fixed integer h!=0.
5. limsup_A R_(A,h)(H_A)<=0 for every fixed integer h!=0.

**Proof.** The equivalence of1 and2 is audited in H5. H1b proves3 implies2
because H_A=o(A). H2c proves3 equivalent4, and positivity of E_H together
with H2c shows liminf R>=0, giving4 equivalent5.

For2 implies3, hold ell fixed. The source bound proved in the prior AR theorem
is 0<r(n)<1/n² for n>=2. Hence

\[
0<F_\ell(n)<\frac{16^\ell-1}{15(n+1)^2}.
\tag{H3a}
\]

Using H2a, |e(x)-e(y)|<=2pi|x-y|, and the ell omitted terms yields

\[
\left|C_\ell(A,h)-W_A(k_\ell;0)\right|
\le\frac\ell A+
\frac{2\pi|h|(16^\ell-1)}{15(A+1)^2}\to0.
\tag{H3b}
\]

k_ell is fixed and nonzero, so2 makes C_ell->0. H1c now proves3 for the
prescribed growing H_A. This is an elementary blocking argument; no uniform
normality rate at the growing frequencies k_ell is assumed. QED.

**Logical contribution:** SIGNED-GATE-OPEN is an equivalent, one-sided
signed aggregate, not a strictly weaker normality conjecture. It permits
cancellation between positive and negative lag covariances and does not
require a low-complexity predictor for the complement. It is therefore a
different attack target from the stronger predictor premises falsified in
the previous round. That distinction does not prove the new target.

## H4. If the forced phase is discarded, its cost is exponential in aperture

Define the *untwisted* covariance at the enlarged frequency by

\[
\widetilde\Gamma_{A,h}(\ell)
=\operatorname{Cov}_J\bigl(e(k_\ell[U_n]_p),
 e(k_\ell(U_n-[U_n]_p))\bigr)
\]

and let R_tilde be its triangular signed average. The same proof gives

\[
\left|E_H-\frac1H-\widetilde R_{A,h}(H)\right|
\le(1-1/H)\rho_A+\frac{H^2-1}{3HA}+B_{A,h,H},
\]

\[
B_{A,h,H}=\frac{4\pi|h|}{15H^2(A+1)^2}
\left[\frac{16(16^H-16H+H-1)}{225}-\frac{H(H-1)}2\right].
\tag{H4}
\]

The bracket equals sum_(ell=1)^(H-1)(H-ell)(16^ell-1), by finite geometric
summation. It is nonnegative. Taking H=max(1,floor(log_16 A)) makes B->0,
so the corresponding untwisted logarithmic signed gate is also equivalent
to normality, by the same fixed-K argument. Dropping F without this term
is unjustified. In particular this estimate alone cannot license a
polynomial aperture for the untwisted covariance.

## H5. Audit of covariance -> all prefixes -> normality

The prior PE identity W_A(h;0)=Cov_A(a,b)+(Ea)(Eb), with |Ea|<=rho_A->0,
proves exact asymptotic equivalence of original covariance decay and the
original Weyl gate, separately for each fixed h!=0. It does not assume
Eb->0. The relevant quantifiers are

`for every fixed h != 0 and epsilon > 0, there exists A0 such that every
integer A >= A0 obeys |W_A(h;0)| <= epsilon`.

Here is an explicit gluing proof. Let |z_n|<=1 and S_N=sum_(n=0)^(N-1)z_n.
If |sum_(n=A)^(2A-1)z_n|<=epsilon A for every A>=A0, repeatedly set
M=floor(N/2). At each step S_N=S_M+sum_(n=M)^(2M-1)z_n plus at most one
unit term. The block lengths sum to at most N. Stop when the remaining
prefix has length below2A0. Therefore

\[
|S_N|\le\epsilon N+\lfloor\log_2 N\rfloor+2A_0.
\tag{H5a}
\]

Thus all-A epoch decay implies prefix Cesaro decay. The reverse follows
from sum_[A,2A)=S_(2A)-S_A. Checking only A=2^j is insufficient: set z_n=1
on the first half and -1 on the second half of each block [2^j,2^(j+1)).
Every such complete block sums to0, whereas at N=3*2^(j-1), S_N/N->1/3.
This is a general bounded-sequence countermodel, not an authenticated BBP
orbit. It diagnoses the quantifier weakening precisely.

The authenticated Green identity is

\[
U_n(0)+T_n=16^n\pi/16,\qquad
T_n=\sum_{j>=1}16^{-j}r(n+j),
\quad 0<T_n<1/[15(n+1)^2]\ (n>=1).
\]

Hence e(hU_n) differs from e(h16^(n-1)pi) by at most2pi|h|T_n. This tends
to0 and changes neither prefix nor epoch Cesaro limits. By the classical
Weyl criterion, all fixed nonzero integer characters decay exactly when
the orbit of pi under multiplication by16 is equidistributed modulo1.
That is exactly base16 normality: a length-k hexadecimal word is the
cylinder interval [j/16^k,(j+1)/16^k), of length16^-k. Equidistribution
gives its frequency, and conversely these cylinder frequencies approximate
arbitrary intervals by finite base16 grids. A finite index shift between
16^(n-1)pi and16^n pi does not alter any limiting frequency.

No defect was found in the inherited chain when its stated all-A quantifiers,
original tail, and bilinear covariance convention are retained.

## H6. Hostile controls and exact boundaries

**Coherent same-forcing real seed.** For s_*=-pi/16, the completed identity
gives U_n(s_*)=-T_n, so every fixed-h phase tends uniformly to1 over [A,2A).
For the constant phase f=1 and H<=A, H1a gives exactly

\[
E_H(1)=1-\frac{H^2-1}{3AH}.
\]

The l2 contraction used in H1 bounds the difference of energy square roots
for the coherent orbit and this constant control by
2pi|h|/[15(A+1)^2]. Thus E_(H_A)(s_*)->1 whenever H_A=o(A), refuting any
seed-blind smoothing argument. Irrational seeds have no canonical rational
p-principal part in this framework; we do not pretend this is a rational
arithmetic control. It is an exact completed-orbit control for H1/H3.

**Periodic completed orbits.** For alpha=k/(16^p-1) and s=alpha-pi/16,
U_n(s)=16^n alpha-T_n. At h=16^p-1, every completed character is1, so the
same argument gives E_(H_A)->1. The all-h gate rejects these nonnormal
sources. No claim about seed1/5 is used.

**Epoch-dependent rational shadows.** The prior PE14/CF-A constructions
give s_A with W_A(h;s_A)->1 and the same p_A-local phase for each fixedh.
H1b and E_H<=1 force E_(H_A)(s_A)->1 for H_A=o(A). H2c, applicable to the
same-forcing rational shadows whose local phase matches, then forces their
transported signed aggregate to1. Their exact seed is not zero. This remains
`for every A there exists s_A`, never a fixed-seed counterexample to pi.

**Signed terms are indispensable.** For the alternating sequence f_r=(-1)^r
on a long even interval, E_H is small for even H, while replacing Re C_ell
by |C_ell| makes the lag sum approach1. The operation loses real cancellation;
positivity of local pin energies cannot restore the discarded signs.

**An excessively large aperture produces false success.** For f=1 and H>=A,
direct triangular counting gives E_H=A/H-(A²-1)/(3H²). Taking H=A² therefore
forces E_H->0 even though W=1. The factor (A+H-1)/A in H1b cannot be
discarded. Our prescribed polynomial aperture has H=o(A), so this control
is rejected by the actual hypotheses.

**Chronology and phase.** Dropping the four-pole F_ell changes H2a; H4
quantifies only the legitimate original-source approximation. Arbitrary
phase rotations, a different forcing, or a mean over random seeds do not
prove the selected zero's signed bound. Full exact source knowledge defines
the correct statistic; it is not itself an upper estimate on that statistic.

## Provenance and remaining theorem debt

- Source, Green identity and r(n)<1/n²: pinned original source and the prior
  `learning_yoneda/arithmetic/THEOREMS.md` AR proof. Every finite source
  identity is independently checked using the literal four fractions.
- Prime selector and rho_A: prior `PRIME_EPOCH_THEOREM.md` PE1--PE9, relying
  on PNT/AP and [Bourgain--Konyagin2003, Theorem2.1](https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf).
- Finite Gram identity, Cauchy--Schwarz and the blocking argument are proved
  directly here. [Tao's account of the classical van der Corput trick](https://terrytao.wordpress.com/2008/06/14/the-van-der-corputs-trick-and-equidistribution-on-nilmanifolds/)
  provides background; no quantitative constant is imported from it.
- Root independently proposed the exact-forcing H2 extension and the
  polynomial aperture. This front rederived its constants and quantifiers.
  This is same-model proof cross-review, not external scholarly refereeing.

## Narrow kernel certificate: integer recurrence transport only

`ExactTransport.lean` proves, in Lean4.14 core, the literal integer zero
boundary, exact finite-window transport, seed dependence and window
composition for every integer-valued forcing sequence. Its nontrivial
theorems use only the standard `propext` axiom, with no `sorryAx`.

For a finite source horizon B, choose a positive common denominator D of
all four original pole denominators through B. Then DU_n and Dr(n) are
integers and satisfy the formalized recurrence through B. This application
of the generic integer theorem is a paper argument: neither common-denominator
divisibility nor the four rational source poles are formalized in that Lean
file. Prime principal parts, complex phases, PNT/AP, BK, the signed gate
and normality are also outside its scope. `LEAN_RECEIPT.json` records the
compiler version, final source hash, command, exit status and axiom report.

The next theorem that would change the verdict is a **source-selected**
upper bound R_(A,h)(floor(A^(1/4)))<=o_h(1), with every sufficiently large A
and each fixedh. The proven local marginal bound already pays all other
terms of H2d. No such signed upper estimate is proved in this package.

**pi base16 normality: OPEN. RH: OPEN.**
