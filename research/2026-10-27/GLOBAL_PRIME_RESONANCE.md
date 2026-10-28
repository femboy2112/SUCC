# Authentic prime resonance can coexist with vanishing averaged matrix energy

**Authority:** PAPER-PROVED all-prime estimates and limiting obstruction;
EXACT FINITE native instruments, independent rational source replay,
cyclotomic checks, and outward interval holdouts. No Lean authority or
independent academic-priority claim is made. **The full selected BBP Weyl
estimate and base-16 normality of $\pi$ remain OPEN.**

This round descends from PR #316 head
`239df54f`, on its separate child research branch. The result concerns a
genuine prime component of the original arithmetic source, with the full
complement retained. It is not a new source model and not an assertion
that the full BBP orbit is coherent.

## 1. Source and the new claim relative to the existing literature in this repository

Retain exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

The genuine first-prime formulas, complete-period cancellation, and
selected-embedding firewall are inherited from
[BBP_CYCLOTOMIC_BIRTH_AND_LAG.md](../2026-10-24/BBP_CYCLOTOMIC_BIRTH_AND_LAG.md),
[BBP_MINIMAL_PATH_GALOIS_SELECTION.md](../2026-10-24/BBP_MINIMAL_PATH_GALOIS_SELECTION.md),
and [SPECTRAL_PURITY_ARITHMETIC.md](../2026-10-25/SPECTRAL_PURITY_ARITHMETIC.md).
Those files already prove prime-local cancellation on long complete
periods, exhibit a finite authentic Galois outlier, and refute promotion
of local cancellation to full-phase cancellation by complementary-clock
controls. None of those facts is claimed anew here.

The additional theorem is an **infinite authentic-source separation** at
a prescribed growing observation window: primitive Galois averaging
passes a growing-width matrix purity test, whereas the actually selected
prime component has asymptotically maximal reinforcement. On the same
window the fresh prime changes the actual full BBP sum from its full
complementary sum by an explicitly vanishing amount. This isolates a
failure of selected-embedding transfer, not merely a formal identity or
a finite numerical outlier.

## 2. The authenticated prime window

Let $p=8m+1$ be prime and $p\ge257$. Its first forcing index with a
$p$ denominator is

$$n_p=m+1=(p+7)/8.$$

Every denominator at earlier indices is less than $p$. At $n_p$, exactly
the first pole has denominator $p$ and contributes $4/p$; the other
three denominators are $p+3,p+4,p+5$. The next $p$-divisible pole occurs
at $4m+1$, where $8n-4=4p$. Indeed the four denominator residue classes
modulo eight are $1,4,5,6$, and $p\equiv1\pmod8$; the multiples $2p,3p$
cannot occur. Thus no new $p$ input occurs during $n=m+1,\ldots,4m$.

The zero anchor and induction through the full recurrence give the
canonical $p$-primary component and its complete complement:

$$
u_{p,t}=\frac{4\,16^t}{p}\pmod1,\qquad
U_{n_p+t}=u_{p,t}+w_{p,t},\qquad
p\nmid\operatorname{den}(w_{p,t}),\quad 0\le t<3m.
$$

We use the displayed unwrapped rational representative for $u_{p,t}$;
$w_{p,t}=U_{n_p+t}-4\,16^t/p$ retains the entire remaining lift. The
complement satisfies the original forced recurrence within this interval.
It is not erased, independently averaged, or assumed random.

Prescribe the two integer scales

$$
\boxed{K_p=\lfloor\log_{256}p\rfloor,\qquad
H_p=1+\lfloor\sqrt{K_p}\rfloor.}
$$

Thus $256^{K_p}\le p$, $K_p\ge1$, and the chosen observations are
$t=0,\ldots,K_p-1$. They lie in the authenticated interval. For example,
$256^K\ge256K$ for $K\ge1$, by induction, so $K\le p/256<3(p-1)/8$.

There are arbitrarily large primes $1\pmod8$, without requiring any prime
distribution theorem here. If there were only finitely many, let $P$ be
their product and take an odd prime divisor $q$ of $(2P)^4+1$. The order
of $2P$ modulo $q$ is exactly eight, since its fourth power is $-1$.
Hence $q\equiv1\pmod8$, but $q$ divides none of $P$, a contradiction.
Therefore $K_p,H_p\to\infty$ along this infinite family.

## 3. The selected prime component remains almost perfectly coherent

For an integer $h\ne0$, put

$$B_p(a;h)=\sum_{t=0}^{K_p-1}e(4ha16^t/p),\qquad 1\le a<p.$$

The source-selected embedding is $a=1$. Other $a$ are genuine relative
Galois alternatives at this prime, fixing the complete prime-to-$p$
cyclotomic carrier; they are not additional observed source trajectories.

**Theorem GPR-1 (PAPER-PROVED, selected local resonance).** For every such
$p$ and every integer $h$,

$$
\boxed{0\le K_p-|B_p(1;h)|
\le\frac{15488h^2(256^{K_p}-1)}{12495p^2}
<\frac{2h^2}{p}.}
$$

The last strict inequality applies to $h\ne0$; at $h=0$ the deficit is
zero. In particular $|B_p(1;h)|/K_p\to1$ for every fixed $h$.

*Proof.* $|B|\ge\operatorname{Re}B$ and
$1-\cos(2\pi x)\le2\pi^2x^2$ give

$$
K_p-|B_p(1;h)|
\le\frac{32\pi^2h^2}{p^2}
\sum_{t=0}^{K_p-1}256^t
=\frac{32\pi^2h^2(256^{K_p}-1)}{255p^2}.
$$

Use $\pi<22/7$ and $256^{K_p}\le p$; the rational coefficient
$32(22/7)^2/255=15488/12495$ is less than two. The estimate is valid
for all $h$, with no hidden small-angle assumption. $\square$

This coherence is caused by the actual first-pole numerator $4$, not a
postselected Galois label. It gives a lower bound on this component's
selected modulus, not on the full BBP modulus.

## 4. Exact primitive Galois mean and divergent selected amplification

**Theorem GPR-2 (PAPER-PROVED, finite cyclotomic identity).** If $p\nmid h$,

$$
\boxed{\frac1{p-1}\sum_{a=1}^{p-1}|B_p(a;h)|^2
=\frac{K_p(p-K_p)}{p-1}.}
$$

*Proof.* The residues $4h16^t$ are distinct modulo $p$ on this window.
If $0\le s<t<K_p$, then $0<16^{t-s}-1<p$, so $p$ cannot divide that
difference; $4h$ is a unit. In the expanded square, the $K_p$ diagonal
pairs average to one. Each of the $K_p(K_p-1)$ off-diagonal pairs has
primitive root average $-1/(p-1)$. Subtract and simplify. $\square$

This is equality **after cyclotomic evaluation**. The corresponding
nonconstant coefficient vector in a formal group algebra need not vanish.
The tests explicitly retain that distinction.

Writing the mean above as $\mathcal M_p(h)$, we obtain simultaneously

$$
\frac{\mathcal M_p(h)}{K_p^2}
=\frac{p-K_p}{K_p(p-1)}\longrightarrow0,
\qquad
\boxed{\frac{|B_p(1;h)|^2}{K_p\mathcal M_p(h)}\longrightarrow1.}
$$

Thus the selected-to-average squared-modulus ratio is asymptotic to
$K_p\to\infty$. This is stronger than a single finite outlier: no
uniform constant can convert this primitive Galois second moment into a
bound for the selected component on these authentic growing windows.
For each fixed nonzero $h$, only finitely many primes divide $h$, so
excluding them does not affect the limit.

The nonaliasing hypothesis is essential. If the observation window
repeats a prime-clock residue, extra diagonal contributions occur. If
$p\mid h$, every summand is one and the mean is $K_p^2$ instead.

## 5. Averaged spectral purity versus maximal selected reinforcement

For the local phase history $a u_{p,t}$, define its ordinary Fourier Gram
matrix with basis $1,e(x),\ldots,e((H-1)x)$, and let

$$
E_{p,H}(a)=\frac{D_{K_p,H}(a u_p)}H
=2\sum_{h=1}^{H-1}\left(1-\frac hH\right)
\left|\frac{B_p(a;h)}{K_p}\right|^2.
$$

The matrix basis here is **unscaled**, regardless of any separately
specified scalar frequency in GPR-1. In the executable joint budget, the
parameter `h` controls only that scalar sum.

**Theorem GPR-3 (PAPER-PROVED, infinite matrix separation).** For
$1\le H\le p$,

$$
\boxed{\frac1{p-1}\sum_{a=1}^{p-1}E_{p,H}(a)
=\frac{(H-1)(p-K_p)}{K_p(p-1)},}
$$

$$
\boxed{0\le(H-1)-E_{p,H}(1)
\le\frac{2H(H^2-1)}{3pK_p}.}
$$

*Proof.* The mean follows by GPR-2 for each $1\le h<H$, followed by the
finite weight identity $\sum_{h=1}^{H-1}2(1-h/H)=H-1$.
Every normalized modulus is at most one. GPR-1 therefore gives

$$
1-\left|B_p(1;h)/K_p\right|^2
\le2\left(1-|B_p(1;h)|/K_p\right)
\le\frac{4h^2}{pK_p}.
$$

Sum with the same weights and use
$\sum_{h=1}^{H-1}2(1-h/H)h^2=H(H^2-1)/6$. $\square$

At the predeclared $H=H_p$, the averaged normalized excess tends to zero
as $O(K_p^{-1/2})$, while

$$
\boxed{E_{p,H_p}(1)=H_p-1+o(1)\longrightarrow\infty.}
$$

The selected deficit from its maximal value is
$O(\sqrt{K_p}/p)=o(1)$. Hence even **growing-width averaged spectral
purity** cannot be promoted to selected purity on this exact source
component. No fabricated source, independent-Haar replacement, or
changed initial condition was used to produce this separation.

The finite exact witness $p=4294967377$ has $K_p=4$, $H_p=3$:
its averaged excess is less than $1/2$, its selected excess is greater
than $199/100$, and its selected squared-modulus amplification at $h=1$
is greater than $399/100$. Outward rational Machin/Taylor intervals
independently corroborate the selected bounds; the universal theorem
uses the displayed inequalities, not these finite observations.

## 6. The fresh prime is almost invisible to the selected full sum

Let the actual full and complementary sums on the same window be

$$
W_p(h)=\sum_{t=0}^{K_p-1}e(hU_{n_p+t}),\qquad
V_p(h)=\sum_{t=0}^{K_p-1}e(hw_{p,t}).
$$

**Theorem GPR-4 (PAPER-PROVED, full-complement comparison).** For every
integer $h$,

$$
\boxed{|W_p(h)-V_p(h)|
\le\frac{28|h|(16^{K_p}-1)}{15p}
\le\frac{28|h|}{15\sqrt p}.}
$$

*Proof.* The exact factorization retains all original complementary
phases. Since $|e(x)-1|\le2\pi|x|<7|x|$,

$$
|W_p(h)-V_p(h)|
\le\sum_{t<K_p}|e(4h16^t/p)-1|
\le\frac{28|h|}{p}\sum_{t<K_p}16^t.
$$

The geometric sum is $(16^{K_p}-1)/15$, and $16^{K_p}\le\sqrt p$.
The case $h=0$ is identically zero. $\square$

For the corresponding full and complementary root energies, the same
finite weighted-vector triangle inequality gives

$$
\boxed{
|\sqrt{E_{p,H}^{\mathrm{full}}}-\sqrt{E_{p,H}^{\mathrm{comp}}}|
\le\frac{28(16^{K_p}-1)}{15pK_p}
\sqrt{\frac{H(H^2-1)}6}.}
$$

This follows by applying the normalized GPR-4 bound to each frequency
$1\le h<H$ and the exact squared-frequency weight sum above. It requires
no smallness premise about either energy and no infinite-frequency
exchange. At $H_p$ its right side is $O(p^{-1/2}K_p^{-1/4})\to0$.

Thus a fresh prime's relative Galois alternatives can look highly
decorrelated while its actual selected contribution changes the full
real sum by almost nothing. The short-window full cancellation problem
lies in the source-generated complementary phases. The theorem does
not estimate their sum.

## 7. Precise obstruction, controls, and next gate

This result rejects the proposed inference

$$\text{small relative Galois matrix energy}
\quad\Longrightarrow\quad
\text{small selected local matrix energy}$$

even for a genuine prime channel freshly generated by the original
zero-initial BBP source. It also rules out treating each fresh-prime
window of this logarithmic length as an automatic local cancellation
event in the actual full signed sum. GPR-4 identifies exactly what such
an argument must still bound: the complete, source-generated
prime-to-$p$ complement on that window.

There is no conflict with the inherited long-window subgroup theorem.
If $L_p=\operatorname{ord}_p(16)$, then
$16^{L_p}\ge p+1>16^{2K_p}$, hence $L_p>2K_p$.
The new window is less than half one prime period. The earlier power
saving applies to an authenticated interval containing complete periods;
its unresolved complementary twist remains unresolved. The present
theorem does not improve the full selected bound $N-c\log N$.

The exact missing constraint is therefore a **selected real-embedding
estimate with both its admissible window length and its complete
complementary source specified**. A relative trace or Ramanujan average
alone cannot provide it. On these short windows, the complement must
already cancel to within the explicit GPR-4 error if the full sum is to
cancel; the fresh local channel supplies no independent saving.

Controls preserved in the instruments:

- A composite $p$ and a prime in the wrong residue class are rejected.
- A repeated prime-clock residue refutes the nonaliasing mean formula.
- A frequency divisible by $p$ refutes the nontrivial primitive-mean
  formula and is rejected by the joint budget.
- Changing the zero anchor, a pole coefficient, a selected prime phase,
  or even the unwrapped integer lift fails the full passport replay.
- The complete complement is kept exactly. No p-free arbitrary control
  is relabelled authentic; existing such controls remain separate.
- Formal coefficient arrays are never treated as already reduced
  cyclotomic values. Small-carrier quotient checks independently verify
  the primitive root cancellation used in GPR-2.

## 8. Executable authority

The new module is `observational_succ/global_prime_resonance.py` and its
focused tests are `tests/test_global_prime_resonance.py`. The existing
integer source carrier is independently checked against the literal
four-pole adapter at every replayed step from zero. The source passport
replay is bounded at 2000 transitions; the all-prime formulas are
paper theorems, not claims of having constructed huge state numerators.
The finite primality instrument has the separate declared budget
$257\le p\le2^{40}$; this is not a domain restriction on the theorem.

The 11 focused tests cover native exact cyclotomic quotients, a complete
primitive exponent histogram at $p=65537$, threshold-adjacent prime
scales through $4294967377$, independently certified selected intervals,
full-complement transport, source-pole chronology and unwrapped replay,
and intentional source/domain mutations.

```bash
python -m unittest discover -s tests -p 'test_global_prime_resonance.py' -v
```

Their successful finite execution supports the instruments. The infinite
matrix separation follows from GPR-1 through GPR-3 and the elementary
infinitude argument, and no numerical trend is substituted for that proof.
