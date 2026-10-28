# Authentic carry-spill sparsity and the conditional parity hierarchy

**Authority.** The all-time sparsity and transport results below are
PAPER-PROVED; the rational instruments and adversarial replays are EXACT
FINITE. No new Lean or scholarly-priority claim is made. The results pay
for a source-dependent representation change, not selected Fourier
cancellation. Base-16 normality of $\pi$ remains OPEN.

This extends the selected-branch interface of PR #312, pinned head
`0c306a889f425418c29cbea3193205fb80c0575e`, and compares its parity channel
with the declared carry/packet map in sibling PR #311, pinned head
`a34c4484059e667202b97d5ab4102560987b1406`. No sibling implementation is
silently imported or substituted for the primary source.

## 1. The precise arithmetic discrepancy

Keep the original four signed poles and zero anchor:

$$
r(k)=\frac4{8k-7}-\frac2{8k-4}-\frac1{8k-3}-\frac1{8k-2},
\qquad U_0=0,\qquad U_k=16U_{k-1}+r(k).
$$

For $n\ge1$ put $x_n=\{U_n\}$, $j_n=\lfloor16x_n\rfloor$,
$t_n=\{16x_n\}$, and
$c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor$. Then

$$
c_{n+1}=j_n+s_{n+1},\qquad
s_{n+1}=\lfloor t_n+r(n+1)\rfloor\in\{0,1\}.
$$

The carry can be $16$. It is retained literally; only a character evaluates
its residue modulo $16$. The unresolved relation between these two
integer observables is the exceptional set where $s_{n+1}=1$.

We also need a scaled observer, **without changing the primary source**.
For any positive integer $a$, define

$$
x_n^{(a)}=\{aU_n\},\quad
j_n^{(a)}=\lfloor16x_n^{(a)}\rfloor,\quad
c_{n+1}^{(a)}=\lfloor aU_{n+1}\rfloor-16\lfloor aU_n\rfloor,
$$

$$
s_{n+1}^{(a)}=c_{n+1}^{(a)}-j_n^{(a)}
=\left\lfloor\{16aU_n\}+a r(n+1)\right\rfloor\ge0.
$$

An early scaled spill may exceed one. The count below counts a positive
spill once, and never assumes these early values are binary.

The established original-source inequality is

$$
0<r(k)<\frac{15}{64(k-1)^2}\quad(k\ge2),
$$

and $r$ is decreasing. Both follow from the literal four-pole positive
moment formula; see the source derivation in
[BBP_DIOPHANTINE_COHERENCE.md](../2026-10-25/BBP_DIOPHANTINE_COHERENCE.md),
section 1. No equidistribution or digit-frequency premise enters this
bound.

## 2. A positive spill forces a logarithmic zero-carry interval

**Theorem SBA-1 (PAPER-PROVED, source-dependent gap).** For $k\ge2$ and
$a\ge1$, put

$$
L_a(k)=\max\left(0,
\left\lfloor\log_{16}\frac{4(k-1)^2}{a}\right\rfloor\right).
$$

If $s_k^{(a)}>0$, then

$$
\boxed{c_{k+\ell}^{(a)}=0
\quad\text{for every }1\le\ell\le L_a(k).}
$$

In particular no further spill can occur in those transitions. This
holds for every real initial value with the same forcing; the zero seed
is not used in this local implication.

*Proof.* At a spill, writing $t=\{16aU_{k-1}\}$ and
$s=\lfloor t+a r(k)\rfloor\ge1$ gives

$$0\le x_k^{(a)}=t+a r(k)-s<a r(k).$$

This is valid even if $s>1$. Since reduction modulo one only decreases a
nonnegative value, monotonicity of $r$ implies, for every $\ell\ge1$,

$$
16x_{k+\ell-1}^{(a)}+a r(k+\ell)
<a r(k)\left(16^\ell+\frac{16^\ell-1}{15}\right)
<\frac{a(16^{\ell+1}-1)}{64(k-1)^2}.
$$

If $1\le\ell\le L_a(k)$, then
$a16^\ell\le4(k-1)^2$, so the last upper bound is strictly less than
one. Its floor is the scaled literal carry, proving the result.
When $L_a(k)=0$ there is no asserted successor interval. $\square$

This is an arithmetic upper bound on an exceptional timeline, with its
definition independent of a Fourier estimate. It is not a statement
that positive or negative carries are uniformly distributed.

## 3. Explicit all-horizon count, including growing scale

Write

$$K_{N,a}=\#\{k\in\{2,\ldots,N+1\}:s_k^{(a)}>0\}.$$

**Theorem SBA-2 (PAPER-PROVED, effective count).** For every integer
$2\le R\le N+1$,

$$
\boxed{K_{N,a}\le\mathcal K(N,a;R):=
\min\left(N,R-2+
\left\lceil\frac{N+2-R}{L_a(R)+1}\right\rceil\right).}
$$

For $R>N+1$ use the trivial upper bound $N$.

*Proof.* There are at most $R-2$ spill indices in $[2,R)$. Among indices
in $[R,N+1]$, successive spills have distance at least $L_a(R)+1$, since
$L_a(k)$ is nondecreasing and SBA-1 applies after every spill. Packing
such indices in an integer interval of length $N+2-R$ gives the ceiling
term. $\square$

Prescribe, before observing any source states,

$$
R_{N,a}=\max\left(2,1+\left\lfloor(aN^2)^{1/4}\right\rfloor\right),
\qquad\mathcal K_{N,a}=\mathcal K(N,a;R_{N,a}).
$$

The implementation uses two nested integer square roots, which compute
the integer fourth root exactly. If $N\ge4$ and $1\le a\le N^2$, then

$$
\boxed{
\frac{\mathcal K_{N,a}}N
\le\left(\frac a{N^2}\right)^{1/4}
+\frac1{1+\lfloor\log_{16}(N/\sqrt a)\rfloor}.}
$$

To check this rate, let $v=(aN^2)^{1/4}\ge2$ and $q=\lfloor v\rfloor$.
Then $q\ge v/2$, so $4q^2/a\ge N/\sqrt a\ge1$ and
$L_a(q+1)\ge\lfloor\log_{16}(N/\sqrt a)\rfloor$.
The packing bound is at most $q+N/(L_a(q+1)+1)$; divide by $N$ and use
$q\le v$. This proves the displayed estimate with all rounding costs.

Consequently

$$
K_{N,1}=O(N/\log N),\qquad
K_{N,a_N}=o(N)\quad\text{for every prescribed integer }a_N=o(N^2).
$$

The latter includes growing observation scales larger than $N$. It is a
transport statement even where very fine conditional tables themselves
have large energy. There is no assertion that such tables approach Haar.

**Corollary SBA-2a (PAPER-PROVED, authentic quadratic-scale obstruction).**
The subquadratic allowance cannot be extended to every quadratic scale:
for every $N\ge1$, the unchanged authentic source satisfies

$$\boxed{K_{N,8N^2}=N.}$$

*Proof.* Directly combine the four signed poles to obtain

$$
r(N+1)=\frac{120N^2+151N+47}
{(2N+1)(4N+3)(8N+1)(8N+5)}.
$$

Writing the positive denominator as $D_N$, the exact difference is

$$
D_N\bigl(8N^2r(N+1)-1\bigr)
=448N^4+184N^3-336N^2-194N-15.
$$

For $m=N-1\ge0$, this polynomial equals

$$448m^4+1976m^3+2904m^2+1478m+87>0.$$

Thus $8N^2r(N+1)>1$ for every $N\ge1$. Monotonicity gives
$8N^2r(k)>1$ for all $2\le k\le N+1$, so
$s_k^{(8N^2)}=\lfloor\{16(8N^2)U_{k-1}\}+8N^2r(k)\rfloor\ge1$.
Every counted transition is a spill. $\square$

This obstruction uses the same genuine four-pole source and the same zero
selector. It is an exact manifestation of the forcing's critical $n^2$
scale, with no finite-window extrapolation. It establishes sharpness in
order for a universal vanishing spill-density guarantee, not an optimal
constant at the critical scale and not a Fourier lower bound.

## 4. Tail bins may be replaced by actual successor bins

Let $M\ge1$, $b_n=\lfloor M t_n\rfloor$, and
$b'_n=\lfloor M x_{n+1}\rfloor$. The original recurrence proves

$$
\boxed{b'_n\equiv b_n+s_{n+1}^{(M)}\pmod M.}
$$

Indeed $x_{n+1}=\{t_n+r(n+1)\}$ and
$\{M t_n\}=\{16M U_n\}$, so
$\lfloor M(t_n+r(n+1))\rfloor=b_n+s_{n+1}^{(M)}$.
Reducing by its integer multiple of $M$ gives the identity. Therefore

$$
\#\{1\le n\le N:b'_n\ne b_n\}\le K_{N,M}\le\mathcal K_{N,M}.
$$

This is a quantitative, source-authentic boundary-cell bound. It does
not infer small boundary occupation from the Lebesgue lengths of the
cells. It derives the count from expansion after an actual source spill.
At every prescribed $M_N=o(N^2)$, the fraction of changed bin labels tends
to zero. A multiple spill can leave a bin unchanged modulo $M$; counting
all positive spills is a safe overestimate.

At the explicit quadratic scale $M=8N^2$, however, **all $N$ bin labels
change**. Corollary SBA-2a gives $s_{n+1}^{(M)}\ge1$. Also
$r(n+1)\le r(2)=106/819<1/2$ and $M\ge8$, so

$$s_{n+1}^{(M)}<1+Mr(n+1)<1+M/2<M.$$

Hence the spill is nonzero modulo $M$, and the exact bin congruence proves
$b'_n\ne b_n$ for every $1\le n\le N$. This is a genuine boundary on
the representation-change statement for the authentic source. It does
not imply that the two conditional energies differ by a positive amount:
different row labels can still give equal energies.

The companion transport module handles the contingency-table effect of
changing row labels. The results below keep the original bins fixed, so
they do not assume that row reassignment is cost-free.

## 5. Conditional energy transport to literal carries

Fix **any** partition $B$ of the finite observation timeline; it may be
the original $M$ tail bins or a joint refinement by genuine source prime
channels. It need not be independent of the carries. Let
$p_b=n_b/N$ and define conditional characters

$$
F_b^j(h)=\frac1{n_b}\sum_{n\in b}\zeta_{16}^{h j_n},\qquad
F_b^c(h)=\frac1{n_b}\sum_{n\in b}\zeta_{16}^{h c_{n+1}},
$$

with energies $E^j(h)=\sum_b p_b|F_b^j(h)|^2$ and similarly $E^c(h)$.
Empty cells are omitted.

**Theorem SBA-3 (PAPER-PROVED, uniform over conditioning).** For every
integer $h$, every $N$, and every common partition,

$$
\boxed{|E^j(h)-E^c(h)|\le\frac{4K_{N,1}}N
\le\frac{4\mathcal K_{N,1}}N=O(1/\log N).}
$$

For the complete conditional branch chi-squared discrepancies,

$$
\boxed{|\Delta^j-\Delta^c|\le\frac{32K_{N,1}}N.}
$$

*Proof.* In a cell containing $e_b$ spills,
$|F_b^j-F_b^c|\le2e_b/n_b$ and both character means have modulus at most
one. Thus their squared moduli differ by at most $4e_b/n_b$; multiply by
$n_b/N$ and sum. For the chi-squared claim use

$$\Delta=\frac{16}{N}\sum_{b:n_b>0}
\frac{\sum_j n_{bj}^2}{n_b}-1.$$

Moving one sample from category $u$ to category $v$ in a fixed row changes
its squared-count sum by $2(n_{bv}-n_{bu}+1)$, whose absolute value is at
most $2(n_b-1)\le2n_b$. Hence each relabel costs at most $32/N$.
Apply one relabel at each spill. $\square$

The bounds hold uniformly even for a partition selected from the entire
source history, provided that precisely the same partition is used on
the two sides. They do not assert either energy vanishes. In particular
conditioning on the exact odd-conductor inverse data can make both
energies maximal, consistent with the independent odd-inverse obstruction.

For a fixed primitive $h$, the inherited midpoint inequality therefore
has the rigorously transported sufficient premise
$E^c_{N,M_N}(h)\to0$, where the literal carries are conditioned on the
original tail bins and $M_N\to\infty$. Proving that premise is still the
selected arithmetic problem; the label-change error is now discharged.

## 6. Parity, quarter turns, and the donor's primitive packet mass

For the conditional literal carry distribution, collapse residues modulo
four to $p_{b,0},\ldots,p_{b,3}$. Then

$$
E^c(8)=\sum_b p_b(p_{b,0}+p_{b,2}-p_{b,1}-p_{b,3})^2,
$$

$$
E^c(4)=E^c(12)=\sum_b p_b\left[
(p_{b,0}-p_{b,2})^2+(p_{b,1}-p_{b,3})^2\right].
$$

These are rational exact statistics, including the Gaussian quarter-turn
signs. The complete hierarchy identity is

$$
\boxed{
E^c(4)=\frac{1+E^c(8)}2-4\mathcal O,
\qquad
\mathcal O=\sum_b p_b(p_{b,0}p_{b,2}+p_{b,1}p_{b,3})\ge0.}
$$

This follows by expanding the two displayed squares. In particular
$E^c(4)\le(1+E^c(8))/2$, sharply: a single conditional row with equal
masses on residues $0$ and $1$ has $E^c(8)=0$ but $E^c(4)=1/2$.
Uniform residues $0,1,2,3$ instead have $\mathcal O=1/8$ and $E^c(4)=0$.
Thus parity balance alone cannot remove the quarter-turn mode. The
missing term is actual opposite-residue pairing inside each source cell;
the source atom identities $G^4=-I/4$, $H^4=I/4$ do not supply that pairing.
These controls are generic distributions, not authentic BBP trajectories.

PR #311's **declared endpoint packet translation** has conditional
primitive mass

$$\Phi_b=\frac49+\frac19\Pr(c_{n+1}\text{ odd}\mid b).$$

Its scalar parity relation therefore gives, exactly,

$$
\boxed{E^c(8)=324\sum_b p_b(\Phi_b-1/2)^2.}
$$

Consequently the authentic original branch parity energy differs from
this explicit conditional primitive-mass statistic by at most
$4\mathcal K_{N,1}/N$. This is a lawful quantitative connection to the
donor's carry-conditioned grammar. It uses the endpoint packet law as
declared; replacing it by the time-dependent packet law must separately
pay the donor's proved packet transport error. No source packet is
silently declared to be a distribution of inverse branch digits.

## 7. Failed shortcuts and exact controls

- Positivity alone does not imply sparse spills. The forced fixed point
  $x=1/32$ with constant forcing $17/32$ has $j=0,c=1$ and a spill at every
  time. It violates the decaying source bound.
- The theorem holds for every changed initial state under the original
  forcing. It therefore cannot select the zero seed or prove normality.
  The familiar same-forcing $V_n=-T_n$ control remains nonnormal and has
  no spills; its two energy representations can agree perfectly.
- Exact near-boundary rational controls retain the entire future
  original forcing and force an initial spill with $j=15,c=16$.
  They verify the nontrivial refractory intervals at transitions
  $k=3,9,33,129,513$ and selected scaled holdouts. They are labelled
  changed-seed controls, not authenticated zero-seed samples.
- The quarter-turn control above retains parity balance while leaving a
  nonzero $h=4$ energy. It prevents promotion of one dyadic shadow to all
  primitive frequencies.
- Conditioning on more arithmetic information does not automatically
  reduce conditional energy. The comparison only pays representation
  errors; source-selected cancellations inside or across cells remain
  necessary.

The focused suite independently rebuilds signed forcing from its four
literal poles and checks the native integer source through transition
258. It checks actual scaled spills and their zero-carry intervals through
513, exact integer fourth-root cutoffs, all-horizon packing holdouts,
multiple early scaled spills, complete quarter-turn/parity identities,
primitive packet mass, and intentional forcing/initialization mutations.
No transcendental approximation is needed for these certificates.

```bash
python -m unittest discover -s tests -p 'test_selected_branch_arithmetic.py' -v
```

**Next genuinely arithmetic obligation:** bound the conditional signed
literal-carry means, or their signed cross-cell aggregate, for the actual
zero-seeded source. The spill error, including the scaled error needed
to use actual successor bins, is now explicit and tends to zero at the
stated schedules. The surviving carry energy and cross-cell cancellation
remain OPEN.
