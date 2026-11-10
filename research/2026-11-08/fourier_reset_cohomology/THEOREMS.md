# Spectral returns, cyclotomic reset ranks, and de Bruijn source-current renormalization

**SUCC research, 2026-11-08.** Parent: draft #557 at `b52f9affcac8be85f532fbe4e667e7ac01159b30`. **π normality: OPEN.** All algebraic statements are for an explicitly specified finite hexadecimal word, unless labeled IID-REFERENCE. Classical BBP source identification is inherited, not changed or proved anew. Scientific and scholarly priority unverified.

## 0. Three noninterchangeable objects

1. The *original selected source*: `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U0=0`, `Un=16 U(n−1)+r(n)` with the true future Green tail. Classical BBP identifies `Un+Tn=16^(n−1)π`. The parent #557 certifies a particular **finite** 16,384-digit prefix using rational tail brackets, without inserting digits as proof premises.
2. The *digit-character path*: for the inherited certified hexadecimal digits `d_n∈{0,..,15}`, set `S_N(h)=Σ_{n=1}^N exp(2πi h d_n/16)`. This is not the still-open continuous-real-phase Weyl sum `Σ exp(2πi h U_n)` of #544. A zero of `S_N(h)` alone is not π-normality.
3. The *finite cyclic k-word law*: given the **first N digits**, count all N periodized length-k windows, with wraparound used only to make exact finite marginals. Define `E_k(N)=16^k Σ_w(p_{k,N}(w)-16^{-k})²`. The cyclic convention differs from real noncyclic prefix counts at up to k−1 boundary windows, giving an O(k/N) comparison for each fixed k. Distinguish change of *time N* from increase of *resolution k*.

## FRH-01: exact cyclotomic reset theorem — PROVED (integer algebra)

For every divisor `m=2,4,8,16` of 16, write `C_r^(m)(N)=#{n≤N:d_n≡r (mod m)}` and

`D_r^(m)(N)=C_r^(m)(N)-C_(r+m/2)^(m)(N)`, for `0≤r<m/2`.

Fix an integer `h` of additive-character **order** `m=16/gcd(16,h)`. Group terms by residues modulo m; the digit character is a primitive m-th root ζ raised to the corresponding residue. Then

`S_N(h)=Σ_(r<m/2) D_r^(m)(N) ζ^r` (up to replacing ζ by another primitive m-th root). Since `Φ_m(X)=X^(m/2)+1` is the minimal polynomial of a primitive power-of-two root of unity and the polynomial degree of that expression is <m/2,

**`S_N(h)=0` iff `D_r^(m)(N)=0` for ALL r.**

The four reset ranks are **1,2,4,8**; the last is eight independent real integer conditions, not eight independent random physical channels. Primitive characters of the same m vanish simultaneously because they are cyclotomic Galois conjugates.

`E_1(N)=0` iff **all sixteen symbol counts equal `N/16`**, necessarily with `16|N`. No individual spectral zero implies this.

## FRH-02: reference random-walk recurrence and rarity of full resets — CLASSICAL/PAPER

**Explicitly hypothetical reference**: digits are independent and uniform on 0,…,15. Then the vector `D^(m)` increments in one of the m signed coordinate directions `±e_r`, each probability 1/m; it is the simple symmetric walk on `Z^(m/2)`.

By the classical Pólya/Chung–Fuchs recurrence theorem, the dimensions 1 and 2 return to zero infinitely often almost surely, whereas dimensions 4 and 8 have only finitely many returns almost surely. This theorem is about the iid reference, **NOT** a theorem that π behaves independently.

For the *full* one-digit histogram, at N=16v exact equality has probability

`P(E_1(16v)=0) = (16v)! / [16^(16v) (v!)^16] ~ 4 (2πv)^(-15/2)`,

and this probability is zero at other N. The series over v converges, so Borel–Cantelli says an iid uniform hexadecimal sequence almost surely has only finitely many full-histogram exact resets, **despite being normal almost surely**. Thus repeated exact global zeroes are not a necessary marker of normality. A partial sector can reset even when full discrepancy stays positive.

## FRH-03: the critical two-dimensional Gamma/elliptic finite part — CLASSICAL/PAPER

For the iid quarter-turn (m=4) sector, after 2n steps its exact return probability is

`a_n = [binom(2n,n)/4^n]² = binom(2n,n)² / 16^n`.

The coordinate change `(x,y)↦(x+y,x−y)` maps each planar walk increment to one of four equally likely pairs of independent signs. Hence returning after 2n steps is the product of two independent central-binomial return probabilities. The generating function is the classical elliptic hypergeometric

`Σ_(n≥0) a_n z^n = ₂F₁(1/2,1/2;1;z) = (2/π) K(sqrt(z))`.

DLMF §19.12 gives `K(sqrt z)= (1/2)log(16/(1−z))+o(1)` as `z↑1`. Since `a_n=1/(π n)+O(n^-2)`, subtract `(1/π)Σ_(n≥1)z^n/n=-(1/π)log(1-z)` and take the boundary termwise on the absolutely convergent difference. That yields `1+Σ_(n≥1)(a_n−1/(π n))=log16/π`. Restoring the sharp harmonic cutoff gives exactly

`lim_(M→∞) [Σ_(n=0)^M a_n − (log M)/π] = (γ+log16)/π`.

**This is a genuine Gamma/Euler–Mascheroni sharp-cutoff correction in the critical 2D reference-return spectrum.** It is *not* an original-zero BBP selected signed inequality, nor the predeclared oily-macaroni `φ^-1−γ` invariant. Reference: https://dlmf.nist.gov/19.12 .

## FRH-04: *orthogonal primitive Fourier sectors* at every digit-word depth — PROVED

Let `C_k(w,a)` be the integer count of cyclic k-words formed by context `w∈{0,..,15}^(k−1)` followed by symbol a. For each m, form the *antipodal channel imbalance*

`B_(w,r)^(m)= Σ_(a≡r mod m) C_k(w,a) − Σ_(a≡r+m/2 mod m) C_k(w,a)`, `0≤r<m/2`.

Define the real nonnegative primitive-sector energy

**`F_(k,m)(N)= 16^(k−1) (m/2) / N² · Σ_(w,r) [B_(w,r)^(m)]²`.**

On the finite group `(Z/16)^k`, every character is of the form `χ_h(w)=exp(2πi Σ h_j w_j /16)`. Orthogonality over the prefix vector and then over primitive m-th roots of unity proves

`F_(k,m) = Σ_(h_1,..,h_(k−1), g: order(g)=m) |hat p_k(h_1,..,h_(k−1),g)|²`.

The *new-coordinate* decomposition is therefore exactly

**`E_k(N) − E_(k−1)(N) = Σ_(m∈{2,4,8,16}) F_(k,m)(N)`**,

with `E_0=0`. The k=1 case gives four positive sectors of one-digit energy. This is a fully explicit integer **sum of squares** and a genuine arithmetic Fourier refinement space, not a source-specific decay estimate. All 15 terminal character modes are partitioned into 1+2+4+8.

## FRH-05: the actual historical word path is a de Bruijn graph circulation — PROVED

A length-k word `(a_1,...,a_k)` is a directed edge from `(a_1,...,a_(k−1))` to `(a_2,...,a_k)` in the full de Bruijn graph. There are `16^(k−1)` vertices and `16^k` edges; the graph is strongly connected.

For cyclic N-word observations the exact integer flow has zero graph divergence: each context has as many outgoing as incoming words. For ordinary noncyclic chronological counts the divergence is **precisely** `δ_(initial k−1 prefix)−δ_(terminal k−1 suffix)`. This is the retained origin/end memory; it is not zero unless the endpoints agree.

The cycle space has dimension `16^k−16^(k−1)+1`; removing total mass leaves dimension **`16^k−16^(k−1)`**. At k=1,2,3 these are 15,240,3840. This removes artificial redundant representation coordinates without discarding the finite word-frequency data. Cyclic flow conservation alone cannot rule out a perfectly periodic de Bruijn cycle (which is an Eulerian circulation).

## FRH-06: an exact iid renormalization baseline — PROVED for N≥2k

For an iid uniform **cyclic** N-digit sample, N≥2k, every nonconstant length-k word character has expected squared empirical Fourier coefficient `1/N`. Distinct shifted windows have zero character correlation: their union contains a boundary digit whose nonzero character coefficient is not canceled by the other window, even when the windows overlap; N≥2k prevents closed alias loops.

Therefore

`E_iid[E_k(N)] = (16^k−1)/N`, and `E_iid[F_(k,m)(N)] =16^(k−1)(m/2)/N`.

The natural *stationary-scale renormalization* is

**`R_k(N)=N E_k(N)/(16^k−1)`**, with iid expectation **exactly one** for N≥2k. This is an expectation reference, not a statement that R_k(N) must converge to one for any one iid or π sample. At the actual π prefix N=16384 the observed values are 0.713151, 0.981495, 0.978388 for k=1,2,3, respectively. These are finite observations, not proof of a deterministic asymptotic.

## FRH-07: the normalized signed-interference identity is not a restoring force — PROVED

For a unit character path `v_n` and `S_N=Σ_(n<N)v_n`, set `Q_N=|S_N|²/N` for N≥1. Exact algebra gives

**`Q_(N+1)−Q_N=[1+2 Re(conj(S_N) v_N)−Q_N]/(N+1)`**.

For a word histogram, replace `v_N` by `e_(word)−u`, whose squared norm is `1−1/16^k`. Under an iid *one-digit* null, the conditional mean signed work vanishes and the apparent `−Q_N/(N+1)` term is **a consequence of dividing by N**, not a physical or arithmetic restoring force. For overlapping k-words, the null conditional distribution is not independent of the preceding context; use the explicit uniform-append Poisson reference of #544 rather than pretending the k-word arrivals are iid.

The source-specific proof target is a **new signed estimate** for the actual zero-seed work term or the #544 forcing-corrected covariance. The normalization cannot itself establish that estimate.

## FRH-08: base-16 spectral alias theorem — PROVED, with a sharp boundary warning

For a depth-k digit-character vector `h=(h1,..,hk)` in `(Z/16)^k`, define the real-circle step function

`f_h(x)=exp(2πi Σ_j h_j d_j(x)/16)`, where `d_j(x)` are the first k hexadecimal digits of x∈[0,1), using half-open radix cells.

For integer real-circle frequency t≠0 its Fourier coefficient is **exactly**

`hat f_h(t) = [1−exp(−2πi t/16^k)]/(2πi t) · Π_(j=1)^k Σ_(a=0)^15 exp(2πi a(h_j/16−t/16^j))`.

If `j*=min{j:h_j≠0}` exists, this coefficient is nonzero **if and only if**

**`t ≡ 16^(j*−1) h_(j*) (mod 16^j*)`.**

Thus each nontrivial word-character belongs to one exact arithmetic progression/shell in the **real-circle Fourier spectrum**, fixed by its earliest nonzero digit coordinate. Zero/constant characters have only t=0. This gives an explicit cross-basis transport between symbolic Fourier (`(Z/16)^k`) and ordinary Fourier (`Z`). The source's expanding ×16 shift acts naturally on the latter frequency ladder.

**Warning:** coefficients generally decay only like 1/|t| and the Fourier series is not absolutely convergent; the sharp digit step functions are discontinuous at radix boundaries. An uncontrolled exchange of infinite frequency summation with the selected time average is invalid. The positive Fejér mean `σ_H f_h` does satisfy, for x not on a depth-k radix boundary and δ=distance(x,16^(−k) Z/Z),

`|f_h(x)−σ_H f_h(x)| ≤ min(2, 1/(H δ))`.

Proof: the Fejér kernel is nonnegative of mass one, f_h(x−y)=f_h(x) for |y|<δ, `F_H(y)≤1/(4H||y||²)`, and `|f_h(x−y)−f_h(x)|≤2`. The issue at the actual zero-selected π orbit is **quantitative occupation near shrinking radix boundaries**—the new still-open source-specific input. There is no automatic cancellation from the exact Fourier support classification.

## FRH-09: dense reset times are sufficient, but exact resets aren't necessary — PROVED

For any fixed k, suppose there are arbitrarily large integer horizons N_j with `E_k(N_j)=0` and `N_(j+1)−N_j=o(N_j)`. Then `E_k(N)→0` at all N: adding Δ chronological symbols changes at most Δ+2(k−1) cyclic edge counts in ℓ1; normalization changes by at most an additional Δ/N. Hence `||p_(k,N)−u||_1≤[2Δ+2(k−1)]/N` between successive reset horizons. If such a family exists for **each fixed k**, the sequence is base-16 normal.

But exact resets are much stronger than necessary and fail almost surely infinitely often even for iid normal sequences by FRH-02. A more reasonable all-epoch sufficient criterion is `E_k(N)→0` for every fixed k. This is equivalent to normality and is still unproved for the actual BBP source.

## FRH-10: executed original-source finite probe and countermodels — OBSERVED FINITE

From the inherited `research/2026-11-08/zero_origin_spectral_flux/CERTIFIED_HEX_16384.txt`, previously certified against the actual zero-seeded recurrence in #557 (not regenerated in this round):

| m | rank | exact digit-character prefix zeroes | final primitive-sector energy F_(1,m) | N F_(1,m)/rank |
|---:|---:|---:|---:|---:|
| 2 | 1 | 157 | 0.00000858307 | 0.140625 |
| 4 | 2 | 5 | 0.00008919835 | 0.730712890625 |
| 8 | 4 | 0 | 0.00022992492 | 0.9417724609375 |
| 16 | 8 | 0 | 0.00032520294 | 0.666015625 |

The full one-digit energy never equals zero at any of the 16,384 prefix times, and neither do cyclic depth-2 or depth-3 energies at any arithmetically eligible horizon within that prefix (N multiples 256 and 4096, respectively). These exact checks **do not** establish permanent nonreturn, transience or normality of π.

The four sector energies sum to the prior certified `E_1(16384)=0.0006529092788696289`. The depth-2 and depth-3 renormalized energies at N=16384 equal 0.9814950980392156 and 0.9783882783882784. The inherited matched-histogram shuffle controls, a constant sequence, a period-16 balanced sequence, and a repeated de Bruijn(3) cycle show that equal low-degree marginals, exact lower-level resets, or apparent flat finite spectra do not imply normality. The recorded finite-time signed-interference work has no demonstrated asymptotic negative drift.

## FRH-11: next verdict-changing gate — OPEN

A genuinely new source-selected theorem would compare the original **four-pole, zero-seeded** carry/prime/complement chronology with one of the `F_(k,m)` primitive-sector currents or its Fejér-smoothed real-circle alias and show a **quantitative all-A signed cancellation bound** that fails coherent same-forcing counterseeds and periodic shadow completions.

A lower-dimensional random-walk analogy, elliptic/Gamma correction, positive de Bruijn circulation, spectral resolution, or a finite normal-looking π digit trace by itself cannot establish the needed bound. The continuous-phase #544 Weyl/lag criterion and π base-16 normality remain **OPEN**.

## References and provenance

- Original source and 16,384 certified digits: SUCC draft PR #557, exact parent `b52f9affcac8be85f532fbe4e667e7ac01159b30`, plus `docs/PI_NORMALITY_FRONTIER.md` and `observational_succ/duck_bbp.py`.
- Source-selected signed lag gate: SUCC draft #544. No code or theorem in that branch is overwritten.
- Pólya/Chung–Fuchs: G. Lawler lecture notes `https://www.stat.uchicago.edu/~lalley/Courses/312/RW.pdf` (classical recurrence/transience theorem); independent digit reference explicitly stated.
- Elliptic/gamma: NIST DLMF §19.12 `https://dlmf.nist.gov/19.12` (complete elliptic K near its singular boundary).
- Normal sequences can exhibit different recurrence patterns: `https://doi.org/10.1073/pnas.1402621111` (for context, not an input to the finite tests).
- All Python test and receipt paths are new and additive; original source contracts and legacy provenance untouched.
