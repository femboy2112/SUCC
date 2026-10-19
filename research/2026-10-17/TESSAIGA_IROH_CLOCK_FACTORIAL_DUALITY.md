# TESSAIGA × GENERAL IROH — exact SUCC/FUCC factorial duality and its RH-hard Green kernel

**Date:** 2026-10-17. **Source parent:** OCG draft PR #165, `research/orbit-clock-genesis-lcm-mobius-2026-10-17@dea8b7f982fd3eb2361ccd5a12d360bcadfa3689`, stacked on draft PR #162 and #157. **Scope:** source-relative classical theorems with new-to-project operator interpretation, exact standalone finite tests, and explicit source boundary. **RH PROVED: NO.** **SIGNED WEIL POSITIVITY: NOT IDENTIFIED.** No nontrivial zero positions used in construction or testing.

## 0. The object and source boundary

The OCG parent (PR #165) constructs **finite clock instruments** with periods `1,...,N` and their minimal synchronized rooted cycle of period `L_N=lcm(1,...,N)`. This is a mathematical instrument construction under declared access to fresh states, transition splicing, replay and synchronized products. It is **not** by itself a continuous, source-equivariant observation of arbitrary physical dynamics. The OCG source-relative identity is

`Delta_N = log(L_N/L_(N-1)) = Lambda(N)`.

This report constructs an exact alternative implementation of the same *authentic metatheoretic arithmetic tape* using additive SUCC accumulation (`n!`), incidence Möbius inversion (quotient lattice), and multiplication/FUCC, separating a source-coherent change of clock log weights from a malformed local perturbation.

All claims about `N`, `Z`, primes, floor, log and factorial here are **classical mathematics imported as ambient structure**; none is a proof that a finite physical observer has constructed an infinite natural-number source. All output files are additive, no historical archival source is edited. Source provenance of OCG / real-Gamma / Tate / Weil is preserved.

## 1. TIR-01 — the exact additive-factorial / multiplicative-clock bridge (CLASSICAL; derived)

Let `F(N)=log(N!)`, `A(N)=log L_N=psi(N)`, with `F(0)=0`, `A(0)=0`, and define the floor-dilation operator

`(T A)(N) = sum_(k=1)^N A(floor(N/k))`.

The fundamental prime-power identity `log n = sum_(d|n) Lambda(d)` gives, with only finite sums,

```
 F(N)=sum_(n<=N)log n
     =sum_(d<=N)Lambda(d)*floor(N/d)
     =sum_(k<=N)A(floor(N/k))
     =(T A)(N).
```

The divisor-incidence inverse is `mu(1)=1`, `sum_(d|n)mu(d)=0` for `n>1`. Since `floor(floor(N/d)/k)=floor(N/(dk))`,

```
 (T_mu T A)(N)
  =sum_(d<=N)mu(d)sum_(k<=floor(N/d))A(floor(N/(d*k)))
  =sum_(m<=N)A(floor(N/m))sum_(d|m)mu(d)
  =A(N).
```

Thus

```
 psi(N)=sum_(d<=N)mu(d)*log(floor(N/d)!)
 L_N = product_(d<=N) (floor(N/d)!) ^ mu(d).     (1)
```

The right side is an **integer**, although individual factors have negative exponents. This product is a classical consequence of Möbius inversion, not a new prime-counting proof.

For `N=6`, `L_6=6!/(3! 2!)=60`. For `N=8`, `L_8=840`. The code checks the exact rational identities without logarithmic rounding.

## 2. TIR-02 — the cumulative Mertens Green kernel (CLASSICAL; exact transfer)

Let `M(x)=sum_(1<=d<=floor(x))mu(d)` and for a length-N input sequence `ell(1),...,ell(N)` define

`U_N(ell)=sum_(n<=N)(mu * ell)(n)`, with Dirichlet convolution.

Reindex the finite sums:

```
 U_N(ell)
 = sum_(n<=N) sum_(d|n)mu(d)*ell(n/d)
 = sum_(m<=N) ell(m) * M(floor(N/m)).
```

Consequently the exact row (Green kernel) is

`K_(N,m)=M(floor(N/m))`, `1<=m<=N`.          (2)

For the genuine logarithm `ell(m)=log m`, this gives the second **multiplicative integer** reconstruction

```
 psi(N)=sum_(m<=N) log(m) M(floor(N/m)),
 L_N=product_(m<=N) m ^ M(floor(N/m)).      (3)
```

**Conservation with cancellation:** applying (2) to `ell(m)=1`, `mu*1=epsilon_(n=1)` implies

`sum_(m<=N)K_(N,m)=1`.                     (4)

Yet for every `m>N/2`, `K_(N,m)=M(1)=1`; therefore, on unrestricted independent real reading perturbations,

```
 ||U_N||_(ell_infinity -> absolute value)
   =sum_(m<=N)|K_(N,m)| >= ceil(N/2).        (5)
```

Equation (5) is a **lower bound on worst-case source-readout conditioning**, not a physical noise model and not a failure of the exact arithmetic source. The cancellation that makes (4) possible is a critical component missing from an all-positive source decomposition.

## 3. TIR-03 — a single local defect has RH-hard sensitivity (CLASSICAL equivalent, NOT a proof)

For the coordinate basis `e_m(n)=1` if `n=m`, `0` otherwise, (2) gives

`U_N(ell+eta e_m)-U_N(ell)=eta M(floor(N/m))`.   (6)

Fix `m=2`. The following are equivalent, by the **classical Littlewood/Mertens criterion**:

1. The Riemann hypothesis.
2. For every `epsilon>0`, `|M(x)|=O_epsilon(x^(1/2+epsilon))` as `x->infinity`.
3. For every `epsilon>0`, the single-coordinate sensitivity of `U_N` to `ell(2)` is `O_epsilon(N^(1/2+epsilon))` uniformly as `N->infinity`.

Indeed `K_(2x,2)=M(x)` for every positive integer `x`; conversely `|K_(N,2)|=|M(floor(N/2))|`. This is an **exact re-expression of an existing RH-equivalent bound**, not a new route that weakens it or proves it. Do not mistake the finite verified numerical sequence for the required universal growth theorem. In particular, the older *false* Mertens conjecture `|M(x)|<=sqrt(x)` must not be silently promoted as a hypothesis.

**Crucial admissibility condition:** the unit-local input `ell+eta e_2` is *not* the logarithm of the original clock index and is not a completely additive homomorphism (`ell'(4) != 2 ell'(2)` for nonzero eta). It is a **hostile single-site readout error**, useful for transfer sensitivity, **not** a lawfully reweighted SUCC/FUCC source. The equivalence tests conditioning of an unrestricted source-information map, and does **not** imply that authentic clock evolution suffers such an error.

## 4. TIR-04 — lawful algebraic prime-weight perturbations are different (CLASSICAL)

For an ordinary prime `p`, the valuation `v_p(n)` obeys `v_p(ab)=v_p(a)+v_p(b)`. An algebraic one-prime reweighting is

`ell_eta(n)=log n+eta*v_p(n)`.

Unlike `e_2`, it preserves complete additivity. Because `v_p = 1 * sum_(k>=1)e_(p^k)` in Dirichlet convolution,

```
 mu*v_p = sum_(k>=1)e_(p^k),
 U_N(v_p)=#{k>=1:p^k<=N}=floor(log_p N).      (7)
```

The sensitivity under that **multiplicatively coherent** perturbation is only `O(log N)` at fixed `p`, compared with the RH-hard `M(N/2)` Green coefficient of a forbidden isolated readout mutation.

**Source distinction:** even a multiplicatively coherent reweighting changes the actual Haar/clock-index `log p` calibration. Hence (7) is an algebraically legitimate **comparison model**, not the genuine unaltered arithmetic source. Preserve original `Lambda`, half-density, log p and completion in all RH applications.

## 5. TIR-05 — no positivity-preserving Möbius inversion (REFUTED naive transfer)

`T` is positive (nonnegative input -> nonnegative output), but `T^{-1}` is not positive on arbitrary nonnegative nondecreasing cumulative inputs. Set `h(n)=1` for `n>=2`, `h(1)=0`. Then at `N=6`:

`(T^{-1}h)(6)=sum_(d<=6)mu(d) h(floor(6/d))=M(3)=-1`.

This exact counterexample invalidates inference of original positivity from positive factorial data by a generic order-preserving transport. It is *not* a negative test of the authentic Weil quadratic form.

A second obstruction attacks indiscriminate absolute values. Let `a_n=Lambda(n)-1` for n>=2. Every multiple of 6 is **not** a prime power, hence `Lambda(6k)=0`; so

`sum_(n<=N)|Lambda(n)-1| >= floor(N/6)`.

This grows faster than `sqrt(N)log²N`. Thus simply applying the triangle inequality to `psi(N)-N` cannot give the RH-scale error, regardless of any finite successful tests. Structured cancellation is indispensable.

## 6. TIR-06 — source-blind PSD is powerless (EXACT negative control)

The vector `K_N` depends only on the divisor incidence algebra. Its outer product `K_N K_N^T` is positive semidefinite for **every** additive reading `ell`, genuine or counterfeit. Injecting a false composite-site `e_6` (or an arbitrary malformed reading) changes `U_N(ell)` by `K_(N,6)` but leaves `K_N K_N^T` exactly unchanged. Thus Gram positivity constructed **solely from the inverse kernel** cannot authenticate the real prime-power source, and cannot by itself establish the **completed signed Weil positivity** required for RH.

This is a typed, finite exact negative control, not a no-go theorem for every possible arithmetic operator: a stronger operator incorporating authentic source weights, Gamma, contact, both polar channels and domains may discriminate.

## 7. RH frontier — precise boundary and actionable next probe

Classical von Koch equivalence gives

`RH <=> psi(N)=N+O(sqrt(N)*log²N)` for integer N.

Equations (1)–(3) therefore yield new **SUCC clock-language presentations of an old equivalent criterion**, but no new error estimate:

```
 log(product_(d<=N)(floor(N/d)!)^mu(d)) - N
       = O(sqrt(N)*log²N)
```

and equivalently with the product over `m` weighted by `M(floor(N/m))`. The sign/cancellation estimate has simply been transported, not discharged. The original signed Weil positivity problem (including the real Gamma, contact, half-density and both poles) remains independent and OPEN.

**Next verdict-changing probe**: independently derive a *source-faithful, non-tautological constraint* on signed cross-index Green coefficients (or a source-specific Schur margin) that excludes both a fake composite 6 and a non-Euler multiplicative mutant. A norm bound based only on the incidence row, with no genuine clock calibration, is not enough. Test whether a source-derived multiplier on the restricted completely additive subspace produces any rigorous margin **stronger than** the inherited elementary/PNT bounds, while honoring all completion channels. No nontrivial zeros can be construction inputs; use fresh hostile finite holdouts and independent interval bounds for any claimed new sign.

## 8. Exact implementation / falsifiers / validation

Files: `observational_succ/clock_factorial_duality.py`, `tests/test_clock_factorial_duality.py`, `scripts/tessaiga_iroh_probe.py`, `research/2026-10-17/TESSAIGA_IROH_CLOCK_FACTORIAL_DUALITY_RECEIPT.json`, this dossier and `docs/CLAIM_SUPPLEMENT_TESSAIGA_IROH.md`.

- **Independent exact implementations:** gcd/lcm superclock, factorial-µ signed product, unit-index/Mertens signed product, independent divisor-convolution response, formal Green-row response.
- **Hostile tests:** fake primitive at 6, true prime-power 8, incorrect µ(6), sign-flipped µ(2), non-prime valuation generator 6, local delta at 2 versus coherent `v_2`, and failure of generic inverse positivity.
- **Locally executed:** **11/11 focused tests passed** under local Python 3.13; deterministic pinned receipt verified. **Finite checks:** 120 horizons of exact three-route clock agreement; random deterministic input vectors; basis-spike Green response; every row sum exactly 1 and its ℓ∞-norm bound.
- **Limitations:** no physical observer/source authentication, no general signed Weil source comparison, no infinite estimate on M, no large-N RH proof. Source familiarity of classical mathematics is not independent mathematical validation.
- **Status:** focused local 11/11 and standalone receipt passed; hosted exact-head and repository-wide CI unverified at this writing. Full repository scripts, hosted CI, and formal Lean checks separately unverified until run.

### Prior art and attribution

- DLMF §27.5, classical divisor-Möbius inversion and its multiplicative variant: https://dlmf.nist.gov/27.5
- DLMF §27.12, prime-number theorem error and RH equivalences: https://dlmf.nist.gov/27.12
- Titchmarsh (2nd ed.), *The Theory of the Riemann Zeta-function*, Thm. 14.25(c); Mertens RH-equivalence summarized in Lynnelle Ye, *Bounding sums of the Möbius function over arithmetic progressions*: https://arxiv.org/abs/1406.7326
- SUCC predecessor: `research/2026-10-17/ORBIT_CLOCK_GENESIS_MINIMAL_SOURCE.md` (draft PR #165), earlier prime-jet genus PR #157 and minimality PR #162.

**Novelty discipline:** mathematical identities are classical or immediately derived from them; the **dual operator/Green-kernel/source-type comparison is a new-to-this-repository synthesis**. Independent literature audit required before any stronger originality claim.
