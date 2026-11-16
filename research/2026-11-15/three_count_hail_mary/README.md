# Three-count Hail Mary: sharp boundary transfer and the remaining zero-seed theorem

**Verdict:** the original zero-seeded positive budget, the selected
carry-density gate, R0, and pi normality remain **OPEN**. This assault
proved a sharp floor-transfer theorem, exact frame and entropy statements,
an explicit finite rational control, and the exact dimension of the
failed-gate endpoint set. A new certified holdout passed the proposed
finite budget with room to spare. None of those facts is promoted to an
all-shell estimate for pi.

**Parent:** draft [#650](https://github.com/femboy2112/SUCC/pull/650),
commit bf27f7ec8e757482613808bff693ba520ac13b3b.
The work began on 2026-11-15 UTC and continued into 2026-11-16.

## 1. The target, with every coordinate retained

The literal original source is

\[
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Put \(C_n=\lfloor U_n\rfloor\), \(J_n=n\bmod4\), and
\(K_n=[U_n-C_n]_4\). Brackets mean odd-denominator rational reduction in
\(\mathbb Z/4\mathbb Z\), not a real quarter-bin. The inherited source
clock says \(C_n=J_n-K_n\bmod4\).

On every integer shell \([B,2B)\), the parent proved

\[
d_B:=\Pr_B(C_n\bmod4\in\{1,2\})
\ \ge\
L_B:=\Pr_B(J=K=0)+\Pr_B(K=1)-\Pr_B(J<2,K<2).
\tag{1}
\]

The requested theorem is \(\liminf_{B\to\infty}L_B>0\), or a genuinely
weaker sufficient estimate for \(\liminf_Bd_B>0\).
The three-mass tolerance in the parent is sufficient, not necessary:

\[
\eta_{1,B}+\kappa_B+\eta_{2,B}\le1/32
\quad\Longrightarrow\quad L_B\ge1/32.
\]

Here the nonnegative errors are respectively the deficit of the first
mass from \(1/16\), the deficit of the second from \(1/4\), and the
excess of the third above \(1/4\).

The existing bridge gives real-phase anti-lock from
\(\liminf d_B\ge\delta>0\), with margin
\(\delta(1-\cos(\pi/8))\). This is only one sufficient rung. Full normality
still requires every nonzero fixed Fourier mode to cancel.

## 2. First result: the three counts collapse to a signed temporal test

All three lanes independently obtained

\[
\boxed{
L_B=\Pr_B(n\equiv2,C_n\equiv1)
   +\Pr_B(n\equiv3,C_n\equiv2)
   -\Pr_B(n\equiv1,C_n\equiv1).
}
\tag{2}
\]

All congruences are modulo four. On a complete four-step block, this
asks whether entry into carry class one at the next clock position,
together with the class-two event at clock three, outweighs the
corresponding exit from class one. It is an oriented temporal statistic.

Its orientation is a real additional burden. With the same forcing and
a changed completed endpoint \(0.\overline{5674}_{16}\), carries have
uniform residues, selected density \(1/2\), and budget tending to
\(-1/4\). This is a scoped control, not a counterexample to the zero seed.

The extra burden can be removed without discarding the finite certificate.
Apply its four common label shifts and the four shifted reflections
\((J,K)\mapsto(-J,1-K)\). Each remains a pointwise lower bound for the
same selected gate; their sum is exactly the gate. If \(M_B\) denotes
the largest of their eight empirical means, then

\[
\boxed{d_B/8\le M_B\le d_B.}
\tag{3}
\]

Thus positive lower density of the frame envelope is equivalent to the
wanted carry density. No single frame is asserted to win on every shell.
Equation (3) repairs the target specification; it does not pay its source
premise. Complete identities, Fourier coefficients, and controls are in
[ADVERSARY_NOTES.md](ADVERSARY_NOTES.md).

## 3. Main analytic gain: remove the floor tail with a sharp error

The authentic completion is

\[
U_n=16^n\alpha-T_n,\quad \alpha=\pi/16,\quad
0<T_n<1/(64n^2).
\]

Let \(Q_n=\lfloor16^n\alpha\rfloor\), and replace \(C_n\) by \(Q_n\)
in (2) and in the selected gate to obtain
\(\widetilde L_B,\widetilde d_B\). Then

\[
\boxed{
|L_B-\widetilde L_B|,\ |d_B-\widetilde d_B|
\le
\frac{1+\lfloor(B-1)/(m_B+1)\rfloor}{B},
\quad m_B=\lfloor\log_{16}(64B^2)\rfloor.
}
\tag{4}
\]

This needs no equidistribution, normality, or assumption that raw borrows
are rare. Both masks agree at residues zero and three. A borrow can
therefore change a mask only at a nonzero completed hexadecimal digit
followed by at least \(m_B\) zeros. Such changes are at least \(m_B+1\)
positions apart. This proves (4) on every integer shell. The eight frame
certificates have the same matching property.

In particular, the two liminf targets are **exactly preserved** when the
actual carries are replaced by the completed digits. The floor boundary
is no longer a separate unbounded error for these observables.

This rate is sharp even with the literal four-pole tail. A single
sparse-marker endpoint can make its nonzero digits borrow at every
marker, with gaps \(2\log_{16}n+O(1)\). Its signed floor correction is

\[
\pm\frac1{2\log_{16}B}+O((\log B)^{-2}).
\]

These sharpness controls use changed real seeds. They show that positivity
of the source tail alone cannot improve the universal order or orient
the signed correction. The canonical zero-seeded orbit could have a
smaller error, but that would need another source estimate.

See [TRANSLATOR_NOTES.md](TRANSLATOR_NOTES.md), T3--T4, and
[CONSTRUCTOR_NOTES.md](CONSTRUCTOR_NOTES.md), Section 4. This is distinct
from the earlier renewal estimate for one-step forcing carries: here the
comparison is the raw floor \(C_n\) against the completed floor \(Q_n\).

## 4. What an entropy proof would actually have to establish

For a limiting clocked digit law, the exact four-slot moment function is

\[
M(t)=\frac{(3+e^t)^2(3+e^{-t})}{64}.
\]

Conditional entropy and the Gibbs inequality give

\[
h\le\log16+\tfrac14\log M(t)-t\,\mathbb E\ell.
\tag{5}
\]

This proves the following sharp thresholds. Entropy here is the rate of
an invariant law obtained from empirical digit windows, not algorithmic
randomness or a claim that the source is physically random.

| Desired conclusion | Sufficient entropy for every shell limit | Boundary |
|---|---:|---|
| Positive fixed three-count budget | More than 3.9793957988 bits/hex digit | Sharp tilted clock law has budget zero at this entropy |
| Budget greater than \(1/32\) | More than 3.9949244219 bits/hex digit | Sharp pressure threshold for this margin |
| Positive selected carry density | A fixed margin above 3 bits/hex digit | An eight-symbol independent law has exactly 3 bits and no hits |
| Positive selected carry density using only residues | A fixed margin above 1 bit/mod-four residue | Separate, potentially weaker premise |

The last two statements use

\[
h_{\rm hex}\le3+H_2^{\rm bits}(d),\qquad
h_{\rm residue}\le1+H_2^{\rm bits}(d).
\tag{6}
\]

A margin \(\epsilon\) gives
\(\liminf d_B\ge(H_2^{\rm bits})^{-1}(\epsilon)>0\), with the inverse
on \([0,1/2]\). Full-digit entropy above three bits implies residue entropy
above one, since \(h_{\rm hex}\le h_{\rm residue}+2\); the converse need
not hold. The high two bits may be deterministic.

Every premise concerns **all subsequential empirical limits of all
integer shells**. Finite histograms, high entropy on selected shells,
and auxiliary random probes do not establish it. No such entropy
lower bound for the authentic source has been proved in this assault.
The point of this comparison is to avoid paying for an unnecessary
clock orientation while attacking the selected event.

## 5. Exact size of the obstruction, and a stronger arithmetic control

For arbitrary completed endpoints with the fixed BBP tail, let

\[
E=\{\beta:\liminf_Bd_B(\beta)=0\}.
\]

The second-pass theorem is

\[
\boxed{\dim_{\rm H}E=7/8.}
\tag{7}
\]

The upper bound counts words with very few symbols outside the eight
unselected digits; the lower bound forces only those eight digits on
widely separated complete shells and allows all sixteen elsewhere.
The floor-transfer theorem identifies the raw and completed exceptional
sets exactly. The full proof is in
[EXCEPTIONAL_SET.md](EXCEPTIONAL_SET.md), independently audited in
[EXCEPTIONAL_SET_AUDIT.md](EXCEPTIONAL_SET_AUDIT.md).

This does not exclude \(\pi/16\) from E. In fact E contains endpoints
of ordinary irrationality exponent two and restricted power-sixteen
exponent zero in every finite hexadecimal cylinder. They can be built
by appending a scaled zero/three Thue--Morse tail. The imported exponent-two
theorem is Bugeaud's; the gate exclusion and dense-prefix construction
are explicit here. Thus even optimal values of these two approximation
exponents, together with any finite correct digit prefix, do not by
themselves pay the required source exclusion.

The source selection remains essential in a second, fully rational way.
For every finite horizon N, precision \(L\ge2\), and prescribed carry word,
we explicitly construct a rational seed \(s\in2^L\mathbb Z_{(2)}\) with

\[
U_n(s)\equiv U_n(0)\pmod{2^{L+4n}}\quad(n\ge0),
\]

while its first N carry residues are exactly the prescribed word.
The seed height is at most \(2^{L+4N+8}+1\), and its construction uses
only a finite rational BBP prefix. This refutes seed-uniform bounded
potential arguments. It does not refute a zero-seed-only or
height-sensitive argument.

The infinite Thue--Morse controls and the finite rational controls retain
different properties; their hypotheses are not silently combined.
The exact zero seed is retained in all affirmative source observations.

## 6. Fresh certified source holdout

The [protocol](HOLDOUT_PROTOCOL.md) was frozen before generating the
extension. Original four-pole outward integer enclosures certified the
source through index 131072. Every integer shell with
\(32769\le B\le65536\) uses only observations beyond the parent's horizon.

| Predeclared finite statistic | Exact extremum | Shell B |
|---|---:|---:|
| Minimum \(L_B\) | \(1997/33657\) | 33657 |
| Minimum selected density \(d_B\) | \(16393/32911\) | 32911 |
| Maximum one-sided error budget | \(136/33785\) | 33785 |

All **32768 shells** passed the predeclared error tolerance \(1/32\).
No carry borrow occurred anywhere in the certified 131072-state prefix.
The first 32768 carries exactly match the parent's receipt.
The final tested shell ends at 131071; the state 131072 is extra.

The root's prefix-sum audit and a separately written sliding sixteen-cell
recount reproduced the same extrema. A literal-four-pole rational
implementation separately checked the first 512 states. These checks
share source provenance; they are not independent evidence of a universal
digit-distribution claim.

Run [independent_audit.py](independent_audit.py) to reproduce the exact
algebra, rational controls, and frozen statistics from the retained
receipts. [VALIDATION.md](VALIDATION.md) records the executed repository
gates and the precise scope of the audit.

## 7. The unresolved step, stated without substitution

The sharpened carry target is

\[
\boxed{\pi/16\notin E,}
\]

or, equivalently, a strictly positive lower shell density of the selected
raw carries. The fixed-frame three-count budget is a stronger sufficient
route. Proving either source claim would be a real advance on the current
anti-lock rung; normality would still require the remaining modes.

Bailey--Crandall's original paper displays exactly this rational
radix-sixteen recurrence with zero seed. Its equidistribution assertion
is an instance of their Hypothesis A. Lagarias proves the general orbit
correspondence while explicitly separating that correspondence from
arithmetic normality. We cannot borrow either missing conclusion as a
transfer-operator theorem.

The next theorem must distinguish the zero-selected endpoint using
the exact source arithmetic, rather than just positivity, a finite
dyadic view, histogram agreement, or a generic-seed probability estimate.
Concrete permissible next targets and their controls are in [NEXT.md](NEXT.md).
No claim of scholarly priority, independent external refereeing, formal
kernel verification, or a proof of pi normality is made.
