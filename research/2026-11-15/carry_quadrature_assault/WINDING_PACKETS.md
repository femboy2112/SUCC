# Integer winding packets and the selected fourth-root obstruction

**Research note, 2026-11-15.** Constructor contribution on branch
`research/carry-quadrature-2026-11-15`, starting at
`895c0ae63af7b09548c608a1b0b6f298cea0e6d1`.

**Verdict.** The authentic zero-seeded source has an exactly quantized
integer winding observable. Each nonzero late winding forces a fixed
amount of real phase energy, and the published irrationality measure of
pi forces at least logarithmically many such windings at all sufficiently
large horizons. This is a direct winding formulation of an already known
logarithmic anti-lock mechanism, not an improvement in asymptotic order
and not a proof of positive shell density. A source-matched Thue–Morse
control has linearly many positive winding packets but no occurrences of
the selected fourth-root event after time 4. Packet energy alone does
not select that orientation.

## 1. Authentic source, domain, and elementary bounds

Throughout the original trajectory is

\[
r(n)=\frac{120n^2-89n+16}
 {(2n-1)(4n-1)(8n-7)(8n-3)},\qquad
U_0=0,\qquad U_n=16U_{n-1}+r(n)\quad(n\ge1).
\tag{WP1}
\]

The inherited BBP completion and positive Green tail are

\[
\alpha=\pi/16,\qquad
U_n=16^n\alpha-T_n,\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j)>0.
\tag{WP2}
\]

These are equalities in the real embedding. No value of pi in a 2-adic
completion is used.

**PROVED elementary source bound.** For every integer \(n\ge2\),

\[
0<r(n)<\frac{15}{64(n-1)^2}.
\tag{WP3}
\]

For positivity, the denominator is positive and the numerator at
\(n=m+1\), \(m\ge0\), is \(120m^2+151m+47>0\).
For the upper bound, subtraction and a common denominator give

\[
\frac{15}{64(n-1)^2}-r(n)
=\frac{5696n^3-9416n^2+4654n-709}
 {64(n-1)^2(2n-1)(4n-1)(8n-7)(8n-3)}.
\]

At \(n=m+2\), the numerator is
\(5696m^3+24760m^2+35342m+16503>0\).
Consequently, for every integer \(n\ge1\),

\[
0<r(n+1)<\frac{15}{64n^2}<\frac14,
\qquad
0<T_n<\frac1{64n^2}.
\tag{WP4}
\]

The tail estimate follows by bounding each \(r(n+j)\) by
\(15/(64n^2)\) and using \(\sum_{j\ge1}16^{-j}=1/15\).

## 2. Exact integer winding and its energy packet

Define the nearest-integer observation with a fixed tie convention,

\[
M_n=\lfloor U_n+1/2\rfloor,\qquad
\epsilon_n=U_n-M_n\in[-1/2,1/2),\qquad
K_n=M_{n+1}-16M_n\in\mathbb Z.
\tag{WP5}
\]

**PROVED exact winding law.** For every integer \(n\ge0\),

\[
\boxed{K_n=16\epsilon_n+r(n+1)-\epsilon_{n+1}.}
\tag{WP6}
\]

This is (WP1) after separating integer and centered fractional parts.
It is an integer quantization law; \(K_n\) is not physical energy.
The specific real phase response used below is

\[
E_n=|e(U_n)-1|^2=4\sin^2(\pi\epsilon_n),
\qquad e(x)=\exp(2\pi i x).
\tag{WP7}
\]

**PROVED packet inequality.** For every integer \(n\ge1\),

\[
K_n\ne0\quad\Longrightarrow\quad
\boxed{E_n+E_{n+1}\ge\frac9{257}.}
\tag{WP8}
\]

Indeed, (WP4) and integer nonvanishing imply

\[
|16\epsilon_n-\epsilon_{n+1}|
=|K_n-r(n+1)|>3/4.
\]

Cauchy–Schwarz gives

\[
\epsilon_n^2+\epsilon_{n+1}^2
\ge\frac{(16\epsilon_n-\epsilon_{n+1})^2}{16^2+1}
>\frac9{16\cdot257}.
\]

For \(|u|\le1/2\), concavity of sine on \([0,\pi/2]\) gives
\(\sin(\pi|u|)\ge2|u|\), hence \(E_n\ge16\epsilon_n^2\).
Combining the two estimates proves (WP8); the non-strict displayed
constant is a conservative choice.

The related pointwise statement is

\[
K_n\ne0\quad\Longrightarrow\quad
\max(|\epsilon_n|,|\epsilon_{n+1}|)>\frac3{68}.
\tag{WP9}
\]

It follows from \(16|\epsilon_n|+|\epsilon_{n+1}|>3/4\).

## 3. Source-selected count theorem with all quantifiers

**Imported classical input.** Zeilberger–Zudilin's published 2020
theorem gives
\(\mu(\pi)\le7.103205334137\ldots<15/2\).
Multiplication by a nonzero rational leaves the irrationality exponent
unchanged. Thus there exists \(\kappa>0\) such that, for every integer
\(p\) and every positive integer \(q\),

\[
\left|\alpha-\frac pq\right|\ge\kappa q^{-15/2}.
\tag{WP10}
\]

One can decrease \(\kappa\) to cover the finitely many reduced
denominators below the eventual bound. Unreduced denominators also obey
the resulting inequality, since reducing only decreases the denominator.
No numerical value for \(\kappa\) is extracted in this note.

**PROVED no-long-winding-lock theorem.** There exists an integer
\(M_0\ge1\) such that for every integer \(M\ge M_0\),

\[
\boxed{\text{some integer }n\in[M,8M)\text{ satisfies }K_n\ne0.}
\tag{WP11}
\]

Choose any integer \(M_0\ge1\) with

\[
\frac{33}{64}\,16^{-M_0/2}<\kappa.
\tag{WP12}
\]

Suppose instead that \(K_n=0\) for every integer \(M\le n<8M\).
Equation (WP5) then gives the exact integer transport

\[
M_{8M}=16^{7M}M_M.
\]

Using (WP2) at \(8M\),

\[
\begin{aligned}
\left|\alpha-\frac{M_M}{16^M}\right|
 &=16^{-8M}|\epsilon_{8M}+T_{8M}|\\
 &\le16^{-8M}(1/2+T_{8M})
 <\frac{33}{64}\,16^{-8M}.
\end{aligned}
\tag{WP13}
\]

But (WP10), with \(q=16^M\), gives the lower bound
\(\kappa16^{-15M/2}\). Equation (WP12) makes the upper bound strictly
smaller for every \(M\ge M_0\), a contradiction. This proof uses the
authentic completion \(\alpha=\pi/16\), hence the selected zero seed.

Define the counting function, for integers \(N\ge1\),

\[
P(N)=\#\{n\in\mathbb Z:1\le n<N,\ K_n\ne0\}.
\]

The intervals \([8^jM_0,8^{j+1}M_0)\) are disjoint. Thus, for every
integer \(N\ge M_0\),

\[
\boxed{P(N)\ge\left\lfloor\log_8(N/M_0)\right\rfloor.}
\tag{WP14}
\]

In particular the original trajectory has infinitely many nonzero
windings. The estimate is all-horizon and logarithmic; it is not a
positive density estimate, nor a one-event guarantee in every
\([B,2B)\) shell. The onset \(M_0\) is not numerically effective in this
note because (WP10)'s constant was not extracted.

**PROVED total phase-energy consequence.** For every integer \(N\ge1\),

\[
\boxed{\sum_{n=1}^N E_n\ge\frac9{514}P(N).}
\tag{WP15}
\]

Sum (WP8) over the winding events with \(1\le n<N\). Each \(E_n\)
appears in at most two of these adjacent pairs. This proves (WP15).
Since \(E_n=2(1-\cos(2\pi U_n))\), (WP14) yields

\[
\sum_{n=1}^N(1-\cos(2\pi U_n))
\ge\frac9{1028}\left\lfloor\log_8(N/M_0)\right\rfloor
\quad(N\ge M_0).
\tag{WP16}
\]

The completed phases have the same lower order of growth. In fact,
\(|\cos(2\pi(U_n+T_n))-\cos(2\pi U_n)|\le2\pi T_n\), and (WP4)
gives \(\sum_{n\ge1}T_n\le\pi^2/384\). Therefore

\[
\boxed{
\sum_{n=1}^N(1-\cos(2\pi16^n\alpha))
\ge\frac9{1028}\left\lfloor\log_8(N/M_0)\right\rfloor
-\frac{\pi^3}{192}.}
\tag{WP17}
\]

## 4. Exact controls and the missing orientation

### 4.1 Authentic positive check and archived carry budget

Direct rational evaluation gives

\[
U_1=47/15,\quad M_1=C_1=3,\quad \epsilon_1=2/15,
\]

\[
r(2)=106/819,\quad U_2=205826/4095,\quad
M_2=C_2=50,\quad\epsilon_2=1076/4095,\quad K_1=2.
\tag{WP18}
\]

Here \(C_n=\lfloor U_n\rfloor\). The actual selected fourth-root
event \(C_n\bmod4\in\{1,2\}\) occurs at \(n=2\).
These finite values check indexing and the sign of (WP6); they do not
prove any asymptotic rate.

For the literal floor carry \(c_n=C_n-16C_{n-1}\) and
\(y_n=U_n-C_n\), the exact quantization is

\[
16y_{n-1}+r(n)=c_n+y_n.
\]

Discounting and telescoping gives the exact total budget

\[
\sum_{n\ge1}16^{-n}c_n
=\sum_{n\ge1}16^{-n}r(n)=\pi/16.
\tag{WP19}
\]

Indeed the two partial sums are \(16^{-N}C_N\) and \(16^{-N}U_N\),
whose difference is \(16^{-N}y_N\to0\). Since \(c_2=2\), its
individual archived contribution to later \(C_n\) is
\(2\,16^{n-2}\). This contribution persists in the full integer while
eventually vanishing modulo every fixed \(2^k\). The budget by itself
therefore supplies no positive rate for fresh low-bit events.

### 4.2 Same-forcing coherent zero-packet control

Change only the real initial seed to \(s=-\alpha\). The resulting
trajectory is \(U_n(s)=-T_n\). By (WP4), for every \(n\ge1\),
\(M_n(s)=0\), \(K_n(s)=0\), and \(C_n(s)=-1\equiv3\pmod4\).
The same four-pole forcing has no late winding packets or selected
fourth-root events on this altered seed. This seed is not the authentic
zero seed and is not an admissible rational 2-adic initialization.

### 4.3 Same forcing, exponent 2, linear positive packets, zero target events

Let \(t_k\in\{0,1\}\) be Thue–Morse:

\[
t_0=0,\quad t_{2k}=t_k,\quad t_{2k+1}=1-t_k.
\]

Define

\[
\beta=3\sum_{k\ge1}t_k16^{-k},\qquad s=\beta-\alpha.
\tag{WP20}
\]

The sequence has no three consecutive zeros: every consecutive triple
contains a pair \((t_{2k},t_{2k+1})\), whose entries sum to one.
Consequently, for every integer \(n\ge0\),

\[
\frac3{4096}\le\{16^n\beta\}\le\frac15.
\tag{WP21}
\]

The upper bound follows by replacing every remaining binary digit by one.
Every finite prefix of the base-16 expansion is an integer with digits
in \(\{0,3\}\), and the remaining tail lies in \((0,1)\); hence it is
the exact integer part.

On the same authentic forcing, the altered seed gives
\(U_n(s)=16^n\beta-T_n\). For every integer \(n\ge5\),
\(T_n<1/(64n^2)\le1/1600<3/4096\). Thus

\[
0<\{16^n\beta\}-T_n<1/5<1/2,
\]

and therefore, for every \(n\ge5\),

\[
\boxed{M_n(s)=C_n(s)=\lfloor16^n\beta\rfloor,
\qquad C_n(s)\bmod4\in\{0,3\}.}
\tag{WP22}
\]

In particular, the target event is absent at every \(n\ge5\).
Nevertheless,

\[
\boxed{K_n(s)=3t_{n+1}\quad(n\ge5).}
\tag{WP23}
\]

Since \(t_{2k}+t_{2k+1}=1\), every interval of \(B\) consecutive
Thue–Morse indices contains \(B/2+O(1)\) ones, with an absolute error
at most one. Hence the nonzero winding packets have shell density
\(1/2+O(B^{-1})\), and they are all positive.

Bugeaud's published 2011 theorem gives irrationality exponent exactly
2 for \(\sum_{k\ge0}t_k b^{-k}\) in every integer base \(b\ge2\).
Here \(t_0=0\), so rational scaling gives \(\mu(\beta)=2\).
This is a classical imported theorem, not a finite-computation claim.

This control also satisfies uniform completed-phase anti-lock:

\[
1-\cos(2\pi16^n\beta)
\ge1-\cos(2\pi\cdot3/4096)>0,
\]

because (WP21) lies in \([0,1/2]\), where the displayed response is
increasing. Thus the fixed fourth-root event is a sufficient condition
for R0, not a necessary condition, even within the same-forcing family.
An energy argument can establish R0 on this control while its chosen
fourth-root orientation remains maximally locked.

**Scope.** The altered seed in (WP20) changes the selected completion and
does not satisfy \(U_0=0\). These facts do not refute the original
zero-seeded density conjecture. They refute a deduction of that event's
positive density from original forcing, finite irrationality exponent,
or even a linear supply of positive winding packets alone. The general
Thue–Morse counterseed method is inherited from OMH-04; the digit scaling
to \(\{0,3\}\), effective time-5 exclusion, and winding/orientation
comparison are the present targeted specialization.

## 5. Provenance audit and exact remaining hole

HBR-05 already uses the published \(\mu(\pi)<15/2\), a nearest-integer
expansion argument, and disjoint \([M,8M)\) intervals to prove
logarithmic selected real lag energy. The proof mechanism of (WP11) is
the same. Here the observable is the literal nearest-integer winding
\(M_{n+1}-16M_n\) of the original trajectory, and (WP8) attaches a
uniform adjacent-phase packet to it. This is a useful exact
quantization statement, not a new Diophantine input, not a stronger
growth exponent, and not a closure of R0.

The earlier `OILY_DIRECT_ARITHMETIC.md` already proves a stronger
logarithmic signed modulus deficit
\(N-|S_N(h)|\ge(\log_8N)/29-O_h(1)\). Since
\(N-\Re S_N(h)\ge N-|S_N(h)|\), (WP17) is not an improvement on that
original-source result either. No novelty is claimed for the
irrationality-based logarithmic anti-lock bound.

The still-open target of this assault is

\[
\exists\delta>0\ \exists B_0\ \forall B\in\mathbb Z,\ B\ge B_0:
\quad
\frac1B\#\{B\le n<2B:C_n\bmod4\in\{1,2\}\}\ge\delta.
\tag{WP24}
\]

Writing \(w_n=\Re[(1+i)i^{C_n}]\), one has exactly
\(\mathbf1_{\{C_n\bmod4\in\{1,2\}\}}=(1-w_n)/2\).
The bounds (WP8)–(WP17) constrain a different observable. In particular,
(WP23) demonstrates that a positive rate of quantized winding packets
does not choose the sign of this fourth-root report.

There is an exact joint packet/sign decomposition. Put
\(b_n=\mathbf1_{\{\epsilon_n<0\}}\) and
\(\sigma_n=1-2b_n\in\{-1,1\}\). The tie convention in (WP5) makes
\(\sigma_n=1\) when \(\epsilon_n=0\). Since
\(C_n=M_n-b_n\) and \(M_n\equiv K_{n-1}\pmod4\), for \(n\ge1\),

\[
\boxed{
\begin{aligned}
\mathbf1_{\{C_n\bmod4\in\{1,2\}\}}
={}&\mathbf1_{\{K_{n-1}\equiv2\ (4)\}}\\
&+\mathbf1_{\{K_{n-1}\equiv1\ (4),\ \epsilon_n\ge0\}}\\
&+\mathbf1_{\{K_{n-1}\equiv3\ (4),\ \epsilon_n<0\}}.
\end{aligned}}
\tag{WP25}
\]

The three events are disjoint. The equivalent signed formula is

\[
\boxed{w_n=\cos(\pi K_{n-1}/2)
-\sigma_n\sin(\pi K_{n-1}/2).}
\tag{WP26}
\]

For example, a positive lower shell density of winding residues
\(K_{n-1}\equiv2\pmod4\) alone would suffice for (WP24). Positive
packet counts without a residue/sign restriction do not: in the
Thue–Morse control, the nonzero packets have residue 3 and the ending
centered phase is positive. Equations (WP25)–(WP26) identify the missing
joint orientation at integer resolution; they are bookkeeping
identities, not a proof of any positive mass in those three cells.

No estimate in this note bounds the original selected count in (WP24)
beyond finitely verifiable events. A further theorem must use the
authentic zero seed together with the original arithmetic in a way
that controls this orientation. The existing four-pole tail bound
and the exponent in (WP10) do not do so. The control in Section 4.3
is a direct falsifier for any proposed deduction omitting that
selection step.

**Next discriminating probe.** For any proposed signed restriction,
evaluate its exact hypotheses and conclusion on the original rational
trajectory and on both same-forcing controls above. If it only sees
the forcing, an irrationality exponent, or positive winding counts,
the Thue–Morse control passes those hypotheses and fails (WP24).
To survive, the restriction must exhibit an actual zero-seed identity
that changes its signed conclusion. Finite original-path counts can
check formulas and constants; they cannot certify the all-B quantifier.

## 6. Primary and repository sources

- Original BBP identity: Bailey, Borwein and Plouffe, *On the Rapid
  Computation of Various Polylogarithmic Constants*, Mathematics of
  Computation 66 (1997), 903–913,
  <https://doi.org/10.1090/S0025-5718-97-00856-9>.
- Zeilberger and Zudilin, *The irrationality measure of pi is at most
  7.103205334137...*, Moscow Journal of Combinatorics and Number Theory
  9 (2020), 407–419,
  <https://arxiv.org/abs/1912.06345v2>,
  <https://doi.org/10.2140/moscow.2020.9.407>.
- Bugeaud, *On the rational approximation to the Thue–Morse–Mahler
  numbers*, Annales de l'Institut Fourier 61 (2011), 2065–2076,
  <https://www.numdam.org/item/AIF_2011__61_5_2065_0/>,
  <https://doi.org/10.5802/aif.2666>.
- Inherited HBR-04/05 and source passport:
  `research/2026-11-02/carrier_hbar_bridge/PROOFS.md`.
- Inherited same-forcing Thue–Morse construction and overlap warning:
  `research/2026-11-02/oily_hbar_seam/PROOFS.md`, OMH-04 and Section 7.
- Inherited stronger logarithmic signed deficit:
  `research/2026-10-26/OILY_DIRECT_ARITHMETIC.md`.

All universal conclusions here rest on the displayed derivations and
the named classical inputs. No Lean verification or finite test suite
is claimed as a proof of (WP11), (WP14), or (WP24).

### Finite constructor calibration executed in this round

An exact `fractions.Fraction` calculation generated the original states
\(U_0,\ldots,U_{256}\), checked all 256 winding identities (WP6), all
source upper bounds at \(2\le n\le256\), and the rational precursor
\(16(\epsilon_n^2+\epsilon_{n+1}^2)\ge9/257\) at each of the 238
nonzero windings with \(1\le n<256\). This avoids approximating sine;
the analytic sine inequality remains part of the proof.
An additional exact run checked all 256 packet/sign decompositions
(WP25) and all 256 signed quadrature identities (WP26) at
\(1\le n\le256\), using the integer tables for quarter-turn sine and
cosine.

For the Thue–Morse control, use
\(\beta_{160}=3\sum_{k=1}^{160}t_k16^{-k}\) and the enclosing interval
\([\beta_{160},\beta_{160}+16^{-160}/5]\). For every
\(5\le n\le128\), enclose \(T_n\) by its first 12 terms and the
remainder upper bound \(16^{-12}/[64(n+12)^2]\). Exact rational interval
comparison certified 124 floor/nearest-integer decisions in (WP22),
123 winding identities in (WP23), and zero selected fourth-root events
over that finite range. These are calibration checks of the formulas;
the all-n conclusions come from (WP21)–(WP23).

The raw check summaries were:

```text
{'authentic_states': 257, 'exact_winding_identities': 256, 'rational_packet_lower_bounds_checked': 238, 'first_two_states': ['47/15', '205826/4095']}
{'tm_interval_floor_and_nearest_certificates': 124, 'tm_exact_winding_certificates': 123, 'target_events': 0, 'n_range': [5, 128]}
{'packet_sign_event_identities': 256, 'signed_quadrature_identities': 256}
```
