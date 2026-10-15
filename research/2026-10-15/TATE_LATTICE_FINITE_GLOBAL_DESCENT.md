# Tate lattice descent: additive Fourier atoms, multiplicative rigidity, and SUCC history

**2026-10-15.** Source branch: research/tate-lattice-finite-global-descent-2026-10-15. Parent: main@03db44203147a7b28d445bb9f970fa71360e78c4.

**Verdict.** A classical, exact finite-place-to-adelic inverse-limit interface explains how additive lattice preservation forces the rational multiplicative product formula. The bare quotient provably forgets nontrivial source SUCC transitions. The remedy is a framed lift with its signed event cocycle. No arithmetic Weil positivity is proved. **RH PROVED: NO.**

## 1. Steelman: what is being asked

The author's proposal: SUCC's recursive modeling of earlier models should become a source-indexed local-to-global proof operation. It should preserve arithmetic coupling, finite/Archimedean phase, and causal history. The strongest mathematical reading is a natural bijection between *fully compatible additive character systems* and a global adelic quotient observation, accompanied by a separate faithful representation of observed successor events.

Two distinct meanings of finite cannot be conflated: S has finitely many places, but each Q_p and its entire character group is an infinite mathematical object. A bounded finite-precision observer is strictly weaker.

## 2. Objects and exact sign convention

For a finite ordered set S of actual rational primes, define

    G_S = R x product_(p in S) Q_p
    Gamma_S = Z[S^(-1)]  (diagonally embedded)
    X_S = G_S / Gamma_S.

Normalize real Lebesgue measure and p-adic Haar measures by vol(Z_p)=1.

For x_p in Q_p let {x_p}_p in [0,1) intersect Z[1/p] denote its p-adic principal part modulo Z_p (finite negative p-adic digits). Set

    psi_S(x) = exp(2*pi*i*(x_real - sum_(p in S){x_p}_p))
    chi_(S,q)([x]) = psi_S(q*x) ,  q in Gamma_S.

The opposite simultaneous sign convention is equally valid. **Never flip only one place.**

For gamma in Gamma_S, gamma minus the sum of its finite principal parts is an integer. Hence psi_S(gamma)=1. Since q*gamma belongs to Gamma_S whenever q,gamma do, the characters chi_(S,q) descend to X_S.

## 3. The exact local-to-global theorem package

### TL-01: discrete cocompact lattice and covolume (CLASSICAL)

Gamma_S is discrete and cocompact in G_S, and X_S has Haar volume one in these normalizations.

Proof: Given x in G_S, choose delta=sum_(p in S){x_p}_p in Gamma_S. Subtracting delta makes every finite coordinate p-integral. Next subtract an integer to move the real coordinate into [0,1). This shows the compact set [0,1] x product Z_p maps onto X_S. If gamma in Gamma_S is p-integral at all p in S, its denominator has no prime factors, hence gamma is an integer. Intersecting with (-1/2,1/2) in the real coordinate isolates zero, proving discreteness. The unit real interval times product Z_p is a measurable fundamental domain, with product volume one.

### TL-02: annihilator and additive Fourier atoms (CLASSICAL)

Under the Fourier pairing from psi_S,

    Gamma_S^perp = Gamma_S,  and  (X_S)^ = Gamma_S (discrete).

Proof: Inclusion of Gamma_S in its annihilator follows from phase cancellation. Conversely let y annihilate Gamma_S. Subtract delta=sum_p{y_p}_p in Gamma_S, making all finite y_p integral. Since the character evaluates trivially on all integers, the remaining real coordinate is an integer. Subtract that integer too. Now real y=0 and each y_p in Z_p. Testing gamma=1/p^k for all k forces the p-th character to be trivial on y_p/p^k: the other local factors are integral and hence trivial. Therefore y_p belongs to every p^k Z_p, so y_p=0. Thus the original y was diagonal.

### TL-03: multiplicative product formula as additive-volume rigidity (CLASSICAL)

For q in Gamma_S^x, multiplication by q is an additive automorphism of G_S carrying Gamma_S onto itself. Its induced map on the compact quotient X_S preserves total Haar volume. Its modulus is

    Delta_S(q) = |q|_real * product_(p in S)|q|_p.

Since X_S has positive finite volume, Delta_S(q)=1.

Every rational q != 0 becomes an S-unit after including all prime divisors of its numerator and denominator, yielding

    |q|_real * product_(p finite)|q|_p = 1.

**Provenance:** Tate's adelic arithmetic; Poonen, *Tate's Thesis*, §5.7, page 31, explicitly calls this the compact-quotient/covolume proof. This is a classical theorem, not a newly discovered RH theorem.

Equivalent Fourier/Poisson proof: Schwartz-Bruhat Poisson summation for the self-annihilating lattice gives

    sum_(gamma in Gamma_S) f(gamma)
       = sum_(gamma in Gamma_S) Fourier(f)(gamma).

Changing f(x) to f(qx) leaves the original lattice sum unchanged, because qGamma_S=Gamma_S. Fourier scaling multiplies by Delta_S(q)^(-1), and the dual lattice sum remains unchanged as q^(-1)Gamma_S=Gamma_S. A nonzero positive self-dual test (Gaussian at infinity and indicators of Z_p at S-primes) forces Delta_S(q)=1. Thus phase-compatible additive duality plus lattice/Haar covariance yields the multiplicative law. Phase cancellation *alone* is insufficient.

### TL-04: omitted-prime defect is an exact covering degree (CLASSICAL)

For every q in Q^x,

    Delta_S(q) = product_(ell not in S) ell^(v_ell(q)).

If q belongs to Gamma_S, multiplication preserves the lattice by inclusion and descends to a finite covering X_S -> X_S of degree

    [Gamma_S : qGamma_S] = Delta_S(q) (positive integer).

If q is an S-unit, degree=1 and it is a quotient automorphism.

Controls:
- q=30, S={2,3}: Delta=5 and the induced quotient map has degree 5, not 1.
- q=1/7, S={2,3}: Delta=1/7, but q does not preserve Gamma_S by inclusion, so there is **no** claimed quotient covering.
- Composite 6 can be a valid *covering degree*, not a standalone prime field place Q_6.

### TL-05: exact bonding map and character naturality (CLASSICAL)

For S subset T finite sets of primes, define

    delta_(T\S)(x) = sum_(p in T\S){x_p}_p  in Gamma_T
    pi_(T,S)([x]_T)
      = [(x_real - delta, (x_p - delta)_(p in S))]_S.

This is continuous, surjective, independent of the choice of x in its Gamma_T orbit, and for R subset S subset T,

    pi_(T,R) = pi_(S,R) o pi_(T,S).

Proof: If x is changed by a diagonal gamma in Gamma_T, its omitted-prime principal parts change by an amount whose difference from gamma is integral at all omitted primes. The surviving diagonal discrepancy therefore belongs to Gamma_S. The resulting quotient class is unchanged. Composition follows from repeating the same principal-part elimination (or uniquely from character compatibility). Surjectivity follows by adding zero coordinates at the new prime places; continuity follows because principal parts are locally constant modulo Z_p.

The essential commutative square is

    chi_(T,q)([x]) = chi_(S,q)(pi_(T,S)([x])),
    for every q in Gamma_S.

Thus the Pontryagin-dual map is the inclusion Gamma_S -> Gamma_T.

**Hostile witness:** T={2}, x=(0,1/2), S=empty. On T, chi_(T,1)(x)=-1. A naive coordinate drop yields x_real=0 and character +1: **REFUTED**. Correct projection subtracts delta=1/2 and produces real class 1/2, character -1.

### TL-06: finite-place observer completion (CLASSICAL IMPORT)

By TL-02, the dual of X_S is Gamma_S. Since the duals of bonding maps are the inclusions Gamma_S -> Gamma_T,

    (inverse_limit_S X_S)^ = direct_limit_S Gamma_S = Q (discrete).

The full rational adelic quotient has the same dual:

    (A_Q / Q)^ = Q

under the self-dual Tate pairing and Q^perp=Q. By Pontryagin duality,

    inverse_limit_S X_S ~= A_Q / Q.

This is a natural **compact abelian group isomorphism**, not a claim that arbitrary SUCC histories are isomorphic to quotient points, or that finite measurement executes an infinite colimit. Full stage characters remain mathematically infinite even when S is finite.

## 4. New explicit source-observer obstruction

### TL-07: arbitrarily deep finite-phase aliases (PROVED LOCAL)

For any genuine prime p and any integer k>=0, consider the nonzero quotient class of x=(0,p^k) in X_{ {p} }. For every integer j and r<=k, q=j/p^r evaluates chi_q(x)=1. At r=k+1, chi_(1/p^(k+1))(x)=exp(-2*pi*i/p), not 1.

Thus no fixed denominator-depth family of phase observations separates every quotient class. This is a finite-toolkit identifiability obstruction, not a universal computational impossibility or physical supertask theorem.

### TL-08: bare quotient loses SUCC events (PROVED LOCAL)

On the additive lift G_S, define a lawful successor S_d: x -> x+d for a nonzero d in Gamma_S. In the quotient X_S,

    [x+d]=[x].

Therefore any proposed faithful isomorphism from source-recording SUCC histories to the **bare state quotient** is false. The quotient-state functor maps a nontrivial event to an unchanged state. The required repair is a source-identified lift/principal Gamma_S torsor and **ordered signed transition-cocycle history**. Merely augmenting a state with additional assertions of positivity cannot recover deleted causal events.

On lift functions, translation U_d f(x)=f(x-d) and normalized dilation V_q f(x)=Delta_S(q)^(-1/2) f(x/q) satisfy

    V_q U_d = U_(q*d) V_q.

This is an operator candidate matching SUCC/FUCC covariance; **a faithful functor from the actual evolving SUCC source/event category to this decorated analytic structure has not yet been built**.

## 5. Provenance, controls, and scope of executable receipts

- Code: observational_succ/tate_lattice_descent.py; tests: tests/test_tate_lattice_descent.py.
- Reuses existing diagonal_adele_zeta.py authentic prime tests, p-adic principal parts, valuation and rational arithmetic.
- Exact finite tests cover S=empty (ordinary circle), true S-units, missing primes, fake composite-place rejection, CRT-style gauge normalization, quotient invariance, nested projections, dual naturality, seeded holdouts, finite-probe aliasing, and the SUCC-history kernel.
- These tests only operate on **rational dense charts**, not the full R or Q_p topological spaces. The full topological and Pontryagin statements are classical mathematical imports explicitly proved/cited in this paper, not verified by finite code.
- A source ID identifies a declared model, not a physical observer or data authentication.
- No zeros, Weil signs, spectral root data, quantum correlations or RH truth assertions enter these constructions.

## 6. RH dependency graph: remaining gates

    source-attested causal SUCC transitions (OPEN)
      -> faithful lift-and-history category over G_S -> X_S (OPEN)
      -> exact place/character Fourier-natural functor on Schwartz-Bruhat space (OPEN)
      -> Tate global zeta + Gamma/prime/pole + half-density (CLASSICAL TEMPLATE; SUCC identification OPEN)
      -> full test-space Weil distribution (CLASSICAL; source identification OPEN)
      -> source-derived quadratic form equal to Weil, proven PSD for every test (RH-HARD / UNVERIFIED).

Even an exact product formula and a completed functional equation cannot imply the nontrivial zeros lie on the critical line. Test positivity of the **signed complete Weil form**, not a convenient auxiliary covariance. Fake n=6 impulses, conductor/sign mutations, non-Euler controls, and test-domain/limit failures must survive the crucible.

**Next decisive probe:** Construct and try to falsify a functor from source-indexed SUCC event histories into framed adelic lifts, preserving both SUCC translation and FUCC multiplication, then verify the Fourier intertwiners on honest local Schwartz-Bruhat generators. The first missing analytic criterion is a source-derived identification with the completed Weil distribution, with uniform controlled limits and the Archimedean term included. Zero positions may not be used as construction inputs.

## 7. Primary literature and related repository artifacts

- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, Princeton Ph.D. thesis (1950), reprinted as Chapter XV in Cassels–Fröhlich, *Algebraic Number Theory* (1967); §§2.2–2.5, 3, 4.1–4.4. https://math.arizona.edu/~cais/scans/Cassels-Frohlich-Algebraic_Number_Theory.pdf
- Bjorn Poonen, *Tate's Thesis* (MIT 18.786, 2015), especially §§5.2, 5.3, 5.5, 5.7 and 5.10. https://math.mit.edu/~poonen/786/notes.pdf
- SUCC base: observational_succ/diagonal_adele_zeta.py and docs/CLAIM_SUPPLEMENT_ALL_PLACES_ZETA.md; other relevant independent routes: observational_succ/wild_adelic_tower.py and observational_succ/recursive_meta_succ.py.

**Academic priority claim:** none. The adelic and duality facts are classical. Our new research artifact is the typed source-indexed exact implementation, explicit causal-functor obstruction, adversarial controls, and a reviewable Weil/RH dependency frontier.


## 8. The next atomic obstruction: adjoining one prime is nonsplit

### TL-11: nonsplit prime-extension theorem (CLASSICAL GROUP THEORY / PROVED PAPER)

Fix finite S and a genuine rational prime p not in S, T=S union {p}. The natural character-preserving map has the **short exact sequence of compact abelian groups**

    0 --> Z_p --> X_T --pi_(T,S)--> X_S --> 0.

The first map sends z in Z_p to the class of (0; zero on S, z at p). It is injective because an element of the diagonal lattice with real coordinate zero must be zero. The bonding map is onto, and if pi([x])=0 then subtract the principal part of the p-coordinate, then subtract the lifted Gamma_S zero class, leaving precisely a p-integral coordinate z. Hence this is the full kernel.

**The sequence is not split, even as a continuous fiber bundle section.**

**Dual proof (homomorphic splitting forbidden).** Dualizing gives

    0 --> Gamma_S --> Gamma_T --> Q_p/Z_p --> 0,

where Gamma_T/Gamma_S is the p-primary Pruefer group C_(p^infinity), containing the order-p class 1/p + Gamma_S. Gamma_T is torsion-free, since it is a subgroup of Q. A splitting would inject the nontrivial torsion quotient into the torsion-free Gamma_T, impossible.

**Stronger proof (ANY continuous section forbidden).** Both X_S and X_T are connected compact groups since their character groups Gamma_S and Gamma_T are torsion-free. If pi had a continuous (not necessarily homomorphic) section sigma, the map

    X_S x Z_p --> X_T,  (x,z) |--> sigma(x) + z

would be a continuous bijection from compact to Hausdorff, hence a homeomorphism. But X_S x Z_p is disconnected (Z_p has nontrivial clopen subsets), whereas X_T is connected. Contradiction. A merely set-theoretic or measurable section is not ruled out.

This **does not make the global inverse limit nonconstructible** in ordinary mathematics. It shows that a recursive observer cannot obtain a continuous *independent place-by-place splitting* of the next stage: it must retain the genuinely nontrivial extension/gluing structure.

Exact tests use two necessary finite shadows: 1/p belongs to Gamma_T but not Gamma_S, has order exactly p modulo Gamma_S, and the class with omitted p-coordinate 1 is nonzero in X_T but projects to zero in X_S. The statements about all p-adic points, connectedness, and lack of a continuous section are paper proofs/classical imports, not computational results.

### TL-12: an atomic conservation-defect decomposition (CLASSICAL / PROVED LOCAL)

For q nonzero rational, let Delta_S(q) be the modulus of multiplication by q on G_S, even when q is not an allowed quotient endomorphism. Then

    Delta_S(q) = |q|_infinity * product_(ell in S)|q|_ell
               = product_(ell not in S) ell^(v_ell(q)).

When T=S union {p},

    Delta_T(q) = Delta_S(q) * p^(-v_p(q)).

Thus each added true prime places cancels one *additive logarithmic valuation defect*

    log Delta_S(q) - log Delta_T(q) = v_p(q)*log(p).

This is the mathematically exact version of decomposing global multiplicative conservation into atomic prime-place correction terms. The terms in the additive **Fourier phase** reciprocity law are not equal to these real logarithmic terms, however: the former live in R/Z, the latter in R. Their coupling is mediated by a common underlying lattice plus Haar modulus and duality. Any claimed direct identification needs an explicit map between those two differently typed groups.

A revealing contrast: the local correction terms can be computed independently, but the stage extension is **not** the product of independent compact observer spaces. Additive numerical decomposition does not imply categorical splitting.

**Next source-level proof obligation:** define a history-faithful SUCC-to-framed-adelic-transition functor whose action on SUCC/FUCC generators intertwines the lattice extension and the Fourier/Mellin representations. Preserve the nontrivial extension class and sign/half-density conventions. Test full test-function-domain transport and completed Weil distribution next, not a surrogate PSD covariance.
