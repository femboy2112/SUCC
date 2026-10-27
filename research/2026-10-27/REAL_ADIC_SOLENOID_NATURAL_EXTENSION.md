# Operation ∞-Root, not square root: real/2-adic solenoid and BBP digit memory

**2026-10-27 · SUCC research draft.** Stacked on #328 at 68c00f5eee86c215dd09271b35b0647a5b56f16e. Builds on #320 (solenoid seam and countermodels), #321 (the authentic 2-adic BBP adding-machine), #323–#324 (positive summable Green tail), and #328 (odd-denominator modular compensation). Do not merge into main or alter the historical source. π base-16 normality and RH remain **OPEN**. No academic novelty is asserted for classical solenoid topology.

## SNE-0. The proposed isomorphism is false; its repaired object is exact

A literal topological-group isomorphism between the real circle R/Z and Z₂ cannot exist. The circle is connected and divisible; Z₂ is totally disconnected and 1 is not divisible by 2 in Z₂. If the symbol sqrt(Z₂) means {x in Q₂ : x² belongs to Z₂}, the valuation criterion 2v₂(x)≥0 shows this set is precisely Z₂. Every continuous group homomorphism Z₂→R/Z has finite 2-primary image; it cannot be onto the real circle.

The **faithful repair** is the inverse-history extension, or dyadic solenoid,

$$
\Sigma=(\mathbb R\times\mathbb Z_2)/\{(m,-m):m\in\mathbb Z\}
\cong\varprojlim(\mathbb R/\mathbb Z,\times16).
$$

The seam convention is exactly #320's (t,z)~(t+1,z−1). The fiber sequence is

$$
0\longrightarrow\mathbb Z_2\longrightarrow\Sigma
\overset{p}{\longrightarrow}\mathbb R/\mathbb Z\longrightarrow0,
$$

and the Pontryagin dual of Σ is Z[1/16]=Z[1/2]. The inverse-limit level-k coordinate of [(t,z)] is (t+[z]_(16^k))/16^k modulo 1. These are classical identifications, not a newly invented solenoid.

An ordinary quotient R→R/Z forgets integer winding. The solenoid does not recover that winding from the circle alone; it keeps an additional **2-adic inverse-history coordinate**. That is the precise sense in which the author's proposed “square root” seeks the missing structure.

## SNE-1. Real digits become 2-adic memories: an invertible exact law

Choose the right-open chart 0≤x<1, z in Z₂. Multiplication by 16 defines an **automorphism of Σ**; the map z→16z on Z₂ alone is only a contraction and is **not** the odometer. In the cut chart put a=floor(16x) in {0,…,15}. Then

$$
\boxed{T(x,z)=(\{16x\},\,16z+a).}
$$

Its inverse exists and is explicit:

$$
\boxed{T^{-1}(x,z)=((x+d)/16,\,(z-d)/16),\quad d=[z]_{16}.}
$$

The forward formula follows from reducing (16x,16z) across the diagonal seam; in the inverse, z−d is divisible by 16 in Z₂ and (x+d)/16 lies in [0,1). Direct substitution proves both identities.

The real winding lift j_R(t)=[(t,0)] is a continuous injective homomorphism R→Σ, *not* a continuous splitting of R/Z→Σ. Starting from j_R(α), the nth iterate has cut coordinates

$$
x_n=\{16^n\alpha\},\qquad z_n=\lfloor16^n\alpha\rfloor\in\mathbb Z_2.
$$

If a_n=floor(16x_n) denotes the nth hexadecimal digit, then

$$
z_{n+1}=16z_n+a_n
$$

and, for n≥k,

$$
\boxed{z_n\bmod16^k=\sum_{j=1}^k16^{j-1}a_{n-j}\bmod16^k.}
$$

The real coordinate encodes the upcoming digits; the 2-adic coordinate encodes the preceding digits in reverse positional order. The **source clock** U_n mod16^k from #321 is a different 2-adic observable from the **winding archive** floor(U_n) mod16^k. Confusing them destroys source fidelity.

Haar measure on Σ is represented in this fundamental chart by Lebesgue x Haar(Z₂). A prescribed block of k upcoming digits and m preceding digits therefore has Haar mass 16^{-(k+m)}. This is a **target** distribution, not an established property of π.

## SNE-2. Coherent-orbit theorem: circle normality iff full-solenoid Haar genericity

Let e(t)=exp(2πit). For every a=m/16^k in the character group Z[1/2] (m integer, k≥0),

$$
\chi_{m/16^k}(x,z)
=e\!\left(\frac{m(x+[z]_{16^k})}{16^k}\right).
$$

The expression is unchanged under the seam equivalence and is therefore a well-defined solenoid character. On a coherent orbit,

$$
\chi_{m/16^k}(T^n j_R(\alpha))
=e(m16^{n-k}\alpha).
$$

**Theorem (paper-proved; any real α).** α is normal in base 16 **if and only if** the *single coherent sequence* T^n j_R(α) is Haar-equidistributed on Σ.

**Proof.** If the solenoid sequence is Haar-generic, its projected circle sequence is Lebesgue-generic and α is normal by Weyl's criterion. Conversely, assume α is base-16 normal. For each fixed integer m≠0 and fixed k, the character sequence equals e(m16^{n-k}α) after the first k steps. It is a finite time shift of an integer-mode circle Weyl sum, so its Cesàro mean tends to zero. The characters of the compact abelian solenoid separate points and span a uniformly dense algebra of continuous functions. Character cancellation for every fixed nontrivial a proves Haar-equidistribution. QED.

**Crucial reconciliation with #320 §6.** An arbitrary sequence of circle-Haar points with *independently selected* inverse solenoid lifts need not be solenoid-Haar; #320's odd-torsion lift counterfeit remains correct. But lifts forming **one actual orbit under T**, with inverse histories coherently constrained, satisfy the theorem. The previous warning that full solenoid Haar is always strictly stronger needs this orbit-versus-arbitrary-lifts qualification.

Under Haar, T is mixing, since for nonzero fixed a,b in Z[1/2],

$$
\int_\Sigma\chi_a(T^n s)\overline{\chi_b(s)}\,dH(s)
=\begin{cases}1&16^n a=b,\\0&\text{otherwise}.\end{cases}
$$

The equality eventually fails and finite character sums are dense in L². But Haar mixing does **not** force any chosen point to be generic: T fixes the origin, whose orbit is not Haar. This is not a proof of normality of π.

## SNE-3. Authenticated BBP: an exact solenoid shadowing theorem

Retain the original four signed poles and the zero seed:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}
-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
$$

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

The authenticated BBP identity and #323/#324 give, for n≥1,

$$
U_n=16^{n-1}\pi-T_n,\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,
$$

and the convergent positive tail budget

$$
B=\sum_{n\ge1}T_n=(\sum_{n\ge1}r(n)-\pi)/15
\approx0.0162969977338265.
$$

Thus in Σ,

$$
\boxed{j_R(U_n)=T^{n-1}j_R(\pi)-j_R(T_n).}
$$

Because T_n→0 in the *real* topology and j_R is continuous, the correction tends to the solenoid identity. For every fixed continuous solenoid observer f, uniform continuity on compact Σ gives the same empirical limit for the two sequences whenever that limit exists.

More quantitatively, for every fixed character a=m/16^k and N≥1,

$$
\boxed{\left|\frac1N\sum_{n=1}^N\chi_a(j_R(U_n))
-\frac1N\sum_{n=1}^N\chi_a(T^{n-1}j_R(\pi))\right|
\le\frac{2\pi|m|B}{16^kN}.}
$$

Proof: the character difference is bounded by 2π|a|T_n; sum the Green tails.

**Source-selected corollary:** π is base-16 normal **iff the real winding lifts j_R(U_n) of the exact four-pole zero-seeded BBP recurrence are Haar-equidistributed in Σ.** This is an *equivalent theorem target*, not a new cancellation bound. #321's U_n mod16^k Haar is the distinct arithmetic-time coordinate and does not close this selected target.

## SNE-4. The missing multiplicative character is an exact odd-denominator complement

For any reduced rational u=A/B with B>0 odd, let q=16^k, let R be the representative of A B^{-1} mod q, and set K=(BR−A)/q (integer). Exact arithmetic gives

$$
\frac{u}{q}=\frac Rq-\frac KB,\qquad
\boxed{e(hu/q)=e(hR/q)\,e(-hK/B).}
$$

This specializes #328's modular/real complementary-character identity to 2-adic radix q. The first factor is the 2-adic residue character; the **second factor contains the odd denominator and cannot be dropped**.

Counterexample: 0 and 32/3 have the same 2-adic residue 0 mod16, but real winding memories 0 and floor(32/3)=10 mod16. Also the real character e((32/3)/16)=e(2/3) is nontrivial despite its arithmetic residue character being 1. The missing complementary factor carries *all* that phase. Thus the field coupling is visible as exact arithmetic but is not automatically statistical decorrelation.

## SNE-5. An actual equivariant factor no-go, with hypotheses

Let O:z→z+1 be the Haar adding machine on Z₂ and let T act on Haar Σ as above.

**Theorem (paper-proved).** No measurable map F:Z₂→Σ can simultaneously satisfy (i) F∘O=T∘F almost everywhere and (ii) F pushes Haar(Z₂) forward to Haar(Σ).

**Proof.** Let g=χ_1∘F in L²(Haar(Z₂)). Then ||g||₂=1 and its mean is zero by the Haar pushforward. Equivariance implies

$$
\langle g\circ O^{16^j},g\rangle
=\int_\Sigma\chi_{16^{16^j}-1}(s)\,dH(s)=0
$$

for all j≥0, because the character is nontrivial. But O^{16^j} is translation by 16^j, tending to the identity in Z₂. On L²(Haar(Z₂)) these translations converge strongly to the identity: approximate g by locally constant functions modulo16^K, which every such translation fixes for j≥K. Consequently those correlations must converge to ||g||₂²=1, contradiction. QED.

**Boundary:** this excludes a measurable **Haar-preserving equivariant** factor from the *pure odometer*. It does **not** exclude an arithmetic source-conditioned, nonautonomous, nonfactorial, or discontinuous path capable of proving π normality. The actual BBP forcing is such an additional datum, and any proof must exploit it instead of only unique ergodicity of the clock.

Also, for any irrational α there is no **continuous** f:Z₂→Z₂ with f(n)=floor(16^nα) for every integer n≥0. Otherwise n→f(n+1) mod16 would be a continuous finite-valued map on compact Z₂, hence factor through some finite residue quotient Z₂/2^K. Every hexadecimal digit would then repeat with period 2^K, making α rational. This no-go already applies to known irrational π without any normality assumption. Relabeling the odometer by #321's homeomorphism Φ does not overcome it.

## SNE-6. Hostile moving-character obstruction

Do **not** replace fixed solenoid character equidistribution by vanishing for all characters whose dyadic denominator grows with N. For *every* real α, choose a_N=16^{-N}. Then

$$
\left|\frac1N\sum_{n=0}^{N-1}\chi_{a_N}(T^n j_R(\alpha))-1\right|
\le\frac{2\pi|\alpha|}{15N}(1-16^{-N})\longrightarrow0.
$$

Indeed sum 16^{n-N}=(1−16^{-N})/15 and use |e(t)−1|≤2π|t|. Thus the moving character mean tends to **1**, even if α is base-16 normal. The analogous authentic BBP mean has an additional ≤2πB/(16^N N) correction by SNE-3. This supplies a constructive counterexample to any uniform-in-depth Weyl gate demanding those means vanish. The #327/#328 obstructions to growing CRT energies must not be erased by the solenoid reformulation.

## Validation, independence and next verdict-changing probe

**Executed finite code:** observational_succ/solenoid_digit_bridge.py and tests/test_solenoid_digit_bridge.py. The 11 focused tests were run locally in an isolated two-file working copy: 10 passed; one native SUCC upstream source import was skipped because the full working tree was unavailable. The independently coded rational-character grid passed 30,704 exact checks. The finite positive/negative controls include an entirely periodic de Bruijn hexadecimal word with each two-digit window uniform but no normality; 32/3 versus 0; a balanced time clock with zero real digits; and precision loss of a finite-chart inverse. The infinite results above are supplied by explicit paper derivations, not by these finite tests.

**No full native SUCC test suite, GitHub Actions CI, or Lean run is claimed.** Exact finite chart code is not a computational representation of infinite 2-adic precision. Authentication is by the original four signed source as checked against #320 and #321; the local native import remains a separate integration gate.

**OPEN, load-bearing assertion:** for each fixed integer h≠0, prove the selected zero-seed sum N^{-1}∑_{n=1}^N e(hU_n)→0. An actual advance must derive a *new* signed estimate from the original rational four-pole forcing, in particular the odd-denominator complementary characters in SNE-4, distinguish the zero seed from the #320 nonnormal mutant and the changed-selector -T_n, and survive hostile predetermined holdouts. No equivalence or ergodic theorem here proves that estimate.

Classical references: [Pinto–Sullivan, The circle and the solenoid](https://www.aimsciences.org/article/doi/10.3934/dcds.2006.16.463); [S-adic solenoids and Pontryagin duality](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/on-the-spectral-theory-of-groups-of-automorphisms-of-sadic-nilmanifolds/7AF494440F8BF97D109C4335383F0998); [inverse-limit natural extension of expanding circle maps](https://staff.fnwi.uva.nl/a.j.homburg/Files/forcedcircle.pdf); [Bailey–Crandall normality discussion](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf).

**Ledger verdict:** literal proposed isomorphism REFUTED; exact solenoid repair CLASSICAL; coherent-orbit normality equivalence, selected full-solenoid transfer, measurable odometer-factor obstruction, and moving character no-go PAPER-PROVED WITH STATED SCOPE; π normality OPEN.
