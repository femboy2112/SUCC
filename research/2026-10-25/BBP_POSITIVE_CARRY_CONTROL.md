# Positive forcing, every authentic carry, and the exact conductor tower still do not select the orbit

**Authority:** PAPER-PROVED all-time countermodel and rigidity theorem;
EXACT FINITE rational execution. No Lean or pi-normality claim. The original
four-pole BBP source is retained unchanged and explicitly distinguished from
the constructed forcing. This extends the carry/tower control in
[PR #301's discussion](https://github.com/femboy2112/SUCC/pull/301#issuecomment-6406560346),
which allowed negative forcing. It is not an assertion of scholarly novelty.

## 1. The retained source and the changed source

Let

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

Write $k_n=\lfloor U_n\rfloor$, $x_n=\{U_n\}$ and
$c_n=k_n-16k_{n-1}$. These are the authentic **rational-state carries**,
not asserted to be pi digits. Define

$$
Q_0=1,\qquad
Q_n=\operatorname{lcm}_{1\le j\le n}\operatorname{den}(r(j)),
\qquad \epsilon_n=1/Q_n.
$$

Every state denominator divides $Q_n$, and $Q_{n-1}\mid Q_n$. The following
recursion defines **one fixed all-time control**, with no horizon-dependent
choice of its source:

$$
y_0=0,\qquad
y_n=\begin{cases}
0,&x_n=0,\\
\max\{\epsilon_n,16y_{n-1}-c_n+\epsilon_n\},&x_n>0,
\end{cases}
$$

$$
V_n=k_n+y_n,\qquad r^*(n)=V_n-16V_{n-1}.
$$

The zero-phase case avoids assuming, without proof, that the authentic
rational state is never an integer. It also preserves all such events.
The control is not a candidate replacement for the authenticated source.

**Theorem PCC-1.** This control has all of the following properties:

1. $V_0=0$ and $r^*(n)>0$ for every $n\ge1$.
2. $0\le y_n\le x_n<1$, so $\lfloor V_n\rfloor=k_n$; its entire literal
   carry sequence equals $c_n$, and $y_n=0$ iff $x_n=0$.
3. Every denominator is odd, and
   $\operatorname{lcm}_{j\le n}\operatorname{den}(r^*(j))=Q_n$ for every
   $n$. Thus the complete conductor and cyclotomic-field towers agree.
4. $y_n=O(n^{-2})$. In particular every fixed Fourier mean of $V_n$ tends
   to $1$, so this trajectory is nonnormal.
5. The scaled source sum remains exactly
   $\sum_{n\ge1}16^{-n}r^*(n)=\pi/16$.
6. The forcing does not vanish: $\limsup r^*(n)\ge1$. Its future Green
   tail does not vanish either; its limsup is at least $1/16$.

Thus positivity, all authentic carries, the entire common conductor tower,
the zero anchor, and even the correct scaled source sum do not replace the
actual vanishing four-pole forcing and its vanishing Green correction.

## 2. Finite source algebra: positivity and exact retained data

Since $r(n)>0$ and its denominator divides $Q_n$, $r(n)\ge\epsilon_n$.
If $x_n>0$, its denominator also divides $Q_n$, so $x_n\ge\epsilon_n$.
Inductively, if $y_{n-1}\le x_{n-1}$, then

$$
16y_{n-1}-c_n+\epsilon_n
\le16x_{n-1}-c_n+r(n)=x_n.
$$

Both branches in the maximum are at most $x_n$. The zero case is immediate.
This proves $0\le y_n\le x_n<1$. The entire $y_n$ sequence lies on the
$Q_n$ rational grid, because the grids are nested.

If $x_n=0$, then
$r^*(n)=c_n-16y_{n-1}=r(n)+16(x_{n-1}-y_{n-1})>0$.
Otherwise, if $16y_{n-1}>c_n$, the nonreset branch gives
$r^*(n)=\epsilon_n>0$. If $16y_{n-1}\le c_n$, the reset branch gives
$r^*(n)=c_n+\epsilon_n-16y_{n-1}\ge\epsilon_n>0$.

Since the floors are identical,

$$
\left\lfloor16y_{n-1}+r^*(n)\right\rfloor
=k_n-16k_{n-1}=c_n.
$$

For the conductor claim, first every $\operatorname{den}(r^*(n))$ divides
$Q_n$. Suppose a new $p$-power layer enters $Q_n/Q_{n-1}$. The old authentic
state has smaller $p$-denominator depth than the new forcing, so $U_n$ has
the new depth and cannot be an integer. Hence $x_n>0$. In the nonreset branch,
$r^*(n)=1/Q_n$, so the layer survives. In the reset branch,

$$
Q_n r^*(n)=c_nQ_n+1-16Q_n y_{n-1}\equiv1\pmod p,
$$

because $Q_{n-1}y_{n-1}$ is an integer and $p\mid Q_n/Q_{n-1}$. The new
layer again survives. Induction proves equality of the cumulative conductors.
It does **not** claim that each individual forcing denominator equals $Q_n$.

## 3. Two elementary authentic-source bounds

The proof of decay uses actual BBP arithmetic, with explicit constants.

**Lemma PCC-2a.** For every $n\ge1$,

$$
\boxed{r(n)>\frac1{16n^2}.}
$$

Indeed its reduced-form numerator satisfies

$$
120n^2-89n+16-47n^2=(n-1)(73n-16)\ge0,
$$

while its positive product denominator is less than $512n^4$.
Thus $r(n)>47/(512n^2)>1/(16n^2)$.

**Lemma PCC-2b.** For every $n\ge1$,

$$
\boxed{Q_n>\frac{(2n-1)^4}{17017},\qquad
\epsilon_n<\frac{17017}{n^4}.}
$$

For each $p\in\{7,11,13,17\}$ and $p^a\le2n-1$, inspect the authentic
forcing at $j=(p^a+1)/2\le n$. The factor $2j-1=p^a$ vanishes to exactly
depth $a$. The other odd denominator factors are $2p^a+1$, $4p^a-3$ and
$4p^a+1$, all $p$-units. The numerator at $j\equiv1/2\pmod p$ is
$3/2\not\equiv0\pmod p$. Therefore $p^a\mid Q_n$. The largest power of
each selected prime at most $2n-1$ exceeds $(2n-1)/p$, including the power
$p^0=1$ when appropriate. Multiplication gives the strict bound, since
$7\cdot11\cdot13\cdot17=17017$. Finally $2n-1\ge n$.

This argument uses only four genuine prime families. It needs neither a
prime number theorem nor an assumption about pi's digit frequencies.

## 4. Quantified reset proof and decay

Call time $n$ a reset if $x_n=0$ or $16y_{n-1}\le c_n$. At a reset,
$y_n\in\{0,\epsilon_n\}$. Let

$$
A=20000,\qquad B=\frac{16384\cdot17017}{15}.
$$

The following inequalities are exact rational checks:

$$
\frac{B}{A^2}<\frac1{16},\qquad
\frac{16^9}{32(A+1)^2}>1,\qquad A^2>32\cdot17017.
$$

**A reset occurs between $A+1$ and $A+10$.** Put $d_n=x_n-y_n\in[0,1)$.
At a nonreset step the recurrence gives

$$
d_n=16d_{n-1}+r(n)-\epsilon_n.
$$

For $n\ge A$, the source bounds give
$r(n)-\epsilon_n>1/(32n^2)$. If all ten steps $A+1,\ldots,A+10$ were
nonresets, then
$d_{A+10}>16^9/[32(A+1)^2]>1$, a contradiction.

**Every later nonzero carry resets.** Start at any reset $a\ge A$. Suppose
the following $L\ge1$ carries are zero. Authentic positivity gives

$$
1>x_{a+L}\ge16^{L-1}r(a+1),\qquad
\boxed{16^L<256(a+1)^2.}
$$

Along that zero-carry run,

$$
y_{a+L}=16^Ly_a+\sum_{j=1}^L16^{L-j}\epsilon_{a+j}
\le\frac{16}{15}16^L\epsilon_a
<\frac{4096\cdot17017}{15}
\frac{(a+1)^2}{(2a-1)^4}
\le\frac{B}{a^2}<\frac1{16}.
$$

The same final bound holds at $L=0$. Consequently when the next carry is
nonzero, $16y_{n-1}<1\le c_n$, which is a reset. There are infinitely many
nonzero carries: an eventually zero carry tail would make the positive
recurrence $x_n=16x_{n-1}+r(n)$ grow beyond $1$. No normality or irrationality
assumption is needed for this fact.

Thus the reset argument repeats forever. Moreover
$256(a+1)^2<16^a$ for $a\ge4$ (check $a=4$ and take consecutive ratios),
so every such zero run has $L<a$. Therefore $n=a+L<2a$ and

$$
\boxed{0\le y_n\le\frac{4B}{n^2}\quad(n\ge A+10).}
$$

This proves the required infinite decay without computing an enormous
source prefix. In particular a finite explicit total-phase budget is

$$
\sum_{n\ge1}y_n< C_*:=A+9+\frac{4B}{A+9}.
$$

Hence, for every fixed integer $h$ and every $N\ge1$,

$$
\boxed{
\left|\frac1N\sum_{n=1}^Ne(hV_n)-1\right|
\le\frac{7|h|C_*}{N}.}
$$

Every fixed nonzero mode tends to one. By retaining arbitrarily many fixed
modes in the exact Fourier-energy identity, $D^*_{N,H_N}/H_N\to\infty$
for every $H_N\to\infty$. At the prescribed Spectral Purity width, the
conductor-birth contribution is still negligible, since its timeline is
identical. The surviving conductor-flat signed innovation therefore fails
maximally for this control, despite its positive forcing and authentic carries.

## 5. Same scaled source sum; a nonvanishing Green tail is the exact failed gate

Since $|V_n-U_n|<1$,

$$
\lim_{n\to\infty}16^{-n}V_n
=\lim_{n\to\infty}16^{-n}U_n=\pi/16.
$$

The original forcing has $r(n)<1$ for $n\ge2$ (discard its three negative
terms to bound it by $4/(8n-7)\le4/9$), so $0\le c_n\le16$ there, and
$c_1=3$. Thus $0<r^*(n)<17$ for all $n$, and telescoping proves the absolutely
convergent positive series identity

$$
\sum_{n\ge1}16^{-n}r^*(n)=\pi/16.
$$

This does not make $V_n$ a vanishing-tail approximation to the actual pi
orbit. Let $T_n$ be the original authenticated Green tail and let
$T_n^*=\sum_{j\ge1}16^{-j}r^*(n+j)$. Then exactly

$$
\boxed{T_n^*=T_n+x_n-y_n.}
$$

At every nonzero carry, $16x_{n-1}+r(n)\ge1$. Since these events occur
infinitely often and $r(n)\to0$, $\limsup x_n\ge1/16$. Consequently

$$
\limsup T_n^*\ge\frac1{16},\qquad
r^*(n)-c_n=y_n-16y_{n-1}\longrightarrow0,\qquad
\limsup r^*(n)\ge1.
$$

The counterfeit transfers authentic carry spikes into its forcing and future
tail. It loses the original vanishing $n^{-2}$ forcing, strict Hausdorff
moment law, and fixed rational four-pole identity. Those are explicit failed
hypotheses, not discarded error terms. The control does not refute pi normality.

## 6. The companion rigidity theorem: asymptotically correct forcing matters

**Theorem PCC-3 (common-carry backward rigidity).** Let $x_n,z_n\in[0,1)$
be any two bounded fractional trajectories with the same integer carries:

$$
x_n=16x_{n-1}+r_n-c_n,\qquad
z_n=16z_{n-1}+s_n-c_n.
$$

Put $\delta_n=z_n-x_n$ and $\eta_n=s_n-r_n$. For every $n\ge0,D\ge1$,

$$
\boxed{\delta_n=16^{-D}\delta_{n+D}
-\sum_{j=1}^D16^{-j}\eta_{n+j}.}
$$

The first remainder has absolute value less than $16^{-D}$. Also
$|\eta_n|=|\delta_n-16\delta_{n-1}|<17$, so the infinite series is
absolutely convergent and

$$
\boxed{\delta_n=-\sum_{j\ge1}16^{-j}\eta_{n+j},\qquad
|\delta_n|\le\frac1{15}\sup_{k>n}|\eta_k|.}
$$

Thus $s_n-r_n\to0$ forces $z_n-x_n\to0$. If
$|s_n-r_n|\le C/n^s$ for all $n\ge1$, $s>0$, then
$|z_n-x_n|\le C/[15(n+1)^s]$. For $s>1$ the phase differences are summable,
giving a uniform-in-$N$ absolute Weyl-sum transfer bound. In particular for
$s=2$,

$$
\left|\sum_{n=1}^Ne(hz_n)-\sum_{n=1}^Ne(hx_n)\right|
<\frac{7|h|C}{15}.
$$

These statements follow by finite backward iteration, a geometric tail and
the integral bound $\sum_{n\ge1}(n+1)^{-2}<1$. No source-selected cancellation
is assumed. They explain precisely why PCC-1 cannot also preserve vanishing
forcing: with its $y_n\to0$, that would force $x_n\to0$, contradicting the
infinitely many positive authentic carries and $r(n)\to0$.

## 7. Execution and claim limits

New code: `observational_succ/bbp_positive_carry_control.py`.
Focused tests: `tests/test_bbp_positive_carry_control.py`.

The finite replay checks the entire carry and common-conductor tapes through
512 source steps, using independent literal four-pole and integer-carrier
implementations. It checks strict positivity, rational grid domination,
exact backward Green identities on held-out windows, and source mismatch.
Separate cheap rational holdouts around 20000 and above one million check
the source lower bound and prime-power proof inputs without building giant
state histories. The bootstrap constants are checked as rational inequalities.
At $n=14$, the earlier carry/tower shortcut gives negative forcing; the new
recursion instead gives exactly $r^*(14)=1/Q_{14}>0$ while retaining that
step's authentic zero carry.

Observed focused command:
`python -m unittest discover -s tests -p 'test_bbp_positive_carry_control.py' -v`.
**11 tests passed.** The universal result is the proof above; no finite test
is promoted to an all-time theorem. The forcing $r^*$ is explicitly synthetic,
not the authenticated original four-pole source.

| Claim | Authority | Boundary |
|---|---|---|
| PCC-1: positive nonnormal control retains all carries, tower and scaled source sum | PAPER-PROVED; EXACT FINITE replay | The actual forcing and vanishing Green tail change |
| PCC-2: explicit source bounds and reset proof $y_n=O(n^{-2})$ | PAPER-PROVED; exact rational constants | Uses original source only to constrain the control's input tapes |
| PCC-3: common carries plus vanishing forcing difference imply asymptotic phase agreement | CLASSICAL backward recurrence, PAPER-PROVED here | Does not establish cancellation of either selected trajectory |
| Positivity + full authentic carries + conductor + source sum imply purity | REFUTED | The one fixed control above violates purity |
| Original four-pole conductor-flat signed innovation saving | OPEN | Not decided by this changed-source obstruction |
