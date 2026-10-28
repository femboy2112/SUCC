# Integer-branch coercivity: a stronger selected BBP logarithmic bound

**Status: PAPER-PROVED from the unchanged source and a published irrationality
bound; exact finite core checked separately.** This is a genuine improvement of
the constant in the selected Fourier bound. It is **not a change of asymptotic
order, not a relative saving, and not a proof of π normality**. Academic priority
is unverified. The numerical onset of the theorem remains unspecified.

Starting tree: PR #310, `a8c7c85b7a1900d422090f1757c174e7aac69f44`.
The original BBP arithmetic engine and all historical archives are unchanged.
The finite source adapter imports `authentic_r` and `original_state` from
`observational_succ.succ_internal_matrix_walk`.

## 1. Result and hole contract

Keep precisely

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

Write $S_N^U(h)=\sum_{n=1}^N e(hU_n)$, where $e(x)=e^{2\pi ix}$.
There exists one integer $J_1$ such that, for **every** integer $N\ge1$ and
**every** integer $h\ne0$,

$$
\boxed{
|S_N^U(h)|\le N-\frac1{29}
\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J_1,1+\lceil\log_{64}|h|\rceil\right)\right).
}
\tag{BC-1}
$$

Thus, for every fixed $h\ne0$,

$$
|S_N^U(h)|\le N-\frac{\log_8N}{29}+O_h(1).
\tag{BC-2}
$$

The previous leading coefficient was $1/1250$. The ratio of the new and old
coefficients is $1250/29>43$. The thresholds of the two theorems are unspecified
and need not be equal: no claim of improvement at every numerically accessible
$N$ follows. The uniform band pays **one additional geometric block** in its
frequency cutoff. The theorem operates directly on $U_n$; it does not subtract
an $O_h(1)$ Green comparison from every block and so does not lose uniformity
in the stated growing frequency band.

**Exact dependency cut.** The old inverse theorem made every centered phase
small, then bounded each possible branch difference by a coordinatewise triangle
inequality. That forced $34a<1$. The new finite lemma instead says: *two distinct
integer branches already consume a definite amount of the total squared phase
error*. It uses the squared norm $546$ of the adjacent branch-difference vector
$(16,-17,1)$. This is an actual inequality improving the proved selected bound,
not a relabeling of the missing normality estimate.

**Novelty tax.** The ingredient is elementary Euclidean coercivity applied to the
existing source inverse theorem. It does not invent a new irrationality input,
prove cross-time independence, or identify a canonical Oily–Macaroni grading.
Its cheapest falsifiers are the adjacent-transition overlap (which defeats the
incorrect coefficient $514$), a large-phase cosine control, a source-unchanged
changed seed, and a missing factor $9$ in the Diophantine comparison. All are
retained in the exact tests.

## 2. The finite integer-branch lemma

Let $T\ge2$ and let real values satisfy

$$X_{t+1}=16X_t+r_{t+1},\qquad 0\le t<T.$$

Fix $h\in\mathbb Z\setminus\{0\}$ and put

$$
L=(T+1)-\left|\sum_{t=0}^T e(hX_t)\right|,
\qquad R=|h|(\max_jr_j-\min_jr_j).
$$

Suppose

$$R<1,\qquad \frac{19(1-R)^2}{546}>\frac1{29}.\tag{BC-3}$$

Then $L\le1/29$ implies that all lifted integer branches are equal, and
consequently, for some integer $p$,

$$
\boxed{
\left|X_0+\sum_{j=1}^T16^{-j}r_j-\frac p{15|h|}\right|
\le\frac{32/15+|h||r_T|}{15|h|16^T}.
}
\tag{BC-4}
$$

This is a necessary condition for extreme coherence, not a sufficient one.

### Proof: pay for branch changes with total energy

Since $L<1$, the sum is nonzero. Choose its direction $e(\theta)$, and choose
$q_t\in[-1/2,1/2]$ such that

$$y_t=\theta+q_t=hX_t+\ell_t,\qquad\ell_t\in\mathbb Z.$$

The exact resultant identity gives

$$L=\sum_{t=0}^T[1-\cos(2\pi q_t)].\tag{BC-5}$$

The standard chord bound $|e(q)-1|\ge4|q|$ for $|q|\le1/2$ implies

$$8\sum_tq_t^2\le L\le\frac1{29}.$$

In particular $q_t^2\le1/232<1/225$, so $|q_t|<1/15$.
On this interval the Taylor bound and elementary rational bounds
$25/8<\pi<22/7$ yield

$$
\begin{aligned}
1-\cos(2\pi q)
&\ge2\pi^2q^2-\frac23\pi^4q^4\\
&\ge\left[2\left(\frac{25}8\right)^2
 -\frac2{675}\left(\frac{22}7\right)^4\right]q^2
\ge19q^2.
\end{aligned}
\tag{BC-6}
$$

The last inequality is strict when $q\ne0$; equality at $q=0$ is retained.
The coefficient minus $19$ is the positive rational
$12559091/51861600$. This **local** cosine estimate is not asserted for arbitrary
$q$; at $q=1/2$ it would be false.

Define the branch residuals

$$d_t=q_{t+1}-16q_t-hr_{t+1}.$$

Substitution of the exact recurrence shows
$d_t=15\theta+\ell_{t+1}-16\ell_t$. Hence every difference $d_j-d_k$ is an
integer. If some two residuals differ, their difference has absolute value at
least one, so

$$
|q_{j+1}-16q_j-q_{k+1}+16q_k|\ge1-R.
$$

For adjacent transitions the linear coefficient vector is, up to sign,
$(16,-17,1)$ and has squared norm $546$. For disjoint transitions its
squared norm is $2(16^2+1)=514$. Therefore Cauchy–Schwarz gives

$$(1-R)^2\le546\sum_tq_t^2.$$

Combining with (BC-5)--(BC-6) gives

$$L\ge19\sum_tq_t^2\ge\frac{19(1-R)^2}{546}>\frac1{29},$$

contradicting the hypothesis. All residuals have a common value $b$.
Write $k=b-15\theta\in\mathbb Z$ and $f=-k/15$. Then

$$y_{t+1}-f=16(y_t-f)+hr_{t+1}.$$

Backward telescoping, followed by the last transition, gives

$$
y_0-f+h\sum_{j=1}^T16^{-j}r_j=16^{-T}(y_T-f),
\qquad
y_T-f=\frac{16(q_T-q_{T-1})-hr_T}{15}.
$$

Because $|q_t|<1/15$, we have
$|y_T-f|\le(32/15+|h||r_T|)/15$.
Finally, $y_0-hX_0\in\mathbb Z$ and $15f\in\mathbb Z$, so division by $h$
proves (BC-4), with a positive denominator $15|h|$. QED.

The overlap coefficient $546$ is exact for the Euclidean comparison. It does
not claim the full analytic threshold $1/29$ is optimal.

## 3. Apply the lemma without changing the authentic selector

The inherited source proof establishes, directly from the four poles,

$$
0<r(n+1)<\frac{15}{64n^2},\qquad
0<T_n<\frac1{64n^2},\qquad
U_n+T_n=16^{n-1}\pi.
\tag{BC-7}
$$

The tail is the actual future Green sum
$T_n=\sum_{j\ge1}16^{-j}r(n+j)$, and the last identity uses $U_0=0$.
These are reused from [the complete source proof](../2026-10-25/BBP_DIOPHANTINE_COHERENCE.md),
not assumed from a normality conjecture.

Take an integer $m\ge8$ and $1\le|h|\le m^2/64$. On the block
$n=m+1,\ldots,8m$, set

$$X_t=U_{m+1+t},\qquad T=7m-1,\qquad r_j=r(m+1+j).$$

Monotonicity and (BC-7) give

$$R<\frac{m^2}{64}\frac{15}{64(m+1)^2}<\frac{15}{4096}.$$

The exact margin is

$$
\frac{19}{546}\left(\frac{4081}{4096}\right)^2-\frac1{29}
=\frac{2329025}{37950062592}>0.
\tag{BC-8}
$$

Thus (BC-3) holds throughout this band. If the block had loss at most $1/29$,
then (BC-4) and the **exact** Green cancellation

$$
U_{m+1}+\sum_{j=1}^T16^{-j}r(m+1+j)
=16^{-T}U_{8m}=16^m\pi-16^{-T}T_{8m}
$$

would produce a rational with denominator $q=15|h|16^m$ satisfying

$$
\left|\pi-\frac pq\right|
\le16^{-8m}16\left[
\frac{32}{225|h|}
+\frac1{64(8m-1)^2}+\frac1{64(8m)^2}
\right]
<3\,16^{-8m}.
\tag{BC-9}
$$

The bracket coefficient is at most $6447953/2822400<3$ (take $m=|h|=1$),
so its bound holds even beyond the required $m\ge8$ regime.

### Imported arithmetic theorem and quantifiers

Zeilberger and Zudilin's corrected paper proves
$\mu(\pi)\le7.103205334137\ldots<15/2$:
[arXiv:1912.06345v2](https://arxiv.org/abs/1912.06345v2), published as
*Moscow Journal of Combinatorics and Number Theory* **9** (2020), 407--419,
[DOI](https://doi.org/10.2140/moscow.2020.9.407).
The authors' abstract, corrected-version date and journal reference were checked
at the primary arXiv source this round. We do not use any claimed improvement to
exponent two or any more recent unverified preprint.

Exactly as in the prior dossier, the theorem implies that some rational
$C\in(0,1]$ satisfies

$$|\pi-p/q|\ge Cq^{-15/2}$$

for all integer $p$ and all positive integer $q$, including unreduced fractions.
The finitely many exceptional reduced denominators are absorbed into $C$ using
irrationality. This $C$ is not numerically extracted here.

Consequently (BC-9) is impossible whenever

$$C^2 16^m>9(15|h|)^{15}.\tag{BC-10}$$

The factor $9$ is essential: the upper approximation bound was $3\,16^{-8m}$,
not $16^{-8m}$. Since exponential growth dominates a fixed polynomial, one
integer $m_1\ge64$ makes (BC-10) true for every $m\ge m_1$ and every
$1\le|h|\le m^2/64$. For example it suffices to require
$C^2 16^m>9(15m^2)^{15}$; the sequence $16^m/m^{30}$ is increasing for
$m\ge64$, by the same elementary Bernoulli bound used in the prior dossier.
Thus one common threshold works, proving

$$
\boxed{
\left|\sum_{n=m+1}^{8m}e(hU_n)\right|<7m-\frac1{29}
\quad(m\ge m_1,\ 1\le|h|\le m^2/64).
}
\tag{BC-11}
$$

This is the new source-selected inequality. The entire signed arithmetic source,
its initial selection and the exact Green cancellation remain load-bearing.

## 4. Assemble all N and audit the frequency band

Put $J_1=\lceil\log_8m_1\rceil$. The complete disjoint geometric blocks
$(8^j,8^{j+1}]$ fit in $[1,N]$ for $0\le j<\lfloor\log_8N\rfloor$.
For $m=8^j$, their frequency condition is

$$|h|\le64^{j-1}\quad\Longleftrightarrow\quad
j\ge1+\lceil\log_{64}|h|\rceil.$$

Apply (BC-11) on eligible blocks and the trivial bound to the remaining
observations. The triangle inequality proves (BC-1), including the empty-block
case. No cancellations between different blocks have been assumed.

For any prescribed maximum mode $H-1\ge1$, the same formula with $|h|=H-1$
controls every $0<|h|<H$. Inserting it in the existing exact Fourier purity
identity yields only

$$
\frac{D_{N,H}}H\le(H-1)
\left(1-\frac{K_1(N,H)}{29N}\right)^2,
$$

where $K_1(N,H)$ is the count in (BC-1) with $|h|=H-1$.
This remains of order $H$ and cannot prove the required $o(1)$ energy.
In particular the new inverse lemma escapes the old *coordinatewise* $34a$
ceiling, but not the *constant total-deficit* regime. Moderate coherence remains
uncontrolled. The larger coefficient must not be advertised as a new order of
arithmetic cancellation.

## 5. Hostile controls, exact instruments and validation

The same-forcing rational changed initial

$$v_m=-16^{-8m}U_{8m},\qquad X_n=U_n+16^nv_m$$

makes $X_{8m}=0$ and every inverse center exactly zero. It has loss tending to
zero for fixed $h$ by the inherited explicit bound, so it defeats any extension
of (BC-11) to arbitrary seeds. It does not refute (BC-11), whose use of the
zero selector is explicit. One seed is constructed per finite window; no
universal rational changed seed is claimed.

Other retained controls:

- Zero forcing and a fixed phase $X_0\in\frac1{15}\mathbb Z$ correctly lie
  inside the necessary arcs.
- A forcing-range mutation with $R=1/100$ violates the new sufficient margin
  and is rejected; the code never claims to handle it through this theorem.
- Adjacent transitions have norm squared $546$, so substituting the disjoint
  value $514$ is a concrete false finite lemma.
- $q=1/2$ defeats an illicit global version of $1-\cos(2\pi q)\ge19q^2$.
- A rational supplied Diophantine constant is tuned so that dropping factor
  $9$ changes the comparison outcome. Neither supplied constant is certified
  as valid for π.
- The previously documented sparse selector
  $\xi=\sum_{k\ge0}16^{-2^k}$ still has exponent two and
  $S_N^\xi(h)=N+O_h(\log N)$. Thus finite irrationality type alone cannot
  supply a superlogarithmic loss, much less normality. The present proof has
  not gained the additional source-specific input needed to evade that ceiling.

Artifacts:

- [Native exact instruments](../../observational_succ/bbp_branch_coercivity.py).
- [Exact and adversarial tests](../../tests/test_bbp_branch_coercivity.py).

The focused invocation
`python -m unittest tests.test_bbp_branch_coercivity -v` completed with **12 tests
passing**. An initial test-only Diophantine mutation fixture was incorrectly
chosen and failed; replacing it with the exact value
$C=15^8/(2\,16^{16})$ at $m=32,h=1$ supplied the intended discriminating witness.
No production theorem or source arithmetic was altered to make that fixture pass.

The independent hostile worker checked every analytic constant and reconstructed
the adjacent and disjoint coefficient vectors independently. Both workers share
a model family; this is not external peer review. The principal is responsible
for the combined-tree full gates, final exact-head status, and any pinned Lean
finite declarations. This dossier does not infer those results from focused tests.

## 6. Verdict and sharp next obligation

**Proved:** an integer-branch total-energy coercivity lemma, its exact source
inverse arcs, the uniform authentic block loss $1/29$, and (BC-1).

**Improved:** the leading constant of the selected logarithmic absolute loss,
by a factor $1250/29$ at fixed frequency after an unspecified onset.

**Not improved:** the order $\log N$, the limiting normalized upper bound $1$,
or the open cross-block cancellation/flat-carry energy estimate.

The next proof must extract more than one constant loss from a growing arithmetic
block. A precise next candidate is a source-derived lower bound on the number or
energy of *distinct actual integer branch events*, after minimizing over the
resultant phase direction, together with a signed mechanism strong enough to
make the normalized modulus tend to zero. Merely counting one event per geometric
scale recovers the theorem above. A positive-density event count alone would give
at best a fixed relative loss; it would still need an additional iteration or
signed cross-block theorem to yield normality. This is where the present proof
stops, with all quantifiers visible.

## 7. A source-selected cross-time energy certificate for every finite N

The same branch object also gives a useful **generic all-$N$ inequality** that
can be evaluated exactly on the authentic source. This is separate from the
logarithmic theorem above. It detects the difference between the actual zero
selector and same-forcing changed seeds in finite windows; a lower bound on its
asymptotic energy is not proved.

Let $N\ge3$, let $X_n=16X_{n-1}+r_n$ for $1\le n\le N$, and fix an integer
$h\ne0$. For every circle center $\theta$, define the actual integer lifts

$$
k_n(\theta)=\left\lfloor hX_n-\theta+\frac12\right\rfloor,
\qquad q_n(\theta)=hX_n-\theta-k_n(\theta)\in[-1/2,1/2).
$$

Their integer carry is $C_n(\theta)=k_n(\theta)-16k_{n-1}(\theta)$.
At **$h=1,\theta=1/2$**, this is exactly the literal source carry
$c_n=\lfloor X_n\rfloor-16\lfloor X_{n-1}\rfloor$.
The adjacent integer carry difference is

$$
B_n(\theta)=C_{n+2}(\theta)-C_{n+1}(\theta)
=k_{n+2}(\theta)-17k_{n+1}(\theta)+16k_n(\theta),
\quad1\le n\le N-2.
$$

Put $d_n=h(r_{n+2}-r_{n+1})$. The source recurrence proves the exact
observable-preserving cross-time identity

$$
\boxed{
A_n(\theta):=d_n-B_n(\theta)
=q_{n+2}(\theta)-17q_{n+1}(\theta)+16q_n(\theta).
}
\tag{BC-12}
$$

The coefficient sum $1-17+16=0$ cancels the center inside each lift cell.
The integer carries remain; replacing them by independent packet grades would
not preserve this identity.

Define the exact finite energies

$$
\mathcal E_{N,h}=\min_{\theta\in\mathbb R/\mathbb Z}
\sum_{n=1}^{N-2}|d_n-B_n(\theta)|^2,
$$

$$
\mathcal J_{N,h}=\min_{\theta\in\mathbb R/\mathbb Z}
\sum_{n=1}^{N-2}\bigl(|B_n(\theta)|-|d_n|\bigr)_+^2.
$$

Then, with no small-deficit hypothesis,

$$
\boxed{
N-\left|\sum_{n=1}^Ne(hX_n)\right|
\ge\frac2{289}\mathcal E_{N,h}
\ge\frac2{289}\mathcal J_{N,h}.
}
\tag{BC-13}
$$

**Proof.** For the direction $\theta_*$ of the resultant, the same exact
identity as (BC-5) gives $D=\sum_n[1-\cos(2\pi q_n(\theta_*))]$.
If the resultant is zero, any direction works. The global chord estimate gives
$D\ge8\sum_nq_n^2$; the sharper local coefficient $19$ is not used here.
Weighted Cauchy–Schwarz gives

$$
(16a-17b+c)^2\le34(16a^2+17b^2+c^2).
$$

Sum over the finite interior indices. Each $q_n^2$ appears with total weight
at most $16+17+1=34$, including all endpoint costs. Hence

$$\sum_{n=1}^{N-2}|A_n|^2\le1156\sum_{n=1}^Nq_n^2.$$

Since $8/1156=2/289$, taking the minimum over centers proves the first
inequality. The reverse triangle inequality proves the second pointwise before
minimization. QED. All forcing and state values in this lemma may be real;
exact rational computation below is an additional finite implementation fact.

### Why the center minimum is necessary

The literal-carry choice $\theta=1/2$ gives one genuine source energy, but its
value alone cannot replace $\mathcal E_{N,h}$ in (BC-13): the modulus chooses its
own resultant direction. Freezing a convenient center would be an unproved
selection step. The oracle computes the minimum over **every** possible lift
pattern, so no such assumption is inserted.

For rational $X_n$, all breakpoints

$$\beta_n=\{hX_n+1/2\}$$

are rational. Each $k_n(\theta)$ is constant between consecutive breakpoints;
therefore every $A_n$, $B_n$ and energy is constant there. At a breakpoint the
chosen half-open lift realizes the preceding interval's pattern. If several
states share a breakpoint, **all their lift jumps must be processed together**;
processing them separately would invent unattainable branch configurations.
A full turn changes every $k_n$ by $-1$ and leaves $B_n$ unchanged. Thus finitely
many cyclic cells, at most $N$, exhaust all centers and give an exact minimum.

A jump of $k_j$ changes only three neighboring $A_n$. After sorting the rational
breakpoints, the grouped sweep uses $O(N)$ exact arithmetic updates. This is a
count of arithmetic operations, not a claim of constant-time operations on
unbounded integers.

### Exact source and changed-seed observations

The standalone independent instrument
[`oily_branch_energy_oracle.py`](oily_branch_energy_oracle.py) reconstructs the
four-pole recurrence literally with rational arithmetic and compares its sweep
against a direct cell-by-cell implementation. It uses **no complex exponential
or π-value oracle**. Its deterministic
[receipt](OILY_BRANCH_ENERGY_RECEIPT.json) contains 16 exact certificates for
$N=16,32,64,128$, $h=1,-3$, and both the authentic zero seed and the rational
terminal-zero changed seed. The displayed decimals below are rounded versions
of exact rational **lower bounds for $D/N$**, not estimates of $D/N$ itself.

| $N$ | Authentic $U_0=0$, $h=1$ | Same forcing, terminal-zero seed, $h=1$ |
| ---: | ---: | ---: |
| 16 | 0.12082338 | 0.00000353 |
| 32 | 0.14670014 | 0.00000177 |
| 64 | 0.21586729 | 0.00000088 |
| 128 | 0.24142197 | 0.00000044 |

For example, the exact rational certificate at $N=128,h=1$ proves a finite
modulus upper bound below $0.759N$. This is substantially stronger in that
window than the asymptotic logarithmic theorem's uncomputed-onset guarantee.
It supplies **no theorem that the displayed energy grows linearly for all N**.
The changed seed depends on the terminal window; its quantifier remains
$\forall N\ \exists v_N$, not one fixed rational control for all N.

Verification performed by the instrument includes direct every-cell holdouts
$(N,h)=(7,-2),(13,5),(19,-3),(29,7),(31,16)$; all coincident breakpoints on
an identically zero orbit; an alternating $0,1/2$ positive control with exact
energy $289(N-2)/4$; same-forcing terminal-zero controls at $N=11,23,47$;
full-circle energy return; and rejection of a deliberately altered state.
The positive and null controls use explicitly different forcings and are never
relabeled authentic BBP sources.

All 128 independently reconstructed states and forcing values were also compared
with the native `original_state`/`authentic_r` adapters and agreed exactly.
A separate verification using `oily_signed_certificate.signed_sum_enclosure`
with `bits=40, order=14` checked all 16 receipt cases: its rational upper
enclosure of $|S|^2$ was below $(N-(2/289)\mathcal E_{N,h})^2$ in every case.
This is a different finite verification route; the universal bound rests on
the proof above.

Both `--write` and `--verify` completed successfully. The standalone oracle and
receipt were added after the production/test freeze; they do not alter the
production modules or the full-suite test tree. Their separate execution is
reported explicitly.

**Authority and remaining hole.** (BC-12)--(BC-13) are elementary paper-proved
finite inequalities, the source certificates are exact finite computations,
and the authentic asymptotic growth of $\mathcal E_{N,h}$ remains **OPEN**.
Even a positive-density energy lower bound would ordinarily yield only a fixed
relative modulus loss. A proof of normality still needs a stronger accumulation
mechanism or a signed cross-block estimate. This object is a genuine
carry-sensitive cross-time bridge and a discriminating finite probe; it does
not settle that missing arithmetic law.

### Sharp limitation of this energy instrument

The independent hostile audit proves the universal ceiling

$$
\boxed{\mathcal E_{N,h}\le\frac{289}{4}(N-2).}
$$

It follows by averaging over the center before taking its minimum; an alternating
$0,1/2$ phase sequence attains equality. See
[the complete proof and independent cell-integration checks](OILY_HOSTILE_AUDIT.md#6-carry-energy-certificate-boundary-audit-and-a-sharp-universal-ceiling).
The alternating control uses a different forcing and establishes sharpness of
the generic instrument, not a claim about authentic BBP asymptotics.

Consequently the modulus upper certificate produced by (BC-13) always satisfies

$$
N-\frac2{289}\mathcal E_{N,h}\ge\frac{N+2}{2}.
$$

Thus **this instrument alone cannot certify a modulus below $(N+2)/2$**, even
on an alternating sequence whose actual sum is zero when $N$ is even. This is a
sharp limitation of the particular bound, not a lower bound on the actual
modulus. Proving arbitrarily strong growth of its existing energy cannot close
normality; another signed estimate or a stronger instrument is necessary.
