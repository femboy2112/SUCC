# Round 2: exact Gaussian descent, orbit saturation, and a real-observable obstruction

Read-only source: SUCC PR #325, commit `95ee2f1fab851afe1517d8ec5a0589885842426f`, `research/2026-10-27/GAUSSIAN_PRIME_RAMIFICATION_PI_FRONTIER.md`. Independent geometry/translator lane; no constructor/adversary conclusions imported.

**Result:** genuine proof steps about the authenticated Gaussian lift, plus an exact obstruction to a continuous real-phase bridge. These do not prove a signed Weyl saving or π normality. The orbit identification uses the original zero seed. The obstruction uses the actual four-pole forcing and its real decay; the phase-pair argument also applies to changed real selectors when the arithmetic clock is used as an external time label, so this is not a zero-selection advantage.

## Hole contract

- **Statement attacked:** identify exactly what the Gaussian extension adds beyond the rational-time odometer, and decide whether the selected real phase can be a continuous observable of that completed clock.
- **Truth state:** the descent, all-level cycle counts, invariant transverse valuation, finite-level ramification defect, and noncontinuity/uniform-approximation obstruction below are proved.
- **Hypotheses:** the authentic rational source `r=A/D`, the uniformly convergent Gaussian series Ψ, its source-specific zero Ψ(0)=0 proved upstream, and the real rational zero-seeded states U_n.
- **Quantifiers:** all Gaussian integral inputs; every λ-adic depth m≥1; every nonzero integer Fourier frequency h; every finite-clock observable, with an explicit positive error bound uniform in m.
- **Weakest sufficient form:** for the no-continuous-bridge result it suffices that r(n)→0 in R and that h r(a) is nonintegral for some positive a. Both hold for every h≠0 for the authentic source.
- **Dependency closed:** Gaussian virtual extension → exact rational descent/leaf saturation; continuous finite-clock observable → impossible representation of authentic selected real phase.
- **Novelty tax:** this is a proved geometric classification and regularity obstruction, not another Weyl criterion. It does not merely restate normality; it holds independently of whether the phase is equidistributed.
- **Known route evaded:** a full Gaussian Haar law cannot be substituted for the natural-time law. The proof quantifies the mismatch and shows that even on the correct rational leaf the real character lacks the continuity needed for a direct compact-clock transfer.
- **Cheapest falsifier:** enumerate R/(λ^m) for small m, especially m=2, where conjugation-fixed residues strictly exceed rational residues; test the source transverse congruence and cycle counts. An executable probe through m=12 passed.
- **Computational boundary:** every infinite claim has an algebraic/topological proof below. The finite probe is a corroboration and rejects the deliberately false finite descent claim.
- **Next lamp:** a noncontinuous, source-authentic correlation estimate coupling the real phase to the rational clock with explicit orbit control. Gaussian Haar averaging alone cannot supply it.

## 1. Independent algebra audit of #325

Write

A(x)=120x²−89x+16,
D(x)=(2x−1)(4x−1)(8x−7)(8x−3)
=512x⁴−1024x³+712x²−206x+21.

Direct exact symbolic calculation gives Res(A,D)=−7,372,800=−2¹⁵3²5² and Disc(D)=3,774,873,600=2²⁴3²5². The displayed degree-four homogeneous resultant gains 512², giving −2³³3²5². The qualification about fixed normalized coordinates is correct; this does not establish minimal bad reduction under all coordinate changes.

For z,w∈R=Z₂[i], D is a unit and

(A(z)−A(w))/(z−w)=120(z+w)−89

is a unit, whereas the corresponding D quotient is divisible by 2. Therefore r is an isometry. The tail Ψ−r is 16 times a 1-Lipschitz map, so Ψ is an isometry too. It permutes each finite λ quotient, and compatibility/completeness give a bijection R→R. All this is valid also in the ramified ring: reduction modulo λ sees 89 as a unit and 2 as zero.

The numerator pair formula at p≥7 and its mixed-valuation pair count are correct. In particular the linear transformation determinant is 240, so the exclusion p∈{2,3,5} is essential. The mod-7 norm identity and the denominator's failure to preserve its numerator mirror also check. No algebraic error in the claims audited here was found.

The inherited zero argument was inspected: the generating rational integrand and logarithmic primitive use convergent logarithms of −i,i,−1 at the endpoint. Their logs vanish. This supplies the genuine source-specific Ψ(0)=0 used to identify Ψ(n)=U_n. The new statements below do not claim that zero theorem as new.

## 2. Exact Galois descent and transverse valuation

Let σ(a+bi)=a−bi. Every coefficient of r is rational, and the Ψ series converges uniformly, so

Ψ(σz)=σΨ(z).

Since Ψ is injective,

Ψ(z)∈Z₂ ⇔ Ψ(z)=σΨ(z) ⇔ Ψ(z)=Ψ(σz) ⇔ z=σz ⇔ z∈Z₂.

Together with bijectivity this proves the exact set identity

**Ψ(Z₂)=Z₂ and Ψ⁻¹(Z₂)=Z₂.**

This is stronger than saying that rational natural times happen to have rational images: there are no imaginary inputs whose images enter the rational sector.

Write Ψ(a+bi)=c+di with a,b,c,d∈Z₂. If b≠0, conjugation equivariance and isometry give

v_λ(2di)=v_λ(Ψ(z)−Ψ(σz))=v_λ(z−σz)=v_λ(2bi).

Hence

**v₂(d)=v₂(b).**

For b=0 both imaginary parts vanish. In particular every closed tube Z₂+2^j i Z₂, and every exact transverse valuation stratum, is preserved by Ψ and Ψ⁻¹.

There is also an exact distance statement. For b≠0,

sup_{x∈Z₂} v_λ(a+bi−x)=2v₂(b)+1.

The lower bound is attained by x=a+b because i−1 has λ-valuation one. No rational adjustment can raise it: after writing z−x=b(i−1)+(a+b−x), the first summand has odd λ-valuation, while the second has even valuation (or is zero). Therefore Ψ preserves the exact distance to the rational subspace, not just its zero set.

A source-specific refinement follows from the actual coefficients. In the restricted power-series ring, modulo 4,

r(z)≡3z+2z²,

because A≡−z and D≡1+2z. Since Ψ−r is divisible by 16, its divided difference with its conjugate gives

**Im Ψ(a+bi)/b ≡ −1 (mod 4), for every b≠0.**

Indeed the quotient for 3z+2z² is 3+2(z+σz)=3+4a≡−1 mod4; all omitted restricted-series coefficients contribute multiples of 4. Thus the first transverse behavior is an authenticated deterministic sign congruence, not an independent Gaussian random channel.

## 3. All finite levels: cycle decomposition and the descent defect

For m≥1 let R_m=R/(λ^m). Its size is 2^m. The image Q_m of Z₂ has size

|Q_m|=2^ceil(m/2),

since λ^m R∩Z₂=2^ceil(m/2)Z₂. The quotient by the rational additive subgroup has size 2^floor(m/2).

Define the source successor

T=Ψ∘(z↦z+1)∘Ψ⁻¹.

On R_m, addition by 1 has order exactly 2^ceil(m/2). Therefore

**T_m has precisely 2^floor(m/2) disjoint cycles, each of length 2^ceil(m/2).**

The rational sector Q_m is exactly one of these cycles. In particular at the authentic depth m=8k,

- full Gaussian states: 16^(2k);
- states visited by natural time: 16^k;
- number of equal-length cycles: 16^k;
- selected occupation fraction: 16^(−k).

The enlargement has introduced distinct invariant cycles; natural time does not acquire extra observations by embedding its old cycle in the larger ring.

The finite conjugation-fixed set is more subtle than infinite descent. If z=a+bi, then σz=z modulo λ^m iff

2+2v₂(b)≥m.

A class is rational modulo λ^m iff its distance to Z₂ has valuation at least m, equivalently

2v₂(b)+1≥m.

Consequently

**Fix(σ on R_m)=Q_m when m is odd, whereas |Fix(σ)|=2|Q_m| when m is even.**

For m=2k the extra fixed classes have b≡2^(k−1) modulo 2^k. They constitute one additional full successor cycle. At m=2k+1, the fixed set is rational again; hence this extra fixed cycle has **no conjugation-fixed lift even one level higher**. The finite false implication “conjugation-fixed ⇒ rational” is a genuine ramification artifact, not a new rational branch. Its smallest counterexample is i modulo λ²=(2): i=−i there, but i is not a rational residue.

At infinite depth the orbit closures are exactly

L_b=Ψ(Z₂+bi), b∈Z₂.

T is conjugate on each L_b to addition by 1 on Z₂. Every orbit is dense in its own L_b; L_0=Z₂ is precisely the natural-time leaf. The measurable first integral B(y)=Im Ψ⁻¹(y) labels the leaves. Thus the Gaussian extension is an exact family of odometers, not a minimal transformation of the whole Gaussian ring.

## 4. A source-authentic real-phase obstruction

Set z_n(h)=exp(2πihU_n), with the literal real rational states U_0=0 and U_n=16U_(n−1)+r(n). Fix any integer h≠0.

### Theorem: no continuous extension of the selected real phase

There is no continuous f:Z₂→C with f(n)=z_n(h) for all n≥0. Equivalently, there is no continuous observable F of the completed arithmetic state with F(U_n)=z_n(h); there is also no such continuous F on the Gaussian state space R.

**Proof.** Suppose f exists. For each x∈Z₂ choose positive ordinary integers n_j→x 2-adically with n_j→+∞ in the real ordering. Since r(n)=O(n^(−2)) in the real completion, the exact phase recurrence and continuity imply

f(x+1)=f(x)^16.

Because f(0)=z_0=1, this gives f(n)=1 for every nonnegative integer n. Thus hU_n∈Z and, by subtracting adjacent source recurrences, h r(n)∈Z for every positive integer n.

Choose a prime p>5 not dividing h, and set a=(p+1)/2. Then

D(a)=p(2p+1)(4p−3)(4p+1),
A(a)=(60p²+31p+3)/2.

Exactly one displayed denominator factor has p-valuation one; A(a) is a p-unit because A(a)≡3/2 mod p. Therefore v_p(h r(a))=−1, contradicting integrality. The state-coordinate formulation follows by composing F with the continuous Ψ. QED.

This theorem does not assert any failure of equidistribution. Equidistributed real phases can be extremely discontinuous in an unrelated profinite topology. It identifies why the already-proved compact-clock structure does not directly transport the real characters.

### Quantitative finite-clock obstruction, at every depth

Let m≥1, q=2^ceil(m/2), and let g:R_m→C be **any** function. Define its error on the authentic selected orbit by

ε= sup_{n≥0} |z_n(h)−g(U_n mod λ^m)|.

Then

**ε ≥ κ_h := (1/34) sup_{a≥1}|exp(2πih r(a))−1| > 0.**

The bound is independent of m and allows arbitrary behavior of g away from the selected cycle.

**Proof.** Put b=a+tq. The states at a and b occupy the same finite bin, as do a−1 and b−1. Hence each corresponding phase difference is at most 2ε. For unit complex numbers, |u^16−v^16|≤16|u−v|. Dividing the two exact source recurrences gives

|exp(2πih r(a))−exp(2πih r(b))|
≤ |z_a−z_b|+16|z_(a−1)−z_(b−1)|
≤34ε.

Let t→∞ and use r(b)→0. Supremize over a. Positivity follows from the prime witness used above. QED.

There is also a fully finite-horizon version. For 1≤a<b=a+tq<N, the maximum error over 0≤n<N obeys

**ε_(N,m) ≥ |exp(2πih r(a))−exp(2πih r(b))|/34.**

No asymptotic equidistribution assumption enters this inequality. For h=1 one may take a=1, where r(1)=47/15; the infinite-horizon lower bound is at least 2 sin(2π/15)/34.

This refutes a particularly tempting bridge: increasing Gaussian precision cannot give uniform finite-clock approximations of the authentic real Fourier phase. A useful bridge must be weaker than uniform approximation and must control the actual selected orbit separately.

## 5. Precise saturation boundary

The rational sector has full finite occupation within its own cycle and zero asymptotic fraction of the full Gaussian quotient. At infinite depth it has zero Haar mass in R; its mth neighborhood has mass 2^−floor(m/2). The natural orbit itself is countable and has Haar mass zero even within the rational leaf.

For any prescribed bounded sequence c_n, assigning H(Ψ(n))=c_n and H=0 elsewhere defines a Borel observable whose Haar integral is zero but whose selected-orbit sequence is exactly c_n. This elementary fact is not a counterfeit forcing construction; it states that Borel regularity and Haar integrals cannot constrain values on this orbit. The authentic phase is moreover excluded from the continuous observable class by the previous theorem.

Therefore the earned Gaussian lift is analytically coherent and arithmetically saturated on its selected leaf, but extra complex points are virtual extension values, not additional real source observations. A signed real-phase estimate still needs a new source-dependent argument connecting this singular orbit sampling to a weaker regularity/correlation class.

## 6. Exact verification record

`pi_gaussian_descent_probe.py` implements Gaussian quotient arithmetic independently, including the tilted odd-depth quotient, direct rational-source evaluation, and the truncated Ψ sum sufficient at each λ depth.

For every m=1,…,12 it verifies:

1. Ψ is a permutation of all 2^m residues;
2. Ψ commutes with conjugation;
3. Ψ maps the rational subset onto itself;
4. the odd/even conjugation-fixed-set formulas;
5. preservation of all visible imaginary valuation strata;
6. the source transverse sign congruence at even depths;
7. the complete successor cycle count and every cycle length.

At m=8 it finds 256 Gaussian residues, 16 rational residues, 32 conjugation-fixed residues, and 16 cycles of length 16. At m=12 it finds 4096 residues, 64 rational residues, 128 fixed residues, and 64 cycles of length 64. The mutation “all fixed residues are rational” is explicitly rejected at m=2 by i.

**Claim state:** genuine proof steps and a decisive obstruction to one proposed bridge. No normality/RH claim or proposed merge. This dossier is integrated additively on the separate research branch.

## 7. Root-proposed strengthening: one explicit constant for every frequency

The quantitative obstruction can be made uniform over **all** nonzero integer h, as well as all Gaussian depths and all complex-valued finite observables:

**sup_(n≥0) |exp(2πihU_n)−g(U_n mod λ^m)| > 47/39168.**

Here m≥1 and g:R_m→C are arbitrary. This is a strict lower bound on uniform approximation; it is not a mean-square or density bound.

Independent verification of the proposed constant: put H=|h|≥1 and a=ceil(sqrt(4H)). Then a≥2 and

4H≤a²≤9H,

because a≤2sqrt(H)+1≤3sqrt(H). For n≥1 the exact numerator identity

A(n)−47n²=(n−1)(73n−16)≥0

and 0<D(n)<512n⁴ prove r(n)>47/(512n²). For n≥2, r(n)<1/n² can be checked without importing any analytic estimate: setting n=t+2 gives

D(n)−n²A(n)=392t⁴+2201t³+4494t²+3902t+1185>0.

Thus

47/4608 < H r(a) < 1/4.

For 0≤u≤1/2, concavity of sin on [0,π/2] gives 2sin(πu)≥4u. Hence

|exp(2πih r(a))−1|=2sin(πH r(a))≥4H r(a)>47/1152.

Dividing by 34 in the previously proved phase-pair bound yields the asserted constant 47/39168. The proof did not require g to take values on the unit circle: only the authentic z_n have unit modulus.

The qualitative no-continuous-extension proof also admits a shorter final contradiction. It forces h r(n) to be an integer for every n, but positivity and real decay give 0<|h|r(n)<1 for all sufficiently large n. The prime-denominator witness in Section 4 remains a separate exact arithmetic derivation of the same contradiction.

## 8. Independent audit of the constructor's full-source collision theorem

At the root's request, this lane subsequently read `PI_FULL_SOURCE_DELAY_RECONSTRUCTION.md` and audited its p=7 proof and p=11,241 holdouts. This audit occurred after the independent geometry/real-observable work above.

**Verdict: the source-specific all-level collision and delay-reconstruction proofs check.** The elementary square-collision count on pZ/p^L is correct, including L=1. The Morse coordinate is an isometry because its derivative is 1 modulo p and its higher Taylor coefficients are integral on the source disks. Each regular pair of residue disks contributes exactly p^(L−1), and the hypothesis that a critical output has no other residue preimage correctly excludes mixed critical/regular contributions.

At p=7 the two-delay intersection Jacobian determinant is 4. At p=11 the reciprocal-coordinate determinant is 7. Thus the unique lifts of the two exceptional ordered orientations persist at every level. The displayed p=7 unordered pairs through L=5 were independently recovered by direct digit-by-digit Hensel lifting. The triple-source isometry follows from injectivity modulo p plus a unit derivative in at least one coordinate on each residue disk.

An independent script, `pi_prime7_independent_audit.py`, used projective cross-products for the base certificates and the opposite chart priority from the constructor for prime-power counting. It reproduced all counts through 7^5 and 11^3 and added the fresh 241^2 holdout:

| p | critical inputs modulo p | W' at critical inputs | C_1(p,1) | off-diagonal unordered two-delay pairs |
|---|---|---|---|---|
| 7 | 1,5 | 1,1 | 19 | {2,3} |
| 11 | 1 | 10 | 27 | {2,4} |
| 241 | 152 | 230 | 497 | none |

At p=241,L=2 the independently counted values are C_1=177617 and C_2=C_3=58081, exactly as the theorem predicts. All critical values are uniquely attained modulo p, all critical points are simple, and every consecutive pair contains a coordinate with unit derivative.

The signed energy identity and bound also check exactly. At p=7,11 the sole exceptional double fiber contributes `2q Re(Z_a conjugate(Z_b))/N²`, whose absolute value is at most `(2/q)(1+q/N)²`. At p=241 the two-delay energy already equals time-residue energy; three delays give equality at all three primes. No sign saving follows from these identities.

One wording refinement is advisable for the general local lemma: explicitly require **integral Taylor coefficients in the chosen input coordinate**, as the authentic rational source automatically has on every selected chart disk. A unit derivative alone for an unrestricted analytic function is insufficient: on pZ_p, f(x)=x−x^p/p^(p−1) has unit derivative everywhere for odd p, yet f(0)=f(p)=0. This does not affect the constructor's source proof because its numerator and denominator have integral coefficients and its chart denominator is a unit; it only prevents overgeneralizing the displayed lemma.
