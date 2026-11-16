# Leah–Gamma Twist: Gamma–prime construction and source-energy audit

## Prospective test declaration — written before new probe execution

Baseline: `db9fb4b84672050efa79b13377f1e73364598a14` (Main XXV).
Branch: `research/leah-gamma-twist-2026-11-13`. The authentic forcing,
zero anchor, archived proofs and production modules remain unchanged.
The following candidates were derived from paper algebra after reading
the archive, before running this round's new probe. They are not blind
discoveries. The numerical locations below are prospective controls;
finite results will not be extrapolated to an all-horizon theorem.

**Candidate A: sharp all-seed state-energy floor.** For fixed nonzero
integer h, A→∞, L→∞ and L≤CA, conjectured-to-be-proved here:

\[
\inf_{s\in\mathbb R}\frac1L\sum_{n=A}^{A+L-1}
[1-\cos(2\pi h U_n(s))]
\sim\frac{\pi^2h^2}{2048L}\sum_{n=A}^{A+L-1}n^{-4}.
\]

The coherent same-forcing seed s=−π/16 asymptotically attains this
floor. For completed states U_n+T_n, that seed has energy exactly zero.
The method is inherited from the archive's lag-energy minimization;
the claim here concerns state energy and the explicit loss on completion.

**Candidate B: quantified fixed-lag Gamma transport.** For any fixed
polynomial P with integer coefficients, write P(z)=(z−1)^qS(z),
S(1)≠0. The inherited algebra is
P(E)U_n(s)=P(16)16^n(π/16+s)−P(E)T_n. The new calculation to audit
is an explicit rational beta-integral remainder for P(E)T_n, using the
literal four-pole density. This is a claim about commuting finite lag
polynomials, not all ordered or nonlinear observers.

| Control | Prospective specification and verdict |
|---|---|
| Source calibration | Four separate poles versus the existing combined rational formula, n=1,...,128; every value must agree exactly. |
| Fixed-lag holdouts | n=137,263,521,1031; P=(z−16)(z−1)^q for q=0,1,2,3, plus P=z−1 and z²+1; exact recurrence identities and the proposed rational beta bounds must hold. |
| State-energy holdouts | A=137,263,521,1031, L=A, h=1; prove branch conditions using rational tail enclosures, certify the finite nonlinear-minimum bracket, and compare its A⁴ scaling with the proved remainder, never a fitted tolerance. |
| Coherent counterseed | Represent U_n(−π/16)=−T_n by rigorous tail intervals. Completed energy must be exactly zero algebraically. |
| Rational alias | Completed boundary 1/15 is fixed modulo one under ×16; it is nonnormal despite a positive frequency-one R0 gap. |
| Old-cofactor rational shadows | A=31,63,127; use only the authentic old source clock Q_A and the finite completion α_(3A) to choose a rational seed. Certify its dyadic-epoch coherence and preservation of subsequently born prime passports. This control mechanism is inherited, not a new invention. |
| Prime/Gamma clock distinction | p=137,281,593 at n=(p+7)/8. Check exact newborn residue and old-cofactor reconstruction; compare the corrected forcing window's candidate capacity on the forcing clock and the accumulated state clock. |
| Source mutation | Add 1/(8n−7), changing the zero total residue to one. The source scale becomes n⁻¹ and the state-tail energy scale n⁻²; it must not pass the unchanged four-pole identities. |

All exact checks use integers and rational intervals. Any diagnostic
decimal formatting is presentation only. Failures and deviations from
this declaration will be recorded below rather than removed.

## Results and proofs

Pending at the time of this prospective declaration.

---

## Completed audit — scope and result

**Paper-proved extension, with exact finite implementation checks:** for the
literal four-pole forcing, the sharp minimum raw state energy over all seeds
is of order A⁻⁴ on a dyadic epoch. Its leading constant is
7π²h²/49152. The same-forcing coherent seed asymptotically attains it;
after exact completion its energy is identically zero. Thus a real,
source-dependent positive energy can be entirely accounted for by the tail
that completion removes. This result prices that effect; it does not prove
R0 or a constant positive selected energy.

The proof adapts the already archived **lag-energy** minimization in
`research/2026-10-30/gamma_twist/signed/SHARP_SEED_ENERGY.md`. The
state-energy asymptotic and finite bracket below are the claimed extension
within this round, without a scholarly priority claim. The fixed-lag algebra,
Gamma representation, source-prime births, corrected Gamma window and
old-cofactor counterseeds are inherited results. Their provenance is
explicit below. The rational beta remainder is an additional quantified
version of that inherited transport, not a newly discovered representation.

**Execution:** Main XXV is the source baseline named above. Tests ran at
`17e58672bbd3954a8e72ec9de9ca90c1c2b5de0d`, the root's preregistration-only
commit atop that baseline. Neither core source nor historical proof files
were edited by this bearing. The initial prospective file has SHA-256
`3af86719e304ce8961f7ec4833f798debc5e71bb6ed70f67c95c5d23b5bb599d`
and was written at 2026-11-13 00:15:46 UTC. The text above this separator is
retained from it. This report and its tests are a same-model derivation and
implementation pass, not an external referee or independent source family.

| Claim | Status and scope |
|---|---|
| GP-1: finite state-energy minimum bracket | Paper-proved below, all real seeds; exact rational implementation checked at the declared epochs. |
| GP-2: sharp dyadic A⁻⁴ constant | Paper-proved corollary; extends the inherited lag-energy argument. No asymptotic inference from finite data. |
| GP-3: fixed-lag beta remainder | Paper-proved for a fixed nonzero integer polynomial, with an explicit coefficient-dependent error. |
| GP-4: Gamma window on two different clocks | Re-derivation and exact controls of the inherited #498 distinction; no state pinning claim. |
| GP-5: old-cofactor rational shadows | Exact finite controls of an inherited changed-seed mechanism; the zero anchor is deliberately not preserved. |
| Selected zero-seed R0 | OPEN in this bearing. No signed old-cofactor inequality with a horizon-independent gain has been proved here. |

## 1. Exact source, residue cancellation and Gamma translation

Write e(t)=exp(2πit), x=π/16, and let U₀(s)=s. The source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_n(s)=16U_{n-1}(s)+r(n).
\]

Its exact positive moment representation is

\[
r(n)=\int_0^1 t^{8n-8}(4-2t^3-t^4-t^5)\,dt
=\int_0^1t^{8n-8}(1-t)N(t)\,dt,
\]

where N(t)=t⁴+2t³+4t²+4t+4=(t²+2)(t²+2t+2).
In particular r(n)>0 and r(n) strictly decreases. Summing the positive
geometric tail, with no conditional interchange, gives

\[
T_n=\int_0^1t^{8n}(1-t)w(t)\,dt,
\qquad
w(t)=\frac{N(t)}{16-t^8}
=\frac1{(2-t^2)(t^2-2t+2)}. \tag{1}
\]

The endpoint zero is exactly the cancellation 4−2−1−1=0. Since w(1)=1,
T_n=1/(64n²)+O(n⁻³). The affine completion is exact:

\[
U_n(s)+T_n=16^n(x+s),\qquad
T_{n+1}=16T_n-r(n+1). \tag{2}
\]

These are inherited source identities, including the two quadratic atoms.
They are not statistical assertions about the selected phase.

### The ordinary Gamma product and the chronological product are different

Put c=(7,4,3,2), a_c=1−c/8 and w_c=(4,−2,−1,−1). On the disk |z|<1,
all factors below are nonzero and the analytic logarithm is fixed to zero
at z=0. Repeated Γ(v+1)=vΓ(v) gives the exact finite identity

\[
G_N(z)=\prod_{n=1}^N\prod_c\left(1+\frac{z}{8n-c}\right)^{w_c}
=\prod_c\left[
\frac{\Gamma(N+a_c+z/8)\Gamma(a_c)}
{\Gamma(a_c+z/8)\Gamma(N+a_c)}
\right]^{w_c}. \tag{3}
\]

The usual Gamma-ratio asymptotic, with fixed parameters and N→+∞, gives

\[
G_\infty(z)=\prod_c
\left[\frac{\Gamma(a_c)}{\Gamma(a_c+z/8)}\right]^{w_c}.
\]

The N^{zΣw_c/8} factor cancels because Σw_c=0. Equivalently, the logarithmic
series converges locally uniformly on |z|<1 by its O_z(n⁻²) summands.
The derivative (log G_N)'(0) is Σ_{n≤N}r(n), **not U_N**.

The authentic chronological object is instead

\[
H_N(z)=\prod_{n=1}^N\prod_c
\left(1+\frac{z}{8n-c}\right)^{w_c16^{N-n}},
\quad H_N=H_{N-1}^{16}\prod_c\left(1+\frac z{8N-c}\right)^{w_c},
\quad (\log H_N)'(0)=U_N(0). \tag{4}
\]

Thus the exact boundary character is e((log H_N)'(0)). The exponentially
weighted chronology cannot be discarded when replacing this product by
(3). Recovering r(n) from a sufficiently rich Gamma/Mellin boundary, then
computing U_N, is identification; bounding its signed circle means is a
separate assertion.

Classical analytic ingredients and hypotheses: [NIST DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1)
is Γ(z+1)=zΓ(z); [5.11.12](https://dlmf.nist.gov/5.11.E12) is the fixed-parameter
Gamma ratio asymptotic in a sector away from the negative axis; here its
argument N is positive real. [5.12.1](https://dlmf.nist.gov/5.12.E1) is Euler's
beta integral for Re a>0, Re b>0. All beta parameters below are positive
integers. These classical identities carry no novelty claim.

## 2. Rational beta bounds for the literal tail

For integer q≥0 define

\[
I_q(n)=\int_0^1t^{8n}(1-t)^{q+1}\,dt
=\frac{(q+1)!}{\prod_{k=1}^{q+2}(8n+k)}. \tag{5}
\]

The expansion N(t)Σ_{j≥0}t^{8j}/16^{j+1} has nonnegative coefficients,
so w, w′ and w″ are nonnegative and increasing on [0,1]. Direct
differentiation gives w(1)=1, w′(1)=2, w″(1)=8. Taylor's formula with an
integral remainder therefore gives, everywhere on that interval,

\[
1-2(1-t)\le w(t)\le1-2(1-t)+4(1-t)^2,
\qquad w(t)\le1.
\]

Consequently the following entirely rational enclosure is valid for n≥1:

\[
\boxed{I_0(n)-2I_1(n)\le T_n\le
\min\{I_0(n),I_0(n)-2I_1(n)+4I_2(n)\}.} \tag{6}
\]

The lower endpoint is (8n−1)/[(8n+1)(8n+2)(8n+3)] and is positive.
The interval width is at most 4I₂(n)=O(n⁻⁴). The archive already proves
the sharper all-derivative asymptotic sandwich
0<1/(64n²)−T_n<7/(512n³), and its derivative analogues, in
`critical_chirp_source/front_ah/PROOFS.md`, AH-01. Formula (6) is used here
because it is a simple exact finite enclosure, not because the tail order
was previously unknown.

## 3. GP-1: finite sharp state-energy bracket

Fix integers A≥1, L≥2 and h≠0. Set f(u)=1−cos(2πu) and

\[
M=\sum_{j=0}^{L-1}f(hT_{A+j}),\quad d_j=-hT_{A+j},
\quad a_j=16^{j-L+1},
\quad Q=\sum_jd_j^2-\frac{(\sum_ja_jd_j)^2}{\sum_ja_j^2}. \tag{7}
\]

**Theorem.** If

\[
\frac{289M}{8}<\frac14,
\qquad \max_{0\le j<L-1}|h r(A+j+1)|<\frac12, \tag{8}
\]

then

\[
\boxed{2\pi^2\left(1-\frac{\pi^2M}{24}\right)Q
\le\inf_{s\in\mathbb R}\sum_{j=0}^{L-1}f(hU_{A+j}(s))
\le2\pi^2 Q.} \tag{9}
\]

**Proof.** The initial circle coordinate h16^A(s+x) ranges over the whole
circle. The finite continuous energy has a minimum. At s=−x its energy
is M. Choose centered representatives u_j∈[−1/2,1/2] for a minimizing
orbit. The elementary chord inequality f(u)≥8u² on that interval gives
|u_j|≤√(M/8). The quantity

\[
u_{j+1}-16u_j-h r(A+j+1)
\]

is an integer. Its absolute value is at most
17√(M/8)+|h r(A+j+1)|<1 by (8), so it is exactly zero. This is where the
integer carries are paid for; no smooth interpolation replaces them.
By (2), d_j solves the same inhomogeneous recurrence. Hence
u_j=d_j+a_jτ for some real τ. The least possible quadratic norm of this
affine line is precisely Q, by completing the square.

For every real u, f(u)≤2π²u². Evaluate that inequality at the quadratic
minimizer τ=−Σa_jd_j/Σa_j² to obtain the upper bound, without requiring
those trial values to be centered representatives. For the actual nonlinear
minimizer, Taylor's inequality gives

\[
f(u_j)\ge2\pi^2u_j^2-\frac23\pi^4u_j^4
\ge2\pi^2\left(1-\frac{\pi^2M}{24}\right)u_j^2.
\]

Summing and using Σu_j²≥Q proves the lower bound. The coefficient is
positive under (8). This is a global minimum over all seeds, not a local
stationary-point computation. ∎

### GP-2: sharp asymptotic and the exact loss on completion

For fixed h≠0 and C>0, let A→∞, L→∞, 2≤L≤CA. Then

\[
\boxed{\inf_s\frac1L\sum_{n=A}^{A+L-1}f(hU_n(s))
\sim\frac{\pi^2h^2}{2048L}\sum_{n=A}^{A+L-1}n^{-4}.} \tag{10}
\]

Indeed T_n=1/(64n²)+O(n⁻³) uniformly on this range. The projection loss
in (7) obeys

\[
0\le\frac{(\sum a_jd_j)^2}{\sum a_j^2}
\le (16/15)^2 h^2T_A^2=O_h(A^{-4}),
\]

whereas Σd_j² is bounded above and below by positive constants times
L A⁻⁴. Thus the relative projection loss is O(1/L). Also M=O_h(LA⁻⁴)
tends to zero, so (8) holds eventually and the two bounds in (9) agree
asymptotically. This proves (10), with the relative losses explicitly
coming from O(1/A), O(1/L), and O_h(L/A⁴).

For L=A, the integral of t⁻⁴ from 1 to 2 equals 7/24, giving

\[
\boxed{\inf_s\frac1A\sum_{A\le n<2A}f(hU_n(s))
\sim\frac{7\pi^2h^2}{49152}\,A^{-4}.} \tag{11}
\]

For L=o(A) the constant is π²h²/2048. More generally, if L/A→θ>0,
the constant multiplying A⁻⁴ is
π²h²[1−(1+θ)⁻³]/(6144θ).

The single fixed counterseed s=−x gives U_n=−T_n, and its energy has the
same leading term in (10). Yet its **completed** state is zero exactly.
Consequently this source-only lower bound cannot transfer as a positive
constant to the completed phase or prove R0.

The raw/complete comparison can be stated sharply by the elementary
reverse triangle inequality in the finite ℓ² space. If
A_raw=L⁻¹Σf(hU_n) and A_comp=L⁻¹Σf(h(U_n+T_n)), then

\[
|\sqrt{A_{\rm comp}}-\sqrt{A_{\rm raw}}|
\le\sqrt{L^{-1}\sum f(hT_n)}
\le\sqrt2\pi|h|\sqrt{L^{-1}\sum T_n^2}=O_h(A^{-2}). \tag{12}
\]

To see this, use √f(u)=|e(u)−1|/√2 and
|e(h(U+T))−e(hU)|=|e(hT)−1|. Equality holds in the first inequality
for the coherent counterseed. Thus completion can remove the entire
sharp A⁻⁴ raw-energy floor. Formula (12) is a classical chord-norm
consequence; it was added after the prospective declaration as explanatory
algebra, not as an independently held-out finding.

For comparison, a quick seed-uniform inequality follows from
|e(hr(n+1))−1|≤|e(hU_{n+1})−1|+16|e(hU_n)−1| and the ℓ² operator norm
of the shift-minus-16 operator:
Σf(hU_n)≥(1/289)Σf(hr(n+1)), with the latter sum omitting the final endpoint.
It already gives the A⁻⁴ order. The minimization above recovers the sharp
bulk coefficient, corresponding asymptotically to division by 15²,
and identifies exactly the seed that attains it to leading order.

### Exact implementation of the bracket

Let [l_j,u_j] be (6), multiplied by |h|. The code uses

\[
\begin{aligned}
Q_-&=\max\{0,\sum l_j^2-(\sum a_ju_j)^2/\sum a_j^2\},\\
Q_+&=\sum u_j^2-(\sum a_jl_j)^2/\sum a_j^2,\\
\overline M&=20\sum u_j^2>M.
\end{aligned}
\]

All are rational. Conditions (8) are certified with M replaced by
M̄ and monotonicity of r. The inherited Machin/arctan interval encloses
π independently of the BBP digit source. Replacing the positive factors
in (9) by outward rational bounds gives the displayed finite minimum
enclosures. No nonlinear optimizer, floating π input, or sampled seed
grid is used to certify a minimum.

## 4. GP-3: a quantified finite-lag filter law

Let P be a fixed, nonzero integer polynomial and write
P(z)=(z−1)^q S(z), with q≥0 and S(1)≠0. If S(z)=Σs_jz^j, set

\[
A_S=\sum_j|s_j|,\quad B_S=\sum_jj|s_j|,
\quad C_P=(2+7q/2)A_S+8B_S.
\]

Then, for every integer n≥1,

\[
\boxed{\left|P(E)T_n-(-1)^q8^q S(1)I_q(n)\right|
\le8^q C_P I_{q+1}(n).} \tag{13}
\]

**Proof.** Apply P(E) under the finite linear combination of the positive
integrals (1). Put V(t)=(1+t+⋯+t⁷)/8. Since
t⁸−1=−8(1−t)V(t), the integrand becomes
(-1)^q8^q t^{8n}(1−t)^{q+1}F(t), with
F(t)=w(t)V(t)^q S(t⁸). On [0,1], 0≤w≤1, 0≤w′≤2,
0<V≤1, 0≤V′≤7/2, |S(t⁸)|≤A_S and
|dS(t⁸)/dt|≤8B_S. Thus |F′|≤C_P and F(1)=S(1).
The mean value theorem followed by (5) proves (13). ∎

The relative error in the leading term is at most
(C_P/|S(1)|)(q+2)/(8n+q+3). The inherited completion identity is

\[
P(E)U_n(s)=P(16)16^n(x+s)-P(E)T_n. \tag{14}
\]

If P(16)=0, (13) therefore gives

\[
P(E)U_n(s)\sim
\frac{(-1)^{q+1}(q+1)!S(1)}{64n^{q+2}}
\]

for every seed. Its fixed-frequency energy is of order n⁻²q⁻⁴.
Such a filter erases the homogeneous selected phase. If P(16)≠0, it
retains the original completion at frequency P(16), with a quantified
small tail correction. For R0, a saving at one arbitrary multiplied
frequency is not automatically the required frequency-one bound.

This class consists of fixed finite **commuting linear lag polynomials**.
Nothing here asserts that every ordered, nonlinear, horizon-dependent,
or source-coupled observer reduces to this class. Identity (14) is already
explicit in `gamma_prybar/front4/FOURIER.md`, F3, and the earlier
mixed-lag/source-transport archive. Its rediscovery alone would not be a
new route. Formula (13) adds the explicit remainder and cancellation order.

The declared annihilators P=(z−16)(z−1)^q satisfy the exact rational
identity P(E)U_n=Δ^q r(n+1). Complete monotonicity from the positive
moment formula proves (-1)^qΔ^q r(n+1)>0 at every n. The probe checks
this separate source expression against the original rational recurrence.

## 5. GP-4: Gamma pins a forcing clock, not the accumulated state

At a first birth p=8n−7, p prime and p≡1 mod8, the authentic forcing is

\[
r(n)=\frac4p+\beta_p,\quad
\beta_p=-\frac{4p^2+33p+67}{(p+3)(p+4)(p+5)},
\quad C_p=\frac{(p+3)(p+4)(p+5)}8,
\quad\operatorname{den}r(n)=pC_p. \tag{15}
\]

Let δ(p)=1/p−log(1+1/p). The inherited #498 correction is

\[
g(p)=30\delta(p)-49/p^3,
\qquad 0<r(n)-g(p)<236/p^4\quad(p\ge41). \tag{16}
\]

For clarity, its coefficients can be recovered without numerical fitting.
Expand the three shifted poles through cubic order:

\[
r(n)=15/p^2-59/p^3+
\frac1{p^3}\left(\frac{54}{p+3}+\frac{64}{p+4}+\frac{125}{p+5}\right).
\]

The corresponding first terms of 30δ are 15/p²−10/p³. Their cubic
discrepancy is exactly −49/p³. Alternating logarithmic bounds put the
next contribution between 7.5/p⁴−6/p⁵ and 7.5/p⁴. The positive pole
remainder lies between 243/[p³(p+5)] and 243/p⁴. These imply positivity
and the upper bound 235.5/p⁴+6/p⁵≤236/p⁴ for p≥12, hence (16) in the
stated prime range.

Define the rational alternating endpoints

\[
\delta_+=\frac1{2p^2}-\frac1{3p^3}+\frac1{4p^4},
\quad\delta_-=\delta_+-\frac1{5p^5},
\quad l=30\delta_- -49/p^3,
\quad u=30\delta_+ -49/p^3+236/p^4.
\]

Then r(n) lies strictly inside [l,u), of width
W=236/p⁴+6/p⁵. Since C_pW<1 for p≥41, at most one member of
4/p+(1/C_p)ℤ lies in this interval. The actual forcing supplies one.
This is exact forcing identification from an already specified clock.

For the state, let Q_n=lcm_{j≤n}den r(j)=pC_n and A_n=Q_nU_n(0).
The newborn p does not occur in Q_{n−1} and occurs to first power in Q_n.
Hence A_n is an integer, A_n≡4C_n modp, and

\[
k_n\equiv(A_n-4C_n)/p\pmod{C_n},\qquad
U_n(0)\equiv4/p+k_n/C_n\pmod1. \tag{17}
\]

This keeps the old cofactor exactly. It is not an independent CRT draw.
The correct number of elements of a coset a+(1/C)ℤ in the half-open
real interval [l,u) is

\[
\lceil C(u-a)\rceil-\lceil C(l-a)\rceil. \tag{18}
\]

Using the same tiny Gamma interval on the much larger state clock still
leaves enormous capacity. **We do not claim U_n lies in that forcing
interval.** Even granting such an extra state enclosure would not identify
the old-cofactor address at the observed clocks. The asymptotic reason is
the inherited source-clock law log Q_n=(6+o(1))n versus log C_p=O(log p).

At the declared p=137,281,593 the forcing coset has exactly one candidate.
The respective state-cofactor clocks have 144, 294 and 616 bits, and
the same interval has more than 7·10³⁶, 8·10⁸⁰ and 5·10¹⁷⁰ candidates
respectively. Exact integer counts are in the JSON receipt; these coarse
lower bounds are presentation only. The reconstruction (17) and newborn
residue pU_n≡4 modp were checked exactly.

## 6. GP-5: hostile old-cofactor controls and the unpaid signed term

The irrational coherent seed s=−x is a valid real-dynamical control,
but it must not be passed into a rational p-primary residue calculation.
The separate rational construction is as follows. At an epoch A, put
Q_A=lcm_{j≤A}den r(j), M=3A, α_M=16⁻ᴹU_M(0), and choose k nearest
to Q_Aα_M. Set s_A=−k/Q_A. Then

\[
|s_A+x|\le\frac1{2Q_A}+16^{-M}T_M,
\quad\max_{A\le n<2A}|16^n(s_A+x)|
\le16^{2A-1}\left(\frac1{2Q_A}+16^{-3A}T_{3A}\right). \tag{19}
\]

Because log Q_A=(6+o(1))A and 2log16<6, the last bound tends to zero
exponentially. For the finite controls the code uses the sharper actual
signed interval α_M+s_A+16⁻ᴹ[l_M,u_M], instead of only the worst-case
nearest-integer error. The construction uses finite rational source data
and a proved tail bound, not π digits.

If p=8n−7 is prime with A<n<2A, p is new after A and is coprime to
Q_A. Therefore 16^ns_A is p-integral and

\[
pU_n(s_A)\equiv pU_n(0)\equiv4\pmod p. \tag{20}
\]

The old cofactor orientation has changed, while all these newborn prime
passports and every source-only Gamma statistic are retained. The initial
condition has changed; this does not refute any theorem that genuinely
uses U₀=0. It refutes a transfer that silently drops that anchor or its
old-cofactor winding. The archive already constructs stronger versions
preserving more denominator/additive data; (19)–(20) are controls of that
known mechanism, not new seed inventions.

At A=31,63,127 all three declared shadows certified a short arc. There
were respectively 10,17,31 checked newborn primes. At A=31 the completed
radius is below 0.010122. At A=63 it is below 4·10⁻¹¹. At A=127 it is
below 10⁻¹⁸, with the sharper exact outward bound in the receipt. None of
these seeds is zero. No claim that every old state denominator is retained
is made by this simpler control.

### What a nonfactorizing inequality still has to control

On any pulse-free p-primary birth window, write the full **completed**
character as a_n b_n, where a_n is the correctly transported p-primary
root of unity and b_n is the literal old-cofactor character times e(T_n).
Both are source-generated and time-ordered. Finite averaging gives the
identity

\[
\frac1L\sum a_nb_n=\overline a\,\overline b+
\frac1L\sum(a_n-\overline a)(b_n-\overline b). \tag{21}
\]

Here overlines mean empirical averages, not complex conjugates. This is
an algebraic, non-Hermitian covariance. An unweighted prime sum controls
the first factor; it does not control the signed covariance. In the exact
coherent control the full character equals one, so b_n=a_n^{-1} and the
covariance in (21) is exactly 1−|ā|². Thus a well-distributed primary
character can coexist with maximally coherent full phase, with the missing
contribution sitting precisely in the old-cofactor cross term.

A sufficient estimate toward R0 would need a fixed positive margin for
the real part of (21), **for the literal zero-seeded cofactor**, over a
family of windows covering the required dyadic epochs with controlled
loss. Applying absolute values, independently averaging CRT coordinates,
or replacing H_N by G_N does not supply that estimate. Stating this signed
covariance bound is a location of the remaining cut, not a proved new
lemma or a claim that its difficulty has decreased. This bearing found no
source-specific order or reciprocity law that bounds that term with a
horizon-independent gain.

## 7. Mutation and rational-alias controls

Adding 1/(8n−7) changes the total pole residue from zero to one. Its extra
tail is

\[
K_n=\int_0^1\frac{t^{8n}}{16-t^8}\,dt,
\quad
\frac1{15(8n+1)}-\frac8{225}I_0(n)
\le K_n\le\frac1{15(8n+1)}. \tag{22}
\]

Indeed v(t)=1/(16−t⁸) has v(1)=1/15 and 0≤v′≤8/225. Thus
nK_n→1/120, and the coherent raw-state energy for the mutated forcing is
of order n⁻² rather than n⁻⁴. This control fails the unchanged authentic
combined forcing identity exactly, at every declared test point. It
separates the role of residue cancellation from generic affine dynamics.

For the same forcing but seed s=1/15−x, completion is 16^n/15≡1/15 mod1.
Its frequency-one energy is the positive constant 1−cos(2π/15), so it
satisfies R0. Its frequency-15 energy is zero, so it is not normal. This
keeps the distinction between the requested one-sided R0 gap and full
normality. The rational alias is a real-seed control, not a rational
source-state passport claim.

## 8. Archive genealogy and novelty limits

| Archive | Relevant established result and its limit |
|---|---|
| #309, `2026-10-26/FOUR_POLE_ATOMIC_SUBSTRATE.md` | The exact two quadratic atoms, source-positive packet compiler, Gamma(2) endpoint law and grammar-dependent golden fixed point. Packet regrading changes the latter while preserving the source. These are not selected-orbit phase bounds. |
| #310, `OILY_TOTIENT_THIRD_SHADOW.md` and `OILY_MACARONI_SOURCE_MELLIN_HILBERT.md` | Source-conditioned connected Mellin/grade identities on an explicitly defined auxiliary carrier. Primitive grade characters can remain uniformly nonzero. The carrier's conditional independence is not independence across source times or primes. |
| #324, `2026-10-27/PI_SELECTED_BOUNDARY_CRT_FRONTIER.md` | Exact nonlinear Lipschitz source/completion transfer with a paid budget; carry discontinuities require a separate seam count. CRT Plancherel and finite-band aliases do not prove selected cancellation. |
| #337, `2026-10-27-furstenberg-kempner/KEMPNER_FURSTENBERG_FIREWALL.md` | Transcendence, finite irrationality exponent and auxiliary invariance can coexist with atomic limits. The Kempner control rejects the free-entropy inference. This is a general bridge refutation, not a counterexample to the original four-pole zero seed. |
| #459 descendants, `2026-11-01/prime_window_interferometry/PROOFS.md` | Full prime windows are not automatically an easier target: the archive gives an equivalence for bounded sequences. Signed full-versus-primary finite controls go in both directions. |
| #497, `2026-11-04/frobenius_prime_saturation/PROOFS.md` | Authentic source-prime transport and the corrected 6N original-source conductor exponent, rather than 8N. Denominator size does not determine the centered real numerator. |
| #498, `2026-11-04/gamma_pigeonhole/PROOFS.md` | The −49/p³ correction and p⁻⁴ Gamma window pin the cubic forcing cofactor. The exponentially larger accumulated cofactor remains. GP-4 rechecks this distinction. |
| #499, `prime_character_primal/PRIMAL_QUOTIENT_THEOREM.md` | A genuine four-class source action and angular/radial decomposition within the declared two-dimensional module. This is source-specific structure, not a selected real Fourier law by itself. |
| #500 descendants, `europa_weyl/radial/RADIAL_CONTROL.md` | A literal zero-seeded radial sibling has large conductors and matching nonzero finite density spectra while its completed period vanishes. These particular arithmetic/spectral statistics do not imply angular normality. |
| `gamma_prybar/front1/COFACTOR_PROOFS.md`, `front4/FOURIER.md` | Old-prime orientation countermodels, fixed-lag identity (14), and paid high-frequency retrieval costs. Stronger cofactor-preserving controls already exist. |
| `2026-10-30/gamma_twist/signed/SHARP_SEED_ENERGY.md` | The sharp all-seed lag-energy minimum, including the no-wrap integer-branch argument. GP-1/2 adapt it to state energy and explicitly compare completion. |
| `critical_chirp_source/front_ah/PROOFS.md` | Sharp all-derivative tail bounds and the coherent high-frequency obstruction. Formula (6) is not a claim of a new tail asymptotic. |

All archive paths and SHA-256 values actually consulted are recorded in
`gamma_prime_sources.json`, with partial-read scopes where appropriate.
Archive claims are treated as constraints and are not renamed as discoveries
of this round. The new paper arguments above have been written out rather
than inferred from a claim ledger or another agent's verdict.

## 9. Executed tests, results and reproduction

The runnable artifacts are `gamma_prime_probe.py`,
`test_gamma_prime_probe.py`, `gamma_prime_results.json` and the source
manifest. The direct stdlib test command is:

```bash
PYTHONPATH=. python research/2026-11-13/leah_gamma_twist/test_gamma_prime_probe.py -v
PYTHONPATH=. python research/2026-11-13/leah_gamma_twist/gamma_prime_probe.py --output research/2026-11-13/leah_gamma_twist/gamma_prime_results.json
```

**14 named tests passed.** The first attempted command used `python -m
pytest`; the default Python lacked pytest, so that command failed before
collecting tests. The stdlib suite then passed (1.003 seconds), and passed
again after exact display-precision cleanup (0.672 seconds). These are the
focused runs, not a full-repository or hosted validation claim. The root
subsequently reported an environment reset; the commands above explicitly
set the import path, and the probe also locates the repository root itself.
All mathematical certificates use integers and Fractions. Decimal output
is outward rounding, with additional places for small positive quantities.

The declared source calibration covers n=1,…,128; the fixed-lag holdouts
cover six stencils at n=137,263,521,1031. The state-energy finite certificates
for h=1, L=A give the following outward enclosures of A⁴ times the global
minimum. These are consequences of (9) and (6), not fitted minima:

| A | Lower bound | Upper bound |
|---:|---:|---:|
| 137 | 0.001405081121470771 | 0.001405118657710424 |
| 263 | 0.001405339633172141 | 0.001405349789375145 |
| 521 | 0.001405465157150441 | 0.001405467741138565 |
| 1031 | 0.001405524837958272 | 0.001405525497293273 |

All declared source mutants, rational aliases, old-cofactor shadows and
prime/Gamma clock controls passed their stated algebraic/certification
conditions. The additional finite chronological-product checks at
N=2,3,7,16 were added as classical calibration after the prospective
declaration and are labeled as such in the receipt. No failed mathematical
control was dropped or replaced. Guard tests reject an uncertified
large-frequency branch and non-exact input types; endpoint tests verify
the half-open convention in (18).

The universal claims rest on the displayed proofs. Finite implementation
agreement, shared source provenance and same-model checking do not confer
external mathematical independence. R0 remains open in this bearing.

## 10. Separate post-derivation audit of RI-01

After the Gamma proofs were banked, the root requested a separate audit of
`R0_INVERSE.md`, RI-01 through RI-7. This is a same-model review of another
bearing, not independent mathematical verification. The audit found no
mathematical defect in the following inspected chain:

1. Small total cosine loss puts every centered phase inside the required
   local arc. A quiet transition exists because the sum of adjacent squared
   norms is at most twice the full norm. The source-span condition then
   normalizes pairwise-integral residual differences into integer defects
   plus a uniformly small forcing.
2. Two defects cost more energy than the permitted threshold. For a single
   defect, the available left/right window has at least one full K-side.
   Its exact quadratic denominator is 255+δ_left+δ_right, at most
   256+δ_K; this includes both endpoint defects without inventing missing
   observations.
3. For the independent quadratic calculation, substitute y=16x+b into
   A_l x²+B_r y². Differentiation gives
   x=−16B_rb/(A_l+256B_r), y=A_lb/(A_l+256B_r), and minimum
   A_lB_rb²/(A_l+256B_r), agreeing with the inverse-Gram expression.
4. The constant integer lift branch and its fixed point give the stated
   inverse arc also for negative h. On the source block U_(m+1),…,U_(8m),
   there are 7m−1 transitions. The selected Green identity consequently
   produces denominator 15|h|16^m and the factor 16·16⁻⁸ᵐ in RI-5.
   The imported irrationality bound yields the stated uniform frequency-band
   contradiction and logarithmic complete-block count.

The exact finite cross-check is preserved in `audit_r0.py` and
`audit_r0_results.json`: **2,520 assertions passed**, comprising 676
left/right/jump Gram cases, 384 signed-frequency constant-lift inverse-arc
cases, five finite original-source Green identities, and the boundary
control q₀=−1/16, q₁=⋯=q₂₀=0. That last control has exactly one nonzero
residual and energy 1−cos(π/8), identifying the stated arbitrary-seed
ceiling. These are separately implemented finite checks, not a machine
proof of the universal result.

The published statement μ(π)≤7.103205334137…<15/2 was freshly checked on
the [Zeilberger–Zudilin author page](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html),
which identifies the 2020 publication in *Moscow Journal of Combinatorics
and Number Theory* 9, 407–419. The Diophantine proof is imported, not
reproduced in this audit. The strict fixed-c condition, non-effective
onset, and lack of an R0 conclusion are essential and were retained.

At execution the audited document's SHA-256 was
`d1fcf1f5490c380ccec769c0fcc4a74dfadefb4f765100e8f24eaaafcd7505d8`;
its RI-01 section hash was
`f20bac32fa76fcfa29cd6090b57b371bb663ebb25b839e1f3b5f0d9f8f567056`.
The receipt pins the constructor code and source oracle too. Later
block-ratio extensions, RI-02 and RI-03 are outside this audit's scope.

```bash
PYTHONPATH=. python research/2026-11-13/leah_gamma_twist/audit_r0.py --output research/2026-11-13/leah_gamma_twist/audit_r0_results.json
```
