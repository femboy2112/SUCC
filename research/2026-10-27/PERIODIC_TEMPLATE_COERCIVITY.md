# Simultaneous coercivity against every periodic phase template

**PAPER-PROVED with classical arithmetic input; EXACT FINITE instruments.**
The zero-selected BBP theorem now controls every periodic unit template
simultaneously, equivalently the sum of the absolute Fourier sums in all
residue classes. The loss constant remains $1/14$, independent of the period.
The onset is not numerically computed. The asymptotic loss remains logarithmic
and does not prove normality.

Provenance: PR #317, parent
`848bad224fef455a9f87ed19e947c936d309c965`, supplies the
[quiet-transition coercivity theorem](GLOBAL_BRANCH_COERCIVITY.md). The new
step is to compare actual integer branches within each congruence class,
prove that extreme weighted coherence forces a periodic integer branch word,
and eliminate arbitrary template phases from its exact rational inverse.
The selected denominator is $|h|(16^p-1)16^m$, not $15|h|16^m$ when $p>1$.
Academic priority is unverified.

## 1. The simultaneous signed theorem

Retain the original source and its zero initial state:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

For integers $N,p\ge1$ and $h\ne0$, define

$$
\mathcal R_{N,p}(h)
=\sum_{a=0}^{p-1}\left|\sum_{\substack{1\le n\le N\\n\equiv a\pmod p}}
e(hU_n)\right|.
$$

There is one integer $J\ge4$, independent of $N,p,h$, such that

$$
\boxed{
\mathcal R_{N,p}(h)\le N-\frac1{14}K(N,p,h;J),
}
\tag{PT-1}
$$

where

$$
K(N,p,h;J)=\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J,4+\lceil\log_8p\rceil,
1+\lceil\log_{64}|h|\rceil\right)\right).
\tag{PT-2}
$$

Equivalently, (PT-1) bounds

$$
\sup_{\substack{|w_n|=1\\w_{n+p}=w_n}}
\left|\sum_{n=1}^N w_ne(hU_n)\right|.
\tag{PT-3}
$$

The equality follows by choosing one unit coefficient to align each nonzero
residue-class sum; for an empty or zero class choose any unit coefficient.
Thus the theorem is simultaneous over uncountably many templates and does
not assume a finite net or charge a template entropy. It also bounds every
rational linear twist $w_n=e(kn/p)$, and even their optimizing periodic
combination. Such a supremum is stronger than a bound on the single
untwisted sum; a concrete control appears in Section 6.

For fixed $p,h$, (PT-1) is
$\mathcal R_{N,p}(h)\le N-(\log_8N)/14+O_{p,h}(1)$.
It is not a new order of cancellation. Periods can vary with $N$ under the
explicit count (PT-2), but no vanishing normalized modulus is asserted.

## 2. Generic finite periodic-branch lemma

Let real states obey $X_{t+1}=16X_t+r_{t+1}$ for $0\le t<T$, where $T\ge2$.
Fix an integer $p\ge1$, a nonzero integer $h$, and any complex unit sequence
$w_t$ of period $p$. Choose real phases $\theta_t$ with
$w_t=e(-\theta_t)$ and **exactly** $\theta_{t+p}=\theta_t$; choosing one real
representative for each of the $p$ values makes this legitimate.
Set

$$
D=(T+1)-\left|\sum_{t=0}^T w_te(hX_t)\right|,
\qquad R=|h|(\max_jr_j-\min_jr_j),
\qquad L=\lfloor T/p\rfloor.
$$

Suppose $L\ge2$, $0\le R<1$, and some $u\ge0$ satisfies

$$u^2L\ge2,\qquad
\frac{19(1-R)^2}{257(1+u)^2}>\frac1{14}.\tag{PT-4}$$

If $D\le1/14$, the actual integer lift branches defined below are
$p$-periodic. For some integer $a$, writing $B=16^p$, one has

$$
\boxed{
\left|X_0+\sum_{j=1}^T16^{-j}r_j-\frac a{|h|(B-1)}\right|
\le\frac{B/5+|h||R_p|}{|h|(B-1)16^T},
\quad
R_p=\sum_{j=1}^p16^{p-j}r_{T-p+j}.
}
\tag{PT-5}
$$

This generic finite theorem does not restrict the frequency size separately.
In particular, zero forcing allows arbitrary nonzero $h$. The authentic
forcing band in Section 4 is an additional sufficient hypothesis, not an
implicit restriction on this generic statement.

### Proof: one quiet transition per congruence class

Under $D\le1/14$ the weighted resultant is nonzero. Let $e(\psi)$ be its
direction and choose centered lifts

$$y_t=hX_t+\ell_t=\theta_t+\psi+q_t,
\qquad \ell_t\in\mathbb Z,\quad q_t\in[-1/2,1/2].$$

Exactly as in the inherited quiet-transition theorem,

$$
D=\sum_t[1-\cos(2\pi q_t)],\qquad
Q:=\sum_tq_t^2\le1/112,\qquad D\ge19Q.
\tag{PT-6}
$$

The first upper bound follows from the global chord estimate $D\ge8Q$ and
is used to justify the local cosine coefficient $19$. Combining that
coefficient with $D\le1/14$ strengthens the bound to $Q\le1/266$.
The rational Machin/Taylor certificate for the local coefficient is retained
unchanged in [the parent proof](GLOBAL_BRANCH_COERCIVITY.md#2-a-finite-whole-block-lemma).

Define the integer branches

$$
k_t=y_{t+1}-16y_t-hr_{t+1}=\ell_{t+1}-16\ell_t\in\mathbb Z,
\qquad a_t=q_{t+1}-16q_t.
$$

Their expanded formula is

$$
k_t=\theta_{t+1}-16\theta_t-15\psi+a_t-hr_{t+1}.
\tag{PT-7}
$$

For indices $s,t$ congruent modulo $p$, the template and resultant-center
terms cancel **exactly**. If their branches differ, then

$$1-R\le|a_t-a_s|.\tag{PT-8}$$

Each class among the $T$ transition indices contains at least $L$ indices.
Within a class $A$, the sum of pair energies is bounded by

$$\sum_{t\in A}(q_t^2+q_{t+1}^2)\le2Q.$$

Choose $s\in A$ with pair energy at most $2Q/|A|\le2Q/L$.
The norm of the two-term coefficient vector $(-16,1)$ is $\sqrt{257}$,
so $|a_s|\le\sqrt{257Q}\sqrt{2/L}$, while
$|a_t|\le\sqrt{257Q}$ for every transition. If any branch differs from
this class's quiet branch, (PT-8) gives

$$
1-R\le\sqrt{257Q}(1+u),
\qquad
D\ge\frac{19(1-R)^2}{257(1+u)^2}>1/14,
$$

a contradiction. Hence $k_t$ is constant in each congruence class. The
finite word is $p$-periodic wherever both indices occur. This proof never
assumes that the chosen quiet transitions have equal residues or that $p$
divides $T$.

## 3. The rational periodic inverse and its endpoints

Extend the period $p$ branch pattern $k_0,\ldots,k_{p-1}$ periodically.
The unique periodic solution of
$f_{t+1}=16f_t+k_t$ starts at

$$
f_0=-\frac{\sum_{j=0}^{p-1}16^{p-1-j}k_j}{16^p-1}.
\tag{PT-9}
$$

Therefore $(B-1)f_t\in\mathbb Z$ for every $t$, and $f_{t+p}=f_t$.
No unknown template phase or resultant center enters this rational carrier.
Let $z_t=y_t-f_t$. Then

$$z_{t+1}=16z_t+hr_{t+1},\qquad
z_0+h\sum_{j=1}^T16^{-j}r_j=16^{-T}z_T.$$

Because both $f$ and $\theta$ have period $p$,

$$z_T-z_{T-p}=q_T-q_{T-p}.$$

The last $p$ transitions, without discarding their forcing, give

$$
z_T=Bz_{T-p}+hR_p,
\qquad
\boxed{(B-1)z_T=B(q_T-q_{T-p})-hR_p.}
\tag{PT-10}
$$

This holds also when $T$ is not divisible by $p$. Since
$|q_t|\le1/\sqrt{112}<1/10$, it implies

$$|z_T|\le\frac{B/5+|h||R_p|}{B-1}.$$

Use $z_0=hX_0+\ell_0-f_0$ in the backward telescope and divide by $h$.
The denominator of $(f_0-\ell_0)/h$ divides $|h|(B-1)$; this proves
(PT-5). The sign of $h$ is absorbed in the integer numerator. QED.

The fact that (PT-5) no longer mentions the template is precisely why one
inverse-arc exclusion controls **all** periodic unit templates. Conversely,
membership in those arcs does not prove coherence with any template.

## 4. Authentic forcing, exact zero selection, and uniform arithmetic

The inherited four-pole proof gives positive decreasing $r$, together with

$$
0<r(n+1)<\frac{15}{64n^2},\quad
0<T_n<\frac1{64n^2},\quad
U_n+T_n=16^{n-1}\pi.
\tag{PT-11}
$$

Take $m\ge4096p$, $1\le|h|\le m^2/64$, and the block
$X_t=U_{m+1+t}$ for $0\le t\le T=7m-1$. Its range satisfies
$R<15/4096$, and every transition class has at least
$\lfloor(7m-1)/p\rfloor\ge20000$ members. Choose $u=1/100$.
The exact margin is

$$
\frac{19}{257}\left(\frac{4081}{4096}\right)^2
\left(\frac{100}{101}\right)^2-\frac1{14}
=\frac{9907077909}{19243046273024}>0.
$$

Thus weighted loss at most $1/14$ would give (PT-5). Monotonicity bounds
its final period forcing by

$$0<R_p\le\frac{B-1}{15}r(8m-p+1).$$

Since $B/(5(B-1))\le16/75$, the exact zero-selected Green cancellation

$$
U_{m+1}+\sum_{j=1}^T16^{-j}r(m+1+j)
=16^{-T}U_{8m}=16^m\pi-16^{-T}T_{8m}
$$

yields an integer numerator $a$ and denominator
$q=|h|(16^p-1)16^m$ such that

$$
\left|\pi-\frac aq\right|
\le16^{-8m}16\left[
\frac{16}{75|h|}+\frac1{64(8m-p)^2}+\frac1{64(8m)^2}\right]
<4\,16^{-8m}.
\tag{PT-12}
$$

The last comparison holds already for $m\ge p\ge1$, since $8m-p\ge7m$.
The authentic partial-sum conductor has been eliminated by an exact lifted
identity, not ignored in a rational-approximation estimate.

The corrected [Zeilberger--Zudilin primary paper](https://arxiv.org/abs/1912.06345v2)
proves $\mu(\pi)\le7.103205334137\ldots<15/2$. Thus a rational
$C\in(0,1]$ exists such that $|\pi-a/q|\ge Cq^{-15/2}$ for every integer
$a$ and positive integer $q$, including unreduced fractions. The finite
exceptional denominators are absorbed using irrationality. We do not compute
$C$ and use no exponent-two claim for $\pi$.

The inverse approximation (PT-12) is impossible if

$$
C^2 16^m>16\bigl(|h|(16^p-1)\bigr)^{15}.
\tag{PT-13}
$$

A sufficient condition is $C^2 16^{m-15p}>16|h|^{15}$.
Because $p\le m/4096$ gives $m-15p\ge m/2$, and $|h|\le m^2/64\le m^2$,
one universal $m_{\ast}\ge4096$ suffices for every allowed $p,h$ and every
$m\ge m_{\ast}$. For example choose it to satisfy

$$C^4 16^{m_{\ast}}>256m_{\ast}^{60}.$$

This condition persists for larger $m$: $16^m/m^{60}$ increases for
$m\ge64$, since $(m/(m+1))^{60}\ge1-60/(m+1)>1/16$ there.
The threshold exists by exponential domination, but it is not numerical
proof authority until a valid value of $C$ is supplied.

We have proved the simultaneous authentic block inequality

$$
\boxed{
\sup_{\substack{|w_n|=1\\w_{n+p}=w_n}}
\left|\sum_{n=m+1}^{8m}w_ne(hU_n)\right|<7m-\frac1{14}
}
\tag{PT-14}
$$

for $m\ge m_{\ast}$, $m\ge4096p$, and $1\le|h|\le m^2/64$.
Choose $J=\lceil\log_8m_{\ast}\rceil$. The eligible complete blocks
$(8^j,8^{j+1}]$ are counted exactly by (PT-2). For any one global template,
apply (PT-14) on each eligible block and the trivial bound elsewhere, then
take the supremum. The local residue alignment can differ by $m+1$ between
blocks; exact periodicity is preserved under each shift. This proves (PT-1).

## 5. Completed-orbit corollary for large frequencies

The generic lemma has a useful second application that must not import the
authentic forcing band unnecessarily. Let $Y_n=16^{n-1}\pi$, so
$Y_{n+1}=16Y_n$. For any integers $p\ge1$, $g\ne0$, the period $p$ template
block theorem holds for $Y$ whenever

$$
m\ge m_{**},\qquad m\ge4096p,\qquad
m\ge60\lceil\log_{16}|g|\rceil,
\tag{PT-15}
$$

where one universal $m_{**}$ exists independently of $g,p$.
When $|g|=1$, the last condition is vacuous. Indeed, use the generic lemma
with zero forcing; its branch range is zero regardless of $g$. The inverse
gives denominator $|g|(16^p-1)16^m$ and error less than $4\,16^{-8m}$
without a Green tail. Now

$$15p\le15m/4096,\qquad15\log_{16}|g|\le m/4,$$

so $m-15p-15\log_{16}|g|>m/2$. The sufficient arithmetic comparison
follows from $C^2 16^{m/2}>16$, which holds after one universal onset.

This is a theorem about the completed orbit. Transport back to a different
observable must explicitly pay its Green error. In particular a naked
large-frequency comparison to $U_n$ may cost $|g|\sum T_n$ and be useless.
The parent synthesis applies the corollary to mixed-lag observables only
after deriving a separate order-independent tail bound; that transport is
not silently assumed here.

## 6. Hostile controls and limits

**Ordinary cancellation does not bound the periodic-template supremum.**
Take the exact unforced orbit $X_n=16^n/9$. Its period-three phases have
residues $7,4,1$ modulo $9$, and

$$e(1/9)+e(4/9)+e(7/9)=0.$$

Yet the period-three template $w_n=e(-16^n/9)$ gives $w_ne(X_n)=1$
at every time. Exact cyclotomic tests verify both assertions. Consequently
the new signed observable is not controlled by the previous untwisted
modulus estimate on a generic orbit.

**The same forcing preserves this control.** The changed seed
$V_0=1/9-\pi/16$ gives $V_n=16^n/9-T_n$. Its untwisted average tends to
zero by periodic cancellation and the summable Green error. The same
period-three template makes the weighted average tend to one. Its weighted
absolute loss stays bounded, so a version of (PT-1) for arbitrary same-forcing
seeds is false. The zero-selected identity in (PT-11) is the failed
assumption; the forcing and its full signs are unchanged. This control has
a changed irrational initial value and is not claimed to preserve the
original rational finite-state conductors.

**Finite generic inverse controls.** For zero forcing and $X_0=1/255$,
the period-two orbit lies in a necessary inverse arc and admits an exactly
matching period-two template. The boundary excursion $X_0=1/16$ lies
outside the certified period-two arcs on the tested long window, forcing
loss greater than $1/14$ for every such template. This is consistent with
the inherited boundary ceiling; no optimal generic threshold is claimed.

**No new asymptotic order follows.** Sparse finite-type changed selectors
remain compatible with logarithmic losses after matching their periodic
part. Extending the tested class of templates does not manufacture a
superlogarithmic event count or relative cancellation. The theorem extracts
one bounded loss from each eligible geometric block, uniformly over a much
larger signed class. The exact missing input is a growing total loss or a
signed inter-block estimate for the zero-selected path.

## 7. Exact instruments, checks, and authority

[`periodic_template_coercivity.py`](../../observational_succ/periodic_template_coercivity.py)
separates the generic finite lemma from the authentic forcing adapter.
It computes the exact rational periodic solution, preserves the ordered
terminal $p$-step forcing, checks integer lift compatibility, and records
the all $N$ count without certifying a supplied numerical onset. Generic
initial values and templates never receive an authentic source passport.

The command
`python -m unittest tests.test_periodic_template_coercivity -v` passed
**13 tests** in 3.789 seconds. Independent holdouts cover nondividing
terminal periods, exact residue counts, arbitrary rational template phases,
the integer fixed-point denominator, literal source ranges, the all $N$
schedule, an altered template, a nonperiodic branch, and the cyclotomic
ordinary-versus-weighted control. After that run only the provenance string
was expanded from its short parent hash to the full parent hash; the
principal records final combined-tree replay and required checks.

Authority labels:

- **CLASSICAL:** the published irrationality bound for $\pi$, Machin's
  identity, and the elementary circle/Taylor inequalities.
- **PAPER-PROVED:** the generic periodic-branch inverse, the simultaneous
  authentic theorem (PT-1), and the completed-orbit corollary (PT-15).
- **EXACT FINITE:** rational lift, carrier, endpoint, margin, and scheduling
  certificates; no floating Fourier observation serves as proof authority.
- **CONDITIONAL:** any numerical onset passed to the executable budget.
- **REFUTED:** extending the selected theorem to arbitrary same-forcing
  seeds; omitting the factor $16^p-1$; inferring the periodic-template bound
  merely from untwisted cancellation.
- **OPEN:** superlogarithmic selected loss, fixed-mode relative cancellation,
  spectral purity, and base-16 normality of $\pi$.

Any Lean authority is scoped to the separately exported finite declarations
in the principal's validation receipt. This dossier does not claim a kernel
proof of the irrationality input, template supremum, or infinite theorem.
