# Operation One-Shot: natural-number BBP, cyclotomic lag spectra, and source-selected proof debt

**Date:** 2026-10-24 · **Research draft only** · **Direct parent:** draft #281, `f3498142319919e61e56bfe80c39d5410d8c61bf`, inheriting #277/#274/#273/#272. **Main untouched.** Independent sibling #271 supplies the four-bit Walsh source jet but is **not merged**. Existing `CYC03_BBP_FOUR_POLE_LANE.md` contains a corrigendum and must be read together with `BBP_SOURCE_MEMORY_REPAIR.md`, not treated as an authoritative closure of the four-pole lane.

**π NORMALITY: OPEN.** No proof of base-16 (hence base-2) normality, decimal normality, or independence. No Lean kernel check, external independent referee, or academic-priority claim. Elementary/new-to-branch derivations, named classical inputs, exact finite certificates, and failure controls are distinguished throughout.

## 0. Goal, already-authenticated carrier and steelman

Take the single arithmetic carrier `(N,0,S)` with `S(n)=n+1`. The internal total natural-state BBP machine from #281 has an anchored section `i(n)`, satisfying `F(i(n))=i(n+1)` and `q(i(n))=U_n`, including its **unwrapped literal rational lift**. The original source is

```
U_0=0,
U_(n+1)=16U_n+r(n+1),
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)
     =(120n^2-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)].
```

All prime, Pascal, Lucas, dyadic and real-circle instruments in this round read this one chronological graph. `π/16=Σ_{j>=1}16^-j r(j)` is the **classical imported BBP identity**, and `16^n π/16=U_n+T_n` uses the inherited strictly positive source tail. The object of proof is the selected orbit, **not the law of an ensemble of possible carriers**.

The correct proof obligation, by Bailey–Crandall/Weyl, is, for every fixed nonzero integer `h`,

```
S_N(h)=Σ_(n=1)^N exp(2πi h U_n) = o(N).
```

One-shot ambition: make this emerge from exact source operations. A formal or finite computation that simply restates this as a hypothesis is not a completed proof.

### Prior-art firewall

- Original [Bailey–Crandall 2001](https://doi.org/10.1080/10586458.2001.10504441) and [Lagarias 2001](https://doi.org/10.1080/10586458.2001.10504456): the equivalence between BBP source equidistribution and normality is classical; general orbit relations need not be statistically decisive.
- `research/2026-10-23/CYC03_BBP_FOUR_POLE_LANE.md` already considers `16^d-1` cyclotomic frequencies and a finite autocorrelation/carry criterion; its original "four-pole lane closed" interpretation was REFUTED by the subsequent [source-fidelity repair](BBP_SOURCE_MEMORY_REPAIR.md).
- `observational_succ/duck_bbp_fourier.py` already contains strong summable real tail and Fourier-transport estimates. **We do not promote any repetition of those bounds to a new result.**
- This round supplies a **sharply calibrated source lag identity**, explicit finite-prime-depth cost, rigorous finite source-selected certificates, and complete held-out four-family factorial controls. **None pays the remaining selected Fourier saving.**

## 1. Exact BBP lag-lift with sharp coefficient (NLG-01–04)

For integers `n>=1`, `k>=1`, define

```
R_(n,k) = Σ_(j=1)^k 16^(k-j)*r(n+j).
```

Induction through the original integer-state machine gives, as an equality of **unwrapped rationals**,

```
U_(n+k)-16^k U_n = R_(n,k),
U_(n+k)-U_n = (16^k-1)U_n + R_(n,k).
```

The second identity is valid after circle reduction because integer coefficients commute with the quotient, but the unwrapped equality is the **source authentication**.

### An all-time positive strict bound (paper proof)

Write `P(j)=120j²-89j+16` and `D(j)=(2j-1)(4j-1)(8j-7)(8j-3)`; for `j>=2`, put `t=j-2`. Direct exact integer multiplication yields

```
15D(j)-64(j-1)^2 P(j)
=5696t^3+24760t^2+35342t+16503 > 0.
```

The inherited positive real source representation proves `r(j)>0`, hence

```
0 < r(j) < 15/[64(j-1)^2],      j>=2.
```

For `n>=1`, every `n+j>=2`; therefore

```
0 < R_(n,k)
  < (15/[64 n^2]) * Σ_(j=1)^k 16^(k-j)
  = (16^k-1)/(64 n^2).                      (1)
```

This constant is **sharp for every fixed k**: the corrected source pole-moment expansion gives `r(n+j)~15/(64n²)`, with `j` in a fixed finite set. Thus

```
lim_(n->infinity) [64 n² R_(n,k)/(16^k-1)] = 1.  (2)
```

This is a special **two-time source forcing** estimate; it is not the previously established one-time tail estimate `T_n~1/(64n²)`.

For `e(x)=exp(2πix)`, `|e(x)-e(y)|<=2π|x-y|`, and using `π<22/7`, for any integer `h`, start `M>=1`, length `L>=0`:

```
|Σ_(n=M)^(M+L-1) e(h(U_(n+k)-U_n))
 -Σ_(n=M)^(M+L-1) e(h(16^k-1)U_n)|
 <= (44|h|/7) * (16^k-1)/64 * Σ_(n=M)^(M+L-1)1/n².
```

For `M>=2`, the last sum is `<1/(M-1)` **regardless of window length**. On starts `M` of size `N`, the Fourier *mean* error for a window of length `N` is `O_h(16^k/N²)`; starts at one cost `O_h(16^k/N)` after normalization. These bounds quantify why growing lag must be budgeted before claiming source phase replacement.

### Important quantified obstruction: the error is not small at all k

At `M=64, L=64`, the numerical difference of the actual lag-character mean and its cyclotomic approximation at `k=6` is approximately `0.39146`. For `M=512, L=512`, the corresponding difference is approximately `0.08659`. These are **uncertified numerical diagnostics** only; the exact rational upper bound is rigorous but often enormous at `k=6`. This is why `k` cannot be driven to arbitrary prime depth at a fixed physical/sample horizon by this triangle argument.

## 2. A genuinely scoped van der Corput/CYC-03 proof contract (NLG-05–06)

For a fixed nonzero integer `h`, write

```
S_N(h) = Σ_(n=1)^N e(h U_n),
C_(k,N,h) = Σ_(n=1)^(N-k) e(h(U_(n+k)-U_n)),
W_(k,N,h) = Σ_(n=1)^(N-k) e(h(16^k-1)U_n).
```

The preceding theorem pays an explicit rational error

```
|C_(k,N,h)-W_(k,N,h)| <= E_(k,N,h),
E_(k,N,h)=(44|h|/7)*(16^k-1)/64 * Σ_(n=1)^(N-k)n^-2.
```

For integers `1<=H<=N`, **classical van der Corput/Cauchy–Schwarz**, by zero-extending `z_n=e(hU_n)` and averaging its H overlapping shifts, proves

```
|S_N(h)|² <= (N+H-1)/H² * [HN+2Σ_(k=1)^(H-1)(H-k) Re C_(k,N,h)].
```

Substituting the authentic source bound gives the nonnegative upper certificate

```
|S_N(h)|²/N² <= (1+(H-1)/N) *
 [1/H+(2/H)Σ_(k=1)^(H-1)(1-k/H)*(|W_(k,N,h)|+E_(k,N,h))/N].   (3)
```

The inequality is VALID and uses genuine source forcing, but does **not** prove the RHS vanishes. The exact Gaussian-integer checker calibrates its Cauchy part on all four-root words of length through 6 and negative/periodic controls.

**Explicit conditional one-shot theorem:** let `H_N=floor((log_16 N)/2)` for `N>=256`. If for every **fixed** `h!=0`

```
(1/H_N)Σ_(k=1)^(H_N-1)(1-k/H_N)*|W_(k,N,h)|/N -> 0,    (4)
```

then base-16 π normality follows by (3), because `H_N->infinity`, `16^H_N<=sqrt(N)`, `Σ n^-2<2`, and the total forcing error in (3) is `O_h(16^H_N/(N H_N²))=o(1)`. Weyl's criterion and the inherited summable shadowing transfer then close the mathematical implication.

**Claim status: CONDITIONAL.** Equation (4) is **not proved**, and the older CYC-03 research already recognized a related divisor/cyclotomic accumulation requirement. This is an exact admissible uniform-in-k schedule, not a new normality theorem. Reducing the first harmonic to many harmonics is **not** an automatic gain unless the four-pole source controls those new harmonics.

## 3. Cyclotomic clock blindness and cost of depth (NLG-07–10)

For each `k`, `16^k-1=Π_(d|k)Φ_d(16)` (classical cyclotomic identity). For the first forcing-relevant primes one has the following **exact** valuations (LTE/elementary modular orders):

```
v_3(16^k-1)=1+v_3(k),
v_5(16^k-1)=1+v_5(k),
v_7(16^k-1)= 0 if 3∤k, otherwise 1+v_7(k/3),
v_13(16^k-1)=0 if 3∤k, otherwise 1+v_13(k/3).
```

In particular, both p=7 and p=13 enter at `k=3`, a **shared cyclotomic clock** rather than evidence of random independent histories. If an actual rational `x` has p-primary fractional denominator depth `e<=v_p(16^k-1)`, then `e((16^k-1)*λ_p(x))=1`; a deeper component is NOT killed.

For each depth B, the *least* lag annihilating p^B for all four p=3,5,7,13 is

| B | minimal k |
|---:|---:|
| 1 | 3 |
| 2 | 1,365 |
| 3 | 1,863,225 |
| 4 | 2,543,302,125 |

These numbers follow by lcm of exact multiplicative orders modulo p^B. The implementation verifies minimality by complete modular order loops for sampled orders, and direct modular divisibility for the larger lcm. **These do not remove the original prime information**, only its finite-depth character at the displayed frequency. The sharp error `(16^k-1)/64n²` becomes unusable astronomically faster than the prime depths grow. This obstructs the *cheap approximation-and-annihilation* route, not every signed-correlation route.

## 4. Exact frequency-uniform adversarial witness (NLG-11)

Every `U_n` is a rational with odd denominator. For a finite source prefix, let

```
L_N=lcm{denominator(U_1),...,denominator(U_N)}.
```

Then for **the growing frequency** `h_N=L_N`, **every** phase `e(h_N U_n)` equals 1 and `S_N(h_N)=N`. Hence no statement such as `sup_(h != 0)|S_N(h)|/N -> 0` can be true. Weyl's criterion fixes `h` before taking `N -> infinity`. This source-exact control prevents an illicit swap of frequency/sample quantifiers. It does not contradict normality of π because `h_N` depends on `N`.

The fixed rational base-16 point `x=1/15` is a separate nonnormal control: `(16^k-1)x` is integral for every k. An abstract van der Corput lag argument cannot force decay on this orbit. This is NOT the anchored BBP orbit.

## 5. Rigorous finite source-selected Fourier certificates (NLG-12)

Nine predeclared selected source windows with lags k=1,2,3 were evaluated. All phases are **exact Fractions** generated by the true BBP recurrence. The unit character angles use a Machin alternating rational enclosure of π; their exact fractions are outward-quantized to a fixed grid, with full angle errors paid; Taylor's theorem supplies independent sine/cosine remainders. The resulting **squared magnitude** intervals are exact rational certificates, reported below as outward seven-decimal-place magnitude brackets.

| Start | Samples | k | mode `16^k-1` | certified magnitude interval |
|---:|---:|---:|---:|---|
| 64 | 64 | 1 | 15 | (0.0945644, 0.0945645) |
| 64 | 64 | 2 | 255 | (0.2014454, 0.2014455) |
| 64 | 64 | 3 | 4095 | (0.0994165, 0.0994166) |
| 128 | 128 | 1 | 15 | (0.0465453, 0.0465454) |
| 128 | 128 | 2 | 255 | (0.0784735, 0.0784736) |
| 128 | 128 | 3 | 4095 | (0.1068723, 0.1068724) |
| 256 | 128 | 1 | 15 | (0.0976589, 0.0976590) |
| 256 | 128 | 2 | 255 | (0.0672271, 0.0672272) |
| 256 | 128 | 3 | 4095 | (0.0605485, 0.0605486) |

These are genuine small source-selected Fourier means, unlike a Haar ensemble. But the first harmonic **rises** between the last two windows, and the third harmonic rises between the first two. No monotonicity or asymptotic saving is inferred from nine points. The exact list and script are retained in `PI_NATURAL_LAG_CRUCIBLE_RECEIPT.json`.

## 6. Full factorial source-observer crucible and holdouts (NLG-13–17)

**Predeclared** training window `64<=n<1024` (960 source states); holdout `1024<=n<2048` (1024); later fresh holdout `2048<=n<3072` (1024). All 3,008 hexadecimal *digit-zero* gates are **certified with the inherited single rational tail upper bound**, without using a supplied decimal digit of π. The gate counts are respectively **56**, **68**, **73**.

Four *actual and synchronized* feature families are read from the SAME anchored rational state:

- **D:** dyadic integral `U_n mod4`;
- **P:** signed one-step Pascal history `(U_n-U_(n-1)) mod8`;
- **L:** `2^(binary-popcount n) mod7`, the Lucas row-support statistic on the **index**, not a fabricated direct residue of U;
- **Q:** combined exceptional odd-prime *negative denominator depths* `v_3(den U_n) mod3` and `v_5(den U_n) mod3` (encoded in nine possible states).

Every one of the **2^4=16** factorial feature subsets is evaluated with a declared Beta(1,15) smoothed empirical conditional predictor of the gate. Thus unknown test feature signatures fall back to probability 1/16, without using future labels in training. All squared/Brier losses and the complete fourth-order mixed contrast are exact rational numbers. This is a finite predictive *diagnostic*, not a proof instrument for infinite digit frequency. Neither training nor time labels are randomly drawn.

| Held-out window | Baseline Brier | Full four-family Brier | Full minus baseline |
|---|---:|---:|---:|
| `1024<=n<2048` | 0.06206053 | 0.06235565 | **+0.00029511** (worse) |
| `2048<=n<3072` | 0.06637302 | 0.06615292 | **−0.00022009** (better) |

The complete factorial four-way contrast switches sign between holdouts, from about `-0.000359337` to `+0.001074740`. **No stable dominance** was observed. Under an explicitly wrong-time-shift mutation of Q (same gate targets), the full held-out error changes. This does not imply a causal prime effect or any theorem about asymptotic π digits.

**Important failed observer shortcut:** the earlier suggestion to use simply `3|den U_n` and `5|den U_n` as features was **uninformative** over these source windows; those Boolean flags are identically true beyond the inspected start. The instrument was repaired to track actual p-adic denominator depth. Using all observers is not equivalent to learning independent useful information from each.

### Probe/calibration receipts

- Three disjoint source windows, no reuse of heldout gate labels when fitting.
- All 16 factorial cells present before claiming an interaction.
- Exact `Fraction` source, exact digit certificates, and exact rational Brier scores; numerical explanatory decimals only.
- Nonnormal constant-gate mutant demonstrates that an arbitrarily large observer bundle has no implication of normality.
- Wrong-time primary feature mutation, parity/residue controls and fixed rational base-16 orbit retained.
- The original `cmath` Fourier experiments are **uncertified diagnostics**; only the independent Machin/Taylor rational brackets above carry finite certificate authority.

## 7. Claim ledger summary, verdict, and next decisive probe

| Claim family | Verdict | Proof debt |
|---|---|---|
| NLG-01–04 sharp authentic two-time lag and summable error | PROVED PAPER + EXACT FINITE | No statement about Fourier cancellation |
| NLG-05 classical signed vdC inequality | CLASSICAL / VERIFIED EXACT FINITE | None within stated domain |
| NLG-06 cyclotomic-mode one-shot criterion | PROVED CONDITIONAL | Uniform **actual source-selected** signed saving (4) is UNVERIFIED |
| NLG-07–10 cyclotomic prime-depth cost | CLASSICAL/PROVED PAPER + FINITE | It only measures visibility, not cancellation |
| NLG-11 finite frequency resonances | PROVED LOCAL | Does not refute fixed-frequency normality |
| NLG-12 nine finite Fourier enclosures | CERTIFIED FINITE | No extrapolation to all N |
| NLG-13–17 factorial/holdout, false shortcut | VERIFIED FINITE / NEGATIVE | No generalization from predictive loss to π frequency |
| NLG-18 pi normality | **OPEN / UNVERIFIED** | Need a source-selected bound, not an exact identity |

**TLICA/source-map view:** κ/contact is exact (all observations read the authenticated N section), σ/source-map adequacy is explicit for dyadic/Pascal/prime and only an index-derived combinatorial map for Lucas, μ/probes are present, φ/candidate pathway has been constructed, ρ/user commitment is a reason for stronger negative controls and blinding, and **discrimination of the actual signed Fourier mean is still absent**. The observation tower can reconstruct a finite digit without certifying its limiting frequency. No collapsed one-number truth score.

### Verdict-changing next move

Constrain the genuine signed sums `W_(k,N,h)` **uniformly for all k<=floor((log_16 N)/2)** by the original four BBP poles, corrected positive Green source, and the actual clock/time coupling (including exceptional 3/5 depths and p7/p13 shared order-3). Seek a nontrivial saving sufficient for (4), or prove a weaker real collision retention under the sibling #271 exact Walsh jet. Use fresh disjoint prime windows, full mixed-term contrasts, no independent-Haar substitution, no fake finite-frequency-uniform estimates, and preserve rejected outcomes. Negative controls: constant/rational periodic source, shifted prime clocks, incorrect initial condition, rational source perturbations from #272, and 2-adic support-vs-residue alias.

**What would change the verdict?** A checked upper bound, from the complete fixed four-pole source and origin 0, of the weighted cyclotomic `W` average in (4) tending to zero for every fixed h. Nothing in the current numerical tables or prime-clock algebra establishes it. Until then, π-normality remains OPEN.
