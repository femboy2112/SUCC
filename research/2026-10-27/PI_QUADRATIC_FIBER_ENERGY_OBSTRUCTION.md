# Adversarial lane: quadratic fibers do not supply a generic cancellation gain

**Status:** PAPER PROOFS below, with exact finite corroboration. Proof dependencies: repository HEAD `76f37996` and PR #325 live head `95ee2f1fab851afe1517d8ec5a0589885842426f`. Authentic pi normality remains OPEN. No external novelty claim.

## Contract

For the unchanged source `A(x)=120x²−89x+16`, `D(x)=(2x−1)(4x−1)(8x−7)(8x−3)`, `r=A/D`, `U_0=0`, `U_n=16U_(n−1)+r(n)`, investigate

`C_A(N,q,h)=(q/N²) sum_a |sum_(1≤n≤N,A(n)=a mod q) e(hU_n)|²`, `q=p^L`, with a fixed prime `p≥7`.

The proposed sufficient authentic estimate is `C_A→0` at a specified growing `q=o(N)`. It remains DARK for authentic U. The questions answered here concern its algebraic spectrum, exact nontrivial controls, and whether normality plus finite irrationality type forces this moving gate.

**New decisive obstruction:** For EVERY prescribed `q(N)=p^{L(N)}→∞` with `q(N)=o(N)`, there is ONE base-16 normal α, with irrationality exponent at most four, for which

`liminf_j C_A(2^j,q(2^j),h;α) ≥ 1/4`

for every fixed nonzero integer h, where phases are `e(h16^(n−1)α)`. The same conclusion holds with the exact original four-pole forcing at changed selector `V_0=(α−π)/16`. This extends E7 to the actual quadratic coarsening; it does NOT follow merely by invoking the earlier fine-residue energy obstruction.

## 1. Exact fibers, spectrum and Haar weights

Write `b=89/240 mod q`, `a*=A(b) mod q`. Both 120 and 240 are units for `p≥7`, and

`A(x)=120(x−b)²+a* mod q`.

Thus the fibers are exactly the square-map fibers after invertible affine changes. The fiber over zero of the square map has size `p^floor(L/2)`. For each `s≥0`, `2s<L`, every nonzero square value of valuation `2s` has fiber size `2p^s`, and there are

`(p−1)p^(L−2s−1)/2`

such values. There are no other occupied fibers. Hence

`k_L=#im A=1+(p−1)/2 sum_(s=0)^floor((L−1)/2) p^(L−2s−1)`,

`k_L/q → p/[2(p+1)]`,

`sum_a m_a²=q+L(p−1)p^(L−1)`.

Let `K_q(r,t)=1_(A(r)=A(t))`, on ordinary counting-measure `C^q`. Its blocks are `J_(m_a)`. Its positive eigenvalues are exactly the nonzero fiber sizes, one eigenvalue per occupied fiber, and zero has multiplicity `q−k_L`. In particular

`lambda_max(K_q)=p^(L/2)` for even L,

`lambda_max(K_q)=2p^((L−1)/2)` for odd L.

At p=7,L=1 the spectrum is `2,2,2,1,0,0,0`; the involution is `r↦5−r` with fixed point 6. The signed correction `K−I` has spectrum `+1` three times, `−1` three times, and `0` once. It is not negative semidefinite. The exact signed mirror formula creates neither a uniform contraction nor a growing saving by itself.

For uniform time r mod q, the correct pushforward Haar weight of output a is `μ_a=m_a/q`, not `1/q` or `1/k_L`. The orthogonal conditional-average operator is `P_q=diag(m_(A(r))^−1)K_q`, with eigenvalues zero and one. For any periodic residue vector w,

`Q_A(w)=(1/q) sum_a |sum_(r in fiber a)w_r|²/m_a = ||P_qw||²/q`,

whereas the proposed gate on a full period is

`C_A(w)=(1/q) sum_a |sum_(r in fiber a)w_r|²`.

They are different norms. The latter magnifies high-multiplicity critical fibers. With arbitrary empirical time counts, conditional expectation uses counts `c_a/N`, not the limiting Haar weights.

## 2. Two exact, nontrivial false inequalities

### No uniform contraction against fine residue energy

For `N` divisible by q, put `Z_r=sum_(n=r mod q)z_n`. Then `C_A=(q/N²)Z*K_qZ` and `E_q=(q/N²)||Z||²`, so the sharp upper comparison is

`C_A≤lambda_max(K_q) E_q`,

not `C_A≤E_q`. The ratio `lambda_max` is attained by Z constant on a largest fiber and zero outside it. This is realizable with unit phases at `N=2q`: on the first period use 1 everywhere; on the second use +1 in the chosen fiber and −1 outside. Thus the failure does not require non-unit phases.

### Global Weyl cancellation still leaves a constant quadratic-fiber gate

For any `p∤k`, take `z_n=e(kn/q)` and N any positive multiple of q. Then

`N^−1 sum_n z_n=0`, `E_q=1`, but `C_A=1−1/p`.

This holds at EVERY depth L. Proof: with `u=x−y`, the equation `A(x)=A(y)` is `u[120(2y+u)−89]=0 mod q`; since 240 is a unit, it has exactly `gcd(u,q)` values of y. Consequently

`q C_A=sum_(u mod q) gcd(u,q)e(ku/q)`.

The u=0 term is q. Grouping the remaining u by `v_p(u)=s` gives Ramanujan sums. They vanish unless `s=L−1`, when the sum is −1 and its coefficient is `p^(L−1)`. The result is `q−q/p`.

Thus a claim that increasing quadratic-fiber depth alone forces `C_A/E_q→0` fails even for phases with exactly zero global mean. These are finite algebraic controls, not one fixed radix orbit as q varies; Section 4 supplies the stronger single normal finite-type orbit.

## 3. Changed-seed and rational fake controls diverge in the unweighted gate

For coherent phases and full periods, `C_A=1+L(1−1/p)`. At arbitrary N≥q, every residue count is between `N/q−1` and `N/q+1`, so every fiber count is between these bounds times m_a. Hence

`(1−q/N)² B_L≤C_A(1)≤(1+q/N)² B_L`, `B_L=1+L(1−1/p)`.

The asymptotic statement for arbitrary schedules `q=o(N)` is `C_A(1)/B_L→1`; the absolute endpoint error need not tend to zero without the extra condition `Lq/N→0`.

For phases z,w of modulus at most one and `D_N=sum_(n≤N)|z_n−w_n|`,

`|C_A(z)−C_A(w)|≤(2m_max/N)(1+q/N)D_N`.

Indeed every time fiber has size at most `m_max ceil(N/q)` and expand the difference of squared sums. Since `m_max≤2sqrt(q)`, this tends to zero whenever `D_N=O_h(1)` and `q=o(N)`.

The original same-forcing changed seed `V_n=−T_n`, with `sum T_n=B<∞`, has `D_N≤2π|h|B` against 1. The #320 fake `U_n*=16^n−T_n*`, `T_n*=(n+1)/[(2n+1)(4n+1)(8n+1)]`, has `sum T_n*<∞` and the same comparison. Thus BOTH obey `C_A/B_L→1`; along growing depth their energy diverges. A normality proof must exclude these controls through a new arithmetic premise, not through generic fiber algebra. Their phases retain no authenticated original zero-selected real orbit, and changed irrational selectors are not assigned authentic p-adic states.

## 4. A normal finite-type counterexample for every prescribed quadratic-fiber schedule

This is an adaptation of E7 at repository HEAD. Its stage construction, word-frequency condition, marker, all-prefix normality proof and rational-separation proof remain as in `PI_NORMAL_FINITE_TYPE_ENERGY_OBSTRUCTION.md`; the energy selection is changed below. The changed selection is essential, because coarse energy is not bounded below by the fine energy.

Fix a prime p≥7 and prescribed `q(N)=p^L→∞`, `q=o(N)`. Take `N_j=2^j`, `P=N_j/2`, `q=q(N_j)` at late stages, and choose a word W of length q whose periodic repetition supplies the next P digits. As in E7, the first digit is forced to be a marker differing by at least two from the prior periodic continuation. Let `H=floor(q^(1/8))`, `δ=q^(−1/8)`.

For sufficiently large j choose the largest S≥0 satisfying

`M*=2p^S≤min(q^(1/16),sqrt(N_j/q))` and `2S<L`.

Then `S→∞`, `M*²≤q^(1/8)` and `qM*/N_j≤sqrt(q/N_j)→0`. Early stages may be arbitrary marker-respecting words.

Let K_S equal the fiber-sum block `J_(m_a)` on fibers whose center valuation is `s≤S`, and zero on all other fibers. This retains complete fibers, not truncated portions. Its counting-measure operator norm and maximum row sum are `M*`; its diagonal trace is

`tr K_S=q a_S`, `a_S=1−p^(−S−1)→1`.

For uniform W among all `16^q` digit words, let `β=A_W/(16^q−1)` and let `w_t(h)` be its cyclic radix phases aligned with the new stage. These are exactly the auxiliary phases in E7, with indices relabeled by absolute time t mod q. Put

`ψ=K_Sw`, `R_W=(1/q)w*K_Sw=(1/q)sum_(selected fibers a)|sum_(r in a)w_r|²`.

The elementary cyclic-word second moment used in E7 gives, for distinct residues r,t and `0<|h|≤H`,

`E[w_r conjugate(w_t)]=ε=16^(−q)`.

The duplicate endpoint among the `16^q` words is responsible for ε. Therefore

`E R_W=(1−ε)a_S+ε b_S≥a_S`, `b_S=q^−1 sum_(selected a)m_a²≤M*`.

### Concentration without falsely independent phases

Change one of the q independent digits of W. For the q cyclic rotations, its changed fractional place runs once through 1,...,q; consequently

`sum_t |w_t−w'_t|≤2π|h|·15 sum_(r=1)^q16^(−r)/(1−16^(−q))=2π|h|`.

Because `||K_Sw||∞≤M*`,

`|R_W−R_W'|≤4π|h|M*/q`.

The elementary independent-coordinate variance bound (proved by resampling one coordinate and telescoping conditional expectations) gives

`Var R_W≤(1/2)sum_(digits i) E(R_W−R_W^(i))²≤8π²h²M*²/q`.

Chebyshev and summing `h²` for `1≤h≤H` bound the probability that some h has `R_W<a_S−δ` by

`8π² M*² H(H+1)(2H+1)/(6qδ²)=O(M*² q^(−3/8))=O(q^(−1/4))`.

This probability tends to zero. No independence between cyclic phases was assumed.

### The old prefix cannot cancel the selected periodic contribution

Let `z_n^old(h)` be the old truncation phases, and group them into C_t by t mod q as in E7. Impose for all `1≤h≤H`

`|sum_(n≤P) z_n^old(h) conjugate(ψ_(n mod q)(h))|≤δP`.

The same exact root-grid second moment, now applied to coefficients `K_SC`, gives

`E |cross|²≤2M*²P²/q+ε M*²P²`.

Here `||K_SC||²≤M*²||C||²≤2M*²P²/q` and `|sum_t(K_SC)_t|≤M*P`. The union-bound failure probability is at most

`2M*²q^(−5/8)+M*²q^(3/8)16^(−q)→0`.

Impose also E7's cyclic digit-frequency condition. Its failure probability tends to zero unchanged. Conditioning on the fixed first-digit marker multiplies total failure probability by at most sixteen. Therefore a word satisfying ALL THREE conditions and the marker exists at every sufficiently late stage. Choose the lexicographically first one. The same one α then handles every fixed h eventually.

### Lower bound for the actual quadratic-fiber energy

For the resulting α define `z_n=e(h16^(n−1)α)` and

`F=sum_(n≤N_j) z_n conjugate(ψ_(n mod q))`.

The old and new radix tail discrepancies have total phase error at most `4π|h|/15`, as in E7; multiplying by ψ costs at most M*. The new-stage periodic inner product has full-period average R_W and endpoint error at most `2qM*`. Thus

`Re F≥P R_W−δP−2qM*−(4π|h|/15)M*`.

Since ψ is constant on every A-fiber, Cauchy–Schwarz directly in those fibers gives

`|F|²≤[sum_a |sum_(n≤N,A(n)=a)z_n|²] [sum_(selected a)|sum_(r in a)w_r|²]`.

The second factor is `qR_W`, so

`C_A(N_j,q,h;α)≥[(R_W−δ)/2−2qM*/N_j−4π|h|M*/(15N_j)]_+²/R_W`.

The function `(R/2−e)_+²/R` is increasing in R for R≥2e. Since `R_W≥a_S−δ→1`, the errors tend to zero and this proves

`liminf_j C_A(N_j,q(N_j),h;α)≥1/4`.

The stages still have `q=o(N_j)`, cyclic normal word frequencies, and the exact same marker. The E7 all-prefix argument proves base-16 normality. Its rational periodic approximants have denominators `<16^(N_j/2+q)` and distances between `16^(−N_j−1)` and `16^(−N_j)`, hence the unchanged separation proof gives `μ(α)≤4`. No uniform bound `Cq^(−4)` is asserted.

Finally `V_n=16^(n−1)α−T_n`, `V_0=(α−π)/16`, obeys the SAME original recurrence. Section 3's stability bound gives `|C_A(V)−C_A(α)|=O_h(sqrt(q)/N)→0`, preserving the 1/4 lower limit.

## 5. Quantifiers and what survives

For one fixed q, the quadratic-fiber gate vanishes for every nonzero fixed h if and only if α is normal to base 16. Necessity follows by Cauchy–Schwarz and `#im A≤q`; sufficiency follows because normality makes every fixed time-residue subsequence Haar-generic, and only finitely many are aggregated. The proof of that latter fixed-residue fact is already in E3 of the preceding energy dossier.

There exists a sufficiently slowly growing p-power schedule along which all these gates vanish if and only if α is normal: use diagonal thresholds for finitely many fixed q and h, also enforcing q/N→0. Such existence is a reformulation. A PRESCRIBED growing schedule asks for strictly more, even among normal α with irrationality exponent at most four, by Section 4.

None of these statements refutes the sufficient bound at the actual U_0=0 orbit. They locate the missing input precisely: source and zero selection must give quantitative conditional cancellation beyond normality and generic finite irrationality type. The numerator mirror, Gaussian sign terminology, and exact local Haar clock alone do not supply it.

## 6. Exact finite corroboration

An independent integer probe enumerated A-fibers and compared the complete positive spectrum, nullity and pair count against the formulas above. For the additive-character control, it reduced the integer coefficient polynomial `sum_u gcd(u,q)X^u` modulo `Phi_(p^L)(X)=sum_(i=0)^(p−1)X^(i p^(L−1))`; the exact remainder was `q−q/p`, with every other coefficient zero. Tested cases:

| p | L | q | positive eigenvalues (multiplicity) | nullity | coherent energy | primitive-character energy |
|---|---|---|---|---|---|---|
| 7 | 1 | 7 | 1 (1), 2 (3) | 3 | 13/7 | 6/7 |
| 7 | 2 | 49 | 2 (21), 7 (1) | 27 | 19/7 | 6/7 |
| 7 | 3 | 343 | 2 (147), 7 (1), 14 (3) | 192 | 25/7 | 6/7 |
| 7 | 4 | 2401 | 2 (1029), 14 (21), 49 (1) | 1350 | 31/7 | 6/7 |
| 11 | 1 | 11 | 1 (1), 2 (5) | 5 | 21/11 | 10/11 |
| 11 | 2 | 121 | 2 (55), 11 (1) | 65 | 31/11 | 10/11 |
| 11 | 3 | 1331 | 2 (605), 11 (1), 22 (5) | 720 | 41/11 | 10/11 |
| 241 | 1 | 241 | 1 (1), 2 (120) | 120 | 481/241 | 240/241 |

The p=241 numerator-root collision does not alter these equal-value fiber formulas: 240 and 120 remain units there. Finite checks corroborate the algebra; the normal-carrier theorem is a paper existence proof, not an executed enormous digit search.

## 7. Strengthening: correct Haar normalization does not rescue a prescribed growing gate

**Status: PAPER PROOF, independently scrutinized in this lane after the root's proposed strengthening.** The SAME α in Section 4 can be selected to satisfy both

`liminf_j C_A(N_j,q_j,h;α)≥1/4`

and

`liminf_j H_A(N_j,q_j,h;α)≥p/[8(p+1)]`,

for every fixed nonzero h, while remaining base-16 normal with `μ(α)≤4`. Here

`H_A(N,q;z)=(q/N²)sum_(a in im A) |S_a|²/m_a`,

`S_a=sum_(1≤n≤N,A(n)=a mod q) z_n`, `m_a=#{r mod q:A(r)=a}`.

This H uses the complete-residue-period Haar masses. At arbitrary N the actual empirical conditional norm is instead

`Qemp_A(N,q;z)=(1/N)sum_(a:c_a>0)|S_a|²/c_a`,

where `c_a=#{1≤n≤N:A(n)=a mod q}`. The same α satisfies the same lower bound `p/[8(p+1)]` for Qemp. Thus the new obstruction is not an artifact of incorrectly uniform output weights or of the growth of critical fiber multiplicities in C_A.

**Selection quantifier:** For this simultaneous theorem, REPLACE Section 4's lexicographically first good-word rule by the lexicographically first word in the augmented intersection containing both the K_S and P_q requirements. This reruns the construction with stronger finite requirements. “The same α” means the one α from this joint construction witnesses both conclusions; it does not assert that an arbitrary α already selected under Section 4's earlier rule automatically has the new proper-Haar property.

### 7.1 Additional good-word events coexist with the Section 4 events

Let `P_q(r,t)=1_(A(r)=A(t))/m_(A(r))`. This is the symmetric orthogonal projection onto fiber-constant vectors. Its operator norm and maximum absolute row sum are both one; `P_q 1=1`; and `tr P_q=k_L`. Keep exactly the same uniform auxiliary q-digit word, stage marker, H, δ and existing three requirements from Section 4. For each `1≤h≤H`, additionally put

`ψ_Q=P_q w(h)`, `R_Q=q^−1 w*P_qw=q^−1||P_qw||²`.

In particular `0≤R_Q≤1`. From the exact duplicated-endpoint covariance,

`E R_Q=(1−ε)k_L/q+ε≥k_L/q`, `ε=16^(−q)`.

The same one-digit estimate now has no M* factor:

`|R_Q(W)−R_Q(W')|≤4π|h|/q`,

`Var R_Q≤8π²h²/q`.

Consequently the probability that any `1≤h≤H` violates `R_Q≥k_L/q−δ` is at most

`8π² H(H+1)(2H+1)/(6qδ²)=O(q^(−3/8))`.

Also impose

`|sum_(n≤Pstage) z_n^old(h) conjugate((P_qw)_(n mod q))|≤δPstage`,

with `Pstage=N_j/2`. If C groups the old phases by residues, the exact second moment is

`(1−ε)||P_q C||²+ε|sum_t(P_q C)_t|²`.

Since P_q is an orthogonal projection and preserves sums, this is at most

`2Pstage²/q+ε Pstage²`.

The union-bound failure probability over h is at most `2q^(−5/8)+q^(3/8)16^(−q)`. Add these two failure bounds to ALL existing Section 4 failure bounds. The total still tends to zero. Conditioning on the prescribed first digit still multiplies it by at most sixteen. Hence one word exists satisfying all five requirements and the marker. Choosing this intersection at every late stage constructs a single α satisfying both energy obstructions; no choice of a separate α for each norm or frequency is needed. Negative h follow by conjugation.

### 7.2 Weighted Cauchy–Schwarz proves the Haar-energy lower bound

Set `F_Q=sum_(n≤N_j) z_n conjugate((ψ_Q)_(n mod q))` for the final radix phases z of α. As `||ψ_Q||∞≤1`, the previous E7 total tail error is at most `4π|h|/15`. A new-stage period contributes exactly `qR_Q`, with partial-period error at most `2q`. Therefore

`Re F_Q≥Pstage R_Q−δPstage−2q−4π|h|/15`.

Because ψ_Q is fiber-constant, weighted Cauchy–Schwarz gives

`|F_Q|²≤[sum_a |S_a|²/m_a] [sum_a m_a |(ψ_Q)_a|²]`.

The second bracket equals `||P_qw||²=qR_Q`. Thus

`H_A(N_j,q_j,h;α)≥[(R_Q−δ)/2−2q_j/N_j−4π|h|/(15N_j)]_+²/R_Q`.

For all sufficiently late j, `R_Q≥k_L/q−δ>0`. The same monotonicity calculation used in Section 4, together with `k_L/q→p/[2(p+1)]`, yields the asserted lower limit `p/[8(p+1)]`. In particular the p=7 lower constant is `7/64`.

The marker, periodic stage lengths and cyclic-frequency requirements were only strengthened, so the E7 all-prefix normality and irrationality-exponent proofs remain unchanged.

### 7.3 Exact all-N comparison with empirical conditional expectation

For every N and q, each residue occurs either `floor(N/q)` or `ceil(N/q)` times. Thus

`m_a(N/q−1)≤c_a≤m_a(N/q+1)`.

When `N>q`, every occupied complete-period fiber has positive c_a, and term-by-term comparison proves

`H_A/(1+q/N)≤Qemp_A≤H_A/(1−q/N)`.

If q divides N, the two norms are exactly equal. The lower comparison remains valid for arbitrary N after empty empirical fibers are omitted; the displayed upper comparison is claimed only for N>q. Along the prescribed schedule q=o(N), the multiplicative factors tend to one. Therefore the SAME positive lower limit holds for Qemp.

For context, the exact inequalities `|N^−1 sum z_n|²≤H_A≤E_q` hold for all N: the first is weighted Cauchy–Schwarz using `sum_a m_a=q`; the second is the orthogonal-projection inequality. Correct Haar coarsening really is a contraction of the fine residue energy. Section 7 shows that even this legitimate contraction does not make a prescribed moving gate necessary for normality plus finite irrationality type.

For coherent unit phases, Qemp equals 1 at every N and q. Also `1≤H_A≤1+q²/(4N²)`: use the preceding contraction and the exact residue-count energy `1+r(q−r)/N²`, where `r=N mod q`. Thus H_A tends to 1 whenever q=o(N), while the unweighted C_A may grow linearly in L. This distinguishes the correct weights from the separate strict-implication obstruction.

### 7.4 Exact stability bounds and unchanged forcing

For arbitrary phases z,w of modulus at most one on the same N time indices, let `D_N=sum_n|z_n−w_n|`. Every fiber satisfies `c_a≤m_a ceil(N/q)`. Expanding the difference of squared sums gives the exact bounds

`|H_A(z)−H_A(w)|≤[2q ceil(N/q)/N²]D_N≤(2D_N/N)(1+q/N)`,

`|Qemp_A(z)−Qemp_A(w)|≤2D_N/N`.

The second formula omits empty empirical fibers and uses `(|S_a|+|R_a|)/c_a≤2`, so it holds for EVERY N,q without a q<N hypothesis. There is no maximum-fiber-size loss in either estimate.

For the same original forcing and changed selector, `V_n=16^(n−1)α−T_n`, `sum_(n≥1) T_n=B<∞`, hence `D_N≤2π|h|B`. Therefore

`|H_A(V)−H_A(α)|≤[4π|h|B/N](1+q/N)`,

`|Qemp_A(V)−Qemp_A(α)|≤4π|h|B/N`.

Both limits transfer, with the original forcing fully retained and the real selector explicitly changed. The same estimates compare the `−T_n` and rational-fake controls against coherent 1; their proper-Haar energies tend to one, so the normalization correction also does not discard those controls.

### 7.5 Endpoint conventions: 1 through N versus 0 through N−1

The construction and displayed finite bounds use `1≤n≤N` and completed phase `e(h16^(n−1)α)`. The PR #325 convention uses `0≤n<N`. For a fixed sequence defined also at n=0, those two windows replace one endpoint by another. Each fiber sum changes by total absolute mass at most two across all fibers. Since each individual N-term window has fiber counts at most `m_a ceil(N/q)`,

`|H_A^[0,N−1]−H_A^[1,N]|≤4q ceil(N/q)/N²≤(4/N)(1+q/N)`.

Similarly the unweighted energy differs by at most `4m_max q ceil(N/q)/N²`, which tends to zero when q=o(N).

For the empirical norm, an endpoint replacement also changes c_a. Nevertheless an exact count-free bound is

`|Qemp_A^[0,N−1]−Qemp_A^[1,N]|≤4/N`.

Proof: Qemp is the maximum over one complex ψ_a per fiber, `|ψ_a|≤1`, of

`N^−1 sum_n [2 Re(z_n conjugate(ψ_(A(n))))−|ψ_(A(n))|²]`.

The maximum is attained at each empirical conditional mean. Every individual summand lies in [−3,1], so replacing one observation changes any objective by at most four; the maxima differ by at most the same bound. This proof covers empty fibers automatically.

For the completed radix sequence one may take `z_0=e(hα/16)`. For the actual recurrence use `V_0=(α−π)/16`, with `T_0=π/16`; adding this one tail term changes the summable discrepancy bound from B to `B+π/16`. All asserted lower limits therefore hold in either endpoint convention. No finite equality between differently indexed energies is silently assumed.

**Resulting verdict:** Both the unweighted ramified energy and the correctly weighted conditional-Haar energy are strictly stronger than normality when their growing p-power schedule is prescribed. One normal finite-type changed-selector orbit simultaneously witnesses both failures of necessity. The authentic source-specific sufficient estimates remain open.

**Additional exact finite audit:** 384 deterministic Gaussian-integer unit-phase cases passed exact `Fraction` checks of `H_A≤E_q`, the all-N H/Qemp comparisons, both endpoint-replacement estimates and both same-window phase-stability estimates. The cases covered `(p,L)=(7,1),(7,2),(7,3),(11,1),(11,2),(241,1)`, and N in `{1,2,5,q−1,q,q+1,2q−1,3q+5}`, including empty empirical fibers and incomplete periods. These finite checks corroborate the displayed inequalities, not the infinite normal-carrier existence theorem.

The executable and raw receipts are preserved in scratch:

- `/workspace/scratch/fe53b3b2e1b1/round2_mirror_haar_audit.py`
- `/workspace/scratch/fe53b3b2e1b1/round2_mirror_haar_audit.json`
- `/workspace/scratch/fe53b3b2e1b1/round2_mirror_haar_audit.log`

The retained replay passed **384 cases and 2,832 exact assertions**, with deterministic seed 708271. Script SHA-256: `8105789675604d2d3c2917f7af77cd2c79a35dd9d3daf8537cb8ac537904159c`. Raw JSON SHA-256: `9af27630dc31e42d2cb9f241c57cb9c1b401a33b0b01aae18834a82e11b14ae1`. The JSON records every case's rational energies, bounds, passed assertions and phase-sequence hash. Replay command:

`python /workspace/scratch/fe53b3b2e1b1/round2_mirror_haar_audit.py --output /workspace/scratch/fe53b3b2e1b1/round2_mirror_haar_audit.json --log /workspace/scratch/fe53b3b2e1b1/round2_mirror_haar_audit.log`
