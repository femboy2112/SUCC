# Operation Dual Categories — BBP Hexadecimal Journals and the Four-Step Collatz Parity Carrier

**20 November 2026. Research-only, stacked above SUCC draft #680.** Status: classical Bernstein/Lagarias and Monks/Yazinski dynamical results, with exact new-to-this-SUCC bookkeeping interfaces and source-specific **finite** BBP certificates. No academic priority or novel theorem about general Collatz or pi normality claimed. The original four signed BBP poles and the literal `U_0=0` remain unchanged.

## Steelman / user hypothesis

The real pi-generating causal category and a suitably chosen dual category may have the **same ordered bookkeeping arrows**, even though one computes hexadecimal digits and the other executes Collatz. The source-filter semicircle has roots at left-arc fractions 1/4 and 3/4, suggestive of odd 4k+1 and 4k+3 branches. A valid theorem requires *actual maps*, not equality of displayed symbols or a forced interpretation of polynomial roots as moving digit states.

Let `e(t)=exp(2pi i t)`. Let `C:Z_2 -> Z_2` denote the **shortcut** Collatz map `C(a)=a/2` for even `a` and `C(a)=(3a+1)/2` for odd `a`. Let `S_2(y)=(y-(y mod2))/2` be the binary 2-adic shift. Let `S_16(Y)=(Y-(Y mod16))/16` be its four-bit block shift. The full one-sided hexadecimal shift space `D={0,...,15}^N` has left shift `sigma`. Every finite-stage source statement below refers to the original `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)` and `U_0=0`.

### DCP-01. Exactly four Collatz steps correspond to one hexadecimal symbolic step (CLASSICAL / PROVED PAPER)

Define the parity vector `Q:Z_2 -> Z_2` by `Q(a)=sum_(j>=0) (C^j(a) mod2) 2^j`. The Bernstein-Lagarias conjugacy is the 2-adic homeomorphism `Q` with `Q C=S_2 Q`. Its inverse `Phi=Q^(-1)` is explicit: for the one-bit locations `0<=d_0<d_1<...` of `y`,

`Phi(y)=-sum_(j>=0) 2^(d_j) / 3^(j+1)` in `Z_2`.

Group chronological parity bits into nibbles `d_(n+1)=sum_(k=0)^3 (C^(4n+k)(a) mod2) 2^k`. Then `Y=sum_(n>=0)d_(n+1)16^n=Q(a)`, and consequently

`C^4 Phi(Y) = Phi(S_16(Y))`.

Proof: apply `Q C^4=S_2^4 Q=S_16 Q`; `Q` is invertible. Every possible nibble word is legal on `Z_2`. The 16 prescribed four-bit words determine disjoint, covering cylinder classes of states modulo 16. No claim is made that the corresponding 2-adic state is a positive integer.

### DCP-02. Literal equivalence of the two *declared* action categories (CLASSICAL / EXACT)

The map `A:D -> Z_2`, `A(d)=sum_(n>=0)d_(n+1)16^n`, is a homeomorphism for the product and 2-adic topologies, with `Asigma=S_16 A`. Therefore `F=Phi A` satisfies `Fsigma=C^4F` and is a topological conjugacy. It induces an isomorphism of forward `N`-labelled action categories `Act(D,sigma)` and `Act(Z_2,C^4)` (objects and labelled arrows transported by `F`). Ordinary Yoneda then represents either action category faithfully in all its Hom probes. A *restricted* physical head/pinbed needs a separate density/source-adequacy proof.

**Critical type:** evaluating a symbolic word on the real side by `R(d)=sum_(j>=1)d_j16^(-j)` yields `[0,1]` with the familiar terminating / infinite-F ambiguity. Choosing the canonical expansion for `[0,1)` excludes eventually-F words and yields an invariant subset. `R` is NOT a global homeomorphism to `[0,1]` with its Euclidean topology. Thus the literal category equivalence is between **symbolic/2-adic** dynamics. The selected real pi orbit provides a canonical symbolic trajectory as an extra *source-dependent choice*, not a full real-to-Collatz conjugacy on positive integers.

### DCP-03. The mirror is a nontrivial Collatz symmetry *after* journal transport (CLASSICAL / EXACT)

For the symbolic digit complement `D(d)_n=15-d_n`, the real evaluated series (on the nonambiguous symbolic domain) satisfies `R(Dd)=1-R(d)`, while the 2-adic address satisfies

`A(Dd)=15 sum_(n>=0)16^n-A(d)=-1-A(d)`.

Therefore the same symbolic mirror is `V(Y)=-1-Y` on `Z_2`. It commutes with `S_2` and `S_16`. Transport back through the parity conjugacy:

`Omega(a)=Phi(-1-Q(a))`.

Then `Omega^2=id`, `Omega C=C Omega` and hence `Omega C^4=C^4 Omega`. This is Monks and Yazinski's known nontrivial Collatz autoconjugacy. Examples: `Omega(0)=-1`, `Omega(1)=2`, `Omega(2)=1`. **Do not** replace `Omega(a)` by `-1-a`, `1-a`, or the raw digit-complement of the *state*: those need not commute with `C`. That was an earlier SUCC hostile control, now correctly repaired at the parity-journal level.

### DCP-04. The exact meaning of 1/4 and 3/4 (ELEMENTARY / PROVED; CHART-RELATIVE)

For every `a in Z_2`, `Q(a) mod4=a mod4`. Proof: for even `a=2k`, the first parity is zero and the second is `k mod2`; for odd `a=2k+1`, the first parity is one and the second is `(3k+2) mod2=k mod2`. Thus both cases give parity word `a mod4`.

In particular, the odd classes `a=4k+1` and `a=4k+3` have two-step parity code `1` and `3`. Their two-step affine actions are **different**:

`C^2(4k+1)=3k+1=(3a+1)/4`,

`C^2(4k+3)=9k+8=(9a+5)/4`.

Encoding their two-bit codes on the normalized quarter grid gives `1/4` and `3/4`. The original BBP filter `H(t)=(t^2+2)(t^2+2t+2)` has conjugate roots `-1+i` and `-1-i` on the left-circle chart at precisely these fractions. So a two-symbol *chart-level* correspondence is exact. However **the original root coordinates at 1/4 and 3/4 are hexadecimal thresholds 4/16 and 12/16**; they are NOT themselves the Collatz residues 1 and3 mod4. Mapping root-port states to parity inputs is an independent, currently unproved source-to-carrier factor map. Their Haar parity port from #678 identifies them as a pair but cannot distinguish orientation; a second, oriented head is needed.

Under chart reflection `u -> 1-u` the two fractions swap, corresponding on the odd two-bit *labels* to `a mod4 -> -a mod4`. This is not the ordinary *raw-state* Collatz conjugacy. The transported `Omega` in DCP-03 is.

### DCP-05. The four-bit parity encoder is a source-independent finite origami (PROVED EXACT)

At the first two bits, `Q mod4=id`. At four bits, the entire map `Q_4:a mod16 -> Q(a) mod16` is the permutation

`(0,5,10,3,4,1,6,7,8,13,2,11,12,9,14,15)`

in input order `a=0,...,15`. It is an involution at this precision, with nontrivial swaps `(1,5),(2,10),(9,13)` and the remaining residues fixed. The next precisions need not be involutions; this finite coincidence is not a universal group law. Because `Q_m` is a permutation for each finite precision `m`, it supplies a lossless, reconstructible relabeling of four-step causal branches at each depth.

For a parity word `epsilon_0...epsilon_3`, with `s=sum epsilon_j`, the four-step Collatz state is

`C^4(a)=(3^s a + beta_epsilon)/16`,

`beta_epsilon=sum_(j:epsilon_j=1)2^j 3^(sum_(l>j)epsilon_l)`

on its **specific congruence cylinder**. The inverse branch `(16 y-beta)/3^s` is a 2-adic contraction of factor `1/16`. This is an actual 16-branch recursive system, not the period-two plain mirror.

### DCP-06. Exact 2/3/Archimedean precision trade (CLASSICAL / EXACT)

Within one prescribed four-bit parity cylinder, the rational same-branch slope is `A=3^s/16`. Consequently

`|A|_infinity=3^s/16`, `|A|_2=16`, `|A|_3=3^(-s)` and `|A|_infinity*|A|_2*|A|_3=1`.

The 2-adic shift expands distances by 16 on a common parity cylinder, while its inverse branches contract by 1/16; the 3-adic same-branch response contracts according to the number of odd encounters. This is **rational product-formula bookkeeping**, not conserved physical energy, mixing, a continuous 2-adic-to-3-adic field isomorphism, or a theorem about arbitrary paths with differing parity words.

### DCP-07. Original zero-seeded BBP selects a 2-adic Collatz path to arbitrary finite precision (EXACT SOURCE-SPECIFIC FINITE)

Let the authenticated four-pole source produce `x=pi/16` and the hexadecimal digits `d_1d_2...`. The real phase obeys `theta_(n+1)=16 theta_n-d_(n+1)` with `theta_0=x`, `d_(n+1)=floor(16theta_n)`. Let the *constructed* 2-adic parity address be

`Y_pi=sum_(n>=0)d_(n+1)16^n in Z_2`, `alpha_pi=Phi(Y_pi)`.

Then, for every finite `n`, the first `4n` parities of `alpha_pi` (under shortcut Collatz on `Z_2`) are precisely the first `n` authentic hexadecimal digits of `pi/16` written low-bit first, and `C^(4n)(alpha_pi)=Phi(S_16^n Y_pi)`. This is an exact selected-path intertwining, **not** an equality between a real `pi` and a preexisting p-adic `pi`, nor a proof that `alpha_pi` is a positive integer.

The original rational BBP tail enclosure at `M=12`, with original zero seed, certifies exactly `3243F6A8885A` as the first 12 hexadecimal digits. The corresponding 48-bit address and unique Collatz seed residue are

`Y_pi == 0xA5888A6F3423 (mod 2^48)`,

`alpha_pi == 0x138D4B466283 (mod 2^48)`.

The finite residue is obtained two independently implemented ways: the Bernstein inverse sum, and 48 reversed lawful Collatz inverse branches. Direct 48-step integer Collatz parity extraction from this residue reproduces all 12 digits. It is a finite exact arithmetic certificate; every generic digit sequence can be encoded similarly, so this alone does not improve the normality frontier.

### DCP-08. Why this does NOT prove Collatz, pi normality, or new BBP real-phase dynamics (HOSTILE CONTROLS)

1. **Domain:** `Phi(Y_pi)` is a 2-adic state, not known to be a positive ordinary integer. The 3x+1 conjecture asks about positive integer seeds. Almost every parity journal under Haar is nonperiodic even though the 2-adic Collatz map is conjugate to a Bernoulli shift.
2. **Source:** a rational, constant-zero, or factorial-sparse nonnormal hexadecimal stream also has a valid conjugate Collatz 2-adic history. The conjugacy is universal for words, not a source-specific BBP anti-lock inequality.
3. **Mirror:** `a -> -1-a` on raw Collatz states is generally NOT the autoconjugacy; only `Phi V Q` is. The root semicircle's reflection chart likewise is not an authenticated state transfer.
4. **Precision:** `4n` parity bits determine only `alpha_pi mod2^(4n)`; finite certification does not identify an integer representative or entire infinite Collatz orbit.
5. **Source mutation:** a changed BBP pole polynomial produces another real digit sequence and hence another valid 2-adic Collatz itinerary; source distinctions require the source head.
6. **Gaussian/Haar:** the topological/measure conjugacy transports Haar measure and mixing on a **space of all 2-adic states**. It does not prove that the *selected* `alpha_pi` is generic for that measure. Full normality would be precisely the missing selected-point genericity.

### DCP-09. Exact remaining proof gate (OPEN)

The new cross-system computational bridge is a sourced **coordinate representation**. The next step is to derive from the original BBP four poles and zero seed an **independently selected** signed observable in the conjugate Collatz/prime-seam frame whose chronological averages cannot lock on all late shells. A mere recalculation of the hexadecimal digits as a parity word is tautological and cannot establish the bound. The root `H` sectors and auxiliary 5/11 evaluator can be joined only through a new authenticated, oriented, source-to-observer map; calibrated projectors/ports alone are insufficient. Keep the changed-seed locked source, fixed digits, odd-slope false Haar, source mutant and moving-frame controls alive. `R0`, base-16 normality, universal positive Collatz termination, RH, physical superfluid energy all remain OPEN.

## Provenance and status

**Classical antecedents:** Daniel J. Bernstein and Jeffrey C. Lagarias, *The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics 48 (1996), 1154--1169, https://doi.org/10.4153/CJM-1996-060-x; K. Monks and J. Yazinski, *The autoconjugacy of the 3x+1 function*, Discrete Mathematics 275 (2004), 219--236, https://doi.org/10.1016/S0012-365X(03)00125-0. SUCC prior #667 and #680 establish related parity cylinders and raw digit-mirror/2,3,5 comparisons. This dossier's assembly is new to this branch; no scholarly novelty or independent theorem certification claimed. All exact computational tests are finite implementation checks of paper algebra, not independent mathematical sources.
