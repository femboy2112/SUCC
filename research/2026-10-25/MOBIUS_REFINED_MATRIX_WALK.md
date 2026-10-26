# Möbius-refined internal matrix walk: positive atoms, dependent interactions, and a source-preserving clock budget

**Research-only, October 25, 2026 (America/New_York).** Parent: PR #296,
`461942c0bf616518e668d236d1c6b1596665a7dd`, tree
`1aa01583379ef70ae3122cb98762a173f79dbd64`. This is an independent stacked
continuation, not a merge of sibling #297 or #295. Original source files and
archival provenance are unchanged. **π normality and RH are not proved.**

[Local claim ledger](../../docs/MOBIUS_MATRIX_CLAIMS.md) ·
[implementation](../../observational_succ/mobius_signed_contrasts.py) ·
[tests](../../tests/test_mobius_signed_contrasts.py) ·
[exact receipt](MOBIUS_MATRIX_RECEIPT.json) ·
[diagnostics](MOBIUS_MATRIX_DIAGNOSTICS.json) ·
[validation and access boundary](MOBIUS_MATRIX_VALIDATION.md) ·
[next execution](../../handoffs/MOBIUS_MATRIX_NEXT_2026-10-25.md).

## 0. Object, acceptance conditions, and verdict

The author's proposal is a progressively richer internal observer, not an
unstructured large matrix: one source-time successor updates a compatible
family of arithmetic, Fourier, prime-place, and prime-power views. The source is

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
$$

The implementation checks the **whole unwrapped rational prefix and the zero
anchor**. A source-name string is not authentication. Forcing masks alone do
not authenticate the state trajectory. The parent supplies the exact character
carrier, source Gram, moving-frequency boundary and Green-tail transport.

**Survives:** positive atomic Gram refinement, exact product-of-chains Möbius
inversion, all four finite restriction/growth squares, nested innovation
energies, exact exceptional-prime densities, and clock balancing with a proved
measure-change budget.

**Fails with a certificate:** arbitrary unordered Möbius contrasts of empirical
conditional energies need not be positive. This failure occurs on the genuine
BBP source, not just on a synthetic model. Positivity is repaired on a balanced
CRT product clock, but returning to actual time has a nonzero cost.

**Moonshot outcome:** no asymptotic signed saving for the zero-selected source
was obtained. A finite-horizon exact-forcing counterfeit makes *every*
partition's innovation small simultaneously; thus the initial selector must do
quantitative work. The resulting bounds and obstructions sharpen, rather than
discharge, the parent normality criterion. Classical ingredients and the new
source-specific assembly are distinguished; scholarly novelty is **unverified**.

## 1. Positive atomic matrices and their directed system

Fix finitely many genuine primes P with caps k_p>=1, distinct integer
frequencies F, and an authentic prefix U_1,...,U_N. Define

$$
a_p(n)=\min\{k_p,\max(0,-v_p(r(n)))\},\qquad
v_n=(e(hU_n))_{h\in F},\qquad e(x)=\exp(2\pi ix).
$$

For a cell a in the product of chains, set

$$
M_a(N,F)=\sum_{n\le N:\,a(n)=a}v_nv_n^*,\qquad
T_b=\sum_{a\ge b}M_a.
$$

All empty cells remain explicit. After the actual circle-character evaluation,
M_a is positive semidefinite: for any complex c,
$c^*M_ac=\sum_{a(n)=a}|c^*v_n|^2$. In the code, identities are first checked in
formal Q[Q/Z]; this ring does not itself impose every cyclotomic relation or
carry a numerical order.

**Atomic inversion theorem.** For all a,b in this finite product poset,

$$
\mu(a,b)=\prod_{p\in P}
\begin{cases}1&b_p=a_p,\\-1&b_p=a_p+1,\\0&\text{otherwise},\end{cases}
\qquad M_a=\sum_{b\ge a}\mu(a,b)T_b.
$$

Proof: on one chain, adjacent differences invert cumulative tail sums.
Tensoring these finite inverses proves the product formula. In particular a
jump from 0 to 2 has coefficient zero, not +1. Boolean parity is valid only
when each increment is at most one. This is classical incidence algebra, not
a new definition of the arithmetic Möbius function.

**Compatibility theorem.** Adding time contributes exactly one rank-one
matrix to exactly one atom. Dropping a prime or lowering a cap sums the
corresponding positive atoms. Restricting F takes a principal submatrix.
Prefix restriction, coordinate coarsening, and frequency restriction commute.
Refinement and time extension commute when refinement replays the *retained
raw history*. Proof: every route is the same finite sum of the same labelled
rank-one terms, with the same final membership predicates and frequencies.

This does not imply that new frequencies can be recovered from an old Gram
alone. Nor may normalized cell means be added without their cell masses.
`RefinedMatrixWalk` retains history and verifies every replay explicitly.

## 2. The critical distinction: ordered innovation versus unordered interaction

For unit phases z_n=e(hU_n), a partition A of the observed times and positive
probability weights w, write

$$
E_A(w)=\sum_{C\in A}\frac{|\sum_{n\in C}w_nz_n|^2}{w(C)}.
$$

Only nonempty cells enter this expression. If B refines A, with cell means m,

$$
E_B(w)-E_A(w)=\sum_{D\in B}w(D)|m_D-m_{A(D)}|^2\ge0.
$$

Proof: expand the square and use
$\sum_{D\subset C}w(D)m_D=w(C)m_C$. This is finite conditional-expectation
Pythagoras, valid without independence. From the trivial partition to
singletons, successive gains telescope to $1-|\sum_nw_nz_n|^2$.

But an unordered Boolean contrast
$I_{12}=E_{12}-E_1-E_2+E_\varnothing$ is a different object.
For z=(1,1,-1), A=(0,0,1), B=(0,1,1), and equal weights on three observations,

$$
(E_\varnothing,E_A,E_B,E_{AB})=(1/9,1,1/3,1),\qquad I_{12}=-2/9.
$$

The conditional projections are noncommuting. A sum of squares proof for a
nested chain cannot be repurposed as a proof for all unordered interactions.

**Authentic-source certificate.** On U_1,U_2,U_3, use the original forcing
pole-depth-one masks at 5 and 7. They give precisely the two partition shapes
above (with the authentic phases instead of 1,1,-1). Rational Machin/Taylor
interval arithmetic proves

$$
-\frac{1682512347}{40000000000}
\le I_{5,7}\le
-\frac{21031404337}{500000000000}<0.
$$

No floating eigenvalue or sign test is used for this conclusion. The exact
receipt and `test_authentic_p5_p7_mobius_contrast_is_certifiably_negative` reproduce
it. This refutes universal empirical-interaction positivity **on the source
of interest**. It does not refute positivity of atomic M_a, or of nested gains.

## 3. Exact BBP pole clocks, including 3 and 5

The independently combined rational form is

$$
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$

Let tau(p,j) be the periodic density of $v_p(r(n))\le-j$, with tau(p,0)=1.
For every j>=1,

$$
\tau(2,j)=0,\qquad
\tau(p,j)=4/p^j\quad(p\ge7),
$$

and

$$
\tau(3,1)=8/9,\qquad\tau(5,1)=14/25,\qquad
\tau(p,j)=4/p^j\quad(p=3,5;\ j\ge2).
$$

**Proof and exceptional residues.** At primes >=7 the four pole locations
7/8, 1/2, 3/8, 1/4 are distinct modulo p and their original residues are
p-units. On a pole disk only its singular term has negative valuation, so
exactly four classes modulo p^j have depth at least j.

At p=3, two denominator factors collide at n=2 modulo 3, with difference
$(8n-7)-4(2n-1)=-3$. The numerator is n+1 modulo 3; its values at n=2,5,8
modulo 9 are respectively 3,6,0 modulo 9. The first two classes separate the
two deeper poles; at n=8 modulo 9 both denominator valuations are one and
the numerator valuation is at least two. Therefore the depth-one event is
exactly n not congruent to 8 modulo 9. The two other poles are simple. At
higher depths the four pole disks are disjoint and again yield four classes.

At p=5, the colliding factors are 4n-1 and 8n-7, with difference -5. On
n=4,9,14,19,24 modulo 25 the numerator has residues 5,10,15,20,0 modulo 25.
The depth-one event is n modulo 5 in {1,3,4}, excluding n=24 modulo 25.
Its density is 3/5-1/25. Deeper pole disks separate exactly as at 3.
At 2 the displayed combined denominator is odd, so r(n) is always integral.

Consequently a valid complete mask period is

$$
Q(P,k)=\prod_{p\in P,\,p\ne2}p^{\ell_p},\qquad
\ell_p=\begin{cases}\max(k_p,2)&p=3,5,\\k_p&p\ge7.\end{cases}
$$

The first exceptional masks cannot be treated as functions modulo p alone.
A capped atom has local mass tau(p,a)-tau(p,a+1) below its cap, or
tau(p,k) at the cap. CRT multiplies these masses across distinct primes
**on complete periods**. This is independence of index masks, not of the
accumulated source phases.

If a cell occupies m residue classes modulo Q and N=qQ+r, then

$$
qm+\max(0,r-(Q-m))\le\#C\le qm+\min(r,m).
$$

Proof: the incomplete prefix selects r distinct residues, whose intersection
with any m-element set has these bounds. They avoid an unjustified replacement
of actual-time counting by Haar counting.

Dyadic pole masks are identically zero. Deeper dyadic *integral residues* of
U_n are a separate, nontrivial chart; `integral_residue` retains integer lifts.
At 3 and 5, nonintegral values must use valuation-plus-unit charts, not illegal
mod-p reduction. The code refuses the latter.

## 4. A quantified repair: balance the clock, then pay to return to the source

For N>=Q>=1 let m_a count times n in 1..N in residue a modulo Q. Keep all the
actual z_n, but assign the explicitly declared comparison weights

$$
\mu_n=1/N,\qquad\beta_n=1/(Qm_{n\bmod Q}).
$$

The beta residue distribution is exactly uniform; it is not a fresh random
source. No missing residue is fabricated, so N<Q is rejected. Let r=N mod Q.
An exact calculation gives

$$
\boxed{\delta_{N,Q}=\sum_n|\mu_n-\beta_n|
=\frac{2r(Q-r)}{NQ}\le\frac Q{2N}.}
$$

There are r residues with q+1 observations and Q-r with q. Summing their
mass discrepancies proves the formula. For arbitrary unit phases the mean
error bound $|\bar z_\mu-\bar z_\beta|\le\delta$ is sharp: choose the phases
+1 or -1 according to the sign of mu-beta.

For every partition A and every collection of unit phases,

$$
|E_A(\mu)-E_A(\beta)|\le\min(1,2\delta).
$$

Proof: $E_A(w)=1-\inf_g\sum_nw_n|z_n-g_{A(n)}|^2$, where each g lies in the
closed unit disk. Each loss lies in [0,4]. A signed measure of total mass
zero changes any such expectation by at most 2 times its l1 norm. Compare the
two infima. This proof does not assume the two conditional means coincide.

For H circle characters, let $A=\sum\mu_n v_nv_n^*$ and
$B=\sum\beta_n v_nv_n^*$. Since $\|v_n\|^2=H$,

$$
\|A-B\|\le H\delta,\qquad
|\mathrm{tr}(A^2)-\mathrm{tr}(B^2)|\le2H^2\delta.
$$

The second bound follows from
$\mathrm{tr}(A^2-B^2)=\mathrm{tr}((A-B)(A+B))$ and the positive operator
A+B of trace 2H. Thus a balanced-clock excess o(H) transports to the raw
source provided **H delta tends to zero**. A sufficient joint growth schedule
is

$$
\boxed{H_NQ_N=o(N).}
$$

This is sufficient, not necessary: delta vanishes when Q divides N. It is
stronger than merely Q=o(N). Clock complexity, Fourier width, and source time
cannot be sent to infinity independently. The bound does not establish the
balanced excess hypothesis.

Under beta, different prime-residue coordinates have their exact CRT product
law. Their coordinate conditional projections commute, so Boolean energy
interactions become squared norms of the corresponding product difference
projections. The raw empirical contrast may still be negative; both views
and their error budget are retained rather than silently interchanged.

## 5. Möbius primitive-clock sectors: a nonnegative budget with an honest remainder

On the uniform Q-cycle, for every d dividing Q define

$$
(P_df)(a)=\frac dQ\sum_{b\equiv a\pmod d}f(b),\qquad
D_d=\sum_{e\mid d}\mu(d/e)P_e.
$$

Finite residue counting gives $P_dP_e=P_{\gcd(d,e)}$. Alternatively finite
characters show that D_d selects exactly characters of additive order d.
Therefore the D_d are mutually orthogonal projections, have rank phi(d),
and sum to the identity. Their kernel is the classical Ramanujan sum
$c_d(a-b)/Q$. These are classical finite incidence/Fourier identities. The
related gcd compression in sibling #297 is acknowledged, not claimed here
as a separate discovery.

Set f(a) to the mean of the actual z_n in residue a. The raw-history/balanced
clock decomposition has the exact identity

$$
1=R_Q+\sum_{d\mid Q}\|D_df\|_{L^2(Q)}^2,
\qquad R_Q=\sum_n\beta_n|z_n-f(n\bmod Q)|^2\ge0.
$$

In particular $\|D_1f\|^2=|\bar z_\beta|^2$, and

$$
\boxed{|\bar z_\mu|\le
\sqrt{1-R_Q-\sum_{d\mid Q,\,d>1}\|D_df\|^2}+\delta_{N,Q}.}
$$

The implementation verifies the complete exact budget, not just selected
sectors. This is a useful positive accounting identity; without a lower bound
on the nonconstant energy it is **not a cancellation estimate**. Likewise,
empirical conditional energy has a floor of (number of singleton cells)/N.
Refining to unique time labels makes E=1 for every source and destroys its
usefulness as a small-energy bound. Observer richness is not automatic decay.

## 6. Exact-forcing hostile family, uniformly against every refinement

Here is a discriminator that must survive any future proposed innovation
lower bound. Fix N>=m>=1 and any finite set of genuine primes P. Define

$$
q_*=-\sum_{j=1}^{N}16^{-j}r(j),\qquad
D=1+128m^2\Big(\prod_{p\in P}p\Big)16^N,\qquad
\xi=\frac{\lfloor Dq_*+1/2\rfloor}{D}.
$$

D is odd and coprime to every p in P. The rational seed xi is nonzero. Evolve
$U_0^\xi=\xi$ with the **original forcing at every step**. Direct telescoping gives

$$
U_j^\xi=16^j(\xi-q_*)-
\sum_{\ell=j+1}^{N}16^{j-\ell}r(\ell).
$$

The genuine source has a positive moment kernel
$r(j+1)=\int_0^1t^{8j}(1-t)(t^2+2)(t^2+2t+2)\,dt$,
so it is positive and decreasing. A direct rational identity, independently
checked symbolically, is

$$
\frac{15}{64}-j^2r(j+1)=
\frac{5696j^3+7672j^2+2910j+225}
{64(2j+1)(4j+3)(8j+1)(8j+5)}>0.
$$

The finite future tail is less than $r(j+1)/15<1/(64j^2)$ and the rounding
term is less than $1/(256m^2)$. Hence for every m<=j<=N,

$$
|U_j^\xi|<\frac5{256m^2}<\frac1{32m^2}.
$$

For every fixed nonzero integer h and **every partition hierarchy on this
window**, the total ordered innovation is bounded by the full variance:

$$
0\le\text{total gain}\le1-|\overline{e(hU^\xi)}|^2
<\frac{5h^2}{128m^4}.
$$

Proof: compare every phase with 1, use
$|e(x)-1|\le2\pi|x|$ and $\pi^2<10$, and apply the nested Pythagoras identity.
The bound holds for all choices of source masks, not only those fitted in a
particular experiment. Thus exact forcing and all of its pole-depth clocks
cannot yield order-one innovation **uniformly over initial states**.

This is a horizon-dependent family, not one established infinite nonnormal
orbit with the authentic seed. It is not a counterexample to π normality.
It violates precisely U0=0. Sibling #297 independently obtains an order-m^-4
coherence obstruction for altered initial states; the result here packages a
rational p-free control and the simultaneous all-partition consequence.

For a single fixed nonnormal changed-source control, reuse SS-08:

$$
U_n^*=16^n/3-T_n^*,\qquad T_n^*=1/((8n+1)(8n+3)).
$$

Its phases equal $e(h/3)e(-hT_n^*)$. For every partition hierarchy on 1..N,

$$
\text{total gain}\le1-|\overline{e(hU^*)}|^2
<\frac{5h^2}{384N}.
$$

Indeed $T_n^*<1/(64n^2)$, $\sum n^{-4}\le4/3$, and compare with e(h/3).
This source has zero initial state but **different forcing**. The two controls
are deliberately complementary; neither satisfies both authentic conditions.

## 7. SUCC/FUCC and Frobenius: maps, not shared names

Literal index paths n -> n+1 -> p(n+1) and
n -> pn -> pn+1 -> ... -> pn+p end at the same authentic source state.
They retain their different histories. The readout after FUCC is U_(pn),
**not** p U_n. With SUCC edges assigned reference phase zero, the relative
mixed phase is $U_{p(n+1)}-U_{pn}-U_{n+1}+U_n$ modulo one; with dU assigned
to *all* edges the full loop telescopes to zero. Neither fact implies mixing.

The implementation provides exact valuation/unit jets and rejects illegal
reductions. It does not implement universal Witt vectors or infer a Frobenius
endomorphism on the entire BBP trajectory. Classical Witt identities explain
why multiplication by p is Verschiebung on W(F_p) (where Frobenius is the
identity); this requires its own source-typed comparison, not renaming V_p.

The parent's n^2 and n^3 moving-frequency witnesses and unit-norm outgoing
Koopman channel remain unchanged and are exercised by inherited regression
checks. The refinement is not an operator-norm closure of that channel.

## 8. Fresh diagnostic holdouts and what they establish

The diagnostic source is independently evaluated from the combined rational
forcing, then each phase is reduced **exactly** modulo one before 80-digit
complex evaluation. No π digits are supplied as inputs. Its numerical
energies are not interval-certified signs or universal estimates.

Predeclared exploratory training: N=128,h=1. Fresh tests use N=256,512,1024
and h=2,3,5,17 as additional frequencies. Three fixed observer grids give
60 rows: 3 training and 57 holdouts. The predeclared finite sanity band
E<=4K/N (K occupied cells) passes all 60 rows. This is **not** a proven
all-horizon inequality, a statistical p-value, or a calibrated asymptotic
confidence statement. A fixed constant here could fail at later horizons.

| N, h=1 | No masks | (7,11,13), caps (2,2,1) | (3,5,7), caps (1,1,1) |
|---|---:|---:|---:|
| 128 | 0.006324340921 | 0.132981205965 | 0.046699975271 |
| 256 | 0.000705721772 | 0.068016898593 | 0.033901324093 |
| 512 | 0.002430750050 | 0.033139904192 | 0.019910538228 |
| 1024 | 0.001869508293 | 0.019046618153 | 0.007207590278 |

At N=1024 the fixed SS-08 control, measured under the **same authentic mask
schedule**, has energies 0.999995569329, 0.999995584874, and 0.999995580383.
All three fail that sanity band. These rows distinguish this control in this
experiment. They do not show that every nonnormal source is rejected.

## 9. Next verdict-changing mathematical target

On the zero-selected authentic history, derive a uniform signed estimate
that fails for both hostile families: altered seed with exact forcing, and
altered recurrence with plausible conductor information. One possible route
is an arithmetic bound on the constant primitive-clock sector after retaining
all complementary phase contributions and paying delta. Another is a directly
controlled conditional cell energy, with small/singleton cells and all
prime-clock dependencies charged rather than discarded.

To use balanced Gram purity, choose H_N,Q_N together and prove both the
balanced excess o(H_N) and its transport condition H_N delta ->0. The
first premise is **open**. To use the primitive-clock budget, prove that its
nonconstant plus within-residue energy tends to one; that premise too is
**open**, not supplied by the positive decomposition. Use source-specific
numerator evolution and the actual zero-selected prefix, not just pole counts.

The parent Green-tail theorem transfers a genuine fixed-frequency o(N) bound
to π's base-16 orbit. This round does not supply that bound, nor decimal or
absolute normality, RH, physical quantum phases, or new Lean authority.

## 10. Provenance and classical references

- Pinned PR #296: `succ_internal_matrix_walk.py`, Git blob
  `fa1abb9dbeee0d7b4d9972e3b0e40a5feaed3c9e`; inherited test blob
  `061f587ee9ea9c6319c55b5f6051d7ac67f97dac`.
- Parent [π frontier contract](../../docs/PI_FRONTIER_CONTRACT.md),
  [IMW proof](SUCC_INTERNAL_MATRIX_WALK.md), and
  [SGO source transport](SIGNED_GAMMA_BBP_GREEN_COHERENCE.md).
- Existing project incidence work: `clock_incidence_inversion.py`,
  `oriented_mobius_adelic.py`, and
  [Möbius index/finite Fourier dossier](../2026-10-18/MOBIUS_INDEX_INFINITY_SOURCE_TRANSPORT.md).
  Their interfaces motivate this assembly; their source files were not changed.
- Sibling #297, inspected at `eca4462ee4d62642b15c4af672136aa5bcacd00b`:
  `handoffs/PRIME_RESONANCE_TO_MATRIX_2026-10-25.md`; no code/history imported.
- SS-08 source: sibling #294 at `82f4617e31e06b84fdbe52b4b217b92dcd4732dd`.
  Its explicit formula is rederived here; its implementation is not imported.
- G.-C. Rota, *On the foundations of combinatorial theory I. Theory of Möbius
  Functions*, Z. Wahrscheinlichkeitstheorie verw. Geb. 2 (1964), 340–368,
  DOI 10.1007/BF00531932. Classical attribution; publisher metadata inspected,
  not a claim of access to subscription full text. Finite proofs are above.
- Mathlib, [conditional expectation as L2 projection](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConditionalExpectation/CondexpL2.html)
  and [Witt identities](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Identities.html).
  These are references, **not** a Lean certification of this module or its
  asymptotic target.

**Verdict:** the refined instrument survives with a necessary correction to
empirical interaction positivity and a quantitative joint-limit budget.
The authentic cancellation estimate remains unpaid truth debt.
