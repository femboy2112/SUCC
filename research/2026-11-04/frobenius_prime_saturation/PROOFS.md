# Operation Prime–Frobenius Echo — source-selected BBP self-shadow and sharp denominator saturation

**2026-11-04. Research draft, exact/paper proofs, not a published-priority assertion or proof of π normality.**

**Pinned starting point:** SUCC draft #496 `a0a2619578a88182c73420901c99994699eb2024`. Preregistration committed first at `ba185173edd60e57148c930e0fd95041fd4bf11e`; the first small universal constants were discovered in developmental exploration **before** preregistration, and are not disguised as blinded tests. `main`, root source, archives, historical claim contracts, formal Lean and workflows are unchanged.

**AUTHENTIC ORIGINAL four-pole source:**

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n),\quad n\ge1.
\]

For rational `x`, `den(x)` is its *reduced positive denominator*; `v_p` is ordinary p-adic valuation. The `×16` source time `n` is NOT the generating-function coefficient index in the different four-dimensional BBP transfer.

## PF-01. Genuine p-pole birth passport (ALL source times in the stated simple-pole regime)

Fix an odd prime `p>5` and horizon `N>=1` with `p²>8N`. All original denominators at source times `j<=N` are less than `p²`, and their four offsets `c=7,4,3,2` are pairwise distinct by at most five. Hence at each `j` at most one of the four original terms can have a p-pole, of valuation exactly `-1` (there are no p² poles). The source-pole event is determined by

\[
 (m,c,w),\quad 8j-c=mp,\quad j=(mp+c)/8\in\mathbb N,\quad
 (c,w)\in\{(7,4),(4,-2),(3,-1),(2,-1)\},\quad p\nmid m.
\]

Between events, `pU_j` multiplies by `16 mod p`; at event `(m,c,w)` it receives exactly `w/m mod p`. All other original terms have p-integral denominators and contribute **zero** after multiplying by `p`. The literal zero seed gives the unique initial `pU_0=0`.

The possible event sequences for `p≡a (mod8)` are periodic with period `m↦m+8`:

| a | Events (m,c,w) within one m-octave | χ₂(p)=(2/p) |
|---|---|---|
| 1 | (1,7,4), (4,4,−2), (5,3,−1), (6,2,−1) | +1 |
| 3 | (2,2,−1), (3,7,4), (4,4,−2), (7,3,−1) | −1 |
| 5 | (1,3,−1), (4,4,−2), (5,7,4), (6,2,−1) | −1 |
| 7 | (2,2,−1), (3,3,−1), (4,4,−2), (7,7,4) | +1 |

Small primes 2,3,5, p² poles and source mutations are **not** included in the claimed simple-pole theorem. Their exclusion is necessary.

## PF-02. The prime-independent rational Frobenius pulse factor (ALL m, all p satisfying the source passport)

Let two successive source p-events have `(m_i,c_i,w_i)` and `(m_j,c_j,w_j)` at source times `t_i,t_j`. Euler's criterion and Fermat's congruence give

\[
\begin{aligned}
16^{t_j-t_i}&=2^{4(t_j-t_i)}
=2^{(m_j-m_i)(p-1)/2}\;2^{(m_j-m_i+c_j-c_i)/2}\\
&\equiv \chi_2(p)^{m_j-m_i}
\;2^{(m_j-m_i+c_j-c_i)/2}\pmod p.
\end{aligned}
\]

The final exponent is an INTEGER because both event times exist. Negative exponents mean inverses of 2, valid modulo every odd p. The factor depends on `p` only through its class mod 8. Thus define an **ordinary rational** universal normalizer `C_a(m)` at each event:

\[
 C_a(m_j)=f_a(m_i,m_j)\,C_a(m_i)+w_j/m_j,
\qquad C_a(m_\mathrm{first})=w_\mathrm{first}/m_\mathrm{first},
\]

with `f_a=χ₂(a)^(m_j-m_i) 2^((m_j-m_i+c_j-c_i)/2)`. These are computed in exact `Q`, not fitted by modular interpolation. At the last p-event m before source time N, at time `t=(mp+c)/8`, the actual original source satisfies

\[
\boxed{pU_N\equiv16^{N-t}C_a(m)\pmod p,}\tag{PF-1}
\]

provided denominators in the displayed rationals are p-units (automatic when `p>m`) and `p²>8N`. This is genuine selected original p-primary information, not a Galois-averaged character.

**FIRST exact normalizers (development observations; certified generally by the recurrence):**

```
a=1:    4,       7/2,       33/10,    47/15
a=3:   -1/2,   16/3,    -19/6,     130/21
a=5:   -1,     7/2,    -66/5,     47/15
a=7:   -1/2,   -4/3,   -19/6,    -520/21
```

The last normalizers already contain the source's original `U_1=r(1)=47/15` and a second `V_1=130/21`, with a relative unit factor `-4`.

## PF-03. **Prime-Frobenius self-shadow and dual-shadow theorem (ALL octaves)**

Define a SECOND exact four-pole recurrence

\[
 V_0=0,\qquad V_n=16V_{n-1}+r^\sharp(n),\qquad
 r^\sharp(n)=\frac8{8n-6}+\frac4{8n-5}+\frac4{8n-4}-\frac1{8n-1}.
\]

At the completion of the `k`-th octave of p-poles (`k>=1`), the universal rational normalizer is **EXACTLY**

\[
\boxed{
 C_1(8k-2)=C_5(8k-2)=U_k,\quad
 C_3(8k-1)=V_k,\quad
 C_7(8k-1)=-4V_k.
}\tag{PF-2}
\]

**Proof at every k, not finite pattern fitting.** In classes 1 and 5, the consecutive-pole transfer factors between successive events are, respectively,

- a=1: `1,1,1,16` cyclically;
- a=5: `−4,−4,−1/4,−4` cyclically.

Both have four-event full-cycle product `16`. Passing from the completed `(8k-2)` normalizer to `(8(k+1)-2)`, the **new pulse injections** combine to

`4/(8k+1)−2/(8k+4)−1/(8k+5)−1/(8k+6)=r(k+1)`.

Since both initial completed values are `47/15=r(1)`, the same exact zero-seeded recurrence implies the first two identities for all k. In classes 3 and 7, the consecutive factors are

- a=3: `−8,−1/2,−2,−2` cyclically;
- a=7: `2,2,8,1/2` cyclically.

Their products are `16`, and full-cycle injections combine to respectively

`r^sharp(k+1)` and `−4r^sharp(k+1)`.

The starting completed values `130/21` and `−520/21=−4·130/21` give the remaining identities. Every full-cycle symbolic factor and source function is independently checked for variable k in `symbolic_oracle.py` (rather than finite k only).

**IMPORTANT type:** the congruence (PF-1) transports each universal rational state to a finite-field **selected residue** for sufficiently large p. It does not identify the real selected phase `U_N mod1` with a uniform distribution or generate independent p-orbits.

## PF-04. Strict all-octave sign/nonzero certificate (ALL m, proven without p tests)

The only remaining point needed for survival is that **no rational `C_a(m)` is exactly zero**. We prove it by a uniform induction over 8-shells; the denominators `8k+j` increase with k, making the first octave extremal.

| a | Start-of-octave invariant | Ordered four event signs | Inductive endpoint bound |
|---|---|---|---|
| 1 | `C_(8k+1)>=4` | + + + + | last `>=47/15>0`; next first `>=16·47/15>4` |
| 3 | `C_(8k+2)<=−1/2` | − + − + | second `>=4`; third `<=−2`; last `>=27/7>0`; next first `<=−54/7` |
| 5 | `C_(8k+1)<=−1` | − + − + | second `>=7/2`; third `<=−66/5`; last `>=47/15`; next first `<=−188/15` |
| 7 | `C_(8k+2)<=−1/2` | − − − − | second `<=−1`; third `<=−2`; last `<=−16+4/7=−108/7`; next first `<=−54/7` |

For example at a=5, a negative first state is multiplied by `−4` and receives `−2/(8k+4)`, leaving at least `7/2`. The next transfer is `−4` and receives `+4/(8k+5)`, leaving at most `−66/5`. The transfer `−1/4` with injection `−1/(8k+6)` then leaves at least `47/15`. Finally multiplication by `−4` and a negative next first injection restores the negative start invariant. All four other rows follow by the displayed exact factors, and the base k=0 cases are the first four normalizers in PF-02.

Therefore

\[
\boxed{\operatorname{sgn}C_a(m)\text{ is prescribed by }(a,m\bmod8),
\quad C_a(m)\ne0\quad\text{for EVERY admissible pulse }m.}\tag{PF-3}
\]

This is a universal arithmetic theorem. Finite signs through 100 octaves are tests only and not used in the proof.

## PF-05. **Sharp denominator saturation theorem (THE MAIN NEW RESULT)**

Let

\[
D_N=\operatorname{den}(U_N),\qquad
M_N=\operatorname{lcm}_{1\le j\le N}\operatorname{den}(r(j)).
\]

Obviously `D_N|M_N`, because the zero-seeded recurrence is an INTEGER linear combination of the original inputs; conversely every source denominator is cleared by `M_N`. The two logarithmic sizes need not match a priori, because p-primary contributions could cancel during recurrence.

**Quantified survival statement.** Fix any real `eps>0` (it suffices `0<eps<1`). Let `B=ceil(8/eps)+8`. There are only finitely many ordinary rational normalizers `C_a(m)` with `m<=B`. Every one is nonzero by PF-04. Let `P_eps` exceed ALL primes dividing the numerators or denominators of this finite family, and all pulse indices <=B. For sufficiently large N, any prime p>eps*N in the original genuine generic source support satisfies `p>P_eps`, `p²>8N` and has at most B p-events. At its last event the universal normalizer is a p-unit; (PF-1) yields `v_p(U_N)=-1`.

Thus **for every fixed eps**, and ALL sufficiently large N,

\[
\boxed{\begin{gathered}
 p>\varepsilon N,\ p>5,\ p\equiv1\ (4),\ p\le8N-O(1)\quad\Longrightarrow\quad v_p(U_N)=-1,\\
 p>\varepsilon N,\ p>5,\ p\equiv3\ (4),\ p\le4N-O(1)\quad\Longrightarrow\quad v_p(U_N)=-1.
\end{gathered}}\tag{PF-4}
\]

The `O(1)` endpoints stand for exact first-birth conditions: p≡1mod8: `(p+7)/8<=N`; p≡5mod8: `(p+3)/8<=N`; p≡3mod4: `(p+1)/4<=N`. No explicit N_eps is asserted, and the theorem does **not** say all smaller primes survive at every finite N.

**Compute the sharp constant.** The generic p support of the original four-pole forcing through N is precisely (up to the fixed exceptional primes) all p≡1mod4 up to 8N with exact endpoints as above, and all p≡3mod4 up to 4N. Higher prime powers contribute at most `O(sqrt(N) log N)` to `log M_N`, because every denominator is <=8N, so repeated powers require p<=sqrt(8N). The classical fixed-modulus prime number theorem in arithmetic progressions gives

\[
\log M_N=\theta(8N;4,1)+\theta(4N;4,3)+o(N)=4N+2N+o(N)=6N+o(N).
\]

By PF-04, for every fixed eps the surviving primes alone give

\[
\log D_N\ge\big[(8-\varepsilon)/2+(4-\varepsilon)/2\big]N+o_\varepsilon(N)
=(6-\varepsilon)N+o_\varepsilon(N).
\]

Let eps→0 after taking liminf. With `D_N|M_N` this proves the **sharp all-N asymptotic**

\[
\boxed{\log\operatorname{den}(U_N)=(6+o(1))N,\qquad
\log\frac{M_N}{\operatorname{den}(U_N)}=o(N).}\tag{PF-5}
\]

This is genuinely for the ONE original selected rational state at each N; it does not use digit randomness, averaging over prime automorphisms, or a false source. It improves main's pre-existing `>=3N+o(N)` certificate (#459) to the sharp matching upper bound.

**Consequence for the ORIGINAL finite BBP truncation.** Let `alpha_N=U_N/16^N`. The inherited original 2-adic isometry proves `v₂(U_N)=v₂(N)` (and its denominator is odd). Therefore

\[
\log\operatorname{den}(\alpha_N)=(6+\log16+o(1))N.
\]

This is arithmetic size, **not** a lower bound on real-circle spacing or signed Weyl cancellation; the centered Archimedean numerator remains uncontrolled.

**Finite exception control:** at the held-out N=509, p=113 and p=151 legitimately cancel from the reduced denominator; similarly N=128,p=37 and N=257,p=47. The theorem explicitly allows these at fixed N. A naive assertion of `D_N=M_N` for every N or every prime is REFUTED.

## PF-06. The dual shadow is a SECOND BBP formula for π and an exact zero-integral Gamma channel

The second rational source `r^sharp` above is a classical alternative BBP-type digit-extraction formula for π (see MathWorld, BBP-Type Formula, displayed formula (3)). In the original BBP eight-shell integral variables, put

\[
P(t)=4-2t^3-t^4-t^5,\qquad P^\sharp(t)=8t+4t^2+4t^3-t^6,\\
F(t)=\frac{2-t^2}{(t-1)^2+1}.
\]

An exact **rational polynomial identity**, checked symbolically, is

\[
\boxed{\frac{P^\sharp(t)-2P(t)}{1-t^8/16}
=-8\frac{d}{dt}\log F(t).}\tag{PF-6}
\]

Since `F(0)=F(1)=1` and F>0 on [0,1], integration gives

\[
\sum_{k\ge0}16^{-k}r^\sharp(k+1)=2\sum_{k\ge0}16^{-k}r(k+1)=2\pi.
\]

Equivalently `sum_(n>=1)16^(-n)r^sharp(n)=pi/8`. So the two source recurrences in PF-03 encode the **same completed circle angle** after a signed radial/logarithmic null contribution; the relation is NOT a fitted identity and uses no π digits. The second identity itself is CLASSICAL; its forced appearance in the p-primary Frobenius reduction is the source-specific new-to-repo part.

Let `d(n)=r^sharp(n)-2r(n)` and `Delta_N=V_N-2U_N`. The exact source bounds imply `d(1)=-8/105` and `d(n)>0` for every n>=2: for n>=2, the genuine original `r(n)<15/[(8n-7)(8n-6)]<1/(2n)`, while `r^sharp(n)>8/(8n-6)>1/n`. From the EXACT ZERO completed value in (PF-6),

\[
\boxed{\Delta_N=-\sum_{j\ge1}16^{-j}d(N+j)<0\quad(N\ge1).}\tag{PF-7}
\]

Thus the finite radial mismatch is never zero at any positive stage even though the completed source difference is exactly zero. Its genuine asymptotic expansion is

\[
\boxed{\Delta_N=-\frac1{8N}+\frac5{64N^2}+O(N^{-3}).}\tag{PF-8}
\]

Proof: `d(s)=15/(8s)+53/(64s²)+O(s^-3)` and `sum 16^-j=1/15`, `sum j16^-j=16/225`. This is a **source-native harmonic/oily remainder**.

A stronger UNIFORM all-n sign/size bound is also valid:

\[\boxed{0<2U_N-V_N<\frac1{8N+4}<\frac1{8N}\qquad(N\ge1).}\tag{PF-8b}\]

To see this, clear the strictly positive denominator of the rational function

`15/[8(s−1/2)]−d(s)`, for real s>=2. Its numerator is exactly

`57344(s−2)^5+465920(s−2)^4+1510528(s−2)^3+2443984(s−2)^2+1974096(s−2)+636885`,

and its denominator is `4(2s−1)(4s−3)(4s−1)(8s−7)(8s−5)(8s−3)(8s−1)`; all factors are positive. Therefore `0<d(s)<15/[8(s−1/2)]` for real s>=2. Every term in PF-7 has `s=N+j>=2`, so its weighted sum is smaller than `[(15/8)/15]/(N+1/2)=1/(8N+4)`. This is a FULL original-source bound, not an eventual asymptotic.

A direct *selected Fourier bridge* follows:

\[\left|\sum_{n=1}^N e(hV_n)-\sum_{n=1}^N e(2hU_n)\right|
\le2\pi|h|\sum_{n=1}^N(2U_n-V_n)
<\frac{\pi|h|}{4}H_N,\quad H_N=\sum_{n\le N}\frac1n.\]

This is an `O_h(logN)` unnormalized comparator, not proof that either sum cancels. Since the corrected `Delta_n+1/(8n)=O(n^-2)` is summable, there is a genuine source-specific constant

\[
C_\mathrm{Frob}=\sum_{n\ge1}\left(\Delta_n+\frac1{8n}\right),
\qquad
\boxed{\sum_{n\le N}\Delta_n
=-\frac{\log N+\gamma}{8}+C_\mathrm{Frob}+O(N^{-1}).}\tag{PF-9}
\]

Here γ is the classical Euler–Mascheroni constant, not the Lorentz factor. The radial/Gamma channel is an exact finite-to-analytic normalization, but it does **NOT** make the original selected Fourier characters equidistributed. The two BBP signed source orbits obey `e(hV_n)=e(2hU_n)+O_h(1/n)` and normalized all-prefix character sums differ by `O_h(log N/N)`; neither sum is proved to vanish.

## PF-07. Provenance, tests, novelty boundary, next falsification

- **Classical inputs:** Euler's criterion/Fermat's theorem, fixed-modulus PNT-AP, standard BBP and alternative formula, ordinary analytic asymptotics. References include NIST DLMF §27.9, Kontorovich et al. formal PNT-AP blueprint, MathWorld's BBP-Type Formula, Lagarias (2001) for why source recurrence alone does not prove normality.
- **New-to-SUCC paper-proved composition:** universal selected p-primary rational Frobenius pulse, exact original/dual BBP source reproduction for all shells, nonzero sign certificate for all source pulses, and sharp denominator saturation `log den(U_N)~6N`. These are not stated as verified global academic first discoveries; a dedicated external scholarly priority review is still required.
- **Tests:** two independent arithmetic representations (full Fraction recurrence and integer common-LCM recurrence), direct source-pole p-local oracle independent of `C_a` and Fermat factor, independent SymPy source symbolic identities, preregistered N=128/257/509/911/1511 and class-specific m sweeps. Finite tests do NOT prove PNT-AP or the universal sign induction.
- **Hostile controls:** wrong radix 4, wrong first pole coefficient, changed p-denominator seed, incorrect χ₂ sign, legitimate finite p cancellation exceptions, p² source-pole exclusion, and the earlier coherent wrong-real-seed / p-free cofactor locking. No nonzero real-circle distance or new Weyl cancellation follows.
- **Next verdict-changing probe:** use the forced original/dual p shadows and Gamma-null gauge to derive a **selected real** bound on the centered numerator / branch-current energy, with a source-specific obstruction for coherent cofactor mutants. Saturating the denominator is an authentic theorem but not yet a selected Archimedean numerator inequality.

**Claim ledger:** PF-01..05 DISCLOSED paper, conditional on classical fixed-modulus PNT-AP; PF-06 first exact π identity CLASSICAL, source-matched null and finite signed correction DISCLOSED; PF-07 heldouts OBSERVED, novelty priority UNVERIFIED; π base16 normality, original `J=o(K)` and RH remain OPEN.
