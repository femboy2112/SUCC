# Suzuki / CARLEMAN: an exact prime/Gamma operator bridge and first-wavefront absorption

**Source pin:** SUCC PRIME-SPHERE PR #68, `17f1c8da3948ddce719cde301423cb3e31bf6716`.
**Child:** `research/suzuki-carleman-markov-prime-gluing-2026-10-14`.
**Question:** can the differentiated chiral Markov energy control the authentic prime-2 interaction without changing the original Weil form? **Answer:** yes for a precisely quantified sub-form, not yet for the complete sign.
**Status:** explicit paper proofs below, exact finite regression certificates, independent numerical source checks. Classical ingredients are credited; scholarly novelty and Lean verification are UNVERIFIED. **RH PROVED: no.** No nontrivial zero coordinates, physical measurement, or new arithmetic ontology is an input.

## 0. Intake, acceptance criteria, and what was actually run

The parent is unchanged. AGENTS.md and docs/METHOD.md were read on its exact commit. Related work inspected: PR #63's first-prime endpoint theorem and failed scalar-multiplier shortcut; PR #64's OU bath; PR #68's chiral form; new sibling PR #69's prime-heat source mapping. The latter is NOT an ancestor and is not imported. No preserved archival theorem or implementation was edited.

**Predeclared acceptance:** (i) any proposed gluing must agree with the original prime/Gamma/pole explicit formula on a common core, (ii) auxiliary terms must cancel or be a proved nonnegative remainder, (iii) the prime bound must hold for all states on its stated support, not a numerical trial space, (iv) source/half-density/boundary mutations must fail their respective gates. Ambiguous outcome: a valid bound on a proper sub-form without full Weil positivity. That is the present result.

The GitHub connector provided source reads and branch writes. Direct container git clone failed DNS; a full source checkout was not available. The local directory is an **isolated authored overlay**, not an authenticated checkout of the entire repository. Therefore no full-repository local CI or imported provenance-verifier run is claimed. A primary-source baseline was instead reproduced by comparing the original Weil functional against the new decomposition on 12 analytic test functions. The new module has no external runtime dependencies; optional independent integration uses mpmath.

## 1. Exact source and common domain

Use Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, 23 September 2026, (1.3), (1.8), (2.5), with Fourier transform `vhat(xi)=int v(x)exp(i xi x)dx`. For `v in C_c^infinity(-a,a)` extend v by zero to R. Put

    k_G(t) = exp(-|t|/2)/(1-exp(-2|t|)),  t != 0,
    E_G(v) = (1/2) int_R int_R k_G(x-y)|v(x)-v(y)|^2 dx dy,
    C_G = gamma + pi/2 + 3 log 2 + log pi.

Distributionally differentiating Suzuki's authentic OU expansion gives

    Q_W^a(v) = E_G(v) - C_G ||v||_2^2
             + 2|int v(x)cosh(x/2)dx|^2 - 2|int v(x)sinh(x/2)dx|^2
             - 2 sum_(n<=exp(2a)) Lambda(n)/sqrt(n) Re int v(x+log n)conj(v(x))dx.       (CG1)

This is the original completed source, not a modified Gamma test function. The negative scalar and negative pole rank-one term are retained. At fixed a the non-Gamma terms are bounded on L2(-a,a). Identities and lower bounds on the smooth core therefore extend through Suzuki's closed form, using the same form norm. No claim is made that an arbitrary L2 function has finite Gamma energy; its logarithmic form domain is essential.

## 2. CG2: the auxiliary chiral energy is a component of an exact ORIGINAL Gamma ladder

For each integer k>=0 define the even positive integrable jump kernel and bounded Dirichlet form

    nu_k(t) = exp(-k|t|)/(2 cosh(t/2)),
    r_k = int_R nu_k(t)dt,
    E_k(v) = r_k ||v||^2 - <nu_k*v,v>
           = (1/2) intint nu_k(x-y)|v(x)-v(y)|^2 dx dy >= 0.

Then, for t!=0,

    sum_(k>=0) nu_k(t) = k_G(t),
    nu_(2j)(t)+nu_(2j+1)(t) = exp(-(2j+1/2)|t|).                              (CG2a)

**Proof:** sum the geometric series in exp(-|t|); the pair identity cancels the factor `1+exp(-|t|)` in the denominator. These are identities of positive original-source kernels, not a permission to add an auxiliary bath. Tonelli applied to the nonnegative difference integrands gives

    E_G(v) = sum_(k>=0) E_k(v),                                              (CG2b)

including +infinity for states outside the form domain. In particular E_0 is EXACTLY the parent's differentiated chiral Markov form `pi(I-P)`; E_G-E_0 is a positive remainder. The introduced 3-mod-4 terms have disappeared through telescoping. This resolves the source-projection obligation for this use of the companion chart.

At finite K the kernel remainder is `exp(-K|t|)k_G(t)`, positive, and

    r_0=pi,  r_k+r_(k+1)=4/(2k+1).

These yield exact affine-in-pi rate certificates. The total rate sum diverges; one may NOT call the original Gamma process a finite-rate compound Poisson process. Each finite layer has finite rate.

### CG2c: exact approximation topology

The original Gamma energy has multiplier

    M_G(xi)=sum_(j>=0) 2 xi^2/[alpha_j(alpha_j^2+xi^2)],  alpha_j=2j+1/2.

Equivalently `M_G(xi)=Re psi(1/4+i xi/2)-psi(1/4)`. The finite Markov sums increase pointwise to it. Their full-line resolvents converge strongly by dominated convergence of `(1+M_K)^-1` in Plancherel; no bounded-operator-norm convergence of the unbounded generators is asserted.

For A=K+1/2 and v in H1(R),

    0 <= E_G(v)-sum_(k<K)E_k(v)
       <= [2/A^3 + 1/(2A^2)] ||v'||_2^2.                                   (CG2c)

Indeed the remainder consists of OU jump rates A+2j, its Fourier multiplier is at most `2 xi^2 sum_j(A+2j)^-3`, and decreasing-integral comparison bounds that sum by `A^-3+1/(4A^2)`. This is a derivative-budget bound, NOT a bare-L2 tail bound. The parent's high-frequency obstruction is preserved.

## 3. CG3: the actual operator-level bridge is the classical Carleman operator

Define the unitary logarithmic half-density chart

    U: L2(R_+,dr) -> L2(R,dx),   (Uf)(x)=exp(x/2)f(exp x).

Let the (unnormalized) Carleman operator be

    (Cf)(r)=int_0^infinity f(s)/(r+s) ds.

A change of variables gives the exact operator identity

    U C U^-1 = convolution by [1/(2 cosh(t/2))],
    U (pi I-C) U^-1 = the operator of E_0.                                  (CG3a)

The normalized Markov density is `q=nu_0/pi`; C itself is not a row-normalized Markov kernel in the dr-coordinate. The half-density and measure change are indispensable.

For the Laplace transform `Lf(t)=int_0^infinity exp(-tr)f(r)dr`, Fubini on a dense positive/core class gives

    C=L*L,     E_0(Uf)=pi||f||^2-||Lf||^2.                                 (CG3b)

The classical Carleman bound `||C||=pi` follows here from its known multiplier `pi sech(pi xi)`; hence L extends boundedly with norm sqrt(pi). L is not a unitary coordinate rotation and no surjectivity is claimed. This is standard Hankel/Laplace theory (Yafaev 2012/2014), newly connected to the inherited SUCC Gamma source, not new operator-theory priority.

The entire ladder also has an exact radial representation:

    C_k(r,s) = [min(r,s)/max(r,s)]^k/(r+s),
    E_G(Uf) = sum_k [r_k||f||^2-<C_k f,f>].                                 (CG3c)

This produces a common analytic operator carrier for all original Gamma layers, without introducing nontrivial-zero data.

## 4. CG4: genuine arithmetic operations, not silently flattened chart arrows

The normalized multiplicative action on the radial carrier is `V_p f(r)=sqrt(p)f(pr)`. For ANY p>0,

    U V_p U^-1 v(x)=v(x+log p),
    C V_p=V_p C,     L V_p=V_(1/p) L.                                     (CG4a)

For a genuine prime, this is its authentic prime multiplication action; the source coefficient in CG1 is independently fixed by Lambda. Composite 6 also satisfies these analytic identities and remains an invalid primitive Euler jet. A map of arithmetic point labels is not an identification of ell2(N) with L2(R_+); Dirac point states are not inserted as L2 vectors.

For **additive SUCC** `S_h f(r)=f(r+h)`, h>0, the correct log-chart action is

    U S_h U^-1 v(x)=sqrt(exp x/(exp x+h)) v(log(exp x+h)),
    S_h V_p = V_p S_(ph).                                                  (CG4b)

Thus the additive action is a nonuniform step with a Jacobian, not translation by h in x. Its Laplace intertwiner includes the explicit lost-head receipt

    L S_h f(t)=exp(ht)[Lf(t)-int_0^h exp(-tr)f(r)dr].                        (CG4c)

Dropping this boundary term is false even for f(r)=exp(-2r), h=log2, t=3: the correct answer is 1/20; the ghost answer is 8/5. On compact core states, the Carleman commutator is likewise exactly

    (S_h C-C S_h)f(r)
      = int_0^h f(s)/(r+h+s)ds
        -2h int_h^infinity f(s)/[(r+s)^2-h^2]ds.                            (CG4d)

This retains, rather than erases, the source's affine noncommutation and boundary data. These commuting-with-receipt squares are the justified part of the proposed categorical gluing; no universal arithmetic sphere or global spectral endpoint is asserted.

## 5. CG5: finite prime ladders are direct-integral PATHS with an exact norm

Let T_ell v(x)=v(x+ell), P_a be multiplication by the interval indicator (NOT the mean-zero projection used for Suzuki's u-variable), and L=2a. On the actual v-variable the prime-power term is

    B_(n,a)=-c P_a(T_ell+T_-ell)P_a,  ell=log n, c=Lambda(n)/sqrt n.

Decompose x=-a+r+j ell, 0<=r<ell. The legal locations on each fiber form a finite path. If L=q ell+d with integer q>=0, 0<=d<ell, its fibers have q+1 vertices for width d and q vertices for width ell-d (empty fibers omitted). Endpoints of measure zero do not add an eigen-direction. The source spaces and path widths reconstruct the whole interval measure exactly.

For L>0 the maximum positive-measure fiber length is `M=ceil(L/ell)`. The standard finite-path adjacency eigenvectors `sin(j k pi/(M+1))` therefore prove

    ||B_(n,a)||=2c cos(pi/(M+1)).                                          (CG5)

For L<=ell this is zero; for ell<L<=2ell it is exactly c. This recovers the parent first-wavefront result and extends it to every source threshold. Positive compressed translations compose for positive steps, but inverse shifts do not cancel: states leaving the interval are lost. This is a source-derived finite-automaton disintegration, not a finite-rank approximation to the original operator.

## 6. CG6: genuine first-prime absorption on the WHOLE admissible state space

For all 0<a<=log(3)/2, only prime 2 has a possibly nonzero coupling (at equality prime 3 has zero overlap measure). Here 2a<2log2, so CG5 gives

    |Q_2(v)| <= c_2 ||v||^2,  c_2=log2/sqrt2.

The chiral Markov layer restricted to states supported in (-a,a) obeys

    E_0(v) >= (pi-a)||v||^2.                                              (CG6a)

**Proof:** the nonnegative convolution kernel nu_0 is at most 1/2. Its row integral over a length-2a interval is at most a, and the symmetric Schur test gives `||1_I (nu_0*)1_I||<=a`. Subtract from pi I. A sharper, unneeded bound replaces a by `2 arctan(sinh(a/2))`.

Exact rational enclosures independently certify

    pi-log3/2 > 2.5922865092,
    c_2 < 0.4901290718,
    c_2/(pi-log3/2) < 0.189073 < 1/5.

Therefore for EVERY admissible state, not merely finite test vectors,

    |Q_2(v)| <= (1/5)E_0(v),
    E_0(v)+Q_2(v) >= (4/5)E_0(v) >= 2||v||^2.                             (CG6b)

The numerical displays are explanatory rounded bounds; the code verifies the inequalities as Fractions using Machin arctan, a positive atanh series for logs, and integer square-root bounds. Wrong prime amplitude 4 fails the certificate; fake 6 fails prime-power authentication independently.

Crucially, insert CG2 into the **unchanged** CG1 to obtain

    Q_W^a(v) >= (4/5)E_0(v)+sum_(k>=1)E_k(v)-C_G||v||^2
              +2|int v cosh(x/2)|^2-2|int v sinh(x/2)|^2.                  (CG6c)

This is a source-faithful signed comparison controlling the entire first prime wavefront. It does NOT say the remaining right-hand side is nonnegative. The negative scalar and pole mode have not disappeared. The all-a RH target remains unproved.

## 7. CG7: why one positive Markov layer cannot replace the Gamma tower

For any nonzero odd smooth v supported in the first-prime window, the cosh moment is zero, E_0(v)<=pi||v||^2, and |Q_2(v)|<=c_2||v||^2. If one drops all k>=1 layers and attempts to certify the resulting lower form as positive, it instead satisfies

    E_0(v)-C_G||v||^2+pole(v)+Q_2(v) < -(6/7)||v||^2.                     (CG7)

Indeed `C_G>9/2`, using gamma>0, pi>3, log2>2/3 and log pi>log3>1, whereas `pi+c_2<22/7+1/2`; the difference exceeds 6/7. This decisive negative control kills the shortcut "the first chiral Markov form by itself is the full positive Weil mechanism". Dropping positive terms remains a valid lower-bound operation, but yields an unhelpful negative bound here. It does not refute positivity of the original form.

## 8. CG8: prime-compatible localization has ZERO atomic gluing debt

For real Lipschitz functions phi_i with sum_i phi_i(x)^2=1 and a common finite Lipschitz bound, the exact nonlocal IMS identity on the core is

    sum_i E_G(phi_i v)-E_G(v)
      = (1/2) intint k_G(x-y) Re[v(x)conj(v(y))]
                         sum_i(phi_i(x)-phi_i(y))^2 dx dy.                (CG8a)

Its absolute value is at most `beta ||v||^2`, where

    beta=(1/2) sup_x int k_G(x-y) sum_i(phi_i(x)-phi_i(y))^2 dy < infinity.

Finiteness follows from O(|x-y|^2) cancellation near the 1/|x-y| singularity and exponential decay at infinity. A coarse explicit bound is 18 L_phi^2 when the vector-valued partition has global Lipschitz constant L_phi: use `int_0^infinity t^2 k_G(t)dt=2 sum alpha_j^-3<=18`.

For one atomic prime shift its localization defect is exactly

    sum_i Q_2(phi_i v)-Q_2(v)
      = c_2 Re int v(x+ell)conj(v(x))
                          sum_i(phi_i(x+ell)-phi_i(x))^2 dx.              (CG8b)

Thus choosing charts with `phi_i(x+log2)=phi_i(x)` on the actual overlap makes the atomic defect identically zero. In the first-prime interval, choose a smooth angle equal to zero on both endpoint strips and pi/2 on a smaller central interval; (cos angle,sin angle) gives such a partition. Prime-2 stays wholly in the paired-boundary chart. The Gamma IMS debt is still present and must be bounded. This is the proposed two-E gluing translated into a lawful operator identity, not an assumption that all chart interactions commute.

## 9. CG9: interval compression still destroys free commutation

Full-line Gamma convolution layers commute. Their interval compressions need not:

    [P A P,P B P]=P B(I-P)A P-P A(I-P)B P   when AB=BA.                    (CG9)

An exact independent sampled-source control uses nu_0 and nu_1 at three sites with spacing h=2 log2. Their 3x3 symmetric Toeplitz compressions have commutator entry (0,1) exactly 3/170. This is a finite-lattice control, not a continuum spectrum calculation. It refutes promoting a full-line commuting product to a finite-interval commuting product without checking the lost paths. Likewise compressing the full-line Markov semigroup is not the same protocol as killing a process at first exit.

## 10. Validation and claim ledger

Commands actually run in the isolated overlay:

    python -m unittest discover -s tests -p test_suzuki_markov_gluing.py -v
    python scripts/suzuki_markov_gluing_probe.py --verify research/2026-10-14/SUZUKI_MARKOV_GLUING_RECEIPT.json
    python scripts/suzuki_markov_gluing_oracle.py

23 unittest methods passed. Their exact controls include hundreds of rational Gamma splits, source orbit lengths, action compositions, prime-versus-composite gates, Machin/log/sqrt inequalities, Carleman Jacobians, boundary receipts, IMS identities and noncommuting finite source compressions.

The separate 55-digit numerical oracle uses original Weil autocorrelations versus the reconstructed Gamma energy on 12 sine profiles at a=1/4, log2/2, 3log2/5 and 0.54, with mode numbers 1,2,5. The tolerance 1e-32 was declared before running. Every identity passed; the errors were below 4e-56. It separately checks Laplace-square versus Gamma/Fourier Carleman energy, actual Markov rate integrals, and positive H1 tails. Numbers are calibration, not certified spectral lower bounds. The smallest displayed trial quotient (~0.0005906 at a=0.54, j=1) is an UPPER bound on the variational infimum, not positivity evidence for the whole space.

No complete checkout, full local repository suite, new Lean run, external physical experiment, or global RH proof is claimed. Remote CI must be read on the eventual exact pushed head. A passing test or source lookup never certifies novelty.

**Remaining verdict-changing target:** retain the entire CG2 Gamma ladder and both pole modes, and produce a domain-correct Schur/IMS bound controlling the residual in CG6c. Alternatively use the exact radial Carleman ladder and reciprocal-prime Laplace transport to derive a stronger weighted inequality. The current result resolves one first-prime absorption obligation, not all-a Weil positivity or Suzuki's compact-uniform spectral limit.

### Primary references and provenance

- Suzuki (2026 v3): https://arxiv.org/html/2606.09096v3 — original Weil functional, (1.3), (1.8), (2.5), form-core statements.
- Yafaev (2012), *Spectral and scattering theory for perturbations of the Carleman operator*: https://arxiv.org/abs/1210.5709 — classical Carleman spectral theory.
- Yafaev (2014), *Quasi-diagonalization of Hankel operators*: https://arxiv.org/abs/1403.3941 — classical Laplace-square framework.
- Parent local proofs: research/2026-10-14/PRIME_CATEGORICAL_SPHERE_GAMMA.md, PS-10; research/2026-10-13/SUZUKI_SOURCE_WAVEFRONT_ROUND_001.md, SW-4/SW-6. These are shared provenance, not independent witnesses.
