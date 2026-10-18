# INDEX AT INFINITY — Möbius orientation, source Haar, and weighted observer transport

**Research date:** 2026-10-18. **Base:** SUCC research/equivariant-redundancy-weil-2026-10-18 at 8216c6fc042704aecd5fb7872facd681216e4be7 (draft PR #175). New research branch research/mobius-index-infinity-2026-10-18. Original archived source, main and earlier research branches unchanged. No zero positions were used. Classical algebra/operator analysis is attributed, not claimed academic priority. **RH PROVED: NO.**

## 0. Fresh cross-branch observations

**New independent context** from three unmerged research branches:
- PR #171 (Infinite Gamma Carleman, head 8c46cca801b5): a genuine one-real-Gamma boundary, in its specified analytic model, is a bounded noncompact strong limit of finite-rank skew commutators, with a paper-derived nonzero essential spectral band. No trace-norm or unrestricted unbounded-operator commutator follows.
- PR #173 (Bidirectional Hilbert cut, head a2ea6859416f): the true backward memory weight W_L differs radically from normalized clock Haar; as LCM clocks grow the total-variation separation approaches one. Its full-weight Hilbert residual remains RH-hard. We independently rederive the required exact weight and transport laws rather than importing unmerged code.
- PR #174 (Gaussian K-relative Suzuki, head 6fb1dba87ed2): original signed source positivity on an authenticated *two-dimensional* clamped high subspace does not yield the full high-space action residual, original S4 sign or RH.
- Parent PR #175 (equivariant source redundancy): original prime multiplication is chain-nullhomotopic in Koszul homology but source-nonzero, and admissible Weil identity/contact data cannot be declared redundant.

**Our discriminating hypothesis:** the signed Möbius inclusion-exclusion might be an EXACT positive projection built from genuine FUCC multiplication, while finite SUCC/FUCC cutoff commutators hide a boundary that survives infinity. Then ask whether restoring backward Hilbert source measure creates a canonical unitary connection, or a source-changing normalization.

## MII-01. Exact unilateral-SUCC index anomaly (CLASSICAL / PROVED)

Let H=ell²(N_{>=1}) with e_n basis and S e_n=e_(n+1). Then S*S=I and SS*=I-P_1, where P_1=|1><1|. Therefore [S*,S]=P_1 has trace 1 and Fredholm index(S)=-1.

Compress to e_1,...,e_N: S_N=P_N S P_N. Matrix multiplication gives, for EVERY N>=1,

    [S_N*,S_N] = |1><1| - |N><N|.

For N=1 this is zero. Each finite commutator has trace exactly zero, as it must. The negative boundary projection |N><N| converges strongly to zero but keeps operator and trace norms equal to one. Therefore the compressed commutators converge strongly to [S*,S]=P_1 with trace one, but not in trace norm.

**Receipt:** independent Python matrices S_N, S_N* and both products for N=1,2,3,4,7,11, not merely the desired diagonal formula. This proves that apparent finite sign cancellation need not be trace-stable as the source horizon changes. It does NOT identify Connes' trace.

## MII-02. Genuine prime FUCC: finite trace zero but nontrivial infinite bulk (PROVED)

For a TRUE Euler prime p, V_p e_n=e_(pn), V_p*V_p=I and V_p V_p*=P_(pN), projection onto integers divisible by p. Thus [V_p*,V_p]=I-P_(pN) is positive and infinite rank, not trace class.

Finite compression V_{p,N}=P_N V_p P_N has diagonal commutator

    <n|[V_{p,N}*,V_{p,N}]|n>
    = 1_{n<=floor(N/p)} - 1_{p|n}.

Its ordinary trace is zero for EVERY N, because each predicate counts floor(N/p) states. At a fixed n, the diagonal stabilizes to 1-1_{p|n}. The omitted upper frontier correction is exactly -1_{n>floor(N/p)}; it has trace -(N-floor(N/p)). Its normalized trace tends to -(1-1/p).

**Consequence:** strong completion of the actual multiplicative action and the normalized trace at infinity do not commute naively. Composite V_6 is still a lawful multiplication map V_2V_3; 6 is rejected ONLY if misrepresented as a new prime place.

## MII-03. Signed Möbius correction produces a POSITIVE complete-Hilbert projection (PROVED)

For a finite sorted genuine prime set P, define M_P=product P. The commuting orthogonal multiplication-range projections R_p=V_pV_p* obey R_p R_q=R_pq for distinct p,q.

    E_P = product_{p in P}(I-R_p)
        = sum_{d|M_P} mu(d) R_d.

Each factor I-R_p is an orthogonal projection; the factors commute. Thus E_P is an orthogonal projection, PSD on EVERY finite or infinite complex vector combination, even though the expanded coefficients mu(d) may be negative. On basis n,

    <n|E_P|n> = sum_{d|gcd(n,M_P)}mu(d)
              = 1_{gcd(n,M_P)=1}.

This is an unconditional exact mathematical realization of negative-counting cancellation leaving a positive SOURCE arithmetic form, not a fitted covariance. It preserves all genuine integer n; p² and other composites are not discarded. Replacing the minus with plus yields I+R_p, eigenvalue 2 at multiples of p, and destroys idempotence (2²!=2), a decisive hostile control.

The construction supplies a positive arithmetic sieve. **It is NOT the original completed signed Weil quadratic form.**

## MII-04. Exact source Haar normalization and finite rational error (PROVED)

Define tau_N(A)=Tr(P_N A P_N)/N, the finite integer-source normalized counting trace. Then

    tau_N(E_P)= (1/N)sum_{d|M_P}mu(d) floor(N/d).

Let h_P=phi(M_P)/M_P=product_{p in P}(1-1/p). Each d>1 contributes a floor error of magnitude less than one, hence

    |tau_N(E_P)-h_P| <= (2^|P|-1)/N.

If N is divisible by M_P, the observed count and Haar product agree EXACTLY by the Chinese remainder theorem. Thus finite arithmetic counting derives the finite-profinite unit Haar mass with quantified source error. Along growing P the product h_P tends to zero by classical divergence of the prime reciprocal series. No finite computation executes that infinite limit.

## MII-05. True all-prime-power half-density from valuation-shell trace (PROVED LOCAL THREE-ROUTE)

For k>=0, the signed difference of true multiplication-range projections

    Q_(p,k)=V_p^k V_p*^k - V_p^(k+1)V_p*^(k+1)

is a positive orthogonal projection onto the original integers of EXACT p-valuation k. Direct finite trace:

    Tr(P_N Q_(p,k) P_N)
       = floor(N/p^k)-floor(N/p^(k+1)).

Its large-N normalized mass is (1-1/p)*p^-k, the genuine additive Haar measure of p^k Z_p^times. Absolute finite-N error is <=1/N, with all quantities exact fractions. Dividing by the SOURCE normalizing unit mass 1-1/p gives p^-k, hence its positive Hilbert half-density amplitude p^-k/2.

For k>=1, the original source log clock [H,V_p]=log(p)V_p independently supplies log p. The resulting **magnitude** log(p)/p^(k/2) agrees exactly with the original Weil prime-jet weight. Code crosschecks genuine SUCC source von-Mangoldt labels, inherited source one-place Tate idelic norm and normalized local shell, and Connes off-identity C_p(p^k)², rejecting fake Euler place 6. No completed Weil sign, real Gamma/poles/contact or all-test spectral positivity is inferred.

## MII-06. Strong source completion differs from norm and from trace state (PROVED)

Increase P cofinally through the genuine primes. Every n>1 eventually has an observed prime divisor, while n=1 never does. On the dense finite-support core E_P e_n tends to 1_{n=1}e_n and ||E_P||<=1. Thus

    E_P --> P_1=|1><1| STRONGLY on ell²(N).

For EVERY finite P choose a prime q outside P; E_P e_q=e_q but P_1 e_q=0, so ||E_P-P_1||=1. The limit is NOT operator-norm convergence.

The original source successor detects its boundary:

    [S,E_P] e_n = (E_P(n)-E_P(n+1))e_(n+1).

It converges strongly to [S,P_1]=|2><1|, but for every finite P containing 2 choose an omitted odd prime q>3: q-1 is even and excluded, q is included, so [S,E_P]e_(q-1)=-e_q while [S,P_1]e_(q-1)=0. Hence the commutator operator-norm error is at least one for every finite P.

**Observer-state distinction:** <1|E_P|1>=1 in the vacuum state, whereas the bulk normalized trace tends to h_P and then zero. It is an error to call one “the” infinity normalization without a declared source observer. The finite normalized density rho_N=P_N/N has trace one but <n|rho_N|n>=1/N for every fixed n<=N, tending to zero. No positive trace-class NORMAL trace-one state can have all diagonal coefficients zero (the trace is their sum). Any weak-* cluster state of these finite tracial states on bounded operators is singular/non-normal. This is classical operator-algebraic information escape, NOT a constructed Connes trace or a claimed RH-positive factorization.

## MII-07. BDC crosspollination: the correct Hilbert clock is a density-transported SUCC (PROVED CLASSICAL)

Independently rederive the mathematical source from sibling PR #173. The original backward x>=1 inverse-square measure folds mod L to a positive density

    W_L(u) = 1_{u>=1}/u² + sum_{j>=1}(u+jL)^-2,   0<=u<L.

The integral over one period is exactly one by pushforward of x^-2 dx on x>=1. Uniform Haar is du/L, not W_L(u)du. The Radon–Nikodym density D_L(u)=L W_L(u) is strictly positive.

The map f -> sqrt(D_L(u))f(u) is a unitary from L²(W_L du) to L²(du/L). The Haar cyclic phase shift f(u)->f(u-a) pulls back to the uniquely source-correct unitary

    (T_a^W f)(u)=sqrt(W_L(u-a)/W_L(u))f(u-a),

where phases are modulo L. The cocycle is algebraically a positive coboundary:

    c_a(u)c_b(u-a)=c_(a+b)(u),

so auxiliary gauge choices cancel around lawful source cycles PROVIDED THE DENSITY ACCOMPANIES BOTH STATES AND ACTIONS. Dropping the density is not a symmetry of the original target norm.

Indeed W_L(3/2)>=4/9 on the source side above the physical cut, while W_L(1/2)<2/L² using sum_{j>=1}j^-2<2. Hence for L>=2,

    ||naive unit phase shift||²_(L²(W_L))
      >= W_L(3/2)/W_L(1/2) > 2 L²/9.

The properly corrected density shift is unitary for each L, but unweighted transport becomes quantitatively worse as L grows. This strengthens the independent BDC-10 TV warning; it is not proof of Nyman/Báez-Duarte closure, Connes trace, Weil positivity or RH.

Tests use exact rational partial memory series with integral-test LOWER/UPPER tail enclosures and exact weighted finite-grid isometries, never pretending finite sampling performs an infinite integral. A regression exposed and killed the incorrect inference that a ratio of two TRUNCATED positive series must lie inside the true ratio's rigorous interval; we use nested FULL-SERIES interval ratios instead.

A nonzero constant periodic ghost added to the backward memory tail leaves its recurrence unchanged but violates decay and adds probability mass L*c. It is not observationally redundant under the physical source. As in ERW, redundancy must be certified against the actual source measure and all future actions.


## MII-09. Hostile source-map blindness: the same positive sieve accepts incompatible completed L-sources (PROVED NON-IDENTIFICATION)

The projector E_P was built solely from the literal integer multiplication isometries V_p and genuine prime divisibility. It contains NO Dirichlet character, conductor, Archimedean Gamma or canonical identity-contact datum. That omission is mathematically decisive and is not a harmless simplification.

Take the two source-typed arithmetic profiles already independently implemented upstream: standard Q zeta, and primitive chi_{-3} with conductor 3, odd Archimedean parity and missing Euler factor at p=3. The SAME V_2,V_3 and hence SAME positive sieve E_{2,3} act on the underlying integer Hilbert space, but the original convergent log-derivative coefficient at p=2 is +log 2 for zeta and -log 2 for chi_{-3}; at p=3 zeta has a source Euler impulse while the chi_{-3} Euler factor is absent. Consequently a construction depending only on V_p/E_P CANNOT uniquely reconstruct both signed explicit formula distributions, since one common input cannot have two different prescribed first-prime outputs.

Independently, the upstream original test f(t)=(1-t²)^3 1_{|t|<=1} has autocorrelation h(0)=2048/3003. Mutating the original signed Weil distribution by +delta_0 changes W(h) by +2048/3003, while all V_p and sieve E_P remain exactly unchanged. This furnishes a SECOND, analytically distinct source-map nonidentification witness (identity contact, not character/conductor).

The executable control imports the ORIGINAL source profiles and the ORIGINAL-source autocorrelation oracle from the pinned SUCC ancestor; it does not construct mutant profiles from arbitrary guessed data. This proves **character, conductor, archimedean parity and canonical contact cannot be dismissed as redundant relative to the full Weil test algebra**, even though E_P itself is an authentic positive arithmetic projection. It is a no-go for a SOURCE-BLIND candidate map, not for an enriched source-aware Connes/Weil construction, nor is it evidence against RH.

## MII-08. What remains RH-hard / falsification gate

All constructions above are genuine classical arithmetic/Hilbert identities with explicit source scopes, and test the user's redundancy intuition. They are not an identification of the COMPLETE signed Weil quadratic:

- One real Archimedean Gamma, both completed poles, canonical identity/contact principal value and character conductor/parity are still distinct authentic source contributions.
- The source-positive sieve projection and weighted clock unitary cannot simply be called the completed Connes trace; their measures and test spaces differ.
- The source Gamma branch #171 has a noncompact Carleman boundary in a different analytic domain; strong-limit similarity is not an intertwiner or proof of equal trace.
- The original high-space action-residual and signed four-low Suzuki Schur from branch #174 remain open despite source-authentic two-dimensional positive high directions.
- The original completed Weil distribution must be shown IDENTICAL to one source-derived positive form on the FULL admissible autocorrelation test space, with quantified analytic convergence and no zero input. This final statement remains RH-hard and UNVERIFIED.

**Next decisive probe:** define a common test class from actual Tate Schwartz–Bruhat / Connes principal-value data and original signed Weil; transport the new source-index projection and density-corrected clock through its genuine action and compare all local and Archimedean compact test values. A nonzero contact, Gamma, pole, phase, or test-domain residual refutes that specific identification; finite source magnitude matches remain local evidence only.

## Reproduction and provenance

Exact files: observational_succ/mobius_index_infinity.py; observational_succ/weighted_clock_cocycle.py; tests/test_mobius_index_infinity.py; tests/test_weighted_clock_cocycle.py; scripts/mobius_index_infinity_probe.py; docs/CLAIM_SUPPLEMENT_MOBIUS_INDEX_INFINITY.md; dedicated Python 3.10 and 3.13 CI workflow. No imported archival source files altered. All original p-place objects come from pinned SUCC source modules; comparison to sibling branches is at the theorem/source-contract level only, not an unreviewed merge.

Every assertion of all-integer or infinite-Hilbert validity is proved algebraically/analytically above and not inferred from finite regression sampling. Independent exact matrix/CRT/valuation oracles calibrate the implementation. Classical provenance includes elementary Fredholm shift index, CRT/Möbius sieve, Euclid primes, additive/multiplicative p-adic Haar, Radon–Nikodym change of measure and operator trace state distinctions. External mathematical priority not asserted. **RH PROVED: NO.**
