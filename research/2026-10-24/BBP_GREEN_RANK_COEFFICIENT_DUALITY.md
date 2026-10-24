# BBP Green-source rank × all-order tail-coefficient transport

**Research-only · 2026-10-24 · Operation GREENPRINT.** Stacked on corrected source-fidelity [PR #252](https://github.com/femboy2112/SUCC/pull/252), pinned head 364962ac0c0e8fb4d06c37468a5d50336d68a9ee. The earlier [PR #251](https://github.com/femboy2112/SUCC/pull/251) pole-orbit-closure claim was explicitly superseded by #252. Consult research/2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md.

**Claim boundaries:** Six analytical claims below have paper proofs and rational finite executable checks, NOT Lean proofs. No claim of scholarly priority, pi-normality, RH, source-derived Weil positivity, or physical gravity. Do not merge this draft without the repository's required review and validation.

## 0. Source typing: signed index poles, positive Green spectrum, selected circle phase

At integer n >= 1 the authentic BBP forcing is

    r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)
         = sum_i rho_i/(n-a_i),

where the signed INDEX-variable poles are

    (a_i,rho_i) = (7/8,1/2), (1/2,-1/4), (3/8,-1/8), (1/4,-1/8).

Define the signed pole measure sigma = sum_i rho_i delta_(a_i) with moments

    m_j = sum_i rho_i*a_i^j.

The BBP Stieltjes readout is r(n) = integral (n-a)^(-1) d sigma(a). **These pole coordinates are not points of the radix-16 circle dynamics.** In particular a formal T16 pushforward of sigma does not preserve the source readout. That was the erroneous interpretation repaired in #252.

The real backward Green tail is

    T_n = sum_(k>=1)16^(-k)r(n+k),     n>=0.

Put g(t) = 4 - 2t^3 - t^4 - t^5 and u=t^8. Define finite positive measures on 0<u<1:

    dnu(u) = g(u^(1/8)) / (8*u^(7/8)) du,
    dmu(u) = (16-u)^(-1) dnu(u).

The parent source identity proves exactly:

    r(n+1) = integral u^n dnu(u),
    T_n = integral u^n dmu(u),
    16*T_n-T_(n+1) = r(n+1).

The measure sigma (signed, index pole), the measure nu (positive forcing spectrum), and mu (positive Green memory) live in separately typed representations. The nonlinear selected phase is additionally fixed by the forcing AND its exact initial condition: 16*T_0 = pi, not by generic moment positivity.

## GRC-01 · RESOLVENT / FINITE-TO-INFINITE RANK

Let U be multiplication by u on L²(nu), and let G=(16I-U)^(-1). Then G is a positive self-adjoint bounded resolvent with

    (1/16)I <= G <= (1/15)I,
    T_n = <1,U^n G1>_(L²(nu))
        = <G^(1/2)1,U^n G^(1/2)1>_(L²(nu)).

This is a source-preserving spectral Green map, not an arbitrarily chosen covariance.

The **signed pole moment** Hankel H_pole = [m_(i+j)]_(0<=i,j<4) factors as V diag(rho_i) V^T, V_(i,j)=a_j^i. Its rational determinant is

    det H_pole = -225/549755813888 != 0.

Thus pole moments have Hankel rank exactly four (for sufficiently large finite sections), and their Gram is INDEFINITE. In contrast, for any d>=1 and nonzero vector c,

    sum_(i,j<d) c_i*c_j*T_(i+j)
      = integral |sum_(i<d)c_i*u^i|² dmu(u) > 0,

because mu has strictly positive density on (0,1). The Green-tail Hankel rank is **infinite**. This forbids finite-dimensional TIME-HOMOGENEOUS linear realizations of T_n, not finite descriptions, time-varying laws, nonlinear observers or oracles.

**Proved resolution:** finite index-pole rank and infinite positive Green-memory rank are simultaneously correct, because the types and observation morphisms differ. It is invalid to identify the signed-pole Gram with the positive Green Gram, or either of them with the signed completed Weil form.

## GRC-02 · ALL-ORDER RATIONAL COEFFICIENTS WITH ALL-n ERROR

Let the geometric Green moments be

    M_l = sum_(k>=1) k^l / 16^k.

For every nonnegative integer l they are rational: F_0(z)=z/(1-z), F_(l+1)(z)=z*dF_l/dz, M_l=F_l(1/16). In particular,

    M_0 = 1/15, M_1 = 16/225, M_2 = 272/3375,
    M_3 = 1712/16875.

For q>=0 define the rational coefficient

    c_q = sum_(j=0)^q (-1)^(q-j)*binom(q,j)*m_j*M_(q-j).

**Theorem.** For every integer n>=1 and every integer Q>=0,

    abs(T_n - sum_(q=0)^Q c_q/n^(q+1))
         <= K_(Q+1)/n^(Q+2),

where the explicitly computable finite **rational** constant is

    K_p = sum_i abs(rho_i)*sum_(k>=1)16^(-k)*(k-a_i)^p.

Proof: for each x=k-a_i>0 and integer n>=1, exact finite division gives

    1/(n+x) = sum_(q=0)^Q (-x)^q/n^(q+1)
            + (-x)^(Q+1)/(n^(Q+1)*(n+x)).

Sum against rho_i*16^(-k), apply n+x>=n and the absolute-value triangle bound. The sums in K_p converge because k-polynomial growth is dominated by 16^(-k); their rationality follows by binomial expansion against the M_l. **No false interchange of a k/n expansion over unbounded k is needed.** This is an asymptotic expansion with effective rational remainder, not a claim of convergence in powers of 1/n.

The actual rational coefficients through q=7 are:

| q | c_q |
|---:|---:|
| 0 | 0 |
| 1 | 1/64 |
| 2 | -7/512 |
| 3 | 55/4096 |
| 4 | -595/32768 |
| 5 | 8551/262144 |
| 6 | -149467/2097152 |
| 7 | 3030175/16777216 |

The leading value 1/64 comes from the signed first pole moment m_1=15/64 multiplied by M_0=1/15. ALL higher coefficients likewise retain explicit source information.

**Independent geometric route.** With H(t)=4+4t+4t²+2t³+t⁴, direct polynomial multiplication verifies

    16-t^8 = H(t)*(2-t²)*(t²-2t+2).

As g(t)=(1-t)H(t), the same tail also admits

    T_n = integral_0^1 t^(8n)*(1-t)
                    /((2-t²)*(t²-2t+2)) dt.

The multiplier expanded in v=1-t starts as 1-2v+4v²-10v³+25v⁴-... . Integrating successive beta moments recovers the first rational coefficients independently from the index-pole expansion. Neither representation alone controls a signed digit-orbit Fourier sum.

## GRC-03 · THE COEFFICIENT JET INVERTS THE FINITE POLE SOURCE

Because M_0=1/15 is nonzero, the coefficient map is triangular and exactly invertible:

    m_q = (c_q - sum_(j<q)(-1)^(q-j)*binom(q,j)*m_j*M_(q-j))/M_0.

If the **four distinct nonzero pole positions are already authenticated**, the first four coefficients c_0,...,c_3 determine the four signed residues by the nonsingular Vandermonde linear system [a_i^j]_(0<=j<4).

If only the model class “exactly four distinct nonzero-weight index poles” is authenticated, **eight** coefficients c_0,...,c_7 suffice. Recover m_0,...,m_7, solve the classical four-dimensional Prony system

    sum_(j=0)^3 p_j*m_(k+j) = -m_(k+4),  k=0,1,2,3,

and factor the monic polynomial with coefficients p_j:

    P(X) = X^4 - 2X^3 + (89/64)X² - (103/256)X + 21/512.

Its four roots recover 7/8, 1/2, 3/8, 1/4. The residues then follow by Vandermonde inversion. The signed moment Hankel determinant in GRC-01 proves this four-atom reconstruction is nonsingular.

**Scope:** this is classical Prony reconstruction transported through the BBP geometric Green map. Eight asymptotic coefficients do NOT determine a completely unrestricted positive measure. Treating the finite-pole source class as known is load-bearing, not an innocent technicality.

## GRC-04 · INFINITE HANKEL RANK BUT RATIONAL ORDER-TWO RECURRENCE

The authentic forcing is exactly r(n)=P(n)/D(n), where

    P(n)=120n²-89n+16,
    D(n)=(2n-1)(4n-1)(8n-7)(8n-3).

For n>=0 define the exact positive rational ratio

    R_n = r(n+2)/r(n+1)
        = P(n+2)*D(n+1)/(P(n+1)*D(n+2)).

Eliminate r from two successive Green recurrences:

    T_(n+2) - (16+R_n)*T_(n+1) + 16R_n*T_n = 0.

This homogeneous law has **time-dependent rational coefficients** and order two. Its other linearly independent solution is 16^n (verify by substitution), which grows while the authentic T_n=O(n^-2) is bounded. The forcing and its selected Green boundary condition fix the normalization.

**Infinite time-homogeneous Hankel rank is compatible with finite nonautonomous recurrence order.** This is the most direct structural answer to the SUCC rank-versus-tail question.

## GRC-05 · BEYOND-ALL-ORDERS POSITIVE COUNTERFEIT

The *entire* algebraic tail coefficient jet, plus absolutely continuous positive Hausdorff density and infinite Hankel rank, does NOT select a unique radix orbit in an unrestricted source class.

Set psi(u)=8*(1/2-u) for 0<=u<=1/2 and zero otherwise. This is a nonnegative unit-mass continuous density with rational moments

    q_n = integral u^n psi(u)du
        = 2^(1-n)/[(n+1)(n+2)],       q_0=1.

Since 16*T_0=pi and 0<pi<4, delta=(4-pi)/16 > 0. Define

    dmu_star = dmu + delta*psi(u)du,
    T_n_star = T_n + delta*q_n.

The new measure is absolutely continuous, positive on (0,1), and has strictly positive finite Hankel Grams of all orders. For every fixed p, n^p*(T_n_star-T_n) tends to ZERO: the difference is exponentially small, hence **all inverse-power coefficients c_q agree to every order**. Nevertheless,

    T_0_star = pi/16 + (4-pi)/16 = 1/4,
    16*T_0_star = 4,

so the authentically selected radix-16 circle orbit of the new source is periodic at zero and is **not normal**.

The modified forcing r_star(n)=16*T_(n-1)_star-T_n_star is positive: the perturbation is delta*(16q_(n-1)-q_n)>0. But **the new source is NOT the exact four-pole BBP source**:

    r_star(1)-r(1) = (95/6)*delta > 0.

Every finite index forcing value changes, though the changes decay exponentially. This counterexample defeats claims from only all-order asymptotics, positivity and infinite-rank memory; it does NOT defeat a theorem using all authenticated exact BBP pole readouts.

## GRC-06 · EXACT CONTACT NULLSPACE OF LATE MOMENT OBSERVATIONS

Allowing an atom at spectral zero gives an even sharper boundary:

    mu_contact = mu + delta*delta_0.

For every n>=1 its moments equal T_n EXACTLY, while T_0 changes to 1/4 and the selected radix orbit becomes periodic. All Hankel matrices stay strictly positive. This modifies **only** r(1), by 16*delta; all r(n) for n>=2 are identical.

The nullspace is sharp: if two finite signed Borel measures on [0,1] agree on all monomial moments u^n with n>=1, their difference equals c*delta_0. Proof: polynomials vanishing at zero are uniformly dense in the continuous functions vanishing at zero. The difference annihilates all those functions and must be supported on {0}.

The exact BBP absolutely continuous four-pole source contract rejects both counterfeits. That is precisely why a source-authentication receipt (including r(1) and the initial phase) matters rather than declaring an observation-only universal deduction.

## Source-relative diagnostic table

| Probe / hypothesis | Four-pole BBP | Smooth positive impostor | Contact impostor |
|---|---|---|---|
| Positive Green Hausdorff moments, infinite Hankel rank | yes | yes | yes |
| Every inverse-power c_q | original | **same** | **same** |
| Exact T_n for every n>=1 | original | no, exponentially close | **same** |
| Exact first forcing readout r(1) | original | shifted by 95delta/6 | shifted by 16delta |
| Exact specified four-pole forcing class | yes | **no** | **no** |
| Source-selected 16T_0 mod 1 | pi mod 1 | 0 | 0 |
| Base-16 normality | **OPEN** | **false** | **false** |

This is an explicit example of an observational pathway gap rather than an impossibility theorem. Source class, observation family and phase selection must be recorded independently. It illustrates why a high-rank model and perfectly identified tail coefficients can still give inadequate source authentication.

## Verification and claim ledger

| Claim | Status | Basis / restrictions |
|---|---|---|
| GRC-01 spectral resolvent; signed rank four vs positive rank infinity | **DISCLOSED (paper)** | Spectral integral; Vandermonde determinant; no completed Weil transfer |
| GRC-02 exact all-q coefficients and global rational remainder | **DISCLOSED (paper)** | Finite geometric identity and rational K; exact finite checks |
| GRC-03 fixed/unknown pole Prony recovery | **DISCLOSED (paper)** | Requires the four-pole model class; exact inversion |
| GRC-04 time-varying rational second-order recurrence | **DISCLOSED (paper)** | Elimination of true forcing; exact interval residual checks |
| GRC-05 positive non-atomic same-jet false-normality countermodel | **DISCLOSED (paper)** | Real pi<4 and exponential bump moments; not same forcing |
| GRC-06 spectral-zero atom exact observation kernel | **DISCLOSED (paper)** | Density of polynomials vanishing at zero |
| New independent academic priority | **UNVERIFIED** | All basic methods classical; needs specialist literature audit |
| Signed all-horizon cyclotomic cancellation for pi | **UNVERIFIED** | No qualifying estimate derived |
| Pi normality in base 16, 2, 10 or absolutely | **OPEN** | Not proved here |
| RH, physical source or signed completed Weil positivity | **NOT ADDRESSED** | Do not transfer conclusions |

Implementation: observational_succ/bbp_green_coefficient_transport.py. Adversarial exact tests: tests/test_bbp_green_coefficient_transport.py. Both use the original #252 forcing/index-pole declarations, Python Fraction, and unittest. No floating point pi or invented finite-rank proxy for the true source.

Run the focused tests:

    python -m unittest discover -s tests -p 'test_bbp_green_coefficient_transport.py'
    python -m unittest discover -s tests -p 'test_bbp_source_memory.py'

The wider AGENTS.md requirements (provenance verification, full tests and two foundation probes) remain mandatory before considering admission. Local focused checks are not equivalent to hosted final-head CI or kernel verification.

## Next verdict-changing probe: source-specific signed phases

For fixed nonzero integer h and integer lag d>=1, the missing object is the genuinely SIGNED correlation

    C_d(N;pi) = sum_(j=0)^(N-1-d)
      exp(2*pi*i*h*(16^d-1)*16^j*pi).

GRC-01 to GRC-04 connect source structure to tails exactly; GRC-05 and GRC-06 prove that positive Green rank and all-order coefficients alone cannot force this correlation to cancel in a broad source class. A new proof must use the **entire exact forcing or a certified discriminator that excludes the flat impostors**, the correct selected initial phase, and an independent all-horizon phase bound. It cannot assume equidistribution or smuggle in Weyl's criterion as a hypothesis.

A concrete intermediate instrument: certify rational BBP intervals deep enough that multiplication by 16^N preserves a chosen finite-horizon phase error, then compare signed held-out lags to the smooth/contact counterfeits. This can validate a finite test and falsify overly broad transports; it does **not** prove normality.

**Result: a genuine source-to-infinite-rank connection with effective, invertible arithmetic coefficients; the still-open wall is signed expanding-orbit cancellation.**
