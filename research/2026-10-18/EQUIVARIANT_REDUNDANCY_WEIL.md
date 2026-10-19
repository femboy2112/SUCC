# Equivariant Redundancy and the Weil Trace — a source-indexed no-ghost theorem and homotopy-defect reconstruction

**18 October 2026. Research extension:** research/equivariant-redundancy-weil-2026-10-18, stacked on research/oriented-mobius-adelic-descent-2026-10-18@793f559ecf4fee9c9b03b98020bb20e3d7e36f3e (draft PR #172). Main and original imported source artifacts untouched. **RH PROVED: NO.**

**Research question.** We may introduce structure not previously visible to the original SUCC/FUCC source, but when, precisely, does it count as *redundant*? Can its arbitrary homological choices cancel while recovering true arithmetic traces, and can the resulting positive Hodge form be identified with the ORIGINAL completed signed Weil form?

## 0. Source baseline and mathematical boundary

Original input is integer SUCC S|n>=|n+1>, genuine prime FUCC V_p|n>=|pn>, full prime-power labels n=p^k, true von Mangoldt Λ(n)=log(p), half-density n^-1/2, and the ONE real Archimedean Gamma plus pole/contact. The inherited completed Weil source and finite-Gamma transport are documented in research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md and observational_succ/one_object_transport.py. The local source-typed Q_p^× off-identity Connes factor is documented in the parent PR #172. No zero locations were used in this work. Auxiliary forms and chain complexes are not asserted to be physically authenticated events.

The classical inputs are elementary Koszul/Clifford homology, finite-chain Lefschetz supertrace, positive-semidefinite bilinear-form descent, Schur complements and the Connes/Tate/Weil papers. They are *not claimed as novel academic priority*. The novel-to-SUCC content is the exact source-relative packaging, concrete arithmetic chain quotients, no-go boundaries, and executable independent controls.

## ERW-01. Redundancy is a relative commuting-square contract

Let q:Vtilde->V be a surjective linear source-observation map, K=ker q, and let A be the original permitted source dynamics/probe algebra. Auxiliary information K is **observationally redundant for a declared symmetric/Hermitian source form** Btilde iff Btilde(x,y)=B(qx,qy) for all x,y, for one well-defined B on V. Equivalently

    K subset rad(Btilde), i.e. Btilde(k,x)=0 for all k in K and x in Vtilde.

This is NECESSARY and SUFFICIENT. It requires the entire row/column block on K to vanish; mere acyclicity is not enough. When Btilde is PSD, requiring Btilde(k,k)=0 for every k is sufficient by Cauchy–Schwarz; for signed forms that diagonal shortcut is invalid.

For a source action Ttilde to descend uniquely to V, the necessary and sufficient law is Ttilde(K) subset K. In block coordinates Vtilde=V⊕K this means its top-right (hidden-to-visible) block is zero. If every generator of the original probe algebra satisfies that condition, all legal finite compositions descend. If even one future probe activates hidden data, the information is NOT dynamically redundant although invisible to a present observer. No-go and positive controls are exact rational matrices. These are the same kind of source-indexed quotient requirements already used in SUCC's no-ghost and dynamic-Fourier research, now explicitly married to signed quadratic-form descent.

### A positivity trap survives contractible auxiliaries

Let the visible form be A, hidden C>0, and mixed coupling B. Minimizing the full energy in the hidden variables yields the EXACT Schur shorting:

    W_eff = A - B C^-1 B*.

C>0 alone does not imply W_eff>=0. For A=1,B=2,C=1, W_eff=-3 even though the hidden block is strictly positive. For A=5,B=2,C=1, W_eff=+1. The full quadratic form must be positive or a new source-derived bound must establish domination; auxiliary Hodge positivity alone cannot do so. A null extension diag(-1,0,0) can be quotiented perfectly, yet the original negative visible form remains negative.

**Verdict:** inserted mathematical information can be removed with zero source loss, but *the source form and the whole permitted future dynamics must certify that removal*. One cannot label all contractible/positive high directions “unobservable” by choice.

## ERW-02. The exact finite Lefschetz supertrace no-go on Koszul prime fibers

For each n>=1 let K_n denote the full prime-polynomial multidegree Koszul exterior complex from the parent work. It has basis wedges S subset supp(n), differential d lowering wedge degree, and an explicit contracting homotopy h when n>1. In particular H_j(K_n)=0 for ALL j when n>1; K_1 has H_0=Q.

**Finite-chain theorem.** For a degree-preserving chain map T commuting with d,

    Str_{K_n}(T) = sum_j (-1)^j Tr(T|H_j(K_n)).

Proof (not a numerical assumption): split each finite chain degree into boundaries, chosen lifts of boundaries, and homology representatives. Since T commutes with d, its diagonal trace on boundaries in degree j cancels exactly against the trace on their isomorphic lifts in degree j+1, leaving the action on homology. Choices of complements do not affect traces.

Consequently, for every n>1 and EVERY admissible chain-map T, Str(T)=0. In particular every scalar original logarithmic test f(H_n) acts as f(log n) I and commutes with d, so

    Str_{K_n}(f(H_n)) = f(log n) sum_{S subset supp(n)}(-1)^|S| = 0.

But the original signed Weil explicit-formula prime-power distribution has NONZERO atoms at every genuine p^k, with coefficients -log(p)/sqrt(p^k) at the two log-clock locations. Thus the candidate “completed Weil = ordinary source-compatible Koszul supertrace of f(H)” is **REFUTED already at p=2**. The ordinary finite source trace cannot produce prime impulses by erasing all acyclic fibers.

This does NOT rule out an analytically regularized infinite-dimensional trace with an explicitly established anomaly, a relative trace, a boundary defect, or a probe that fails to commute with d. Those possibilities need declared trace domains, source support and regularization controls. Merely saying “infinite” does not override the finite theorem.

## ERW-03. Source FUCC acts by a chain map — but the first prime activation is NOT quasi-isomorphic

Let j_{p,n}:K_n->K_{pn} preserve the literal exterior subset S and multiply the underlying polynomial monomial by x_p. Since the original Koszul differential is polynomial-R-linear, d_{pn} j_{p,n}=j_{p,n} d_n. The source module proves this by exact basis maps against the inherited full-powers Koszul differential.

There are three fully classified cases:

- If p divides n already: supp(pn)=supp(n), the exterior subset map is an isomorphism of complexes. Quotient zero.
- If p does not divide n and n>1: the quotient K_{pn}/j K_n is, up to a one-degree shift and a parity sign, the Koszul complex K_n itself. Both are acyclic, so the quotient is acyclic. This is a legitimate DERIVED redundancy statement about *these chain objects*.
- If n=1 and p is first activated: K_1 has one degree-0 state, K_p has degree-0 and degree-1 states with d(theta_p)=1. The image is the degree-0 subspace. The quotient has H_1=Q; it is NOT acyclic and j_{p,1} is NOT a quasi-isomorphism.

Moreover d* fails to commute with j_{p,n} whenever a previously absent prime first appears: the target's newly available exterior creation theta_p is absent from the source. Thus an ordinary chain-map law for d is NOT the stronger Hodge/adjoint equivariance contract. This is a precise, origin-indexed source defect; even if its quotient is acyclic for n>1, one still has to check the relevant adjoint-valued source tests.

## ERW-04. An exact positive example: finite exterior multiplicities ARE removable for a specified arithmetic trace

Let H|n,S>=log(n)|n,S> and use the isometric source chain inclusion j_{p,n}. Arithmetic multiplication gives

    j_{p,n}* [H,j_{p,n}] = log(p) I_{K_n}.

Therefore its ordinary source-restricted normalized trace is

    (1/dim K_n) Tr_Kn(j* [H,j]) = log(p).

The new exterior dimensions at the target do not affect THIS observable. This is an honest source-relativity statement: the trace normalization divides the arbitrary exterior multiplicity 2^omega(n), and unique prime factorization proves the log-clock value without numerical logarithm fitting. No zero-side data enter.

Do not identify this particular finite source-normalized trace with Connes' global trace: other observables and the full SUCC action distinguish added exterior states. This is a positive example of **restricted redundancy**, not a global equivalence.

## ERW-05. Stabilizing every fiber enables SUCC isometries, but ghosts are future-observable

At n=6, dim(K_6)=4 while at n=7, dim(K_7)=2, obstructing a fiber-to-fiber isometric unit successor with no new space. Choose a common finite exterior prime pool F and use the same Fock wedge space E=Lambda(Q^F) at every source n. The map S|n,S>=|n+1,S> is now an isometry.

However at n=1, theta_2 is an extra “ghost” outside the authentic K_1. After unit SUCC 1->2 or genuine FUCC V_2, it belongs to the authentic source K_2 and d(theta_2)=1. Thus it is not dynamically redundant under the authentic action family. Similar source exposure occurs with theta_7 along 6->7. The test checks both positive reactivation and the reverse case where a once-valid wedge becomes a ghost.

A general **operator obstruction** is independent of that finite model. If Q and Q* both commute with S and H={Q,Q*}, then H must commute with S. But for the actual source arithmetic energy,

    [H,S]|n> = (log(n+1)-log n)|n+1> != 0.

So a representation that reproduces this H cannot make BOTH the graded supercharge and its adjoint S-equivariant. At least one connection/commutator defect is load-bearing. The finite stabilized checker limits log-energy claims to prime pools containing every genuine prime of n AND n+1; it does not silently treat omitted places as nonexistent.

## ERW-06. Stronger theorem: an arbitrary contracting homotopy drops out of the source anomaly

For ANY finite contractible graded complex, take odd d,h with dh+hd=I, and any even operator T. Graded cyclicity of ordinary finite trace proves

    Str(T)=Str(T d h)+Str(T h d)
          =Str((T d-d T)h)
          =Str([T,d]h).

This theorem does **not** require T to commute with d. If T DOES commute with d, its supertrace vanishes. A nonzero source signal is precisely a chain-equivariance defect paired with the contracting homotopy.

For genuine n>1, take the canonical source grade-zero projector P0, which is defined without the zeros of zeta. The Koszul differential lowers exterior degree, and

    Str_Kn(P0)=1 = Str_Kn([P0,d_n] h_{n,p})

for **every chosen active prime pivot p|n**. Different pivots produce visibly different intermediate homotopies h_{n,p}=exterior-wedge(theta_p), but the final source trace remains exactly ONE. The arbitrary introduced homotopy is therefore redundant for THIS observable. This is a finite certified instance of “invent information, then prove it cancels.” The trace uses the genuine original n fiber; no pole/Gamma information is guessed.

The model is NOT secretly discovering primality from its homogeneous complex: the grade-zero defect equals one on ALL n>1, including n=6. The actual source-derived **prime-power projector** remains necessary. This is an essential provenance control.

### Prime sector of the ORIGINAL signed Weil distribution (all compact log tests)

The source arithmetic also supplies on the finite-support domain

    V_p* [H,V_p] = log(p) I,
    half-density = p^(-k/2) on n=p^k.

Therefore for every h in C_c²(R), whose prime-power support is finite,

    W_prime(h)
      = - sum_(n=p^k>=2) [log(p)/sqrt(n)]
             (h(log n)+h(-log n))
             Str_Kn([P0,d_n] h_(n,pivot)).

Each supertrace factor is exactly 1, independently of the chosen pivot, so the right side is IDENTICALLY the authentic prime-power sector of the inherited Weil distribution, with no nontrivial zeta zeros used. The code keeps log(p)/sqrt(n) symbolically to avoid pretending that rational amplitude SQUARED 1/n is the amplitude itself. Fake composite6 probes are rejected as nonprimepower impulses.

This is a **universal (all compact tests) but only PRIME-SECTOR equality**, not a proof of Weil positivity. The already existing analytic source gives W=W_prime+W_arch+W_pole/contact with proper finite-Gamma/truncation domains. We have not rewritten or eliminated W_arch or contact. Thus gluing the new exact prime identity to the inherited original source yields exactly the same signed W, not a new positive form.

### Why the result matters

The added homotopy's specific pivot **does cancel**; the original prime-power weight **does not**. The surviving invariant is the source-relative defect [P0,d], not an arbitrary global choice of positive/negative sign. This gives a concrete mathematical target for a possible Connes-to-Weil transport: derive the relevant even test operator T_h FROM a genuine adelic scaling/test representation and prove its defect trace agrees with the canonical local/global trace, including the identity singularity. It would be circular to choose T_h solely by fitting the desired Weil coefficients.


## ERW-09. Stronger “redundancy” theorem: the original FUCC multiplication is a KOSZUL BOUNDARY (PROVED CLASSICAL)

This is a nontrivial strengthening of ERW-03. Work in the complete prime-polynomial Koszul module K=R tensor Lambda(theta_p) with differential d=sum_q x_q iota_q. Write epsilon_p for exterior wedge with theta_p. The Clifford relation {iota_q,epsilon_p}=delta_qp yields on the full module, with the natural homogeneous degree maps:

    d epsilon_p + epsilon_p d = x_p I = V_p.

Both terms map source multidegree n to the original target p*n. This holds at first prime activation (even n=1), repeated prime powers, and cross-prime multidegrees, WITHOUT truncating actual p²/p³ states. The implementation constructs the source/target chain map and independently checks both terms on every genuine exterior wedge.

**Consequently the nonzero original FUCC operator V_p is null-homotopic as a map of Koszul complexes.** In the derived/homology quotient its class is zero, although V_p|n>=|pn> is absolutely nonzero on the original integer source. The original arithmetic carrier and its observational action are *not faithfully represented by Koszul homology*. This gives a source-indexed mathematical reason why “homologically redundant” cannot mean “safe to erase for all arithmetic measurements.”

The source arithmetic logarithm acts by H|n,S>=log(n)|n,S> on each total-degree fiber. Therefore epsilon_p raises arithmetic energy by log(p), with the exact graded identities

    [H,epsilon_p] = log(p) epsilon_p,
    [H,V_p] = [H,{d,epsilon_p}] = log(p) {d,epsilon_p}
            = log(p) V_p.

The equalities are algebraic on the finite-support source core. They explain why the log-prime clock survives at CHAIN LEVEL as the energy of a nullhomotopy witness even though ordinary homology erases the multiplication map itself. Its canonical source-restricted trace is ERW-04. This is not a new RH operator construction, and the unbounded full-infinite-places trace/domain remains unbuilt.

**New discriminating gate:** any proposed functor to Connes' adelic trace that factors only through Koszul homology must send every V_p and [H,V_p] to zero. It cannot then recover the actual nonzero prime-power fixed-point/explicit-formula response without separately retained boundary, equivariant chain data, or a rigorously defined trace anomaly. The missing “information” must be shown source-redundant only AFTER such an enhanced action is transported and tested; homology alone provably forgets too much.


## ERW-10. What is NOT redundant: the canonical identity contact (PROVED EXACT TEST)

The off-identity Connes local factor and the homotopy prime distribution can agree on every test whose support avoids the identity, while their extensions around the identity still differ by c*delta_1 in the multiplicative chart (c*delta_0 in the additive log chart). This is a real source-map ambiguity until Fourier/Haar/contact normalization has been independently supplied. It can change the Weil quadratic form even on ORIGINAL admissible autocorrelation tests.

A calibrated concrete test is f(t)=(1-t²)^3 for |t|<=1 and zero elsewhere. This is a genuine C_c² function: its first two derivatives vanish at the boundary. Let h=f*tilde(f), so h(0)=||f||². Exact integration gives

    h(0)=int_-1^1 (1-t²)^6 dt = 2048/3003 > 0.

Therefore

    (W+c delta_0)(h)-W(h)=c*(2048/3003).

The prime-power distribution away from log-time zero is unchanged, and every off-identity local Connes test has the same value, yet an authentic Weil autocorrelation changes unless c=0. This directly proves that the canonical contact datum is NOT redundant under the required full test algebra. It cannot be freely chosen to manufacture a positive form. The implementation checks the rational integral independently by the beta recurrence I_m=(2m)/(2m+1)*I_(m-1), I_0=2, as well as both positive and negative mutations. The result does not claim the original canonical c is nonzero or that an actual Weil witness is negative; it diagnoses insufficiency of off-identity data.

## ERW-07. Exact no-ghost / positivity comparison and what can falsify it

The completed signed Weil form on the appropriate convolution tests is RH-equivalent to positivity. An auxiliary positive Koszul-Hodge Laplacian only certifies energy positivity in its constructed carrier; the required equality with W has NOT been proved. An all-test reconstruction must satisfy:

1. **Original source and topology:** genuine p^k, primitive log(p), half-density, one real Gamma, completed pole/contact, character conductor/phase and admissible Schwartz–Bruhat/Weil test domains.
2. **Equivariant reduction:** characterize exactly which chain states are forgotten, which source observables vanish on them, and which original SUCC/FUCC/idelic dynamics preserve that kernel; no hidden future reactivation.
3. **Test-distribution commutative square:** source-derived T_phi from actual Connes scaling/Haar/Fourier data satisfies a canonical principal-value trace identity, including at u=1. Matching local p^k magnitudes or exact off-identity Qp balls is not enough.
4. **Positive sign:** prove the entire remaining signed form, including the Schur correction when auxiliaries couple, is >=0 on EVERY required autocorrelation test. A fitted positive Gram, a finite positive matrix or a contractible auxiliary is insufficient.

**Verdict-changing probes.** If the candidate T_phi is a chain endomorphism on acyclic fibers and uses only its supertrace, it must lose all prime impulses (ERW-02). If the candidate uses the P0 defect, test fake6 and p² and compare an *independent* original Weil atom oracle and compact balls. If the quotient's null source form changes under SUCC or FUCC, it is not redundant (ERW-05). If Schur A-B C^-1 B* has a certified negative direction while only C is positive, the proposed positivity inference is refuted, not RH. If a new trace identity fails on a compact bump with its Gamma/contact and Fourier conventions preserved, the full Connes identification is refuted. Surviving finite tests are evidence of implementation fidelity, not universal positivity.

## Provenance, execution, and status

**Files (new, additive only):**
- observational_succ/equivariant_koszul_descent.py
- observational_succ/observable_redundancy_forms.py
- observational_succ/stabilized_exterior_source.py
- observational_succ/source_homotopy_defect.py
- four exact independent tests/test_*.py counterparts
- .github/workflows/equivariant-redundancy-weil.yml
- this manuscript and docs/CLAIM_SUPPLEMENT_EQUIVARIANT_REDUNDANCY.md

**Ancestor code and source contracts:** original Koszul PrimeKoszul, SUCC arithmetic H and von_mangoldt_labels, the signed finite-Gamma W_J and source admissible tests, authentic Tate/Connes off-identity compact-open Haar, projective full p^k radial origin, archived frozen provenance manifest. No original files overwritten; no zero-side arrays.

**Independent standard proof of ERW-09:** The Stacks Project, [Koszul complex Lemma 15.29.5–15.29.6](https://stacks.math.columbia.edu/tag/0621), proves exactly f=d(e∧-)+(e∧-)d and that multiplication by each Koszul generator is null-homotopic. SUCC's new result is the source-typed identification of this classical law with true FUCC prime multiplication and its observed log-clock, not discovery of a previously unknown algebraic theorem.

**Primary / classical references:** Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1999), arXiv:math/9811068; Connes–Consani, *Weil positivity and Trace formula, the archimedean place* (2021), arXiv:2006.13771 (restricted Sonin trace); Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (23 September 2026). Finite chain Lefschetz supertrace, Koszul/Clifford, rank-nullity, Sylvester/Schur and product formula are classical imported algebra.

**Reproduction:** python -m unittest discover -s tests -p 'test_equivariant_koszul_descent.py' -v; analogous test_observable_redundancy_forms.py, test_stabilized_exterior_source.py, test_source_homotopy_defect.py; scripts/verify_provenance.py. Focused GitHub workflow runs Python 3.10 and Python 3.13 and the inherited Koszul regression. Full repository test validation is separate and is not inferred from focused tests. Status flags in all APIs retain RH_proved=False and full Connes/Weil identification=False.

**Ledger:** ERW-01/02/03/04/05/06/09/10 proved local or classical; ERW-07 full global transport and RH UNVERIFIED. Nothing is a proof of RH or a new independent academic priority.
