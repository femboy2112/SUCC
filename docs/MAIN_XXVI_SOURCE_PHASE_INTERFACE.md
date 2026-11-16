# Main XXVI adversarial carry–Gamma synthesis

Audit date: 2026-11-16. This dossier is an integration-time derivation and proof audit. It establishes a quantitative interface and an indistinguishability obstruction; it establishes no new positive carry-density estimate. R0 and π-normality remain OPEN.

## Provenance and exact object

The audited heads are #652 `b8e0454d5c295bdc582bd5ddb5c794b484b6ad1b`, #654 `595c4e8f64b5a3578f343d486eb98c2440bd7ef1`, #651 `94c7252ac7db3c8b14229544087119bd9cc01933`, #650 `bf27f7ec8e757482613808bff693ba520ac13b3b`, and #647 `fec5cdda24ca36328e123b0b367a0628491e1eb8`. The earlier #643/#645 instruments are inherited by the carry stack. Repeated proofs within that stack are one provenance family.

Keep the literal signed four-pole r(n), U₀=0, Uₙ=16Uₙ₋₁+r(n), and Uₙ+Tₙ=16ⁿα with α=π/16. Let Cₙ=floor(Uₙ), d_B=B⁻¹Σ_{B≤n<2B}1_{Cₙ mod4∈{1,2}}. The source completion uses the imported BBP identity; the Gamma observation is not an independent proof that the completion equals π/16.

## Contract fixed before the integration-time recount

The candidate source estimate is: there exist δ>0 and B₀ such that, for every integer B≥B₀, d_B≥δ. This is stronger than R0, weaker than normality, and equivalent to α∉E for #652's exact exceptional set. It is OPEN. The candidate quantitative training guess δ=1/32 is falsified on a specified finite interval by any exact certified shell with selected count <B/32. A finite pass cannot establish the eventual quantifier.

For the combined instrument below, fix real labels (ξ,ω), fixed independently of B, and define a≠0 and G_B as stated. The equivalent eventual estimate is limsup_B Re((1+i)G_B/a)<1. A proposed finite margin must include the explicit deconvolution error. A high-frequency choice with a tiny response is not a bounded inverse.

The retained horizon 131072 and shells 32769≤B≤65536 are existing training data, not a new holdout in this integration. The recount only checks implementation/indexing consistency. A future genuine holdout starts beyond index131072, after constants and time range are frozen.

## CI-CG1: a quantitative Gamma-weighted carry interface

Status: PROVED COMPOSITE DEDUCTION / EQUIVALENT INSTRUMENT. Hypotheses: original positive Green source, fixed real ξ,ω, all integer n≥1; use #654 GM9's source-conditioned characteristic

Ψₙ(ξ,ω)=E[e^(−iξYₙ)Yₙ^(iω)],
a=Γ(2+iω)/(1+iξ)^(2+iω),
|Ψₙ−a|≤7/(4n).

These expectations are over the declared conditioned Green observer only. They do not randomize Uₙ or Cₙ. Set

G_B=B⁻¹Σ_{B≤n<2B} i^(Cₙ) Ψₙ(ξ,ω),
H_B=B⁻¹Σ_{B≤n<2B} i^(Cₙ).

Then, for every B≥1,

|G_B−aH_B|≤(7/(4B))Σ_{n=B}^{2B−1}1/n≤7/(4B),

and consequently

|d_B−[1−Re((1+i)G_B/a)]/2|≤7√2/(8|a|B).

Proof: i^(Cₙ) has modulus one, so the first bound follows by the triangle inequality. The exact four-residue identity is

1_{c mod4∈{1,2}}=[1−Re((1+i)i^c)]/2.

Average it, divide the first bound by |a|, and use |1+i|=√2. By the classical [Gamma zero-free property (NIST DLMF §5.2)](https://dlmf.nist.gov/5.2), Gamma has no zeros and the principal power of 1+iξ is nonzero, so a≠0 for every fixed real label pair. The constants deteriorate as the inverse response grows. There is no uniform stable inversion over all labels.

If Re((1+i)G_B/a)≤1−2δ on every sufficiently late shell, then liminf d_B≥δ. For any δ'<δ, d_B≥δ' eventually. #647's source-faithful carry-to-phase bridge then supplies R0 with any conservative eventual margin below δ'(1−cos(π/8)). Full normality still needs the remaining modes.

This is a useful interface: it preserves the actual integer winding, has a declared phase frame, and quantifies exactly the inverse cost. It also proves that a fixed Gamma window merely reweights the unpaid signed carry statistic. Thus it pays the transport/interface debt, not the arithmetic estimate.

## CI-CG2: source data plus deep dyadic agreement still do not select a carry word

Status: PROVED COMPOSITE OBSTRUCTION. For any finite N, L≥2 and any prescribed word c₁,…,c_N∈{0,1,2,3}, #652 A-FS constructs a rational changed seed s∈2^L Z_(2), using only a finite literal BBP prefix, such that all states retain odd denominators,

Uₙ(s)−Uₙ(0)=16ⁿs∈2^(L+4n)Z_(2),

and floor(Uₙ(s))≡cₙ mod4 for 1≤n≤N. Meanwhile every source-only Gamma/Green window, including all complex labels and every source time, is identical because the forcing and Green source are identical.

Therefore the exact source windows plus any fixed amount of dyadic agreement do not imply a seed-uniform positive carry drift, even if the source windows are supplied without numerical error. Choosing cₙ=0 gives zero selected events throughout the prescribed finite horizon. The construction varies its rational seed with N,L; it does not produce one rational seed that realizes an arbitrary infinite word. It does not refute a theorem using the exact zero seed, nor one with a quantified seed-height cost.

The denominator-grid version in #652 C8 additionally preserves the authentic current denominator divisor when its displayed lattice-spacing hypothesis holds. It is a late-state construction, not a claim that every preceding denominator history is unchanged. These hypotheses must remain distinct.

## CI-CG3: exact growing-CRT state with the carry branch retained

Status: PROVED COORDINATE REDUCTION; no new estimate. This is a fourfold lift of #647 NEXT N1, useful for auditing a signed source estimate.

Let L₀=1 and Lₙ=lcm(1,3,…,8n−1). The reduced denominator of Uₙ divides Lₙ. Define Aₙ to be the least residue of LₙUₙ modulo4Lₙ, so 0≤Aₙ<4Lₙ and A₀=0. With bₙ=Lₙ/Lₙ₋₁ and Rₙ=Lₙr(n)∈Z,

Aₙ=[16bₙAₙ₋₁+Rₙ]_(4Lₙ),
Cₙ mod4=floor(Aₙ/Lₙ),
1_{Cₙ mod4∈{1,2}}=1_{Lₙ≤Aₙ<3Lₙ}.

Proof: multiply the original rational recurrence by Lₙ. Changing its previous numerator by 4Lₙ₋₁ changes the next numerator by64Lₙ, hence does not change this residue. If LₙUₙ=Aₙ+4Lₙk, division and flooring gives Cₙ=4k+floor(Aₙ/Lₙ). No real branch, chronological sign, pole, or cofactor is discarded.

The next actual arithmetic estimate can therefore be stated on this exact nonautonomous source-selected orbit:

Σ_{n=B}^{2B−1}1_{Lₙ≤Aₙ<3Lₙ}≥δB,
A₀=0,
all integer B≥B₀.

It is still the carry gate in exact finite arithmetic, not a proof of its frequency. Replacing A₀=0 by a generic residue law or replacing the changing Lₙ by independent clocks loses the required source selection. The zero-seed boundary and complete chronological update are the load-bearing information.

## Audit of #652's inherited results

- Sharp floor transfer survives: both selected mask and all eight frame certificates match at residues0 and3. A mask-changing borrow must occur at a nonzero completed digit followed by m_B=floor(log₁₆(64B²)) zeros. Thus discrepancies are spaced by ≥m_B+1 and have density at most [1+floor((B−1)/(m_B+1))]/B. General masks do not enjoy this transfer: α=0 makes the zero-residue indicator disagree everywhere.
- The exact dimension dim_H E=7/8 survives. The bad-shell count has B−1 unrestricted preceding digits, then B digits with only eight unselected choices; the cover depth is2B−1. The lower bound uses widely separated forced shells with limsup restricted-position density1/2. The mass bound is for every strict s<7/8; a critical-exponent uniform Frostman constant is not established or needed.
- The entropy thresholds survive with their units and quantifiers: a uniform margin above3 full-digit bits, or above1 residue bit, for every subsequential limit of every integer shell is sufficient. It is not supplied by a finite histogram. The fixed signed three-count budget requires the much stronger sharp entropy threshold3.979395798805217 bits. Its orientation is not necessary for positive selected density.
- The eight-frame envelope satisfies d_B/8≤M_B≤d_B. The fixed-frame signed budget can converge to−1/4 despite uniform carry residues and selected density1/2, using the changed completed period5674. There is no assertion that one frame wins on every shell.
- The finite source holdout is scoped correctly:32768 integer shells, B=32769,…,65536; final observed shell ends at131071 and state131072 is extra. No eventual theorem follows.

## Controls and scope of minimum repairs

| Control | What it preserves | What it defeats / hypothesis missing |
|---|---|---|
| Coherent s=−α | Literal forcing and every Gamma/Green window | Completed orbit0; Cₙ=−1, d_B=0. Exact zero seed absent; real seed is outside rational carrier. |
| Completed rational β=1/16 | Same forcing/tail | Eventually Qₙ≡0 and Cₙ≡3 mod4; zero gate. Seed β−α is not rational. |
| A-FS rational seed, prescribed zero word | Literal forcing, rational odd denominators, arbitrary deep fixed dyadic agreement, all source windows | Zero gate for arbitrary finite horizon. Exact zero seed and uniform height bound absent. |
| Period5674 | Literal forcing, uniform carry residues | Fixed budget−1/4 despite d=1/2. Refutes a marginal-to-oriented-budget inference. |
| Zero/three Thue–Morse endpoint | Literal forcing, optimal approximation-type controls in cited scope | Zero selected density; R0 can still hold. Defeats conflating the selected gate with R0. |
| g(n)=2n² source coboundary | Completed real π endpoint with corrected tail | Alters source presentation/arithmetic holonomy. Must not be called a changed real π target. |
| Bernoulli π coin Fourier before mean | Exact BBP click marginal | E e(h16ⁿC)=1 while e(h16ⁿEC) is the real orbit. Observation order cannot be exchanged. |

The first three controls do not all have the same carrier typing. No nonexistent combined counterexample is inferred by intersecting their separate properties.

## Evidence executed in this integration audit

The original #652 `independent_audit.py` was replayed from a disposable extraction of its exact head. Exit0;127594 assertions;1143 rational-shadow positions; the B=8/M=48 denominator-grid control has L₈=−1/4. The stored source files retain prefix hash `379b98f2d2e3d69976ec8d819cd21ea9e032bf229784ad88a4f3f216e43c1594` and residue hash `ae15aa4aaf63849ba61f29c925e3f69581542bbb71a3df788835a96556546962`.

The replay reproduced minimum L=1997/33657 atB33657, minimum d=16393/32911 atB32911, and maximum error136/33785 atB33785. It found no tolerance failures and no recorded borrows through131072. This reruns donor code on shared retained source data, so it is a replay rather than an independent source computation.

A separate integration-time implementation in `scripts/main_xxvi_source_phase_probe.py` independently computed512 literal Fraction states and512 growing-CRT states, checked15 exact Gaussian-rational transport controls, rejected orientation/forgotten-winding/zero-inverse mutants, and recounted all32768 retained shells with a sliding joint table. It reproduced all three extrema. Its residue normalized-content hash agrees with the stored hash above; the file-byte hash including the final newline is `c8868a139dee1b217c654da72f70480fc6e3bbbc619760b137e5c7abce37b08e`. These hash domains are deliberately distinguished. The standalone probe and all5 focused unittest cases passed. Its artificial Gaussian-rational perturbations calibrate the transport inequality; no Gamma quadrature certification is claimed. None of this source-sharing audit is fresh empirical evidence for an eventual digit theorem.

## Verdict and next offensive

No new source-selected saving has been established. The smallest still-unproved statement in this combined route is positive lower shell density of the two selected carry residues on A₀=0's exact growing-modulus orbit, equivalently α∉E. The weakest maintained overall π rung is R0, which is less restrictive than this selected gate.

The next offensive should seek a zero-seed/height-sensitive signed potential or a direct one-sided count bound on Aₙ in[Lₙ,3Lₙ), with the exact Lₙ/Rₙ history retained. Before searching data, require any proposed potential to state its boundary cost as a function of seed height. If a proposed positive-count lower bound has an additive boundary debt that is uniform over the larger seed family, an A-FS zero word of length N forces that debt to be at least the claimed positive rate times N. Thus a uniformly bounded seed-blind debt is impossible; no unconditional seed-height lower bound is asserted here.

The cheapest decisive experiment for a proposed estimate is exact replay on short rational A-FS shadows at increasing N,L plus the B=8/M=48 denominator-grid control. If it survives only by using exact zero ancestry, then freeze constants and a fresh authentic source interval beyond131072, certify every carry and all integer shells in that interval, and compare the predicted bound. That can falsify the finite conjecture; an eventual theorem still requires the source-selected derivation.
