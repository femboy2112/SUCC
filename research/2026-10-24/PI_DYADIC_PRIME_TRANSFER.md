# π source × dyadic four-gate tomography × all-prime digit transfer

**Operation Prime-Base Interferometry — 2026-10-24.** Research-only branch stacked on [SUCC PR #268](https://github.com/femboy2112/SUCC/pull/268), exact parent 06f6b03eed2521c6bd5c02db618cb421ac6b5a51, coherent main e648df3e4fca73ab6b942232b5ca4b310e9cac08. Carry-rigidity [PR #266](https://github.com/femboy2112/SUCC/pull/266) is an inspected sibling, **not** silently merged. No source archive or main change. No new Lean declarations or academic priority claims.

**Verdict.** The sixteen-branch obstruction admits an exact four-step binary filtration and an exact four-shell signed Fourier formula, both applied to the authentic zero-initial BBP source. The binary-to-any-prime mesh has an exact finite ambiguity count; the corresponding pointwise precision budget at π is eventually finite, using a published irrationality bound. **No asymptotic selected-source Fourier cancellation, four-gate retention theorem, π-normality proof, or π-specific independence theorem is claimed.**

## DPT-01 — identify the three distinct carriers (PROVED distinction)

The following are **not interchangeable**:

1. Circle dynamics: multiplication by 16 mod 1; a hexadecimal digit contains exactly four binary digits. The base-16 and base-2 normality properties are classically equivalent because their bases are multiplicatively dependent.
2. Adic digit coding: the inverse limits of integers modulo 16^n and 2^n are the same topological ring, Z_2. This reflects their cofinal filtrations, not an assertion that the digit shift is multiplication by 2 on Z_2.
3. BBP rational torsion: the p-primary projection of a rational phase in Q/Z used in the SUCC prime-clock analysis. It is neither the actual base-p fractional expansion nor the adic integer from (2).

The authentic source is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
$$

Exact regrouping gives

$$
r(n)=\frac4{8n-7}-\frac1{8n-3}
-\frac{3n-1}{(2n-1)(4n-1)}.
$$

All reduced denominators on the right are odd. Induction proves every rational y_n has odd denominator: hence the *2-primary torsion projection* of y_n is **zero at every n**. This does **not** make the dyadic fractional digits of y_n trivial. The useful 2-adic datum below is instead an integer **centered carry**.

For p≠q, every continuous additive group homomorphism Z_p→Z_q is zero, because its image is both pro-p and pro-q. A nonlinear, measurable, usually discontinuous cross-base symbolic decoder is possible; see DPT-02.

## DPT-02 — exact binary/prime-base finite-grid transfer (PROVED, elementary)

For any integer b≥2, digit depth n≥1, let q=b^n and H=2^k≥q. The q base-b cylinder cells on [0,1) have boundaries a/q. A binary k-cylinder crosses a target boundary exactly when that boundary does not align with an H-grid line. Since H≥q, distinct interior target boundaries occupy distinct binary cells.

There are q−1 target boundaries. Exactly gcd(q,H)−1 align: divisibility q|aH has gcd(q,H)−1 solutions for 1≤a<q. Thus the number of ambiguous binary cylinders and their Haar measure are **exactly**

$$
\boxed{B(b,n,k)=q-\gcd(q,2^k)},\qquad
\boxed{\lambda(\mathrm{bad})=\frac{q-\gcd(q,2^k)}{2^k}}.
$$

If k=ceil(log_2(q))+s, the exceptional Haar measure is at most 2^{-s}. For b=16 and k≥4n, ambiguity is **zero**. For every odd prime p, B(p,n,k)=p^n−1; the grid boundaries never align with a finite dyadic grid.

The exact fail-closed decoder from a dyadic prefix j computes the first and last possible target cells,

$$
L=\left\lfloor \frac{qj}{H}\right\rfloor,\qquad
R=\left\lfloor \frac{q(j+1)-1}{H}\right\rfloor,
$$

and returns L only when L=R. The integer implementation has explicit endpoint and domain checks; neither floating arithmetic nor a randomness assertion is needed.

**Nonuniformity receipt:** For any odd p and any finite k, the boundary 1/p lies strictly inside one binary k-cylinder. Construct two rational phases on opposite sides of 1/p inside that same cylinder: they have identical k-bit binary prefixes but different first base-p digits. Consequently NO finite worst-case universal binary-prefix delay exists for all real points.

**Almost-everywhere all-prime result:** Set

$$
k(p,n)=\lceil n\log_2 p\rceil+
2\lceil\log_2n\rceil+2\lceil\log_2p\rceil+c.
$$

The exceptional Haar mass is at most 2^{-c}n^{-2}p^{-2}. Summation over all primes p and depths n is finite, and Borel–Cantelli gives eventual simultaneous prefix-decodability for almost every real. This **cannot** be applied to π merely because almost all real numbers satisfy it.

**Source-specific π corollary (classical dependency):** Zeilberger and Zudilin proved μ(π)<7.104; hence exponent 8 gives, for all sufficiently large q and all integer a,

$$
|\pi-a/q|>q^{-8}.
$$

For q=p^n sufficiently large, the first

$$
\boxed{k=\lceil 8n\log_2 p\rceil+1}
$$

binary fractional digits of π uniquely determine its first n base-p fractional digits: a binary cylinder of width less than q^{-8} containing π cannot cross any rational a/q boundary. The published theorem does not supply a small explicit qualifying threshold here. An independently computed Machin rational interval certifies concrete small digit prefixes in the attached finite receipt.

**Boundary:** this is a theorem about decoding *precision*, not Birkhoff genericity. Schmidt and Becher–Slaman construct numbers normal in base 2 and nonnormal in base 3; changing finite observational bases cannot infer statistical normality in multiplicatively independent bases.

## DPT-03 — four exact binary gates in authentic BBP pair carries (PROVED identity)

Following PR #268, take a source prime p=8m+1 with the source windows

$$
A=m+1,\quad B=4m,\quad
W=\{A,\ldots,B-1\},\quad W^+=\{A+1,\ldots,B\},
\quad d=3m-1.
$$

For ordered pairs (s,t)∈W² write

$$
\delta_{s,t}=\operatorname{cen}(y_t-y_s),\quad
\delta^+_{s,t}=\operatorname{cen}(y_{t+1}-y_{s+1}),\quad
\eta_{s,t}=r(t+1)-r(s+1),
$$

where cen maps each circle phase into [-1/2,1/2). Source monotonicity gives

$$
|\eta_{s,t}|\le\epsilon_p:=r(A+1)-r(B)
<\frac{15}{(p+8)(p+9)}.
$$

Define the **centered integer carry**, with BOTH true source forcing and centering retained,

$$
\boxed{\kappa_{s,t}
=16\delta_{s,t}+\eta_{s,t}-\delta^+_{s,t}\in\mathbb Z.}
$$

This is generally **not** the difference of literal source carries (#266 has exact counterexamples).

For ε_p<τ≤1/4, set

$$
E_\tau=\{(s,t)\in W^2:|\delta^+_{s,t}|\le\tau\}.
$$

Integrality and |κ|<8.5 imply κ∈[-8,8] on E_τ. Moreover the event κ≡0 (mod 16) is exactly κ=0 and exactly |δ|≤1/32: if κ=0 then |δ|≤(τ+ε_p)/16<1/32; conversely |δ|≤1/32 implies |κ|<1 and hence κ=0. Therefore this is the **same zero inverse branch** Z_W(τ) defined in TWA-15, not a new substituted target.

Define the nested conditional binary gates:

$$
\boxed{Q_j(p,\tau)=\#\{(s,t)\in E_\tau:
\kappa_{s,t}\equiv0\pmod{2^j}\}},\quad j=0,1,2,3,4.
$$

Then Q_0=Q_{W^+}(τ), Q_4=Z_W(τ), and Q_0≥Q_1≥Q_2≥Q_3≥Q_4. When all denominators are nonzero,

$$
\frac{Z_W(\tau)}{Q_{W^+}(\tau)}
=\prod_{j=1}^4\frac{Q_j}{Q_{j-1}}.
$$

There are **exactly four successive binary retention decisions** in the 16-way carry. Alternatively 4²=16 is the two-stage subfiltration Q_0→Q_2→Q_4. The numerical factorization is exact; equidistribution of each *conditional* decision is a separate, unproved arithmetic question.

## DPT-04 — exact 1/16 criterion from four conditional halves (PROVED CONDITIONAL; hypotheses UNVERIFIED)

Assume there exist constants c_1,…,c_4≥0, uniform across sufficiently large good primes and ALL of TWA-15's prescribed shrinking inverse-branch scales, with

$$
\boxed{Q_j(p,\tau)\le\frac12Q_{j-1}(p,\tau)+c_jd}
\qquad(j=1,2,3,4).
$$

Iterating the four inequalities gives

$$
\boxed{Z_W(\tau)\le\frac1{16}Q_{W^+}(\tau)
+d\left(\frac{c_1}{8}+\frac{c_2}{4}+
\frac{c_3}{2}+c_4\right).}
$$

This supplies θ=1/16 with an allowed uniform linear additive budget in PR #268's rigorously derived scale recursion. Therefore the inherited selected-source collision bound K_p(1)=O(1) would follow, implying normality of π in base 16 and thus base 2 by the already-established SCE dense-window-to-prefix theorem.

**No four-gate uniform hypothesis has been proved.** The additive O(d) cannot be arbitrarily removed: the d diagonal ordered pairs always survive every gate. The conditional proof is not a normality proof and is stronger than rate-free normality of a generic real. If only one, two or three conditional gates were established, the best corresponding branch fractions 1/2, 1/4, 1/8 would give first polynomial savings but not the SUCC normality target.

## DPT-05 — four genuine primitive signed cyclotomic shells (PROVED exact identity)

Define e(x)=exp(2πix) and the Ramanujan sum for a primitive power-of-two character shell:

$$
c_{2^j}(k)=\sum_{\substack{1\le a\le 2^j\\a\ {\rm odd}}}
e(ak/2^j)
=\begin{cases}
2^{j-1},&2^j\mid k,\\
-2^{j-1},&2^{j-1}\mid k,\quad 2^j\nmid k,\\
0,&\text{otherwise}.
\end{cases}
$$

For the **actual selected** pair set, define the SIGNED shell correlation S_j(p,τ)=Σ_{E_τ}c_{2^j}(κ). Root-of-unity orthogonality gives

$$
\boxed{16Z_W(\tau)=Q_{W^+}(\tau)+
S_1(p,\tau)+S_2(p,\tau)+S_3(p,\tau)+S_4(p,\tau).}
$$

The required source-specific estimate could be **one total signed bound**

$$
\sum_{j=1}^4S_j(p,\tau)\le Cd
$$

uniformly across good primes and all required shrinking scales. Individual shell O(d) estimates would be a stronger alternative. This is not a positivity theorem; signs are essential, and dropping them creates fake cancellation or fake lower bounds.

The exact transported character, with the BBP forcing and actual selected source retained, is

$$
\boxed{e(h\kappa_{s,t}/16)
=e\left(h\delta_{s,t}+
\frac h{16}(\eta_{s,t}-\delta^+_{s,t})\right).}
$$

This is a declared common-basis phase relation suitable for a source-specific bilinear incidence probe. It is an **identity**, not a bound on a sum. At p=97 and τ=1/16, the first signed shell is actually **negative** (S_1=-7), refuting any assumed nonnegative-shell invariant.

## DPT-06 — why primes 3,5,…,13 cannot independently close 1/16 (PROVED obstruction)

The unit group (Z/16Z)×, including multiplications by 3,5,7,11,13, preserves each 2-adic valuation class. Its orbits on carry residues are

$$
\{0\},\quad\{8\},\quad\{4,12\},\quad
\{2,6,10,14\},\quad
\{1,3,5,7,9,11,13,15\}.
$$

An invariant probability distribution may place **all mass at 0**. Therefore even exact invariance under every odd unit does NOT imply central-branch mass 1/16. A point-mass-at-zero mutant is included in the tests.

On Z_2, ×16 is a strict contraction; on Z_p for odd p, it is an isometry, and on the real circle T_16 expands. Transporting a contraction claim between these spaces would be false. The orders of 16 modulo odd primes below 16 are ord_3=1, ord_5=1, ord_7=3, ord_11=5, ord_13=3. None of these primes is 1 mod 8; the smallest prime in the first BBP p=8m+1 family is 17. Base 3 may be a **separate coprime gain** to eliminate aliasing (TWA-07 proves sharp gains 2 and 3), but not a source-authenticated proof of conditional carry equidistribution.

## DPT-07 — exact finite receipts (VERIFIED FINITE; not asymptotic)

Files:

- observational_succ/pi_dyadic_prime_transfer.py — pure integer/Fraction source, mesh decoder, centered carry and exact primitive-shell calculator.
- tests/test_pi_dyadic_prime_transfer.py — 9 focused adversarial unittest methods.
- scripts/pi_dyadic_prime_transfer_probe.py — independent rational Machin interval source for selected finite π-digit prefixes, deterministic JSON generator.
- research/2026-10-24/PI_DYADIC_PRIME_TRANSFER_RECEIPT.json — full exact, hashed selected-source rows, boundary measures and π prefix decodings.

Selected authentic rows at successor τ=1/4:

| p | d | Q0 | Q1 | Q2 | Q3 | Q4=Z | signed shell vector (S1,S2,S3,S4) |
|---:|---:|---:|---:|---:|---:|---:|---|
| 41 | 14 | 96 | 60 | 36 | 32 | 26 | (24,24,112,160) |
| 97 | 35 | 645 | 331 | 191 | 119 | 83 | (17,102,188,376) |
| 257 | 95 | 4513 | 2287 | 1175 | 609 | 333 | (61,126,172,456) |

Every row passes 16 Q4=Q0+ΣS_j **exactly**. Off-resonant mutations include omitted signed shell, boundary-crossing fractional codes and an invariant δ_0 carry law. At base3 with n=3,k=9, exactly 26 of 512 binary cells are ambiguous; for base5 with n=3,k=11, 124 of 2048; base16 at k=4n has zero. An independently computed exact Machin interval for π has width <2^-300 and certifies **28** finite prefix conversions for b=2,3,5,7,11,13,16 and n=1,2,4,8. The first 8 ternary fractional digits of π are certified by 17 binary fractional digits, versus the information-theoretic 13-bit floor. No π digit file or floating sign decision is used.

Local 9/9 focused tests, finite JSON byte-for-byte replay, and strict compileall passed in an isolated pure-Python reconstruction; the receipt includes SHA256 hashes of all three Python files. **A full repository suite and GitHub hosted CI on this new branch have NOT been run or claimed.** The code and exact receipt are accessible for fresh checkout reproduction:

    python -m unittest discover -s tests -p 'test_pi_dyadic_prime_transfer.py' -v
    python scripts/pi_dyadic_prime_transfer_probe.py --output /tmp/dyadic.json
    cmp /tmp/dyadic.json research/2026-10-24/PI_DYADIC_PRIME_TRANSFER_RECEIPT.json

## Verdict and next falsification opportunity

| Claim | Status | Proof debt |
|---|---|---|
| DPT-01: distinct source carriers and odd-denominator BBP law | DISCLOSED, exact | none for stated scope |
| DPT-02: finite cross-base mesh and eventual π coding | DISCLOSED elementary + published irrationality input | no selected frequency estimate |
| DPT-03: four nested BBP carry gates | DISCLOSED, exact | none for decomposition |
| DPT-04: four half-retentions imply π hexadecimal/binary normality | PROVED CONDITIONAL | every selected-source half-retention remains UNVERIFIED |
| DPT-05: four signed Ramanujan shells | DISCLOSED, exact | signed source sum bound UNVERIFIED |
| DPT-06: small-prime unit symmetries insufficient | DISCLOSED exact mutant | other nonunit, source-authenticated probes open |
| DPT-07: 9 tests, 28 selected finite π digit-prefix readouts | VERIFIED FINITE | no infinite extrapolation |

**Highest-leverage next theorem:** with actual y_0=0, forcing, every carry, and the chosen π embedding fixed, prove either each Q_j−Q_{j−1}/2≤c_j d on every required inverse-branch scale, or their equivalent weaker total signed-shell excess ΣS_j≤Cd. A result holding only for Galois averages, only for one/two steps, or for the wrong initial selector cannot discharge the proof.

Try source-selected bilinear twisted sums on the exact transported characters, primitive dyadic Ramanujan filters, and independent interval holdouts at unseen good primes. Re-run the changed-initial-state counterfeit from #266 and wire-label/coprime-gain controls from #268. Test whether the source produces *conditional* carry bit estimates rather than apparent marginal fairness. A genuine source-specific bound is the remaining lamp.

**Primary external sources:** Bailey–Borwein–Plouffe, original digit-extraction identity, https://www.davidhbailey.com/dhbpapers/digits.pdf; Zeilberger–Zudilin, *The Irrationality Measure of Pi is at most 7.103205334137...*, Moscow J. Comb. Number Th. (2020), https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html; Becher–Slaman, *On the Normality of Numbers in Different Bases* (2014), https://doi.org/10.1112/jlms/jdu035. No new academic novelty claim.
