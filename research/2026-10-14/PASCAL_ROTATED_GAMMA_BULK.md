# Pascal Bulk / Rotated SUCC / Gamma — source-indexed exact research

**Checkpoint:** 2026-10-14. **Parent:** `femboy2112/SUCC` draft [Structural-Coupling Discovery PR #65](https://github.com/femboy2112/SUCC/pull/65), commit `cf36f907ac042f82c349b4c601083473836e34ca`, which descends from `main@6e0d88f`. **New branch:** `research/pascal-rotated-gamma-transport-2026-10-14` (not merged). **Scopes:** rationally labelled SUCC units, free ordered word fibers, finite Pascal matrices, exact rational projective Bernoulli laws, synthetic group-coupling models and conditional positive exponential moment functionals. No physical carrier authenticated. RH, global Weil form and academic priority not claimed.

## 0. The actual hypothesis and the essential repair

Author's proposal: arrange successor objects of multiple unit lengths into a Pascal-triangle-shaped finite↔infinite bulk, with neighboring cells specifying upward/downward construction, a proposed one-object global Archimedean apex and a geometrically rotated 90° perspective; investigate whether Gamma is the resulting global transform. Preserve the insight, but **do not conflate four distinct maps**: literal finite planar rotation; linear inverse/adjoint; conditional stochastic time reversal; and analytic Mellin transform. Similarly, a graded Pascal carrier is not automatically a probability space, universal field of all arithmetic structures, real-place adelic completion, or completed Gamma normalization.

Existing SUCC inputs (not re-proved as novelties): `research/2026-10-11/PROTO_SUCC_VARIABLE_UNIT_LIFT.md` defines formal SUCC `S_d:x↦x+d` and warns about specialization losses; `FINITE_DIFFERENCE_SUCC_INTEGRATION.md` develops exact Pascal/Newton coefficients and initial/basis transport; `MAHLER_SUCC_CLOCK_KUMMER.md` explains why p-adic interpolation needs continuity/Kummer constraints. [PR #65's structural coupling dossier](../2026-10-13/STRUCTURAL_COUPLING_DISCOVERY.md) builds `C_k` by `C_q` via action + twisted cocycle, with D8/Q8 and source-relative observer policies. This research ties their order-sensitive dynamics to the Pascal lattice.

## 1. PB1 — the graded successor algebra actually exists (CLASSICAL / PROVED LOCAL)

Start with the free word monoid on named actions `A`, `B`. At depth `n`, words have length `n`; define `k=#B`. The cell `(n,k)` has precisely `binom(n,k)` words and predecessors `(n-1,k)` (last A) and `(n-1,k-1)` (last B). Thus the multiplicities satisfy Pascal's recursion. Assign **formal** step units `a,b`, and an address to each cell:

`x(n,k)=(n-k)a+kb`, `S_a(x)=x+a`, `S_b(x)=x+b`.

In the universal degree-two monomial chart, retain `a^(n-k)b^k` and multiplicity independently of the eventual numerical address. Under specialization `a=b`, every address in the row collapses although the ordered words and formal cells remain distinct. Therefore the completed numerical address alone need not be a faithful source map.

Let `H=Q[x]` be the polynomial Hopf algebra with primitive generator `x`, multiplication as usual, coproduct `Δx=x⊗1+1⊗x`, counit `ε(x)=0`, antipode `S(x)=-x`. Being an algebra homomorphism, `Δ` yields

`Δ(x^n)=Σ_{k=0}^n binom(n,k) x^k ⊗ x^(n-k)`.

**Direct coassociativity proof.** The coefficient of `x^a⊗x^b⊗x^c`, `a+b+c=n`, is `binom(n,a+b) binom(a+b,a) = n!/(a!b!c!)` on `(Δ⊗id)Δ`; on `(id⊗Δ)Δ` it is `binom(n,a)binom(n-a,b)`, the same quantity. The antipode convolution cancels via `Σ_k (-1)^k binom(n,k)=0` for n>0. In the divided-power basis `e_n=x^n/n!`, `e_m e_n=binom(m+n,m)e_(m+n)` and `Δe_n=Σ e_k⊗e_(n-k)`. This **is an algebra and coalgebra**, not an arbitrary array of numbers. No claimed novelty: classical Hopf algebra/binomial theorem.

A **possible** Archimedean one-generator extension is `T_t=e^(tD)` on polynomials, `D=d/dx`: the exponential is finite on every polynomial and `T_t x^n=(x+t)^n`. The rational `B_t` matrices compose `B_a B_b=B_(a+b)`, and the polynomial identity extends to real scalar t without convergence trouble on each polynomial. However, that is a *chosen* real translation representation, **not** an inevitable one-point Archimedean boundary of the infinite Pascal graph, and not the arithmetic adele place. On larger function spaces, strong continuity and operator domains require separate proofs.

## 2. PB2 — Pascal's scalar quotient fails precisely at noncommuting couplings (CLASSICAL / SHARP COUNTERMODEL)

The cell `(n,k)` groups `binom(n,k)` **ordered** words. Replacing those words by the one endpoint `A^(n-k)B^k` with multiplicity `binom(n,k)` is valid for arbitrary n if `AB=BA`. The necessity is already exposed by n=2:

`(A+B)^2=A²+AB+BA+B²` versus `A²+2AB+B²`.

Equality at n=2 is equivalent to `AB=BA`. In a noncommuting SUCC source, the Pascal triangle requires an *ordered-word fiber over each cell*; the commutator/holonomy is information **inside** the fiber, not represented by its scalar cardinality.

**Live coupling test:** PR #65 supplies four exact `C4` by `C2` structures, including two with quotient action `g=3`. With `A=(1,0)`, `B=(0,1)` and multiplication from the actual validated extension, `AB=(1,1)` but `BA=(3,1)`. The Pascal cell `(2,1)` retains two endpoints, each weight 1; naive scalar Pascal gives only endpoint `(1,1)` weight 2. The two `g=1` groups are commuting and scalar collapse is exact at every checked length. This is source-specific and is a significant requirement for the proposed B/C/D coupling engine: **use Pascal as a graded index, not as an unqualified commutative quotient**.

## 3. PB3 — literally rotating the finite triangle does NOT rotate its infinite boundary (CLASSICAL / EXACT NO-GO FOR THIS EMBEDDING)

Plot `(n,k)` in **screen coordinates**, `(x,y)=(k,n)` with y increasing downward, in a finite square of depth N. Screen-clockwise rotation about that square gives the coordinate map

`R_N(n,k)=(N-n,k)`, inverse `(n,k)=(N-x,y)`.

This is a bijection between finite triangular domains, checked exhaustively. But for any **fixed source cell** `(n,k)`, `R_N(n,k)` has first coordinate `N-n→∞` as N→∞; no finite coordinatewise limit exists **in that fixed codomain**. This is a no-go for taking the literal finite diagram rotation as a global fixed-coordinate limit, **not** a general no-go for renormalized, rescaled, projective or categorical rotations.

Algebraic analogues must be separately typed: the finite binomial transport `B_d(n,k)=binom(n,k)d^(n-k)` has inverse `B_-d`, whereas an adjoint is `B_d^†=W^-1 B_d^T W`, requiring positive pairing `W`. These are not identical in general; `W` is an additional source/geometry choice. Exponential generating functions provide a truthful change of basis: if `g_n=(B_d f)_n` and `F(z)=Σ f_n z^n/n!`, then `G(z)=e^(dz)F(z)`. The coefficient identity is proved by formal Cauchy multiplication, with no Gamma yet.

## 4. PB4 — projective backwards Pascal transport has infinitely many global sources (CLASSICAL / COMPUTED)

Choose a Bernoulli parameter `p∈[0,1]`; at depth n the quotient count has law `μ_n^p(k)=binom(n,k)p^k(1-p)^(n-k)`. For source-supported `(n,k)` with n>=1, the **backward** conditional kernel is

`K((n,k),(n-1,k-1))=k/n`, `K((n,k),(n-1,k))=(n-k)/n`.

Derive it by Bayes conditioning on a source path: `binom(n-1,k-1)p^k(1-p)^(n-k)/μ_n^p(k)=k/n`. In particular the **reverse kernel does not depend on p**, even though the **forward kernel** `A with 1-p / B with p` does. All rational rows, source-supported Bayes quotients and finite mixtures were tested for exact projective compatibility `μ_(n-1)=K_* μ_n`. Conditioning on a source-null vertex is explicitly rejected.

The classical extreme central measures/boundary of the infinite Pascal graph are the Bernoulli product laws indexed by a *continuum* of p's; mixtures give the general exchangeable laws (de Finetti). See A. M. Vershik, **The problem of describing central measures on Bratteli diagrams**, e.g. https://www.pdmi.ras.ru/~avershik/centralmeasures.pdf (Pascal graph and Bernoulli boundary). **We do not locally prove de Finetti**: our exact contribution is finite projective compatibility and the sharpened source-identification countercontrol. A single apex object may be chosen as *the space of all boundary laws*, but collapsing that object to one p destroys source-identifying information. Thus the "one global Archimedean unit" must specify which representation or measure has been selected.

## 5. PB5 — spectral specialization is exact after source selection (CLASSICAL / PROVED LOCAL)

For integer unit labels a,b and a declared probability p, reduce addresses modulo m. The group-algebra law `R_n` is a normalized distribution on `C_m`:

`R_n(r)=Σ_{k: (n-k)a+kb = r mod m} binom(n,k)(1-p)^(n-k)p^k`.

Then `R_(n+h)=R_n * R_h` by independence **explicitly declared for the Bernoulli source**, verified against a separately calculated cyclic convolution. Its Fourier character at ζ_m^j is `((1-p)ζ_m^(ja)+pζ_m^(jb))^n`; for m=2 the exact sign character is

`R_n(even)-R_n(odd)=[(1-p)(-1)^a+p(-1)^b]^n`.

The latter is a genuine finite spectral prediction, not a generalized zeta zero or an RH spectral realization. Correlated or changing source steps require different kernels; a full noncommuting coupling needs word-order observables, not this abelian cyclic quotient alone.

## 6. PB6 — the actual Gamma bridge is Pascal + a positive moment law (CLASSICAL / DERIVED)

Supply a **positive** linear functional `L_λ` on real polynomials using the exponential probability measure `dμ_λ(t)=λ e^(-λt)dt` on `[0,∞)`, with declared rate λ>0. Integration by parts gives `L_λ(t^n)=n!/λ^n`. Applying the exact Pascal translation to its moments yields

`M_n(d;λ)=L_λ((t+d)^n)=Σ_k binom(n,k) d^(n-k) k!/λ^k`,

with `M_0=1`, `M_n=d^n+(n/λ)M_(n-1)`. The formula is an **exact all-integer identity**, independently checked as a rational binomial sum, a Pascal matrix action and a recurrence.

Now **and only now**, extend the moment observable from integer n to complex order s using the *specified* exponential measure:

`L_λ(t^s)=λ^(-s) Γ(s+1)` for Re s>-1,

and when d>0,

`L_λ((t+d)^s)=e^(λd) λ^(-s) Γ(s+1,λd)`.

Here `Γ(s+1,λd)` is the **upper incomplete Gamma function**. Both formulas follow immediately by real substitution in the defining integrals (choose the usual real logarithm on positive t). At d=0, the ordinary Gamma formula is recovered for Re s>-1. For d<0, integer polynomials still make sense, but unrestricted complex powers have branch/domain problems: no unearned analytic continuation is asserted. Sources: NIST [DLMF §5.2](https://dlmf.nist.gov/5.2) and [§8.2](https://dlmf.nist.gov/8.2).

**A surprisingly strong CONDITIONAL uniqueness theorem:** If a Borel probability μ supported on `[0,∞)` has *all* integer moments exactly `m_n=n!`, then μ **must** be Exp(1). Indeed for every `0<=u<1`, monotone convergence implies

`∫ e^(ut)dμ=Σ_(n>=0) u^n m_n/n!=1/(1-u)`.

Thus μ has the same finite exponential moment-generating function as Exp(1), which determines the positive law uniquely by the standard uniqueness theorem for moment-generating/Laplace transforms. The analytic Mellin transform, and therefore Gamma, then follows from the identified measure. This is classical measure/transform uniqueness under explicitly strong **all-n positive source** hypotheses. The Pascal geometry alone does NOT provide m_n=n! or the positivity hypothesis.

**Hostile controls (two independent source ambiguities).** First `δ_1`, another positive probability source, has moments `1,1,1,...`, obeys the same Pascal binomial-translation identities, but produces `(1+d)^n`, **not Gamma**. Second, the positive 2-point measure

`μ_2 = ((2+√2)/4) δ_(2-√2) + ((2-√2)/4) δ_(2+√2)`

has moments `m_0=m_1=1`, `m_n=4m_(n-1)-2m_(n-2)`, hence `1,1,2,6,20,...`. It agrees with Exp(1) on n=0,1,2,3, **then fails at n=4** (`20` against `24`). This is a rigorous finite-moment model-selection obstruction. The exact `Q(√2)` multiplication was implemented as an independent 2-coordinate oracle; no approximate fitting is used.

**Further analytic interpolation obstruction.** Even all integer factorial values and the recurrence `F(s+1)=(s+1)F(s)` do not uniquely determine F. For any nonzero real ε,

`F_ε(s)=Γ(s+1) exp(ε sin(2πs))`, real s>-1,

is positive, matches n! at each nonnegative integer and satisfies the same recurrence, but differs away from integers. Bohr–Mollerup log-convexity (plus the proper normalization) excludes nontrivial such periodic factors and characterizes Gamma. See [DLMF §5.5(iv)](https://dlmf.nist.gov/5.5). This is a proof of the **need** for analytic regularity/representation selection, not proof Gamma equals a quarter-turn of a diagram.

## 7. PB7 — finite Pascal rows can become infinite analytic rows, but positivity is lost

Define generalized coefficients by the *polynomial*, Gamma-independent falling-factorial formula `binom(s,k)=s(s-1)...(s-k+1)/k!`. For each nonnegative integer s=n, the coefficients vanish for k>n. For noninteger `s`, generally infinitely many are nonzero; Pascal recurrence `binom(s+1,k)=binom(s,k)+binom(s,k-1)` still holds. The generalized binomial series `Σ binom(s,k)z^k=(1+z)^s` is analytic for |z|<1.

For real s>-1, `|z|<1`, cutoff K with `N=K+1>=s`, and k>=N, the omitted term ratio is `|s-k||z|/(k+1) <= |z|`. Thus a **rigorous tail certificate** is

`|Σ_(k>N-1) binom(s,k) z^k| <= |binom(s,N) z^N|/(1-|z|)`.

The exact test at `s=1/2,z=1/2,K=18` encloses `√(3/2)` against an independently certified rational integer-square-root bracket; every term and bound is a `Fraction`. But `binom(1/2,2)=-1/8`: this analytic row is **signed**, not a legitimate positive Pascal path-count or stochastic law. A complex/signed analytic interpretation requires its own target category, norm and convergence assumptions. This is a particularly good finite↔infinite transport stress test.

## 8. PB12–PB14 — the actual operational 90° rotation: Pascal counting → Gamma waiting time

This is the strongest confirmed reading of the author's suggested rotation. **The horizontal/vertical exchange is not a physical quarter-turn of a triangular diagram. It is an order-theoretic exchange of which variable is fixed and which is measured.**

### PB12. Count/time threshold adjunction (UNCONDITIONAL FOR A LAWFUL ORDERED PATH)

Let ordered actual event times satisfy `0<=T_1<=T_2<=...` and let `N(t)=#{i:T_i<=t}`. Then for every integer `n>=1` for which the nth event exists and every time `t>=0`,

`N(t)>=n  ⇔  T_n<=t`; equivalently `T_n>t ⇔ N(t)<n`.

*Proof:* at least n entries of a nondecreasing sequence are at most t iff its nth entry is at most t. **No Bernoulli, independent-increments, Poisson, Gamma or physics assumption is used.** This is the Galois-style adjunction between monotone count and its generalized inverse. The finite implementation exhaustively checked sorted sequences with repeated/tied times, all thresholds and all valid n; no reset or hidden-source oracle is added. This supplies the exact mathematical backbone of a ``rotated observation''.

### PB13. Bernoulli/Pascal → Poisson/Erlang via a genuine continuum limit

At one discrete SUCC tick of length δ, suppose an independently actualized *model* supplies a Bernoulli success with p. At fixed tick-count m, the number of arrivals `N_m` is binomial `Bin(m,p)`, and Pascal's row controls its law. If instead **fix the nth arrival** and vary tick count `T_n`, then

`P(T_n=m)=binom(m-1,n-1)p^n(1-p)^(m-n)` for m>=n,

because the first m-1 ticks contain n-1 successes and tick m succeeds. This is the **Pascal/negative-binomial waiting-time distribution**. The duality `P(T_n>m)=P(N_m<n)` is the same pathwise count/time adjunction. For p>0, total waiting-time mass is 1, since the binomial lower tail tends to 0; p=0 is a genuine nontermination control.

Now supply **additional source law**, not contained in the Pascal shape: fixed real t>0, rate λ>0, split the interval into m equal ticks δ=t/m, with Bernoulli parameter `p_m=λδ=λt/m`, and let m→∞. Every fixed-k binomial event probability tends to

`P(N(t)=k)= exp(-λt)(λt)^k/k!`.

Using the count/time adjunction with a fixed positive n gives

`P(T_n>t)= exp(-λt) Σ_(k=0)^(n-1) (λt)^k/k!`.

Differentiation telescopes and yields the Erlang/Gamma density

`f_(T_n)(t)=λ^n t^(n-1) exp(-λt)/(n-1)!  =  λ^n t^(n-1) exp(-λt)/Γ(n)`.

**This is a mathematically rigorous count↔time dual to the Pascal boundary.** It is established stochastic-process theory: the MIT OpenCourseWare [6.041 lecture on Poisson processes](https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/c3a76a2ab596356f320c89740525aad3_MIT6_041F10_L14.pdf) explicitly tabulates `Binomial ↔ Poisson` counting and `Pascal ↔ Erlang` waiting times. Our contribution is integrating it into SUCC's source-indexed and exact-certificate machinery, not discovering the probability theorem.

**An exact quantitative transport estimate (CLASSICAL / DIRECT PROOF):** Let `Λ=λt`, integer m with `0<=Λ/m<=1`. For a single tick compare `Bern(p)` with `Poisson(p)` where `p=Λ/m`. Their total variation is exactly `p(1-exp(-p))<=p²`; direct check on `{0,1,2,...}` gives this identity. Couple m independent coordinates and push forward through addition, which cannot increase total variation. Thus

`TV(Bin(m,Λ/m),Poisson(Λ)) <= m p² = Λ²/m`.

Consequently, **uniformly in every positive event threshold n**,

`| P(δ T_n > t) - P(Gamma(n,λ)>t) | <= Λ²/m`

for δ=t/m and the indicated Bernoulli scaling. No claim about an arbitrary independently sampled or nonstationary source. The exact Python certificate uses rational Bernoulli sums and an alternating-Taylor rational bracket for `exp(-1)`, verifying the bound at m=4,8,16,32,64 and n=1..4. The **general inequality is proved by the coupling argument**, not inferred from those five samples.

**Falsifier:** keep `p=1/2` while making m→∞ at fixed t. The number of arrivals grows with m; it is *not* a finite-rate Poisson(λt) source. Exact Bernoulli waiting-time source reports differ violently from the correct scaled `p=Λ/m` source. This is the precise content of the continuum source/normalization gate.

### PB14. The missing coupling that makes Pascal and Poisson one lawful source

Give each Poisson event an independently marked label `A`/`B`, probability `1-p`/p. Conditional on the actual total count `N(t)=n`, the number of B marks has **exactly** the Pascal/binomial row law. Hence their **joint** source model is

`P(N(t)=n, K_B=k) = exp(-λt)(λt)^n/n! * binom(n,k)(1-p)^(n-k)p^k`.

This is a declared full joint coupling, not an assumption that two unrelated marginals can be freely combined. The executable tests independently sum every colored row and recover the uncolored Poisson prefactor, while retaining exact Fraction coefficients for the `exp(-λt)` normalization.

**Interpretation:** The same source can be viewed through (a) a Pascal-colored event-count slice, (b) a time-to-count slice, and (c) a continuous Erlang/Gamma waiting-time law, **provided the independent-increments, mark-thinning, and continuum scaling contracts are present**. A literal rotation with none of these is still empty metaphor. Neither this probabilistic Gamma nor the earlier exponential Mellin moment functional proves that the arithmetic completed zeta uses this source; recovering `π^(-s/2)Γ(s/2)` remains an independent Gaussian/theta-normalization problem.

### PB15. Fractional Gamma successor as a positive Hopf-convolution semigroup

**This is the most direct mathematical synthesis of the proposed one-global-unit idea.** Fix a *source-selected* rate `λ>0`. Let `μ_α` be the Gamma probability law with real shape `α>0` and rate λ; set `μ_0=δ_0`. Its density and Laplace transform are

`dμ_α(t) = [λ^α/Γ(α)] t^(α-1)e^(-λt)dt`,

`L_α(u)=∫ e^(-ut)dμ_α(t)=(λ/(λ+u))^α`, `u>=0`.

Define the (mathematical) fractional successor on positive measures by `S_α(ν)=ν*μ_α`. Multiplication of the displayed Laplace transforms gives

`μ_α*μ_β=μ_(α+β)`,  `S_α∘S_β=S_(α+β)`, `S_0=id`.

At α=n∈N this is exactly the law of the waiting time to n arrivals in a homogeneous Poisson process; α fractional is a valid positive Gamma law but **not** a literal half of an observed event. The shape axis is continuous; the event-count axis is discrete. The choice of rate λ is an indispensable scale/orientation/source parameter.

**Gamma ↔ Pascal Hopf compatibility (CLASSICAL / DIRECT EXACT IDENTITY).** Let `L_α(x^n)=E_(μ_α)[X^n]=α^(overline n)/λ^n` where the rising factorial `α^(overline n)=α(α+1)...(α+n-1)` and the empty product is 1. Use the *same primitive Hopf coproduct* from PB1:

`(L_α ⊗ L_β)(Δ(x^n)) = Σ_k binom(n,k) L_α(x^k)L_β(x^(n-k)) = (α+β)^(overline n)/λ^n = L_(α+β)(x^n)`.

The key identity is the **rising-factorial Vandermonde identity**. Proof: expand the formal exponential generating functions `Σ_n α^(overline n)z^n/n!=(1-z)^(-α)` and similarly for β. Multiplication gives `(1-z)^(-(α+β))`, whose coefficient equality is precisely the formula above. An independent positive-measure proof follows from the Gamma Laplace transforms, under independence of the two convolved variables. The code checks every identity exactly for rational fractional shapes (including 1/2, 1/3, 3/2) and multiple rates, and rejects compositions with untransported incompatible rates.

**Uniqueness boundary (CLASSICAL PAPER ARGUMENT):** Within weakly continuous probability-measure convolution semigroups on `[0,∞)` with `μ_0=δ_0` and **the same anchored unit law** `μ_1=Exp(λ)`, the entire semigroup is uniquely pinned. For each u>=0 the positive Laplace transform `L_α(u)` satisfies `L_(α+β)=L_α L_β` and is continuous in α; its unit value is `λ/(λ+u)`. Positivity fixes rational roots, continuity fixes real α, and uniqueness of Laplace transforms identifies Gamma(α,λ). The semigroup conclusion is **conditional on continuity, positivity, a common source rate, and the unit source law**, not inferred from Pascal combinatorics alone.

This yields a bona fide continuous-time *mathematical* SUCC whose moment coproduct is Pascal and whose continuum kernel is Gamma. It is arguably the cleanest repair of the geometric "quarter-turn" hypothesis. Whether a physical observer can implement its fractional operator, or the Archimedean place of the zeta function realizes this semigroup, is **UNVERIFIED**.

## 9. What remains missing and how to falsify the preferred framing

1. **Integrated carrier gluing:** compose this graded Hopf/path algebra with `CyclicExtension` and source changing histories. Ordered fibers are mathematically computed, but NO-GHOST stochastic public-policy instruments and physical preparations have not been incorporated.
2. **A real operator-theoretic rotated transport:** specify the Hilbert/Fréchet/Banach pairing `W`, domain/core, and semigroup topology; establish a coherent adjoint/direct-integral or Mellin-Plancherel intertwining theorem, not merely a transpose or a redrawn finite triangle.
3. **A uniquely selected source/analytic functional:** show why a declared arithmetic/physical source should supply `m_n=n!` or Gaussian theta moments and prove all-n or source-first norm bounds. Test delta, positive 2-node, wrong rates, signed generalized rows and source-dictionary drift.
4. **Adelic/Gamma/RH adapter:** the Gamma in the completed Riemann xi factor is `π^(-s/2) Γ(s/2)`, stemming from Gaussian/theta normalization. The present exponential moment functional constructs `Γ(s+1)` and **has not identified** the adelic Archimedean local factor, functional equation, prime jets, or completed Weil form. A valid adapter must derive the normalizations with true Euler/prime powers and matched composite/non-Euler controls, no zero-oracle.
5. **Formal and independent verification:** Python 3.13 exact probes plus a few numerical analytic checks are not a proof assistant. Mechanize coassociativity, factorization, noncommutative-word no-go, central Pascal transport and the carefully scoped moment uniqueness result; a mathematician unfamiliar with our model should audit attribution and novelty.

### Status verdict and reproducibility

PB1–PB8 and PB12–PB15 are classical theorems with new-to-SUCC executable source-typed instantiations and exact countermodels; no independent academic-priority claim. The all-moment uniqueness and analytic Gamma identities have paper derivations citing standard measure/transform results, not local Lean kernel checks. The finite Bernoulli boundary is established literature; our direct verification covers selected exact finite cases only. `scripts/pascal_rotated_transport_probe.py` recomputes `research/2026-10-14/PASCAL_ROTATED_RECEIPT.json` deterministically. `tests/test_pascal_rotated_transport.py` contains hostile exact tests, count/time duality, exact Poisson convergence certificates, and an independent mpmath integration holdout. Python full-repo CI must be checked on the exact pushed head; no successes invented. The parent 22 structural coupling tests are unchanged.

```
python -m unittest discover -s tests -p 'test_pascal_rotated_transport.py' -v
python scripts/pascal_rotated_transport_probe.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
```
