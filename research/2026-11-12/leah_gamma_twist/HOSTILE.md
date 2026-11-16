# Hostile derivation: sparse centered carries and the negative Green profile

Status: local paper derivation, with exact finite implementation checks. This is a
conditional structural consequence and a hostile finite-history construction,
not R0 or normality. No claim of scholarly priority. Parent source inspected:
Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.

## 1. The exact boundary response retained by a centered integer carry

Keep the original four-pole forcing and let `U` be any real-seeded solution.
For `n >= 1`, define

\[
m_n=\lfloor U_n+1/2\rfloor,\quad v_n=U_n-m_n\in[-1/2,1/2),
\quad a_{n+1}=m_{n+1}-16m_n.
\]

The actual original source has `0 < r(n+1) < 1/2`, so
`a_(n+1) in {-8,...,8}`. This is a **centered integer carry**, distinct from
the literal floor carry and from the completed hexadecimal digit.
Let `T_n` be the exact authentic positive Green tail. Then

\[
\boxed{v_n+T_n=\sum_{j\ge1}16^{-j}a_{n+j}.}\tag{H1}
\]

Proof: the exact recurrence gives
`v_(n+1)=16v_n+r(n+1)-a_(n+1)`, whereas
`16T_n=r(n+1)+T_(n+1)`. Hence
`v_n+T_n=(v_(n+1)+T_(n+1)+a_(n+1))/16`.
Iterate and let the bounded terminal remainder tend to zero. No phase,
source forcing, or carry winding was averaged away. For finite `L`, the
corresponding purely rational identity is

\[
v_n+\sum_{j=1}^L16^{-j}r(n+j)
=\sum_{j=1}^L16^{-j}a_{n+j}+16^{-L}v_{n+L}.\tag{H2}
\]

For the authentic zero seed, `e(v_n+T_n)=e(16^n pi/16)`. H1 is a
source-preserving boundary response, but a cancellation theorem still needs
information about its **actual** impulse train.

## 2. Quantitative pulse density and shell coherence

For an integer `B >= 1`, write

\[
\mathcal A_B=\frac1B\sum_{n=B}^{2B-1}[1-\cos(2\pi(U_n+T_n))],
\quad K_B=\#\{B+1\le k\le2B-1:a_k\ne0\},
\quad c_B=1-r(B+1)>0.
\]

Then

\[
\boxed{\mathcal A_B\ge
\frac{4c_B^2}{257}\frac{K_B}{B}-\frac{\pi}{32B^2},}\tag{H3}
\]

and

\[
\boxed{\mathcal A_B\le
\frac{128\pi^2}{225}\frac{K_B+1}{B}
+\frac{128\pi^2}{3375B}.}\tag{H4}
\]

Proof of H3: whenever `a_(n+1) != 0`,

\[
c_B\le |a_{n+1}-r(n+1)|=|16v_n-v_{n+1}|
\le\sqrt{257}\sqrt{v_n^2+v_{n+1}^2}.
\]

Use `1-cos(2 pi v) >= 8v^2` on `|v| <= 1/2`, sum over the
interior edges, and note that each vertex is counted at most twice.
The difference between the rational and completed shell averages is at most
`(2 pi/B) sum T_n < pi/(32B^2)`, using `T_n<1/(64n^2)`.

For H4, weighted Cauchy applied to H1 gives

\[
(v_n+T_n)^2\le\frac1{15}\sum_{j\ge1}16^{-j}a_{n+j}^2
\le\frac{64}{15}\sum_{j\ge1}16^{-j}\mathbf1_{a_{n+j}\ne0}.
\]

Use `1-cos(2 pi t) <= 2 pi^2 t^2`. Each impulse with
`B+1 <= k <= 2B` contributes at most `1/15` to the summed convolution;
there are at most `K_B+1` such impulses. The total convolution weight from
`k>2B` is `(1-16^(-B))/225 < 1/225`. This gives H4.

Thus R0 is equivalent to positive lower density of these source-centered
nonzero carries. **This equivalence is not counted as an arithmetic saving.**
It is a different exact integer interface for the existing digit-change
obstruction. The useful additional information is the localized response below.

## 3. Conditional all-orders Green-tail locking

If `a_(n+1)=...=a_(n+L)=0`, H1 gives the sharp elementary bound

\[
|v_n+T_n|\le16^{-L}(1/2+T_{n+L}).\tag{H5}
\]

For any `1 <= L < B`, at most `L(K_B+1)` indices in `[B,2B)` fail the
pulse-free condition after discarding the last `L` positions. More precisely,

\[
\#\{B\le n<2B:
 |v_n+T_n|>16^{-L}(1/2+T_B)\}
\le L(K_B+1).\tag{H6}
\]

Each interior pulse contaminates at most `L` starting indices; the final
`L` indices pay the entire unknown future boundary. This proves H6 even
when the right side is larger than the shell.

**Theorem H7.** Suppose a sequence of shells `B_i -> infinity` satisfies
`A_(B_i) log B_i -> 0`. Then, for every fixed `p>0` and every `epsilon>0`,

\[
\frac1{B_i}\#\{n\in[B_i,2B_i):n^p|v_n+T_n|>\epsilon\}\longrightarrow0.
\]

Proof: H3 bounds `K_B/B = O(A_B+B^(-2))`. Set
`L=ceil((p+1) log_16 B)`. H6 has exceptional fraction
`O((A_B+B^(-2)) log B + log B/B)=o(1)`, while
`(2B)^p16^(-L)(1/2+T_B)=O(B^(-1))`. QED.

In particular, the source expansion `n^2 T_n -> 1/64` yields

\[
n^2v_n\longrightarrow-1/64
\quad\text{in shell density along that sequence}.\tag{H8}
\]

The coefficient follows directly from
`n^2 r(n+j) -> 15/64` for fixed `j`, geometric dominated convergence,
and `sum_(j>=1)16^(-j)=1/15`.
All higher fixed asymptotic orders of the Green tail likewise persist wherever
the corresponding source expansion is established: H7 pays an arbitrary
fixed power before any such expansion is used.

**Meaning.** A sufficiently coherent shell does not contradict the authentic
Gamma/Mellin forcing profile. It forces the rational fractional state to follow
the negative of that profile on most of the shell, with all source poles
retained. Every fixed asymptotic source jet is compatible with this local
locking. An arithmetic contradiction must use something beyond the jet.

**Boundary.** Ordinary failure of R0 only supplies `A_(B_i)->0`.
It does not supply `A_(B_i) log B_i ->0`. For mere failure, H6 remains
available with any schedule `L_i -> infinity` for which
`L_i(A_(B_i)+1/B_i)->0`, but that schedule need not reach the logarithmic
depth needed to resolve the `n^-2` source scale. This rate gap must not be
silently crossed.

## 4. Exact finite terminal-root control

Let `P_M=sum_(j=1)^M16^(-j)r(j)` and change only the seed to the rational
`s_M=-P_M`. The entire original forcing is retained. For `0<=n<=M`,

\[
U_n(s_M)=-\sum_{j=n+1}^M16^{n-j}r(j),\qquad U_M(s_M)=0.
\]

These states lie in `(-1/2,0]` because the whole source sum is
`pi/16<1/2`. Consequently **all centered carries through M are zero**.
The completed orbit is

\[
U_n(s_M)+T_n=16^{n-M}T_M.
\]

Take `M=2B`. Then the exact geometric sum and the source tail bound give

\[
\mathcal A_B(s_{2B})\le
\frac{2\pi^2T_{2B}^2}{255B}(1-16^{-2B})
<\frac{\pi^2}{8355840\,B^5}.\tag{H9}
\]

Thus fully rational states, exact future forcing, all original poles, and a
perfectly coherent finite rendezvous at a zero terminal state coexist with
arbitrarily coherent shells. These are **different seeds for different B**;
no single wrong rational seed is asserted to fail R0 asymptotically. The
original zero-anchor certificate rejects every `s_M`, since `P_M>0`.
This construction is a calibrated hostile control, not a source-compatible
counterexample after imposing the exact original seed.

For the coherent infinite seed `s=-pi/16`, `U_n=-T_n`, all centered carries
are zero and H1–H8 hold identically. For the rational alias `s=1/16`, all
centered carries from `a_2` onward agree with the authentic ones, because
`U_n(s)-U_n(0)=16^(n-1)` is an integer for `n>=1` and is homogeneous.
The carry statistic therefore cannot replace the exact zero-anchor kernel.

## 5. A sharp rate countercontrol: R0 fails but the Green scale is never reached

This construction is a single fixed same-forcing changed seed. It is stronger
than a different finite counterseed for every shell, while still failing the
original-zero authentication contract.

Set `t_1=16` and recursively

\[
t_{j+1}=t_j+\lceil\log_{16}t_j\rceil,\qquad
\beta=\sum_{j\ge1}16^{-t_j},\qquad s=\beta-x.
\]

Define the future impulse response

\[
S_n=\sum_{t_j>n}16^{n-t_j},\qquad
C_n=\sum_{t_j\le n}16^{n-t_j}\in\mathbb Z.
\]

Then `16^n beta=C_n+S_n`, so
`U_n(s)=C_n+S_n-T_n`. Since `0<=S_n<=1/15` and `0<T_n<=x<1/2`,
`S_n-T_n` lies in `(-1/2,1/2)`. Therefore the nearest integer is exactly
`m_n=C_n`, and the centered carry is `1` exactly at the prescribed pulse
times `t_j`. For `n>=16`, let `t_j<=n<t_(j+1)`. Then

\[
t_{j+1}-n\le\lceil\log_{16}t_j\rceil
\le\lceil\log_{16}n\rceil,
\qquad S_n\ge16^{-\lceil\log_{16}n\rceil}\ge\frac1{16n}.
\]

Thus

\[
\boxed{n^2(v_n+T_n)=n^2S_n\ge n/16\longrightarrow\infty.}\tag{H10}
\]

Nevertheless, for every integer `B>=16`, the pulse count obeys

\[
\frac{B}{\lceil\log_{16}(2B)\rceil}-2
\le K_B\le\frac{B}{\log_{16}B}+1.\tag{H11}
\]

For the upper bound, successive pulse times lying in the shell are separated
by at least `log_16 B`. For the lower bound, all gaps meeting the shell have
length at most `ceil(log_16(2B))`; the two endpoints pay the displayed 2.
Apply H3–H4, whose proofs hold for every seed of the original forcing, to get

\[
\boxed{\mathcal A_B(s)=\Theta(1/\log B)\longrightarrow0.}\tag{H12}
\]

This one source history fails R0 on **every** sufficiently late shell but
never approaches the negative Green-tail profile at the `n^-2` scale.
It shows why the hypothesis `A_B log B -> 0` in H7 cannot be replaced by
mere `A_B -> 0` or even `A_B=O(1/log B)`.

The completed digits have zero asymptotic density of 1s, so the point is
nonnormal. They are nonperiodic because the zero runs are unbounded while
infinitely many 1s occur; hence `beta` is irrational. No irrationality-measure
assertion is made. The seed is certainly nonzero: `beta<=16^(-16)/(1-1/16)
<1/16`, whereas `x=pi/16>3/16`. Thus the exact original-zero authentication
contract rejects this control without presupposing anything about pi's digits.

## 6. Archive novelty and source map

The source Green identity and tail bound are inherited from
`research/2026-10-25/BBP_DIOPHANTINE_COHERENCE.md` and the current frontier.
The nearest-integer lift is elementary. The predecessor is the whole-block
integer-branch coercivity argument in
`research/2026-10-27/GLOBAL_BRANCH_COERCIVITY.md`.
The binary-change equivalence and signed binary jump representation already
exist in `research/2026-11-12/frontier_rungs/LIMIT_FACES.md` (LMF-03), so no
new discovery is claimed for the broad idea of sparse jumps.

The added local result is H5–H8: an explicit source-centered Green response,
exceptional-set budget, and all-orders density locking conditional on the
specified coherence rate. H9 is an exact rational terminal-root calibration.
These are source-specialized lemmas, **not a new unconditional statistical
estimate for the original orbit**. No exhaustive literature novelty search
has been performed.

Important already-known obstructions found during this audit:

- `research/2026-10-30/arithmetic_barrier/signed_crt/`: dyadic wrong seeds
  preserve all odd-primary marks while producing arbitrary coherent finite
  windows; this must not be presented as a new result here.
- `research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md`:
  `log den(U_n)=6n+o(n)` and the fixed-filter `P(16)` dichotomy; denominator
  growth supplies no real separation.
- Main XXV's `v_16=0` countermodels already exclude a shortcut from a
  radix-restricted exponent, even zero, to R0.
- `research/2026-11-05/yoneda_circle/PROOFS.md`: approximate finite-depth
  source observations coexist with nonnormal periodic same-forcing seeds.

## 7. Verification and next falsifier

Exact `fractions.Fraction` execution in this round checked H2 at
`n in {1,2,7,19,31,83,127,251}` and `L in {1,2,5,11,23}` (40 cases),
the centered-carry range through `n=320`, and every terminal-root state for
`B in {3,8,17,37,83,127}` (terminal times 6 through 254). All checks passed.
The terminal-control and finite-Green loops reported 602 exact grouped
cases; the carry-range assertion was separate. These are implementation
checks; H1–H9 derive their infinite quantifiers from the paper proofs.
No floating phase sample was used as a certificate.

The rate countercontrol was subsequently checked with exact integer/Fraction
arithmetic at every `n=16,...,8192` (8,177 waiting-time cases), plus 10
shell-count cases at `B=16,31,64,127,256,511,1024,2048,4096,8192`.
All 8,187 cases passed; the finite upper count check used the weaker rational
bound `B/floor(log_16 B)+1` to avoid a transcendental numerical oracle.
The sharper H11 is justified by its paper proof.

A decisive falsifier for the formulas is one exact H2 failure, a carry outside
the declared range, or a seeded finite shell violating H9 with rigorous
phase intervals. A decisive **new arithmetic** input would be a lower bound
on the authentic number of impulses in source windows that cannot be
obtained for the terminal-root controls. Merely reproducing the negative
Green profile or its Gamma jets does not provide that input.


## 8. Reproduction and cross-route scope repair

The finite checks are preserved in [hostile_probe.py](hostile_probe.py), with
raw deterministic output in [HOSTILE_RESULTS.json](HOSTILE_RESULTS.json).
Run `python research/2026-11-12/leah_gamma_twist/hostile_probe.py`.
The source oracle is a separate direct four-pole Fraction implementation;
no selected-orbit production implementation is imported.

The root repaired an overstatement in the holographic dossier: the symmetric
endpoint-vs-midpoint response difference is a lower bound on ambiguity, not
its supremum for every frequency and resolution. At `h=32,q=1`, the target
is `e(2y)`. Endpoint pair `{0,1}` and midpoint `{1/2}` have equal response,
whereas interior pair `{1/4,3/4}` and midpoint `{1/2}` have identical mass and
first moment but response gap 2. The repaired wording in
[HOLOGRAPHIC.md](HOLOGRAPHIC.md) explicitly retains that counterexample,
the half-open-cell caveat, and the fixed-frequency quadratic-order conclusion.
The separate exact root-of-unity calculation is included in `hostile_probe.py`.
This audit checked the repaired scope; it does not independently certify every
other assertion in that dossier.
