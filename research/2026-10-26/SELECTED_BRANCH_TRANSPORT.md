# Carry and future-bin transport with a source-derived error bound

**Authority: PAPER-PROVED finite inequalities and all-horizon transport;
EXACT FINITE rational/cyclotomic instruments. Selected cancellation OPEN.**
The original four-pole forcing, unwrapped states, zero initial state, and
literal carries are unchanged. The new estimates bound a representation
error; neither side of the comparison is proved small.

Parent: PR #312 at `0c306a889f425418c29cbea3193205fb80c0575e`.
The carry/packet scalar identity is independently rederived from sibling
PR #311 at `a34c4484059e667202b97d5ab4102560987b1406`; that sibling is
not merged or silently treated as an ancestor.

## 1. The actual two conditional laws

For the authentic orbit write

$$x_n=\{U_n\},\quad j_n=\lfloor16x_n\rfloor,\quad
t_n=\{16x_n\},\quad
c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor.$$

For $1\le n\le N$ and an integer $M\ge1$, compare the records

$$R_n=(\lfloor Mt_n\rfloor,j_n),\qquad
\widetilde R_n=(\lfloor Mx_{n+1}\rfloor,c_{n+1}\bmod16).$$

Reduction modulo 16 occurs only in the character or contingency label.
The literal carry, including the possible value 16, is preserved upstream.
Let $E_{N,M}(h),\Delta_{N,M}$ be PR #312's original conditional quantities,
and put tildes on the quantities from $\widetilde R_n$. Thus the latter
condition an actual carry on its actual arrival state, rather than on an
artificially uniformly sampled predecessor.

## 2. Changing a record: sharp universal conditional stability

Consider any $N$ labelled observations partitioned into bins. For a fixed
character, each observation has a complex value $z$ of modulus one. A bin
with $n$ observations and sum $S$ contributes $|S|^2/(Nn)$ to $E$;
an empty bin contributes zero. Write $F(S,n)=|S|^2/n$.

**Lemma 1.** Adding one unit observation to a bin changes $F$ by a number
in $[-3,1]$. For $n>0$, direct subtraction gives

$$F(S+z,n+1)-F(S,n)
=\frac{2\operatorname{Re}(S\overline z)+1-|S|^2/n}{n+1}.$$

The upper bound follows from $F(S+z,n+1)\le F(S,n)+1$, the weighted
Cauchy inequality. For the lower bound use $|S|\le n$ in the displayed
numerator: it is at least $1-3n$, hence the quotient exceeds $-3$.
Adding to the empty bin gives exactly 1. Removing a record is the
negative of an addition. Consequently replacing one record, allowing
both its label and its bin to change, changes $E$ by at most $4/N$.
Perform the replacements one at a time, retaining total size $N$ after
each pair; the temporary $N-1$ table is only an unnormalized sum.

For the full 16-category table put $G(v,n)=\|v\|_2^2/n$, where $v$ is
the count vector. Adding label $j$ changes it by

$$\frac{2v_j+1-\|v\|_2^2/n}{n+1}\in[-1,1].$$

The upper bound again is weighted Cauchy; the lower uses $v_j\ge0$ and
$\|v\|_2^2\le n^2$. Since $\Delta=(16/N)\sum_bG(v_b,n_b)-1$,
one arbitrary replacement costs at most $32/N$. Thus, if two ordered
data sets differ in at most $K$ records,

$$\boxed{|E(h)-E'(h)|\le\min(1,4K/N),\qquad
|\Delta-\Delta'|\le\min(15,32K/N).}$$

These constants cannot be uniformly reduced: a single bin of $N$ copies
of digit zero, with one copy changed to digit one, changes parity energy
by $4(N-1)/N^2$ and total defect by $32(N-1)/N^2$. Bin changes cannot
be omitted from the budget: two opposite parity labels in one bin have
energy zero; separating them into singleton bins gives energy one.
The lemma is universal; its arithmetic content comes from the independent
source bound on the number of changes below.

## 3. The original forcing pays for both changes

The [carry-spill theorem](SELECTED_BRANCH_ARITHMETIC.md) proves the
following without inspecting any measured Fourier energy. At an integer
scale $a\ge1$ define

$$\sigma_k^{(a)}=
\left\lfloor\{16aU_{k-1}\}+a r(k)\right\rfloor\ge0.$$

If it is positive, then $\{aU_k\}<a r(k)$. Positivity and the original
four-pole bound $r(k)<15/[64(k-1)^2]$ force the following

$$L_a(k)=\max\left(0,\left\lfloor
\log_{16}\frac{4(k-1)^2}{a}\right\rfloor\right)$$

scaled literal carries to be zero. This gives the explicit prior bound,
for any integer $2\le R\le N+1$,

$$K(N,a)\le B(N,a;R):=
\min\left(N,R-2+
\left\lceil\frac{N+2-R}{L_a(R)+1}\right\rceil\right),$$

where $K$ counts positive spills at transitions $2,\ldots,N+1$.
Use the preset cutoff $R=\max(2,1+\lfloor(aN^2)^{1/4}\rfloor)$, and
the trivial bound $N$ if this exceeds $N+1$. Denote this bound by
$B(N,a)$. The proof gives $B(N,1)=O(N/\log N)$ and, for every
prescribed integer schedule $a_N=o(N^2)$, $B(N,a_N)=o(N)$.
The same estimate holds for arbitrary real initial states with this
forcing, so it is not by itself a zero-selector theorem.

Now $c_{n+1}\ne j_n$ implies $\sigma_{n+1}^{(1)}>0$. For the bins let
$b=\lfloor Mt_n\rfloor$ and $\sigma=\sigma_{n+1}^{(M)}$. Since
$\{16MU_n\}=\{Mt_n\}$, the original recurrence gives exactly

$$\lfloor Mx_{n+1}\rfloor\equiv b+\sigma\pmod M.$$

Thus a changed bin implies a positive scaled spill. This includes early
spills larger than one: the count records the event, not its magnitude.
There are at most $K(N,1)+K(N,M)$ changed records in the comparison.
Applying Lemma 1 proves the new source-conditioned inequality

$$\boxed{
|E_{N,M}(h)-\widetilde E_{N,M}(h)|
\le \min\left(1,\frac{4[B(N,1)+B(N,M)]}{N}\right),
}$$

$$\boxed{
|\Delta_{N,M}-\widetilde\Delta_{N,M}|
\le \min\left(15,\frac{32[B(N,1)+B(N,M)]}{N}\right).
}$$

Both errors tend to zero for every prescribed $M_N=o(N^2)$. In
particular $M_N=\max(2,\lfloor\log_2N\rfloor)$ gives an
$O(1/\log N)$ error. The estimate is uniform in the character $h$;
it bounds an energy difference, not merely a difference of square roots.
Fine bins may still make both energies maximal. There is no assertion
that the schedule condition alone implies cancellation.

## 4. What the carry-sensitive Oily totient actually contributes

The endpoint translated packet law of pinned #311 has conditional
primitive mass

$$\Phi_b=\frac49+\frac19\Pr(c_{n+1}\text{ odd}\mid
\lfloor Mx_{n+1}\rfloor=b).$$

This follows also by folding $w_j=(j+1)/2^{j+2}$: its even mass is
$5/9$ and odd mass $4/9$; translating by an odd carry interchanges them.
The exact parity calculation is

$$\boxed{\widetilde E_{N,M}(8)
=324\sum_b\widetilde p_b(\Phi_b-1/2)^2.}$$

Combining this identity with Section 3 pays rigorously for the passage
from the genuine carry-conditioned primitive statistic to the original
inverse-branch parity energy. This is the previously missing quantitative
edge between those two specific constructions. It does not prove that
$\Phi_b$ approaches $1/2$. Auxiliary unconditioned packet marginals,
Gaussian coefficient holonomy, and grading-dependent cumulants supply
no estimate for that conditional variance.

## 5. Retain signed cross-bin terms: a cheaper finite Weyl instrument

The positive energy is sufficient, but it discards potentially decisive
signs between bins. Put $\tau_b=(b+1/2)/M$ and define the signed quantity

$$\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N
e\left(\frac{h(c_{n+1}+\tau_{\lfloor Mx_{n+1}\rfloor})}{16}\right).$$

The exact unwrapped recurrence implies
$x_n=(c_{n+1}+x_{n+1}-r(n+1))/16$. The character Lipschitz inequality
therefore proves, for every integer $h$ and all $N,M\ge1$,

$$\boxed{
|A_N(h)-\widetilde C_{N,M}(h)|
\le\frac{\pi|h|}{16M}
+\frac{\pi|h|}{8N}\sum_{n=1}^N r(n+1).
}$$

The source sum is at most 15, so the second term is $O_h(1/N)$.
Unlike the discontinuous conditional-energy comparison, this continuous
signed transport needs no spill count and no upper bound on $M$.
All fixed frequencies, including multiples of 16, are covered directly.
No source term is dropped without paying this displayed error.

The smallest required object for this route is the actual bin amplitude
vector, with its phases $e(h\tau_b/16)$, rather than its diagonal
conditional energies. Squaring the signed sum retains every cross-bin
term. This is the same signed-observable discipline as #306, not a new
positive-Gram cancellation claim. The code uses the existing Machin/Taylor
rational interval instrument to evaluate this finite vector. It does
not add a new cyclotomic or transcendental source engine.

For example the synthetic three-bin records $(0,0),(1,5),(2,10)$ at
$M=3$ have midpoint phases $1/96+k/3$. Their $h=8$ signed sum is zero
although their conditional parity energy is one and total defect is 15.
The [analytic control](SELECTED_BRANCH_ANALYTIC.md) strengthens this
finite example to a single history satisfying the original forcing,
with a clearly disclosed changed initial seed.

The signed instrument alone is a representation, not a new asymptotic
saving. Its role is to avoid demanding conditional-energy decay where
cross-bin cancellation could suffice. The new arithmetic theorem in
this dossier is the source-derived, all-horizon stability estimate in
Section 3, built on the proved sparse spill set.

## 6. Authority and next obstacle

The perspective inequalities, scaled-spill transport and signed bound
are paper proofs. Exact rational source reconstructions, cyclotomic
Parseval checks, held-out bin/label replacements, sharp constant controls,
source mutations and outward character intervals test their native
implementations. The Lean parity-perspective lemma is only a finite
real inequality; it does not formalize these complete analytic statements.

The remaining stronger statement is an independent source-selected
bound on $\widetilde E_{N,M_N}(h)$, or on the signed cross-bin sum
$\widetilde C_{N,M_N}(h)$, at a preset growing resolution. The universal
spill bound has removed a particular discrepancy between actual carries
and inverse digits; it has not proved that the remaining carry/arrival
correlations cancel. π normality remains **OPEN**.
