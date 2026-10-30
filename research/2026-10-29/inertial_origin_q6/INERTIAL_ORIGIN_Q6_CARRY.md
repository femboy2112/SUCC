# SUCC: Inertial Origin Torsor × Source-Marked q=6 Carry × Observer-Resolution Frontier

**Date:** 2026-10-29. **Status:** independently derived research supplement, not a proof of π normality or RH. Starting source: SUCC draft #376 at `4a396badd6069a8011352133c02ec09af35b2bf6`; read-only sibling draft #373 at `262ed838b30b7ec50f4d05a4ec8fa1c977970dec`, and #375 at `bcc86f1f5edcb9696ae11451fb6dffede1530434`. Main at reconnaissance `ac7303b2e0e2ec16e3b1d88d186324e1fae65ea5`. The original four signed BBP poles, `U_0=0`, historic proof IDs and source archive are NOT modified. The finite Pascal/Bernoulli sensor is declared, not derived as a physical sampler of π digits.

## 0. Verdict

An observer's unknown **coordinate origin** is not an unknown **physical initial seed**. The former is a gauge choice and must be transported with the source reference; the latter is a possible physical homogeneous preparation. A neutral preparation can coexist with a nonempty, fluctuating virtual carrier and with ignorance of absolute coordinates. PR #373 already proves zero-preparation and retarded causality under a stated free-operation grammar. Here we add its *source-covariant full carry lift*, exact Haar-physical-seed conditional Fourier moments at all 17 BBP carry bins, a full q=6 factorial consequence, an exact 1/N seed-ensemble spectral law, exponential initial-resolution cost, and deterministic genuine-zero-seed run-length constraints. No original selected signed Weyl o(N) estimate follows.

## 1. Authentic source and moving reference

Write `e(t)=exp(2πit)` and use the original source

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0(s)=s`, `U_n(s)=16U_(n-1)(s)+r(n)`.

The unwrapped actual zero-prepared response is `A_n=U_n(0)=sum_(k=1)^n 16^(n-k) r(k)`. A prepared response is `U_n(s)=A_n+16^n s`. Its fractional part `x_n(s)={U_n(s)}` and original *literal integer carry* are

`κ_n(s)=floor(16 x_(n-1)(s)+r(n))`, `x_n(s)=16x_(n-1)(s)+r(n)-κ_n(s)`.

Let `g` be a **chart** offset, not a new physical preparation. Write the chart coordinates `V_n(s,g)=U_n(s)+16^n g` and the co-moving source reference `O_n(g)=16^n g`. Their **relative** state `W_n(s,g)=V_n(s,g)-O_n(g)=U_n(s)` is independent of `g`. Its phase `e(hW_n)` and its literal carry are consequently independent of `g` when carried with this marked source reference.

**RIO-01 (coordinate covariance):** For all real `g,s` and `n>=0`, these relative objects are gauge-invariant. Conversely, the simultaneous action `(V_n,O_n)->(V_n+16^n g,O_n+16^n g)` has no distinguished absolute coordinate point. A neutral preparation is the *relative* condition `V_0=O_0`; there is no claim that an unmarked translation-invariant state picks an absolute point. A static translation `V_n=U_n+g` instead changes the source forcing to `r(n)-15g` and is not an unchanged-source symmetry except at appropriate circle torsion.

**RIO-02 (physical distinction):** Keeping `O` fixed and changing only `s` changes `W_n` by `16^n s`. The coherent original-forcing preparation `s_*=-π/16` gives the exact `U_n(s_*)=-T_n` and all sufficiently late literal carries 15. It is *not* a coordinate change of the source-marked neutral orbit. The 15-torsion shift `s=1/15` rotates every absolute circle phase by a constant and is invisible to relative phase ratios; this kernel and the -1/-16 integer aliases were already proved by PR #373. Their different unwrapped preparation costs cannot be recovered from phase data alone.

## 2. Full q=6 rank/cototient × all 17 literal carries × absolute-relative phase

The authentic **declared** finite Pascal observation from PR #370 has exact positive rational weights

`q_n(j)=binom(n,j)/r(n) * sum_(k=0)^j (-1)^k binom(j,k) r(2n-j+k)`, `0<=j<=n`, `sum_j q_n(j)=1`.

For `q=6`, define both primitive bits `a_j=1_[gcd(j,6)=1]` and `b_j=1_[gcd(j+2,6)=1]`. Their Oily endpoint four-cell masses are `5/9, 172/1323, 352/1323, 64/1323` as in PR #374. For fixed integer `h!=0`, cell `(a,b)` and literal carry `c=0,...,16`, define

`T_(n,a,b,c,h;s,g)=sum_(j=0)^n q_n(j) 1_[a_j=a,b_j=b] 1_[κ_(n+j)(s)=c] e(hW_(n+j)(s,g))`.

This is **not** a Gamma-independent probability model for π; it is a deterministic phase/carry mark on the honest source-derived auxiliary grade law. Gamma-rank contrast `D(j+2)=H_(j+1)-γ-λ^(j+2)` and Abel quarter-phase `theta_j=e^(iπ(j+2)/8)` may multiply the j term: they are graded internal observables, not physical coordinate rotations. The q6 seam `(a_(j+2)-a_j)(D(j+4)-D(j+2))` retains the original rank-shift obstruction from #376, with γ canceling from its increment.

**RIO-03:** The complete 4×17 tensor is exactly **chart-gauge-invariant**, retaining all literal carry bins and absolute phase *relative to the inertial source reference*. An unmarked absolute phase or carry is not gauge invariant under arbitrary coordinate translation. The full tensor changes under genuine physical preparation `s`, including the coherent counterseed.

## 3. Exact Haar-seed signed carry theorem (ensemble, not selected)

Now make a **different** choice: keep source reference fixed and let the *physical* preparation `s` be uniformly Haar on the circle. For every `n>=2`, the source satisfies `0<r(n)<1`. Then `x_(n-1)(s)` is exactly Haar even though the dynamics are deterministic. Partition `x∈[0,1)` according to the literal carry `κ=floor(16x+r)`.

The 17 carry probabilities are EXACTLY

`P_Haar(κ=0)=(1-r)/16`, `P_Haar(κ=c)=1/16` for `1<=c<=15`, and `P_Haar(κ=16)=r/16`, with `r=r(n)`.

For **every nonzero integer Fourier harmonic h**, put `J_h(r)=(e(hr)-1)/(2πih)=integral_(0)^r e(hy)dy`. Directly integrating over the corresponding carry subintervals gives

`E_Haar[1_[κ_n=0] e(h x_n)]=-J_h(r(n))/16`,
`E_Haar[1_[κ_n=c] e(h x_n)]=0` for **each** `c=1,...,15`,
`E_Haar[1_[κ_n=16] e(h x_n)]=+J_h(r(n))/16`.

**RIO-04 (complete source-marked conditional Fourier law):** These identities hold exactly at every source time `n>=2`; no independence of adjacent carries and no digit randomness are assumed. Since `|J_h(r)|<=r`, each boundary magnitude is at most `r(n)/16<1/(16n²)` using the inherited original forcing bound. The boundary terms cancel in the unconditioned mean, as they must.

**RIO-05 (q6 all-cell law):** For each of the four q6 grade/rank sectors, form the full tensor `T` above. The positive `q_n(j)` are independent of physical seed. Therefore its Haar seed expectation is identically zero in every interior bin `c=1,...,15`; the `c=0,16` expectations are the corresponding **opposite signed** weighted sums of `J_h(r(n+j))/16`, bounded in modulus by `1/(16n²)` *per cell*. A bounded grade-dependent Gamma increment or 45° phase can be inserted without changing the bound. This is a rigorous original-source conditional-carry estimate **for the Haar physical-seed ensemble**, not for the `s=0` orbit.

**RIO-06 (physical counterseed):** For the coherent preparation `s_*=-π/16`, `x_n=1-T_n`, `κ_n=15` at every late time, and `e(hx_n)->1`. Thus the Haar interior-bin expectation zero coexists with a coherent path whose interior bin 15 is persistently occupied. Averaging unknown *physical seeds* is not the same as forgetting an *absolute chart* while retaining the source reference.

## 4. Exact seed-ensemble L² and reference information cost

For integer h≠0 put `S_N(h;s)=N^(-1)sum_(n=1)^N e(hU_n(s))`. Since distinct frequencies `h16^n` are orthogonal on Haar physical seed space,

`E_Haar[S_N(h;s)]=0`, `E_Haar[|S_N(h;s)|²]=1/N` for every N>=1.

**RIO-07:** The `1/N` mean-square is exact, source-independent, and does NOT evaluate `|S_N(h;0)|`. For the translated Eisenstein observer of PR #375, `Energy_N(y;s)=2sum_(h>=1) a_h(y)^2 |S_N(h;s)|²` with positive exponentially decaying a_h, so `E_Haar Energy_N(y;s)=C_y/N` where `C_y=2sum_(h>=1)a_h(y)^2>0`. But the coherent same-forcing seed has `Energy_N(y;s_*) -> C_y`, and the zero-seed limit is precisely the still-open π normality gate.

There are even source-sensitive, seed-averaged **frequency ladder correlations**: for k!=0,

`E_Haar[S_N(16k;s) conj(S_N(k;s))] = N^(-2)sum_(n=1)^(N-1) e(-k r(n+1))`.

The correction `sum_(n>=1)(e(-k r(n+1))-1)` converges absolutely, because r(n)=O(n^-2), and the correlation is `1/N+O_k(1/N²)`. Its next coefficient remembers the genuine four-pole source, but the relation itself is insensitive to the seed. This explicitly rejects an incorrect claim that different frequency channels become independent under ensemble ignorance.

**RIO-08 (relative preparation resolution):** Let a physical seed prior be uniform on a source-relative arc of length ε<=1 around 0. Its KL cost relative to Haar is exactly `log(1/ε)` nats. The terminal-phase expectation is

`E[e(hU_n(s))]=e(hU_n(0)) * sinc(πh16^n ε)` where `sinc(t)=sin(t)/t`.

To retain terminal-phase expectation of modulus **greater than 1/2**, one necessarily needs `ε<2/(|h|16^n)` (as otherwise `|sinc|<=1/(2π)`). For |h|=1 this requires more than `4n-1` **bits** of source-relative location information. This cost is a theorem about a *specific physical-seed uncertainty model*, not about chart/gauge ignorance. If source and observer reference are shifted together, the relative phase is unaffected and no absolute-position measurement is required. It is a sufficient obstruction to cheap ensemble-to-selected inference, not an all-purpose information-theoretic lower bound for every conceivable observation protocol.

## 5. Deterministic carry restrictions on the actual source

There is a useful, completely **deterministic** gain that does not average over seeds. With `a=8n-7`, exact original pole regrouping gives

`r(n)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)] > 15/[a(a+5)]` for all `n>=1`.

**RIO-09 (logarithmic ceiling on zero-carry runs):** If the consecutive *future* literal carries `κ_(n+1),...,κ_(n+L)` all equal zero, then

`x_(n+L)=16^L x_n+sum_(j=1)^L16^(L-j)r(n+j)<1`.

In particular `16^(L-1)r(n+1)<1`, giving the source-only exact necessary bound

`16^(L-1)*15 < (8n+1)(8n+6)`.

Thus any such run satisfies `L<1+log_16(((8n+1)(8n+6))/15)=2log_16 n+O(1)` for **every physical seed**, including s=0. It is a real carry-language restriction, not hexadecimal digit normality.

**RIO-10 (forbidden transition 16→16; in fact 16→0):** For all `n>=3`, the original source has `16r(n)+r(n+1)<1` (direct exact rational check for n=3,4; for n>=5 use `r(n)<1/n²`). If `κ_n=16`, then `0<=x_n<r(n)`, so `0<=16x_n+r(n+1)<1` and consequently `κ_(n+1)=0`. This holds for every physical seed and is a true finite-type constraint on the 17-label source-specific carry system. It says nothing about uniformity of the ordinary 16 digit symbols.

For Haar-physical-seed input, `P(κ_n=16)=r(n)/16`; summability of r gives by first Borel–Cantelli `P(κ_n=16 infinitely often)=0`. No independence assumption is needed. This **almost-sure** statement is not a theorem that the selected zero-seeded π orbit has finitely many carries 16.

**RIO-11 (genuine zero-seed carry-15 run → Diophantine approximation):** Let `T_n=sum_(j>=1)16^-j r(n+j)`, with the inherited authentic identity `U_n(0)+T_n=16^(n-1)π` and `0<T_n<1`. If `κ_(n+1)(0),...,κ_(n+L)(0)` all equal 15, solve the L-step recurrence and add the Green tail to obtain the **exact identity**

`x_n(0)+T_n = 1+16^-L ( x_(n+L)(0) -1+T_(n+L) )`.

Since `x_(n+L)∈[0,1)` and `T_(n+L)∈(0,1)`, it follows that

`||16^(n-1) π||_R/Z <16^-L`.

An established bound `μ(π)<=7.103205334137...` (Zeilberger–Zudilin) therefore implies that for every sufficiently large n, such a run has `L<6.11(n-1)` (choose exponent ν=7.11). The threshold is not made effective here. This is an authentic-zero-seed all-late-time restriction using π's known irrationality bound; it remains consistent with *zero-density* non-15 carries and does not imply normality. Newer September 2026 claims about sharper exponents are not required.

## 6. What survives and what remains open

The local q6 Γ-sector weights `D(j+2)=H_(j+1)-γ-λ^(j+2)` and Abel 45° grade twists are compatible with the marked relative-origin tensor, but they do **not** independently select a gauge origin. In a normalized primitive-minus-cototient contrast, γ cancels as a common additive reference, as already established in PR #374. The genuine zero preparation is a *source-relative operational boundary*, NOT a claim that the absolute numeral zero is objectively preferred in an unmarked translation-homogeneous universe.

The new deterministic restrictions `0`-run ceiling, `16→0`, and authentic `15`-run Diophantine ceiling constrain the allowed original-source literal-carry language. The full Haar carry Fourier identities and exact seed-average 1/N law give an analytic benchmark, but **no** theorem currently transfers them to the fixed prepared seed `U_0=0`. The observed nondecay q6 seam from PR #376 is gauge-invariant *after marking the source*, yet is a limsup result compatible with normal sequences. Turning these local constraints into `S_N(h;0)=o(1)` for all h≠0 requires new **zero-prepared, source-specific positive-density or signed long-range carry estimates**, not an ensemble or a change of coordinates. π normality and RH are OPEN.

## 7. Reproduction and external input

- `python inertial_gauge_probe.py` — 21 exact Fraction focused tests, including the source, gauge covariance, full q6 tensor, 17-bin Haar carry coefficients, and actual carry-run controls.
- `python independent_oracle.py` — independent SymPy reduced four-pole identity, direct 40 complex carry-bin integrals, two FFT Haar mean-square checks and four high-precision coherent-seed checks.
- Required original-source checks, full SUCC suite, hosted CI, Lean receipts and external referee review have **not** been run on a repository checkout in this isolated research package.
- Connected GitHub source refs: `research/2026-10-29/inertial_information_boundary/POINTED_PREPARATION_AND_CAUSALITY.md` (#373), `research/2026-10-29/q6_gamma_abel_tiling/OPERATION_GAMMA_TRIANGLE_Q6.md` and `CESARO_FIREWALL.md` (#376), `research/2026-10-29/golden_gamma_farey_twist/README.md` (#375), the original positive `OILY_MACARONI_SOURCE_BRIDGE.md` and `PI_PASCAL_REAL_KERNEL.md` on merged main.
- Published conservative irrationality measure input: D. Zeilberger and W. Zudilin, *The irrationality measure of π is at most 7.103205334137...*, 2020; see https://teorth.github.io/optimizationproblems/constants/7a.html and https://mathworld.wolfram.com/IrrationalityMeasure.html. No claims about unresolved 2026 preprints are imported.

**Truth status:** RIO-01..10 elementary paper proofs; RIO-11 paper argument conditional on published irrationality input; numerical oracles finite corroboration only; original zero-selected signed o(N) is **UNPROVED**.
