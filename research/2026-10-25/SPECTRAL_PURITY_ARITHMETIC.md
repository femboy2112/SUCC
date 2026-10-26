# Spectral purity: authentic conductor layers, relative matrix traces, and a sparse-step obstruction

**Authority:** PAPER-PROVED finite algebra and all-horizon counting obstruction;
EXACT FINITE executable witnesses. No Lean authority is claimed here. This is
a source-typed application of classical cyclotomic trace, not an assertion of
academic priority. **Pi normality remains OPEN.**

This work descends from PR #296, commit
`461942c0bf616518e668d236d1c6b1596665a7dd`. It retains the literal source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

The prior first-prime/prime-power results and complementary Galois means are
in `BBP_CYCLOTOMIC_BIRTH_AND_LAG.md`,
`BBP_MINIMAL_PATH_GALOIS_SELECTION.md`, and
`observational_succ/bbp_minimal_path_births.py`. They already distinguish
Galois means from the selected complex embedding. The contribution here is
the **relative trace of the arriving matrix while fixing the entire past**,
its exact Fejer consequence, and the **weighted density obstruction to using
conductor growth as the good-step classification**.

## 1. The source field and the trace being taken

For a reduced rational $x$, write $\operatorname{den}(x)$ for its positive
denominator. Define the authentic, increasing carrier

$$
Q_n=\operatorname{lcm}_{1\le j\le n}\operatorname{den}(r(j)),\qquad Q_0=1.
$$

Every $Q_n$ is odd. In fact

$$
Q_n=\operatorname{lcm}_{0\le j\le n}\operatorname{den}(U_j).
$$

Proof: the recurrence expresses every state as an integer linear combination
of forcings; conversely $r(j)=U_j-16U_{j-1}$. Each side therefore divides the
other. This equality uses the complete history, not just the last reduced
state, which may cancel an old denominator factor.

Fix $n\ge2$ and an odd prime $p$ such that

$$
b=v_p(Q_{n-1}),\qquad v_p(Q_n)=b+1=:a.
$$

The new $p$ layer cannot cancel in $U_n$: the old summand $16U_{n-1}$ has
denominator depth at most $b$, whereas $r(n)$ has depth $a$. Hence the
$p$-primary phase $u=\lambda_p(U_n)$ has exact denominator $p^a$.
Let $c=U_n-u$ be the full $p$-free rational complement, retaining its lift.

Put $M=Q_n/p^a$, $L=\mathbb Q(\zeta_{Q_n})$, and
$F=\mathbb Q(\zeta_{Mp^b})$. Then $F$ contains every prior state character
and every other new prime channel. Define the normalized field trace

$$
\mathcal T_{n,p}(z)=\frac1{[L:F]}\operatorname{Tr}_{L/F}(z).
$$

Its automorphisms fix the full $p$-free component and multiply the primitive
$p^a$ root by all units congruent to $1$ modulo $p^b$ (all units if $b=0$).
Thus this is a single **conditional algebraic average** fixing the past.
It is not a stochastic law for the authentic time step and is not a change
to the source recurrence. The actual root of unity remains the chosen
embedding $e(U_n)$ throughout.

## 2. Exact matrix trace and Fejer bound

Let $H\ge1$, $v=(e(kU_n))_{0\le k<H}$ and
$w=(e(kc))_{0\le k<H}$. The previous normalized Gram $A=A_{n-1,H}$
has entries in $F$, is positive semidefinite, and has trace $H$.
Assume first $H\le p$.

**Theorem AR-1 (new higher layer).** If $b\ge1$, then

$$
\boxed{\mathcal T_{n,p}(vv^*)=I_H,\qquad
\mathcal T_{n,p}(q_{n-1,H})=H.}
$$

**Proof.** For an off-diagonal index difference $s=k-l$, $0<|s|<p$.
Writing $u=d/p^{b+1}$ with $p\nmid d$, its new-layer character average is

$$
e(su)\frac1p\sum_{j=0}^{p-1}e(sd j/p)=0.
$$

The complement and all previous Gram entries are fixed. Diagonal entries
are one. Linearity and $q=\operatorname{tr}(A vv^*)$ now give $H$.

**Theorem AR-2 (first prime layer).** If $b=0$, then

$$
\boxed{\mathcal T_{n,p}(vv^*)=\frac{pI_H-ww^*}{p-1},\qquad
\mathcal T_{n,p}(q_{n-1,H})=\frac{pH-q_c}{p-1},}
$$

where $q_c=w^*Aw\in[0,H^2]$. In the selected embedding of the fixed field,

$$
\boxed{\frac{H(p-H)}{p-1}\le\mathcal T_{n,p}(q_{n-1,H})
\le\frac{pH}{p-1}.}
$$

**Proof.** Each nonzero $s$ with $|s|<p$ has average
$(p-1)^{-1}\sum_{t=1}^{p-1}e(sdt/p)=-1/(p-1)$. The diagonal is one.
This proves the matrix identity. Positivity and the direct Fejer expression
give $0\le q_c\le H^2$, yielding both bounds. All prior source correlations
remain in $q_c$; no independence of their prime components is used.

These are genuine exact restrictions on the relative conjugates of the
authentic arriving matrix. They do **not** bound its selected conjugate.

### The frequency boundary is explicit

For $b\ge1$ and arbitrary $H$, the correct trace is

$$
[\mathcal T_{n,p}(vv^*)]_{kl}
=\mathbf1_{p\mid(k-l)}e((k-l)U_n).
$$

It is a direct sum of rank-one blocks indexed by frequencies modulo $p$,
not the identity. Its largest eigenvalue is $\lceil H/p\rceil$, so
$\mathcal T(q)\le H\lceil H/p\rceil$. Modes divisible by $p$ survive.
For a first layer, the general trace instead is
$[pB-ww^*]/(p-1)$, where
$B_{kl}=\mathbf1_{p\mid(k-l)}e((k-l)c)$. The $H\le p$ condition is therefore
a real nonaliasing condition, not a convenient omission of high modes.

## 3. The selected embedding violates the tempting upper-bound shortcut

An actual-source counterexample, independently interval-certified in
`spectral_purity_certificates.py`, is

$$
n=2,\quad H=p=3,\quad v_3(Q_1)=1,\quad v_3(Q_2)=2.
$$

AR-1 gives relative trace exactly $3$, but the actual Fejer innovation
$q_{1,3}$ is **strictly greater than $5$**. Indeed
$U_1=47/15$ and $U_2-U_1\equiv r(2)=106/819\pmod1$; hence

$$
q_{1,3}=3+4\cos(2\pi\,106/819)+2\cos(4\pi\,106/819)>5.
$$

The strict inequality is certified with outward rational Machin/Taylor
intervals, not decimal sampling. A separately chosen first-layer holdout,
$n=14,H=4,p=109$, has selected innovation exceeding $4\cdot109/108$, the
AR-2 upper bound for its relative average. Thus **even the authentic source**
refutes selected $q\le\mathcal T(q)$ and selected $q\le pH/(p-1)$ as universal
birth-step rules. This does not refute an asymptotic signed innovation saving.

The exact trace law also survives a deliberately changed pole weight
$4\mapsto5$. It is a theorem of the retained source-layer structure, not
an authentication theorem for the four-pole coefficients. The executable
source wrapper never certifies that mutant as authentic.

## 4. A quantitative obstruction to a conductor-growth good set

Define the independently arithmetic growth set

$$
\mathcal C_N=\{1\le n\le N:Q_n>Q_{n-1}\}.
$$

**Theorem AR-3.** The authentic source obeys

$$
|\mathcal C_N|\le
\#\{p^a\le8N:p\text{ odd prime},\ a\ge1\}=o(N).
$$

Consequently, for the innovation indices $m=n-1$,

$$
\boxed{
\sum_{\substack{1\le m<N\\m+1\notin\mathcal C_N}}m
=\frac{N(N-1)}2-o(N^2)\sim\frac{N^2}2.}
$$

**Proof.** The odd source decomposition is

$$
r(n)=\frac4{8n-7}-\frac1{8n-3}
-\frac{3n-1}{(2n-1)(4n-1)}.
$$

Since $\gcd(2n-1,4n-1)=1$, each prime power in its reduced denominator
divides at least one of $8n-7,8n-3,2n-1,4n-1$. In particular it is at
most $8n$. At every growth time choose one newly reached prime-power layer;
layers assigned at different times are distinct because $Q_n$ is increasing.
This proves the injection and finite count bound.

The number of prime powers of exponent at least two below $X$ is at most
$\lfloor\log_2 X\rfloor\sqrt X=o(X)$. Also the elementary prime-density
fact $\pi(X)=o(X)$ suffices here; no prime number theorem in progressions
is needed. A self-contained argument is as follows. For fixed $Y$, put
$M_Y=\prod_{p\le Y}p$. All primes greater than $Y$ are coprime to $M_Y$,
so $\limsup_{X\to\infty}\pi(X)/X\le\varphi(M_Y)/M_Y$ by counting residue
classes. The finite Euler product satisfies

$$
\prod_{p\le Y}(1-1/p)^{-1}
\ge\sum_{j=1}^{\lfloor Y\rfloor}\frac1j\longrightarrow\infty;
$$

therefore the upper bound tends to zero. Finally the growth-step weight is
at most $N|\mathcal C_N|=o(N^2)$. Subtract it from $N(N-1)/2$.

**Corollary AR-4 (failed exceptional-step strategy).** If a proposed good
set contains only arrivals with a new cyclotomic conductor layer and all
other steps are exceptional, then for every $H_N\to\infty$,

$$
\frac{2H_N}{N^2}\sum_{m\in\mathcal B_N}m
\ge H_N(1-o(1))\longrightarrow\infty.
$$

It cannot meet Target B's required exceptional budget. This remains true
even under the hypothetical grant that all growing-conductor arrivals
already satisfy the desired selected innovation bound. The proof concerns
the authentic four-pole source, not a counterfeit. It rejects this specific
classification; it does not rule out exploiting old prime clocks on the
conductor-flat steps, propagation from birth times, or direct signed saving.

## 5. Birth innovations can be removed at a prescribed growing width

The sparse-step obstruction has a stronger positive consequence. Set,
**before observing any source spectrum**,

$$
H_N=\max\left(2,1+\left\lfloor\sqrt{\lfloor\log_2N\rfloor}\right\rfloor\right).
$$

**Theorem AR-5 (source-specific partial-timeline saving).** For the original
four-pole BBP source and this explicit schedule,

$$
\boxed{
\frac{2}{N^2H_N}
\sum_{\substack{1\le m<N\\m+1\in\mathcal C_N}}
m\,|q_{m,H_N}-H_N|\longrightarrow0.}
$$

This is an unconditional upper bound on an arithmetically defined part of
the actual selected Fejer innovation, with no Galois substitution and no
Weyl cancellation assumption. In fact it has bound

$$
O\!\left(\frac1{\sqrt{\log N}}+
\frac{(\log N)^{3/2}}{\sqrt N}\right).
$$

**Proof with explicit finite budget.** Write $X=8N$,
$L=\lfloor\log_2X\rfloor$ and $K=\lceil\log_2X\rceil$. The central binomial
coefficient gives

$$
\prod_{m<p\le2m}p\ \mid\ {2m\choose m}<4^m,
\qquad
\vartheta(2m)-\vartheta(m)\le2m\log2.
$$

The divisibility holds because every prime in $(m,2m]$ occurs in the
numerator factorial and not the denominator factorials. Summing at
$m=2^j$, $j=0,\ldots,K-1$, gives

$$
\vartheta(2^K)\le(2^{K+1}-2)\log2.
$$

Every prime greater than $\sqrt X$ contributes more than
$\frac12\log X\ge\frac L2\log2$. Hence

$$
\pi(X)\le\lfloor\sqrt X\rfloor+\frac{4(2^K-1)}L.
$$

For powers with exponent $2,\ldots,L$, the base is at most $\sqrt X$.
Combining with AR-3 gives the **entirely rational, effective finite bound**

$$
|\mathcal C_N|\le B_N:=
\min\left(N,L\lfloor\sqrt{8N}\rfloor+\frac{4(2^K-1)}L\right).
$$

For $H\ge2$, $0\le q\le H^2$ implies $|q-H|\le H(H-1)$. Therefore

$$
\frac{2}{N^2H}\sum_{m+1\in\mathcal C_N}m|q_{m,H}-H|
\le\frac{2(H-1)}{N^2}\sum_{m+1\in\mathcal C_N}m
\le\frac{2(H-1)B_N}{N}.
$$

Since $2^K<16N$ and $L\asymp\log N$, the right side tends to zero at the
specified $H_N=O(\sqrt{\log N})$, with the displayed rate. This controls
the absolute sum on birth steps, so it does not falsely assume that their
individual signed defects are positive. The constants are loose; the
implementation evaluates the rational bound exactly even at large $N$.

**Corollary AR-6 (strictly narrower surviving timeline).** At this same
prescribed width, the sequential identity now has the proved form

$$
\boxed{
\frac{D_{N,H_N}}{H_N}
=\frac{2}{N^2H_N}
\sum_{\substack{1\le m<N\\Q_{m+1}=Q_m}}
m(q_{m,H_N}-H_N)+o(1).}
$$

The error is explicitly bounded by
$(H_N-1)/N+2(H_N-1)B_N/N$. Consequently the next sufficient estimate
is a signed $o(1)$ bound **only on conductor-flat steps**, at this fixed
schedule. Birth contributions require no further selected-embedding
estimate. The remaining sum is still OPEN; the established saving does
not control its density-one timeline.

### An effective modulus for the removed part

Let $t=\lfloor\log_2N\rfloor\ge64$, and denote the flat-step sum in AR-6
by $J_N^{\rm flat}$. A convenient explicit bound is

$$
\boxed{\left|D_{N,H_N}/H_N-J_N^{\rm flat}\right|
\le\frac{130}{\sqrt t}.}
$$

Indeed $L=t+3$, $K\le t+4$, $N\ge2^t$, and $\sqrt8<3$ give

$$
\frac{B_N}{N}\le3(t+3)2^{-t/2}+\frac{64}{t+3}.
$$

Since $H_N-1\le\sqrt t$, the birth contribution is at most
$6\sqrt t(t+3)2^{-t/2}+128/\sqrt t$.
For every integer $t\ge64$, $6t(t+3)\le2^{t/2}$. To prove it, square
both sides, check $t=64$, and note that the left side's successive ratio
is at most $(65/64)^4<2$, the ratio on the right. Thus the birth bound is
at most $129/\sqrt t$. The rank boundary is at most $1/\sqrt t$ because
$t\le N$. This proves the displayed modulus for every such $N$.

In particular, for any $\varepsilon>0$, the effective cutoff

$$
N\ge2^{\left\lceil\max\left(64,(130/\varepsilon)^2\right)\right\rceil}
$$

guarantees removal error at most $\varepsilon$. This very loose cutoff
controls only the part already proved negligible, not $J_N^{\rm flat}$.
It is not an effective normality theorem.

## 6. Exact conductor and positivity still admit maximal reinforcement

**Theorem AR-7 (positive exact-conductor counterfeit).** Use the authentic
$Q_n$ above, but deliberately replace the source by

$$
U_n^*=16^n-\frac1{Q_n},\qquad
r^*(n)=\frac{16}{Q_{n-1}}-\frac1{Q_n}.
$$

Then $U_0^*=0$, $U_n^*=16U_{n-1}^*+r^*(n)$, and
$r^*(n)\ge15/Q_{n-1}>0$. The reduced state denominator is exactly $Q_n$,
and the cumulative forcing denominator is also exactly $Q_n$, by the
state/forcing lcm identity from Section 1. Hence this changed source has
the **same complete conductor tower, field tower and prime-power birth
timeline** as authentic BBP, not merely the same finite list of primes.

Nevertheless $Q_n\to\infty$. Otherwise its increasing sequence would
eventually be a fixed integer $Q$, whereas the authentic positive
$r(n)\to0$, whose denominator divides $Q$, would have to satisfy
$r(n)\ge1/Q$. This is impossible. It follows that

$$
e(hU_n^*)=e(-h/Q_n)\longrightarrow1,
\qquad \frac1N\sum_{n=1}^N e(hU_n^*)\longrightarrow1
\quad(h\in\mathbb Z).
$$

The counterfeit is nonnormal. For each fixed $H$, its spectral excess
obeys $D_{N,H}^*/H\to H-1$, maximal reinforcement. The first fixed Fourier
mode already forbids purity along every diverging width. In particular,
the relative trace and conductor-birth removal theorems hold for this
countermodel, while its conductor-flat timeline retains the obstruction.

This is not a counterexample to any theorem with the authentic four-pole
law as a hypothesis. It changes that law, its $n^{-2}$ asymptotic, and the
carry history. It proves that **retaining even the exact conductor tower**
does not substitute for using the original numerator/pole relations in the
remaining flat-step estimate.

## 7. What is narrower now

The new matrix trace cannot be inserted into the sequential purity formula
as if it bounded $q$. The results distinguish two tasks:

1. For any attempt to use the trace **pointwise**, the selected-embedding
   deviation $q-\mathcal T(q)$ needs control; it is already positive on two
   exact authentic witnesses.
2. For the global purity target at AR-5's specified width, those birth
   deviations can instead be removed by the proved counting budget. Only
   the signed conductor-flat innovation remains; its total time weight is
   asymptotically $N^2/2$.

The source identity uniquely specifies those quantities, but uniqueness is
not a bound. Algebraic prime novelty provides exact averages on a sparse
set; it supplies neither a real-order comparison at the chosen embedding
nor a signed estimate on the much larger old-conductor timeline. The next
arithmetic target is therefore an estimate using **propagated, existing
prime channels and their full complementary phases**, not merely counting
new primes or replacing a selected root by its trace.

## 8. Execution and authority boundaries

The new module is `observational_succ/spectral_purity_arithmetic.py`.
`tests/test_spectral_purity_arithmetic.py` compares its trace with explicit
automorphism averages in the existing exact cyclotomic quotient, including
mixed-conductor holdouts. It independently checks source lifts and common
conductors against the integer carrier, compares the Fejer expression with
the inherited Gram innovation, and rejects composite labels and aliased
windows. Zero forcing, a changed pole coefficient, and the formal-versus-
cyclotomic distinction are retained as negative controls.

The trace representative belongs to $\mathbb Q[\mathbb Q/\mathbb Z]$ only
as an output representation: its asserted equality with the conjugate
average holds **after cyclotomic evaluation**. For example
$(e(1/9)+e(4/9)+e(7/9))/3$ is formally nonzero and evaluates to zero.
No Python test is an all-$N$ proof; AR-3/AR-4 have the paper proof above.
No field trace, positive Gram certificate, or finite interval witness here
proves base-16 normality of pi.
