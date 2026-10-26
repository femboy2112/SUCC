# Finite-frequency cancellation with maximal conditional branch energy

**Authority:** PAPER-PROVED obstruction and EXACT FINITE interval/cyclotomic
certificates. One strengthening imports a CLASSICAL irrationality-exponent
theorem. No infinite assertion below is Lean-checked. Academic priority is
unverified. **The original zero-initial BBP cancellation problem remains OPEN.**

For every finite frequency cutoff $H\ge1$, there is one fixed real initial
state with the **entire original BBP forcing**, such that:

1. Every selected mode $0<|h|\le H$ tends to zero, at rate
   $O_H(\log(N+1)/N)$.
2. Every conditional inverse-branch mode energy tends to **one**, and the
   conditional chi-squared defect tends to **15**, uniformly over every
   bin count $M\ge q$ for one fixed $q\le9H$.
3. The selected endpoint has irrationality exponent two and obeys the
   same $1/29$ logarithmic **absolute-loss** bound as the PR #311 proof,
   after an unspecified onset, at every fixed nonzero frequency.
4. A higher fixed frequency has a nonzero limiting mean. The orbit is
   nonnormal. Its initial state is explicitly nonzero.

This is an actual temporal/source-compatible family, not a synthetic
contingency table. It sharpens the missing gate: per-mode conditional energy
decay is strictly stronger than that mode's signed cancellation, even after
retaining the forcing, finite Diophantine type, and the established logarithmic
absolute loss. The original zero selector is the property this family fails.

## 1. Provenance and what is new in this interface

The definitions of selected digits, tail bins and conditional energies are
those of [PR #312's source dossier](LAMBDA_INSIDE_OUT_SOURCE_DUALITY.md).
The original forcing and Green engine are imported unchanged. We inspected
[PR #311's direct arithmetic proof](https://github.com/femboy2112/SUCC/blob/a34c4484059e667202b97d5ab4102560987b1406/research/2026-10-26/OILY_DIRECT_ARITHMETIC.md)
and its hostile audit at exact donor SHA
`a34c4484059e667202b97d5ab4102560987b1406`; no donor code is imported or merged.

The donor already establishes the coefficient $1/29$, the constant-total-loss
inverse lemma, the $O(\log N)$ order limitation from a sparse selector, and the
sharp ceiling of its carry-energy certificate. None of these is claimed as a
new authentic-source bound here. The additions are simultaneous cancellation
on **any prescribed finite frequency band**, maximal conditional energies
**uniformly over all fine partitions**, exact same-forcing temporal controls,
and their combination with the donor-level all-mode absolute-loss property.

## 2. Full forcing, selected endpoint, and quantitative Green budget

Keep all four original signed poles and indices:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j).
$$

The established source identity and bounds are

$$
16T_n-T_{n+1}=r(n+1),\qquad T_0=\pi/16,\qquad
0<T_n<\frac1{64n^2}\quad(n\ge1).
\tag{SA-1}
$$

For every real endpoint $\alpha$, define

$$
V_0=\alpha-\pi/16,\qquad V_n=16^n\alpha-T_n.
\tag{SA-2}
$$

Then $V_{n+1}=16V_n+r(n+1)$ at every time. Thus the forcing, its moment
geometry, its moving-frequency forcing bands and its forcing-conductor clock
are exactly unchanged. The states and their denominators are not unchanged:
these real controls are not assigned the original rational-state passport.

Since $\sum_{n\ge1}n^{-2}<2$,

$$
\sum_{n\ge1}T_n<\frac1{32},\qquad
\left|\sum_{n=1}^Ne(hV_n)-\sum_{n=1}^Ne(h16^n\alpha)\right|
<\frac{11|h|}{56}.
\tag{SA-3}
$$

Here $|e(x)-e(y)|\le2\pi|x-y|$ and $\pi<22/7$. All later transport errors
are normalized by $N$. No infinite future is silently dropped.

## 3. Periodic rational endpoints cancel an arbitrary finite band

Fix $k\ge2$, $q=3^k$, $L=3^{k-1}$, and $1\le p<q$ with $3\nmid p$.
Set $\alpha=p/q$ and $a_n\equiv16^np\pmod q$, $0<a_n<q$.

**Lemma SA-3A.** The multiplicative order of 16 modulo $q$ is $L$, and
one orbit period contains exactly the residues congruent to $p$ modulo 3.

**Proof.** $16=1+5\cdot3$. If $u$ is not divisible by 3 and $r\ge1$,
the binomial expansion shows

$$
(1+3^ru)^3=1+3^{r+1}u',\qquad u'\equiv u\pmod3.
$$

Inductively $v_3(16^{3^s}-1)=s+1$. Therefore the order is exactly
$3^{k-1}$. All its distinct powers are 1 modulo 3, and that residue class
has exactly $3^{k-1}$ units modulo $q$. Multiplication by $p$ gives the
asserted coset. QED.

The exact evaluated character mean over a complete period is consequently

$$
\frac1L\sum_{n=1}^{L}e(ha_n/q)
=\begin{cases}
0,&L\nmid h,\\
e(hp/q),&L\mid h.
\end{cases}
\tag{SA-4}
$$

This follows by summing the character on the additive coset
$p+3\mathbb Z/q\mathbb Z$. It is an evaluated cyclotomic identity, not an
equality asserted in the free group algebra.

Put $r_N=N\bmod L$ and write $A_N^V(h)=N^{-1}\sum_{n=1}^Ne(hV_n)$.
For every $N\ge1$,

$$
\begin{aligned}
|A_N^V(h)|&\le\frac{\min(r_N,L-r_N)+11|h|/56}{N},&&L\nmid h,\\
|A_N^V(h)-e(hp/q)|&\le\frac{11|h|}{56N},&&L\mid h.
\end{aligned}\tag{SA-5}
$$

For the first inequality, every complete period sums to zero, and the
incomplete period is bounded both by its own length and the complementary
length. The second uses a character constant on the periodic coset. Then
apply (SA-3). In particular, choosing $L>H$ cancels every $0<|h|\le H$,
while mode $h=L$ tends to $e(p/3)\ne0$.

The fixed initial value $p/q-\pi/16$ is nonzero because π is irrational.
This periodic family fails a logarithmic-loss theorem at the surviving
frequency $L$, where its absolute loss is only bounded. Section 5 repairs
that extra diagnostic with an irrational sparse perturbation.

## 4. Conditional energies are maximal uniformly in every fine partition

For the real trajectory (SA-2), use exactly the source-duality observation

$$
x_n=\{V_n\},\quad j_n=\lfloor16x_n\rfloor,\quad t_n=\{16x_n\},\quad
b_n=\lfloor Mt_n\rfloor.
$$

Let $n_{bj}$, $n_b$, $E_{N,M}(h)$ and $\Delta_{N,M}$ be the corresponding
empirical counts and energies from PR #312. In this section they belong to
the changed-selector control, never to the original zero-initial orbit.
Let

$$
n_0=\min\{n\ge1:4n^2\ge q\},\qquad B=n_0-1.
$$

**Theorem SA-4A.** For every $N\ge1$, every integer $M\ge q$, and every
integer $h$,

$$
1-\frac{4B}{N}\le E_{N,M}(h)\le1,\qquad
15-\frac{32B}{N}\le\Delta_{N,M}\le15.
\tag{SA-6}
$$

Negative lower bounds can of course be replaced by zero. The conclusion
is uniform even if $M$ grows faster than any function of $N$.

**Proof of deterministic late branches.** For $n\ge n_0$, (SA-1) gives
$16T_n<1/q$. Since $q$ is odd, the fractional part of $16a_n/q$ is
$a_{n+1}/q$, at distance at least $1/q$ from either integer endpoint.
Consequently

$$
j_n=\lfloor16a_n/q\rfloor,\qquad
t_n=a_{n+1}/q-16T_n
\in\left(\frac{a_{n+1}-1}{q},\frac{a_{n+1}}q\right).
\tag{SA-7}
$$

Different backbone numerators in the coset differ by at least **three**,
so their open tail intervals are separated by more than $2/q$. A bin
of width at most $1/q$ cannot contain points from two such intervals.
Also $a_{n+1}$ uniquely determines $a_n$ modulo $q$. Every bin's late
observations therefore select one digit. No independence or random
branch sampling is involved. QED.

**A contamination bound used here and below.** Suppose at most $B'$ of
the $N$ observations are exceptional, and every bin's other observations
have one digit $j_b$. Write $\beta_b$ for the exceptional fraction of a
nonempty bin. Its conditional character $F_b(h)$ is within $2\beta_b$
of the unit character $\zeta_{16}^{hj_b}$, so

$$
|F_b(h)|^2\ge1-4\beta_b.
$$

For $\beta_b\le1/2$ this follows from $(1-2\beta_b)^2\ge1-4\beta_b$;
for larger $\beta_b$ the right side is nonpositive. Similarly, since
the dominant digit has mass at least $1-\beta_b$,

$$
16\sum_jp_{bj}^2-1\ge16(1-\beta_b)^2-1\ge15-32\beta_b.
$$

Average with weights $n_b/N$; their exceptional mass is at most $B'/N$.
This proves (SA-6) using $B'\le B$, including empty bins and $N<n_0$.

Thus even the actual temporal cancellation of one selected mode does not
imply its conditional energy decays. For every frequency below $L$, (SA-5)
gives cancellation while (SA-6) gives maximal conditional energy.

## 5. Add finite irrationality type without losing the obstruction

Define the fixed sparse number and its shifted tails

$$
\xi=\sum_{k\ge0}16^{-2^k},\qquad
s_n=\{16^n\xi\}=\sum_{2^k>n}16^{n-2^k}.
$$

The digits are 1 at powers of two and zero elsewhere, so the displayed
tail is indeed in $[0,1)$ and no carry normalization is needed.

**Classical input, checked at the primary publication.** This number is
transcendental with irrationality exponent two. The result for every
integer base is stated in
[Hone and Varona, section 4, equation (4.2)](https://doi.org/10.1007/s00605-018-1244-1),
which cites Bugeaud, Han, Wen and Yao, *Hankel determinants, Padé
approximations, and irrationality exponents*, IMRN 2016, 1467–1496.
The exponent statement is imported, not inferred from sparse finite prefixes.

Now set

$$
\alpha=\frac1q+\xi,\qquad W_n=16^n\alpha-T_n.
\tag{SA-8}
$$

There is one fixed initial state for each fixed $q$. It is strictly
negative, since

$$
\alpha<\frac19+\frac1{15}=\frac8{45}<\frac3{16}<\frac\pi{16}.
$$

This proves failure of the zero anchor without assuming an unproved
algebraic independence between π and $\xi$. The same full BBP recurrence
holds at every time.

### 5.1 An all-N sparse-tail sum, with the unrestricted future paid

By summing nonnegative terms in the other order,

$$
\boxed{
\sum_{n=1}^{N}s_n\le
\frac{1+\lfloor\log_2(N+1)\rfloor}{15}+\frac1{225}
=:S_*(N).
}\tag{SA-9}
$$

For each power of two at most $N+1$, its inner geometric sum is at most
$1/15$. For each later power $a$, that sum is at most
$16^{N+1-a}/15$. Its positive gaps $a-(N+1)$ are distinct, so the total
is bounded by $(1/15)\sum_{d\ge1}16^{-d}=1/225$.
This includes every future sparse digit.

Let

$$
C_*(N,h)=\frac{44|h|}{7}\left(S_*(N)+\frac1{32}\right).
$$

Combining (SA-9), the Green sum and the periodic character gives, for all
$N\ge1$,

$$
\begin{aligned}
|A_N^W(h)|&\le\frac{\min(r_N,L-r_N)+C_*(N,h)}N,&&L\nmid h,\\
|A_N^W(h)-e(h/q)|&\le\frac{C_*(N,h)}N,&&L\mid h.
\end{aligned}\tag{SA-10}
$$

In particular $A_N^W(h)\to0$ on any prescribed band $0<|h|\le H<L$,
but $A_N^W(L)\to e(1/3)\ne0$.

### 5.2 Uniform conditional-energy obstruction, including all fine schedules

Define the explicit integer constants

$$
\ell=\min\{a\ge0:16^a\ge32q\},\qquad
n_1=\min\{n\ge1:2n^2\ge q\},
$$

and the integer upper bound

$$
B_N=\min\left(N,\ n_1-1+
\ell\bigl(1+\lfloor\log_2(N+\ell)\rfloor\bigr)\right).
\tag{SA-11}
$$

Declare a time good if $n\ge n_1$ and no power of two lies in
$(n,n+\ell]$. This classification is explicit before measuring any
Fourier sum or conditional defect.

If no such sparse position occurs, the geometric bound gives
$s_n\le16^{-\ell}/15\le1/(480q)<1/(32q)$. Also $T_n<1/(32q)$
when $n\ge n_1$. Hence on a good time

$$
|16(s_n-T_n)|<\frac1{2q}.
$$

Writing the periodic residue as before, this perturbation preserves the
selected digit of $a_n/q$, and puts its tail in

$$
\left(\frac{a_{n+1}-1/2}{q},\frac{a_{n+1}+1/2}{q}\right).
$$

Every endpoint residue is at least $1/q$ from 0 and 1, so no wraparound
was omitted. Distinct residues are $3/q$ apart; the open tail groups
are more than $2/q$ apart. Every bin with $M\ge q$ thus has at most one
good selected digit.

For each sparse position at most $N+\ell$, there are at most $\ell$
preceding indices to exclude. There are
$1+\lfloor\log_2(N+\ell)\rfloor$ such powers. Together with the first
$n_1-1$ indices, this proves the count (SA-11), with overlaps only
decreasing the count. Applying the contamination lemma proves

$$
\boxed{
1-\frac{4B_N}{N}\le E^W_{N,M}(h)\le1,\qquad
15-\frac{32B_N}{N}\le\Delta^W_{N,M}\le15
\quad(M\ge q).
}\tag{SA-12}
$$

For fixed $q$, $B_N=O_q(\log(N+1))$. Thus the maximal-energy limits hold
uniformly over **all** bin counts $M\ge q$, including arbitrary
horizon-dependent choices. This is not a fixed-bin limit followed by an
unjustified exchange with a growing partition.

There is also a conditional entropy obstruction. Choose in each bin its
good digit as decoder, and choose any digit in bins having no good
observations. Its empirical error probability is at most
$\beta_N=B_N/N$. For $\beta_N\le15/16$, the elementary error-indicator
entropy decomposition gives

$$
H(j\mid b)\le h_2(\beta_N)+\beta_N\log15\longrightarrow0,
$$

where $h_2(u)=-u\log u-(1-u)\log(1-u)$. For the actual decoder error
$e_N\le\beta_N$, the indicator costs at most $h_2(e_N)$ and a wrong
digit has at most 15 choices. The combined expression
$h_2(e)+e\log15$ is increasing on $[0,15/16]$, giving the stated
upper bound. Conditional Haar branch entropy
would instead be $\log16$. This entropy conclusion is paper-level;
the exact code measures integer counts, not floating logarithms.

### 5.3 The sparse controls also satisfy the donor's all-mode logarithmic loss

Irrationality exponent is unchanged by a nonconstant rational affine
transformation: rational approximations transform with denominator bounded
by a fixed multiple, and constants do not change the supremum exponent;
apply the inverse affine map for the reverse inequality. Hence

$$
\mu(16\alpha)=\mu(16/q+16\xi)=2<15/2.
$$

There exists $C_q>0$ such that
$|16\alpha-a/b|\ge C_q b^{-15/2}$ for all integer $a$ and positive
integer $b$, including unreduced fractions. As in the donor, finitely
many small reduced denominators are absorbed into the positive constant.

The donor finite lemma does not require its trajectory to start at zero.
Here is the relevant argument and the exact point where the selector enters.
On $(m,8m]$, suppose absolute modulus loss is at most $1/29$ and
$1\le|h|\le m^2/64$. Center the phases on the resultant direction and
write lifts $\theta+u_t$, $|u_t|\le1/2$. The chord bound gives
$\sum u_t^2\le1/(8\cdot29)$, hence $|u_t|<1/15$; on that interval
$1-\cos(2\pi u_t)\ge19u_t^2$. The source forcing range is less than
$15/4096$. Two different integer branches would force

$$
\sum_tu_t^2\ge\frac{(1-15/4096)^2}{546},\qquad
\frac{19(1-15/4096)^2}{546}>\frac1{29},
$$

because the overlapping branch-difference vector has squared norm
$16^2+17^2+1=546$. This contradicts the assumed loss. All branches
therefore coincide. Backward telescoping and the final transition yield
the necessary rational arc radius

$$
\frac{32/15+|h|r(8m)}{15|h|16^{7m-1}}.
$$

The exact Green identity is now

$$
W_{m+1}+\sum_{j=1}^{7m-1}16^{-j}r(m+1+j)
=16^{-(7m-1)}W_{8m}
=16^m(16\alpha)-16^{-(7m-1)}T_{8m}.
$$

Thus the hypothetical coherence gives an approximation to **$16\alpha$**,
not π, with denominator $15|h|16^m$ and error less than
$3\,16^{-8m}$. The Diophantine bound excludes this whenever
$C_q^2 16^m>9(15|h|)^{15}$. Exponential domination makes that true
uniformly for $1\le|h|\le m^2/64$ beyond one unspecified threshold.
Disjoint geometric blocks give an integer $J_q$ such that

$$
\boxed{
\left|\sum_{n=1}^{N}e(hW_n)\right|
\le N-\frac1{29}\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J_q,1+\lceil\log_{64}|h|\rceil\right)\right)
}\tag{SA-13}
$$

for every $N\ge1$ and every nonzero integer $h$. This reproduces the
donor proof with its actual endpoint variable. The finite cosine bound,
coercivity margin, radius and factor nine were checked against the pinned
donor proof. The classical input and unspecified threshold are explicit;
no Lean authority or numerical value for $C_q,J_q$ is claimed here.

At the surviving frequency $L$, (SA-10) gives absolute loss at most
$O_q(\log N)$ while (SA-13) gives loss at least a positive logarithmic
amount. Thus these controls retain exactly the logarithmic order while
remaining maximally biased at a higher mode. They also cancel every mode
in the chosen finite test band. A new argument must therefore use more
than those tests and the finite-irrationality/coercivity mechanism.

## 6. Quantifiers, source passport, and the strictly narrower requirement

For any fixed $H\ge1$, choose the least power $L=3^{k-1}>H$, with
$k\ge2$, and put $q=3L$. Then $q\le9H$. Choose **one** of the fixed
selectors (SA-8) before taking $N\to\infty$. For every $0<|h|\le H$,
the signed means vanish; for every bin schedule eventually satisfying
$M_N\ge q$, their conditional energies tend to one. The same one
selector has a higher surviving mode and satisfies (SA-13) for all modes.
There is no claim of one selector passing every possible frequency band.

This refutes an implication from selected-mode cancellation to conditional
mode-energy decay, even with true time evolution and the unchanged BBP
forcing. It does not refute the valid sufficient direction in PR #312.
Nor does it refute the theorem for the unique source initialized at zero.
The all-mode normality equivalence from that PR remains intact.

The controls use changed **real** initial states; the original source's
rational state conductors cannot be attached to them. The forcing
conductors and forcing labels remain the original ones. The finite
rational approximants below have their own explicitly changed seeds;
their denominators are not asserted to be odd or original.
The periodic family's initial state is provably irrational. For the
sparse family's initial state, only nonzero negativity is established
here; the rationality of $1/q+\xi-\pi/16$ is not asserted.

For a primitive mode whose means do vanish in this family, the actual
signed cross-bin sum vanishes as bins grow, by the same finite phase
approximation used in PR #312. Its positive conditional energy does not.
The next source-specific gate must retain that signed cross-bin information
or prove a genuine uniformity law special to $U_0=0$; it cannot derive
conditional-energy decay merely from moderate phase cancellation,
summable forcing, finite irrationality type or logarithmic absolute loss.

## 7. Exact instruments, hostile controls, and validation

Artifacts:

- [Native analytic control instruments](../../observational_succ/selected_branch_analytic.py).
- [Independent finite tests](../../tests/test_selected_branch_analytic.py).

`PeriodicGreenSelector` stores the rational backbone $p/q$.
`SparsePeriodicGreenSelector` stores the backbone $1/q$ and the explicit
sparse series. Both label the zero anchor false. The code imports the
existing original forcing and strict rational Green intervals. It does
not import any PR #311 production code and does not evaluate π.

For a finite real control cell, rational upper and lower bounds on the
Green tail and sparse tail certify the circle winding, selected digit
and tail bin. A rational midpoint is then used **only to replay these
already certified cell labels**, not as a replacement orbit. Failure to
separate a boundary within the declared precision fails closed. The finite
branch statistics are therefore exact for the actual real control.

An independent finite witness approximates the selected initial value by
a rational number, then evolves it with the exact original recurrence.
The entire future-state error through $N$ is bounded by $16^N$ times the
sum of the two omitted endpoint tails. For the sparse control those two
errors can have opposite signs; both are paid. These rational seeds are
chosen separately for each finite horizon. Their exact recurrence and
certified branch-table agreement are checks, not a claim of one rational
seed satisfying the infinite sparse-selector theorem.

The 17 focused tests passed. They include:

- direct cyclotomic period sums at conductors 9, 27 and 81, independently
  of the coset formula;
- held-out order/coset checks through conductor $3^8$;
- literal four-pole replay and independent Green prefix/tail brackets;
- all fifteen branch energies exactly one on certified good-time subsets;
- full tables at independent horizons and bin counts, including bins far
  finer than the backbone conductor;
- exact rational changed-seed approximations retaining every forcing step;
- zero-anchor rejection, a changed pole sign, illegal residue classes and
  bounded-precision/type failures.

The all-$N$ results rest on the proofs above, not these finite holdouts.
The classical irrationality-exponent input is separately sourced. Full
combined-suite results, commit SHA, hosted CI and any unrelated finite Lean
declarations belong to the principal's receipt.

| Statement | Authority | Scope |
| --- | --- | --- |
| Exact period/coset and character classification | PAPER-PROVED; EXACT FINITE | Rational periodic backbone, evaluated cyclotomic field. |
| Uniform maximal conditional energies, (SA-6) | PAPER-PROVED; EXACT FINITE tables | Changed real selector; all $M\ge q$. |
| Sparse finite-band cancellation and uniform obstruction, (SA-10)–(SA-12) | PAPER-PROVED; EXACT FINITE intervals | One fixed selector per chosen finite band. |
| $\mu(\xi)=2$ | CLASSICAL published result | Imported; no finite-prefix inference. |
| Logarithmic absolute loss for the sparse family, (SA-13) | PAPER-PROVED with CLASSICAL input | Unspecified onset; not a new bound for π. |
| Cancellation forces conditional energy decay for each tested mode | REFUTED | Even the exact BBP forcing and donor-level loss allow counterexamples. |
| Original zero-selected signed saving beyond logarithmic absolute loss | OPEN | No new asymptotic order for the authentic π orbit is claimed. |
