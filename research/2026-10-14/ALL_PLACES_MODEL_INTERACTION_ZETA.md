# SUCC — all-place source atlas, interacting prime models and analytic zeta gluing

**Checkpoint:** 2026-10-14. **Stacked parent:** `research/real-place-weil-identification-2026-10-14@55307fec354be0c671562233ca744907cf716ca5` (draft PR #71, behind #69/#67/#65). **Research branch:** `research/all-places-model-interaction-zeta-2026-10-14`. Do not alter `main`, old receipts or provenance archives. **Status:** classical number theory (Tate/CRT/Poisson/Möbius) reassembled as a source-typed and executable mathematical observation system, with explicit proof-level analytic tail bounds; academic priority UNVERIFIED. **RH PROVED: no.** No nontrivial-zero locations or unperformed physical measurements are construction inputs.

## 0. User object and repaired interpretation

The author's proposal: an embedded E models other SUCCs *inside the same carrier*, then investigates laws governing **the models' interactions**. The interaction law may justify analytic truths outside the Euler product's nice half-plane without E physically leaving its original location. The phrase "all places" here means the ordinary places of **Q** (one real and one for every genuine prime), and "complete zeta" means

`Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s)` (meromorphic; poles 0,1),
`xi(s) = s(s-1)Lambda(s)/2` (entire),

NOT a separate new zeta function at every point of the spectrum, all Dirichlet/Hecke L-functions, completed Weil positivity, all embeddings of number fields, a physically real observer that queries infinitely many places, or an approximation of RH by finite checking.

**Correctness principle.** A mathematically exact finite model cannot *alone* justify analytic continuation. The load-bearing new model relation is **Poisson reciprocity on one original integer/rational carrier** plus suitable domains/convergence. After it is independently proved, an internal E may use it to derive consequences across the complex plane, without actually executing infinite many field experiments. The same behavior for generic affine/composite-digit SUCCs does not authenticate primes.

## 1. All places and one source: two independently exact coherence constraints (AP-01–03)

For `x=a/b in Q^×` in lowest terms, let `v_p(x)=v_p(a)-v_p(b)`, and choose normalized absolute values `|x|_p=p^(-v_p(x))` and the usual real `|x|_infinity=|a/b|`. Unique prime factorization gives the **finite-support** all-place product formula

`|x|_infinity * prod_p |x|_p = 1`.

The code factors the numerator and denominator independently; *no infinite loop over all primes* is performed. Define p-adic fractional-part `fr_p(x) in [0,1) ∩ Z[1/p]` as the unique residue modulo `Z_p`; when `v_p(x)<0`, invert the denominator's p-adic unit modulo the requisite `p^k`. With

`psi_infinity(x)=exp(-2pi*i*x)`, `psi_p(x)=exp(2pi*i*fr_p(x))`,

CRT gives `x - sum_p fr_p(x) in Z`. Thus **the product of additive characters is one on diagonal Q**. For `x=7/12`, the p=2 and p=3 fractional parts are respectively `1/4`, `1/3`; their sum is `7/12`. Omitting either prime destroys this coherence. Tests enumerate 1920 rational source forms and another 935 rational additive-character probes, checking direct factorizations. A source ID or name by itself does NOT prove the actual mathematical/physical source map.

For each genuine p and integral Re(s)>0, normalize multiplicative Haar measure so `vol(Z_p^×)=1`. Shell decomposition

`Z_p \ {0} = disjoint_union_(k>=0) p^k Z_p^×`

gives the local Tate zeta integral

`Z_p(1_{Z_p},s)=sum_(k>=0) p^(-ks)=1/(1-p^(-s)),   Re(s)>0`.

At infinity, with `f_infinity(x)=exp(-pi*x^2)` and `d^×x=dx/|x|`, the local integral is

`Z_infinity(f_infinity,s)=pi^(-s/2)Gamma(s/2),    Re(s)>0`.

Each local real/p-adic factor has its own analytic meaning; the **global** product converges absolutely only for `Re(s)>1`. A finite prime model `P` has only a finite Euler product; it does not acquire the all-prime continuation by being interpreted at Re(s)=1/2.

**Finite Fourier model.** On `G=Z/p^(2r)Z`, subgroup `H=p^r G` has |H|=p^r, and the normalized character transform `p^-r sum_(x in H) exp(-2pi*i*k*x/p^(2r))` is exactly `1_H(k)`. This is an honest exact finite shadow of the standard local self-duality `Fourier(1_{Z_p})=1_{Z_p}` under the properly normalized additive character/Haar measure. The finite shadow is *not* a standalone proof of the infinite Q_p identity; that established local harmonic analysis is an external mathematical ingredient. Mutating the subgroup depth or normalization fails.

**Literature:** J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (1950; published Cassels–Fröhlich 1967), Chapter XV (https://old.maa.org/node/110814); Columbia Tate notes (https://www.math.columbia.edu/~avizeff/quals/Tate.pdf); NIST DLMF §§20.7,20.10,25.4,25.5,27.10 (https://dlmf.nist.gov/25.4 and https://dlmf.nist.gov/27.10).

## 2. Category of finite source-model interactions (AP-04–06)

For a finite set `P` of genuine distinct prime-place labels, let `m=prod_(p in P) p` (empty P: m=1), and define the *sieved integer source theta observable*

`Theta_m(t)=sum_(n in Z \ {0}, gcd(n,m)=1) exp(-pi*t*n^2),  t>0`.

Each `P` is a **mathematical observation context over the SAME original Z**. An attached prime p not dividing m refines the original state predicate, without pretending a separate sensor was built:

`Theta_(mp)(t) = Theta_m(t) - Theta_m(p^2*t)`.                 (AP-04)

**Proof:** among integers with gcd(n,m)=1, those not coprime to p are exactly `n=p*q` with gcd(q,m)=1 (because p∤m). Their Gaussian heat is `exp(-pi*p^2*q^2*t)`. This is an equality of infinite functions for every t>0; absolute heat convergence justifies subtraction. Crucial source gate: p must be genuine and new. If p|m the q↔pq source relation fails, so the engine refuses that comparison.

For distinct new primes p,q, applying these two refinements in either order gives the source-faithful square

`Theta_(mpq)(t)=Theta_m(t)-Theta_m(p^2*t)-Theta_m(q^2*t)+Theta_m(p^2*q^2*t)`.

General finite faces carry Möbius signs `(-1)^|A|` for subsets of attached primes A, so the higher cube coheres by ordinary commuting dilation/Boolean inclusion-exclusion. These are **genuine model-level relations**, not mere similarity of visual diagrams. They have typed provenance: same source ID, basis, epoch, real Gaussian and Fourier convention; duplicate primes or mismatches are refused.

The CRT/frequency counterpart is exact:

`c_m(k) = sum_(r modulo m, gcd(r,m)=1) exp(2pi*i*k*r/m)`
`       = sum_(d|gcd(m,k)) d*mu(m/d)`,

and for squarefree `m` its Fourier character sum decomposes into the **interacting true-prime local clocks**:

`c_m(k)=prod_(p|m) (p-1 if p|k else -1)`.

The engine computes the divisor-side formula with pure integers and compares against an independently coded direct finite character sum and the prime factor formula. These phase coefficients matter: making them all positive or deleting a local clock does not preserve theta Fourier transport.

## 3. From source models to meromorphic global analytic truth (AP-07–09)

**Fundamental spectral gluing law.** For m>=2, Fourier/Poisson summation on each arithmetic progression gives

`Theta_m(t)= 1/(m*sqrt(t)) sum_(k in Z) c_m(k)*exp(-pi*k^2/(m^2*t))`.

For m=1, the original theta has the zero-state correction `Theta_1(t)=t^-1/2(Theta_1(1/t)+1)-1`. This correction is **not optional**: it produces the -1/s pole below. The source can be reconstructed by the independent Möbius representation

`Theta_m(t)=sum_(d|m) mu(d)*Theta_1(d^2*t)`.

The projected Mellin transform is initially defined, for `Re(s)>1`, by

`Lambda_m(s) = (1/2) integral_0^infinity Theta_m(t) t^(s/2-1) dt`
`           = Gamma_R(s) sum_(n>=1,gcd(n,m)=1) n^-s`
`           = Gamma_R(s) zeta(s) prod_(p|m)(1-p^-s)`.

For m>=2, split the t-integral at **t=1**, apply the exact spectral relation to the small-t side, and substitute u=1/t. The source-derived result is

`Lambda_m(s) = [phi(m)/m]/(s-1) + sum_(n>=1,(n,m)=1) I_n(s) + 1/m sum_(k>=1) c_m(k) J_(m,k)(s)`

where

`I_n(s) = (pi*n^2)^(-s/2) Gamma(s/2, pi*n^2)`,
`J_(m,k)(s) = (pi*k^2/m^2)^((s-1)/2) Gamma((1-s)/2, pi*k^2/m^2)`.

These *upper incomplete Gamma* terms are **entire** in s for each fixed positive lower argument. Both infinite sums converge absolutely and locally uniformly everywhere due to Gaussian decay in n and k (proof §4). Thus this formula constructs a **meromorphic continuation to ALL s** with only a possible simple pole at s=1 (actual residue phi(m)/m). It is not evaluating a divergent Euler product.

For m=1, the zero-state boundary instead gives

`Lambda_1(s) = 1/[s(s-1)] + sum_(n>=1) I_n(s) + sum_(k>=1) I_k(1-s)`.

This formula is meromorphic on C with the usual poles s=0,1. The **stable entire** construction is

`xi(s)=1/2 + s(s-1)/2 * [sum_n I_n(s) + sum_n I_n(1-s)]`.

No numerical zeta library and no nontrivial-zero list enters either constructive evaluator. `xi(0)=xi(1)=1/2` and `xi(s)=xi(1-s)` are manifest from the expression. On Re(s)>1, Mellin/Dirichlet calculation identifies it with the authentic completed zeta; uniqueness of meromorphic continuation then identifies it throughout C. This is the classical Riemann theta proof, here made source-typed and separately certified by finite truncation bounds.

**The decisive interaction theorem (AP-09):** from AP-04 the Mellin transforms obey

`Lambda_(mp)(s) = (1-p^-s) Lambda_m(s)` for Re(s)>1.

Both sides are already meromorphic on **all** C from the independent theta/Fourier gluing; hence the identity theorem extends the relation as a meromorphic identity to every s. The relation can also be checked by direct source-level theta subtraction. No step leaves E's mathematical carrier or requires sampling Euler products where they diverge. But the analytic prerequisites are genuine: *just having abstract models and their finite relations does not automatically imply continuation*.

## 4. Uniform, exact rational analytic error certificates (AP-10)

Let `N,K>=1` truncate the positive n and positive k series of §3. Set `M>=0` and consider ANY complex s with `-M<=Re(s)<=M`; **there is no bound on Im(s)**. Write

`C_1=max(M/2-1,0)`, `C_2=max((M-1)/2,0)`,
`A=3*N^2`, `B=(3/m^2)*K^2`.

Assume `A>C_1` and `B>C_2`. For an integer power `L>=1`, define the *exact nonnegative rational number*

`epsilon_primal = (1+A/L)^(-L) / (6*N*(A-C_1))`,
`epsilon_dual   = phi(m)*(1+B/L)^(-L) / [2*m*(3/m^2)*K*(B-C_2)]`.

**Theorem:** the difference between the exact meromorphic `Lambda_m(s)` and the finite expression in §3 is absolutely at most `epsilon_primal+epsilon_dual` on this entire vertical strip (at s=0,1 interpret the polar part separately; the same estimate applies to the **entire remainders**). For m=1 the formula still holds for the finite remainder; to certify xi, multiply by |s(s-1)|/2.

**Proof:** for `t>=1`, monotonic Gaussian tails obey

`sum_(n>N) exp(-a*n^2*t) <= integral_N^infinity exp(-a*x^2*t) dx <= exp(-a*N^2*t)/(2*a*t*N)`.

Also `log t<=t-1`, so `t^q<=exp(max(q,0)(t-1))`. Integrate the resulting decaying exponential. Apply `pi>3`, and finally `exp(-x)<=(1+x/L)^(-L)` from `exp(x/L)>=1+x/L`. The spectral series has coefficients `|c_m(k)|<=phi(m)` and `a=pi/m^2`; its exponent is `-(Re(s)+1)/2`. This gives precisely the displayed rational formulas, with no dependence on Im(s). The 41 targeted tests compare certificates against a **separate** analytic special-function/zeta evaluator on withheld points outside Euler convergence; that numerical comparison is a *diagnostic*, not the proof of the universal bound.

**Consequence:** for any fixed s away from poles and any requested positive rational tolerance, E can choose N,K (possibly enormous), compute the finite incomplete-Gamma formula and a mathematical tail bound, obtaining arbitrarily tight approximations to completed zeta across C. The s-plane is a **coordinate of the constructed mathematical model**; no physical observer has to actualize an infinity of distinct instruments. This is not a finite algorithm for deciding RH or the zero-free strip.

## 5. A genuinely analytic source-interaction invariant at the missing place (AP-11–13)

From the base m=1 theta formula, `Lambda_1(s)=-1/s+O(1)` at s=0. For `P` a nonempty finite set of distinct genuine primes, every attached prime contributes

`1-p^(-s)=s*log(p)+O(s^2)`.

Therefore the **entire leading germ at s=0 is determined by interactions among the prime models**:

`Lambda_P(s)= - (prod_(p in P) log p)*s^(|P|-1) + O(s^|P|)`.

The exact order is |P|-1, with no reference to a zero table:
- P={2}: `Lambda_P(0)=-log(2)`.
- P={2,3}: `Lambda_P(0)=0`, `Lambda'_P(0)=-log(2)*log(3)`.
- P={2,3,5}: a zero of order 2 with leading coefficient `-log(2)log(3)log(5)`.

**Decisive fake-place negative control:** a fictional *single prime* p=6 would instead give `(1-6^-s)Lambda_1(s)` and limit `-log(6)` at s=0. Genuine 2+3 filtering has source indicator `1_{gcd(n,6)=1}`, whereas a fake single 6-exclusion keeps n=2,3,4,...; their source profiles differ even before continuation. The analytic germs at s=0 differ too. This makes actual prime factorization/multiplicativity load-bearing, rather than just claiming the same generic digit-tree algebra.

**Boundary pole/zero transfer.** For p a prime, `s=2*pi*i*k/log(p)` with nonzero integer k gives `1-p^-s=0`. `Lambda_1(s)` is finite there (its only poles are 0 and 1); therefore `Lambda_{p}(s)=0` **at those imaginary local-clock points**. These are zeros of the *depleted* completed zeta, NOT evidence of any Riemann-zeta zero or RH. They cancel the spurious poles of separately continued finite-place inverses.

**Twisted, not naïvely symmetric.** In general, depleted `Lambda_m` is not invariant under s↔1-s. The exact cross-multiplied functional equation is

`Lambda_m(1-s)*prod_(p|m)(1-p^-s) = Lambda_m(s)*prod_(p|m)(1-p^(s-1))`.

The untouched m=1 model is self-dual; model projections carry **source-controlled twist factors**. This is a precise representation of how a globally true spectral statement can survive across nonidentical local model perspectives without claiming all local models are directly isomorphic.

## 6. What does NOT follow — full negative suite (AP-14–17)

1. **Model completion alone is not continuation.** A finite Euler product for a fixed P is holomorphic only in Re(s)>0 (and meromorphically continues with clock poles on Re(s)=0); it does not converge to global zeta in the critical strip. Infinite-prime product limits cannot be interchanged with analytic continuation without new estimates. The theta/Fourier source supplies the actual analytic bridge.
2. **Finite observable/model agreement is not global identity.** A symmetric entire polynomial `R(s)=prod_j(s-s_j)(s-(1-s_j))` vanishes on any listed finite probes and their functional-equation reflections, yet differs from zero elsewhere. Replacing xi by xi+epsilon*R preserves symmetry and sampled values, but generally violates its **Euler germ and analytic growth/source law**. This is a pure probe/language closure negative control.
3. **Quadratic structure does not force prime identity.** Composite radial digit clocks and generic Pascal diffusion yield valid algebraic/heat models, but only genuine prime factorization gives the local Euler factorization and coherent cube.
4. **No universal Tate mechanization.** We instantiate finite exact p-adic shadows, a real Gaussian, CRT finite joins and classical real Poisson/theta theorems; there is no independently formalized *full restricted adelic product, global Schwartz–Bruhat category, or general Tate functional equation*.
5. **No Weil positivity or RH.** Meromorphic construction, pole accounting, symmetry, source faithfulness and effective evaluation at any s do NOT imply absence of zeros outside the critical line. The prior completed-Weil branch remains signed. No finite control demonstrates a source-derived positivity lower bound for all test vectors.
6. **No physical source authentication.** E's prime tables, basis, source ID, p-adic labels and mathematical algorithms are stipulated/classically grounded; they are not laboratory sensor access, proof of physical infinitary computation or an empirical realization of a metaphysical global observer.

## 7. Reproduction, claim ledger, comparison and actual scope

New executable artifacts:

- `observational_succ/all_places_zeta.py`: exact Q place valuations/product formula, p-fractional additive reciprocity, p-clock Fourier projector, typed source atlas, CRT, Ramanujan/Möbius spectral coefficients, source theta refinements, global xi and m-sieve analytic continuations, uniform rational error bound, twisted reflection and fake-6 controls.
- `tests/test_all_places_zeta.py`: **41 exact/numerical-hostile tests**; independent direct finite Fourier oracle, finite total enumeration, multibranch source diagram, reflection and all-s-plane evaluation, p=2/3/6 model collisions, rational bound diagnostics and analytic zero-order mutants.
- `scripts/all_places_zeta_probe.py`: deterministic frozen scientific receipt; no nontrivial zero-input calls.
- `research/2026-10-14/ALL_PLACES_ZETA_RECEIPT.json`: source/epoch/gauge/validation and representative complex-plane values, exact rational uniform bound.
- `docs/CLAIM_SUPPLEMENT_ALL_PLACES_ZETA.md`: AP-01..AP-17 statuses.
- `.github/workflows/all-places-zeta.yml`: Python 3.10 +3.13 targeted checks, deterministic receipt and provenance gate.

At the initial isolated source overlay (the exact published parent modules and receipts for structural coupling/Pascal/prime heat/completed Weil, with **no full Git checkout possible due to container network restrictions**) all **214/214** unittest cases passed on Python 3.13.5, and the scientific receipt replays byte-identically. This is **not** yet the full integrated >2000-test repository CI or a Lean kernel proof. The GitHub CI result for this branch must be checked at the exact pushed commit before promoting a status.

## 8. Highest-leverage next research gate

**Take the source-indexed global theta/adelic gluing one level higher to a *completed Weil distribution* with actual test-space naturality.** Demand a commuting square of the prime-source additive/logarithmic derivative and the Archimedean gamma model against C_c^∞ test functions, preserving Weil's pole/contact and conductor/half-density, and a quantified uniform remainder in each interval's H¹ norm. This is *not* automatic from the all-s evaluation formula or finite Fourier shadows. The prior branch's signed form identification and O(J^-2) Gamma approximants are the correct audit baseline. A positive source-identified factorization, or an all-test sign lower bound, remains the genuine RH-bearing missing theorem. Compare against matched non-Euler L-functions (proper conductor and parity), fake composite 6 and incorrect Euler characters, with no zero-list construction inputs.

**Novelty verdict:** classical exact mathematical ingredients, useful project-original type discipline, executable countermodels, source-indexed analytic-model transport and auditable proof obligations. No independent theorem-priority claim and RH remains open.
