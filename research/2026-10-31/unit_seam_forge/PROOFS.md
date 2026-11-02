# Operation UNIT–TO–UNIT: free path history, Pascal extrusion, Hausdorff–Gamma completion

**Scope:** classical algebra/analysis specialized to the *unchanged original four-pole* BBP forcing with literal `U_0=0`. The mathematical derivations below are paper proofs, not a Lean-kernel proof, external peer review or claims of priority. **Base-16 normality of π and RH remain OPEN.** All operations have explicit source, domain and observation type. Main XVIII plus draft PR #439 were inspected before constructing this additive research package.

## U1. How far can “every form is a linear combination of unit SUCCs” go?

In the free commutative semiring `N[x]`, a **finite** polynomial with nonnegative integer coefficients is constructed using constants 0/1, successor/addition, multiplication and diagonal copying. Group completion yields `Z[x]`, and localization adds rational coefficients. A pure single-register operation `S(x)=x+1` alone does **not** generate arbitrary multiplication `x -> 3x`, rational shifts, exponentials or every analytic function; those require additional typed operations.

Retain literal word history in the free path category with generators `S`, `V_m(x)=mx` (integer `m>=1`), and optional **declared** rational translations `T_c(x)=x+c`. Distinct words may map to the same endpoint affine function. The endpoint-image semigroup has normal forms `(a,m):x->mx+a` and composition `(a,m)(b,n)=(a+mb,mn)` (acting first with `(b,n)`). The exact law on state maps is

`V_m ∘ S = S^m ∘ V_m`.

For example, `S; V_3` and `V_3; S; S; S` both map `x->3x+3` but have different intermediate states and different length. A toy prestate-dependent edge cochain detects their path difference. This toy is **not** a BBP phase. Source labels must be independently supplied before calling any such difference physical/arithmetic holonomy. The user's sample `6(3x+1)=18x+6` has ordered witness `V_3;S;V_6`; the endpoint-equivalent `V_18;S^6` has a different path history.

All pure integer affine paths have integral translation. Since the actual BBP forcing already has `r(1)=47/15`, the BBP system requires rational localization or equivalent source-carry encoding. Free unit successor alone is not a universal analytic carrier. **Path equality is a quotient; path-history charge does not descend automatically.**

## U2. Original positive source as a complete Hausdorff moment carrier

The unmodified original source is

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `n>=1`, `U_0=0`, `U_(n+1)=16 U_n+r(n+1)`.

Set `P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2)>0` for `0<t<1`. Direct integration of four monomials gives

`r(n)=int_0^1 t^(8(n-1)) P(t) dt`.

Put `u=t^8`; let `mu` be the finite positive measure on `[0,1]` with density

`dmu(u)=(1/8) u^(-7/8) [4-2u^(3/8)-u^(1/2)-u^(5/8)] du`.

Then for `Re z > -1/8`,

`f(z):=r(z+1)=int_0^1 u^z dmu(u)`.

The half-plane is *sharp for this integral*: near zero the density is asymptotic to `(1/2)u^(-7/8) du`, and the integral fails as an ordinary absolutely convergent integral for `Re z <= -1/8`. These statements require this exact source density; a matched finite jet does not suffice. In the completely monotone positive-measure class, the complete integer sequence determines `mu` uniquely by the classical Hausdorff moment theorem; finite prefixes do not determine it.

## U3. Every finite source value is a signed Pascal combination of **positive** unit differences

Write `Delta f(x)=f(x+1)-f(x)` and introduce the *unit difference atoms*

`a_k=(-1)^k Delta^k f(0)=int_0^1 (1-u)^k dmu(u)>0`, for every `k>=0`.

The integrand is strictly positive on an interval, so `a_k>0`, `a_(k+1)<a_k`, and `a_k -> 0`. The positive Beta/Gamma formula is exactly

`a_k = (1/8)[4 B(1/8,k+1)-2 B(1/2,k+1)-B(5/8,k+1)-B(3/4,k+1)]`,

with `B(a,k+1)=k!/[a(a+1)...(a+k)]`. In particular `a_0=47/15`; all `a_k` are **rational** and strictly positive. A separate finite signed-difference implementation and a factorial/Gamma-ratio oracle give the same values.

For every positive **integer** n, expanding `u^(n-1)=[1-(1-u)]^(n-1)` and interchanging a **finite** sum and integral yields the exact finite Newton/Pascal formula

`r(n)=sum_(k=0)^(n-1) (-1)^k binom(n-1,k) a_k`. (U3)

No infinite analytic continuation is needed at any finite n. This is a complete finite-to-finite realization over primitive successor differences. It is signed; positivity of `a_k` does NOT imply positive phase or Fourier cancellation.

The Beta asymptotic `B(a,k+1)~Gamma(a) k^(-a)` proves

`a_k ~ [Gamma(1/8)/2] k^(-1/8)` as `k->infty`. (U3A)

This **slow** (non-summable) jet tail is an important resolution cost. Since all `a_k>0`, the BBP source has no globally finite-degree Newton polynomial; only each *finite* integer evaluation truncates.

### Analytic extension, with a sharp convergence boundary

For each complex z with `Re z > -1/8`,

`r(z+1) = sum_(k=0)^infinity (-1)^k binom(z,k) a_k`. (U3B)

Proof: for `0<u<1`, the binomial theorem gives `u^z=[1-(1-u)]^z`. For a nonnegative integer z, it terminates. For any other fixed z, `|binom(z,k)|=O_z(k^(-Re z-1))`. From U3A, `a_k=O(k^(-1/8))`, so `sum |binom(z,k)|a_k<infty` whenever `Re z>-1/8`. Tonelli/dominated convergence then permits the termwise integral. On compact subsets the Gamma-ratio estimate is uniform, giving local uniform convergence and a holomorphic representation. If `Re z<=-1/8` and z is not a nonnegative integer, `|binom(z,k)|a_k` has a non-summable `k^(-Re z-9/8)` tail; hence this particular Newton series fails to converge **absolutely**, matching the sharp integral boundary. We do NOT assert it cannot possess some separate regularization/continuation.

Note: this is a **real/complex** Newton expansion; it is not automatically a `Q_p`-convergent Mahler series. The operator and source completion must be declared separately at each place.

## U4. Actual BBP states form a **unimodular extruded Pascal-16 triangle**

For integers `n>=1`, `0<=k<n`, put

`C_(n,k)=sum_(j=k)^(n-1) 16^(n-1-j) binom(j,k)`.

Substitute U3 into the **original zero-seeded recurrence**, interchange only finite sums, and obtain

`U_n = sum_(k=0)^(n-1) (-1)^k C_(n,k) a_k`. (U4)

The exact recurrence and boundary are

`C_(1,0)=1`, `C_(n+1,k)=16 C_(n,k)+binom(n,k)`, and `C_(n,n-1)=1`.

The first rows are `(1)`, `(17,1)`, `(273,18,1)`, `(4369,291,19,1)`. A second implementation builds rows recursively rather than using the defining sum. The matrix sending `(a_0,...,a_(N-1))` to `(U_1,...,U_N)` is lower triangular with diagonal `((-1)^k)_(k=0)^(N-1)`, and therefore determinant `(-1)^(N(N-1)/2)`. **It is unimodular and invertible over Z for every finite N.**

Thus no finite rational source information is lost by the full signed extrusion; forgetting the signs, clocks, off-diagonal phase products, or sufficiently high levels is a **different, lossy observer**. The path coefficients have generating function (as a formal series):

`sum_(n>=k+1) C_(n,k) z^n = z^(k+1)/[(1-16z)(1-z)^(k+1)]`. (U4G)

The two denominators track multiplication by 16 and the Pascal successor count. This is an identity of **formal** power series; passing to complex variables requires a convergence domain. At a fixed h, the genuine phase is `e(h U_n)=prod_(k<n) e(h (-1)^k C_(n,k) a_k)`. This retains exact cross-atom interactions, but supplies no signed saving on their time average.

## U5. Green completion is a first-order **unit-jet-to-unit-jet** boundary equation

Define the authentic future tail for `Re z>-1/8`,

`T(z) = sum_(j>=1)16^(-j) r(z+j) = int_0^1 u^z/(16-u) dmu(u)`.

The equality is Fubini on the positive real axis and then analytic continuation in the common half-plane. Its unit coefficients are

`tau_k=(-1)^k Delta^k T(0)=int (1-u)^k/(16-u) dmu(u)>0`.

Because `15<=16-u<=16`, we have `a_k/16 <= tau_k <= a_k/15`, and `tau_k/a_k->1/16`. Multiplying by `15+(1-u)=16-u` proves for **every** k

`15 tau_k + tau_(k+1) = a_k`. (U5)

The solution is unique among **bounded** coefficient sequences: the difference of any two solutions obeys `d_(k+1)=-15 d_k`, so a nonzero difference grows as `15^k`. The original positive measure supplies the unique bounded/vanishing branch; the zero-at-infinity selector is not a free assertion.

In particular `tau_0=T(0)=pi/16` is an exact consequence of the authentic BBP formula, and solving U5 backwards gives the new-to-this-dossier representation

`pi/16 = sum_(j>=0) (-1)^j a_j/15^(j+1)`. (U5P)

This is a **geometrically convergent rational expansion**, not a new normality result or numerical improvement over the original BBP digit-extraction algorithm. With `alpha_J=sum_(j<J) (-1)^j a_j/15^(j+1)`, the exact positive integral remainder is

`pi/16-alpha_J = (-1)^J/15^J int_0^1 (1-u)^J/(16-u) dmu(u)`,

hence its **sign is exactly `(-1)^J`** and

`a_J/(16*15^J) <= |pi/16-alpha_J| <= a_J/15^(J+1)`. (U5R)

The finite-cutoff relation is also exact:

`15 tau_(k,J)+tau_(k+1,J)-a_k = (-1)^(J-1) a_(k+J)/15^J`,

where `tau_(k,J)=sum_(j<J) (-1)^j a_(k+j)/15^(j+1)`.

## U6. Genuine, all-horizon **finite-jet to real-circle phase** transport with a paid error

For `h in Z\{0}`, integers `M,J>=1`, let

`W_M(h; alpha)=sum_(n=1)^M exp(2 pi i h 16^n alpha)`, `alpha=pi/16`;
`W_M(h;alpha_J)` is defined similarly with the exact rational shadow U5R.

Use `|e(x)-e(y)|<=2 pi |x-y|`, `pi<22/7`, the geometric finite time sum `sum_(n=1)^M16^n=16(16^M-1)/15`, and U5R. The completely explicit source-certified bound is

`|W_M(h;alpha)-W_M(h;alpha_J)|`
`  < (44/7)*|h|*a_J *16*(16^M-1)/15^(J+2)`. (U6)

No hidden analytic or numerical constants. Choosing `J=2M` and using `a_J<=a_0=47/15` yields

`|W_M(h;alpha)-W_M(h;alpha_(2M))|`
`  < (33088/23625)*|h|*(16/225)^M`. (U6A)

This is **exponentially small in the finite observation horizon** and exactly reproduces the original full zero-seeded finite circle observations through moving rational approximants. For every **fixed J**, the rational alpha_J is periodic under base-16 multiplication and nonnormal; J must grow with M, with limits in the declared order. U6 proves precision transport only, never that either time-averaged signed sum tends to zero. The exact rational test oracle compares U6 intervals to independent Machin arctan bounds of pi.

## U7. Integer SUCC/dilation operations form an exact, noncommuting **moment functor**

For any positive measure `nu` on `[0,1]`, define `f(x)=int u^x dnu(u)` and its unit jets `c_k=int(1-u)^k dnu(u)`. On functions set `(S f)(x)=f(x+1)` and `(V_m f)(x)=f(mx)` for integer m>=1. On **complete jet sequences**, the corresponding operations are

`(A c)_k = c_k-c_(k+1)` and

`(B_m c)_k = sum_(j=0)^(mk) [v^j](1-(1-v)^m)^k * c_j`. (U7)

Both are *finite at each output coordinate* and have integer coefficients; they preserve actual positive measures by multiplication by u and pushforward under `u -> u^m`. On functions,

`S V_m = V_m S^m`,

hence their exact jet lifts satisfy

`A B_m = B_m A^m` on every **complete** moment tower. (U7D)

Proof directly in variable `v=1-u`: set `p_m(v)=1-(1-v)^m`. Left side integrates `p_m(v)^k(1-p_m(v))=p_m(v)^k(1-v)^m`; right integrates the same polynomial after expanding the two operators. This checks the actual map, not an unlabeled diagram. For m=3,

`(B_3 c)_1 = 3c_1-3c_2+c_3`;
`(B_3 c)_2 = 9c_2-18c_3+15c_4-6c_5+c_6`.

**The precision cost is real:** an exact k-th dilated unit jet depends on moments up through `mk` (the top coefficient is nonzero). In analytic x, `f(mx)` may have a smaller half-plane of convergence than f(x); for this original measure, the half-plane `Re x>-1/8` becomes `Re x>-1/(8m)`. Neither exact integer polynomial algebra nor positive measure pushforward automatically yields a common `Q_p` or complex Fourier phase law.

### A decisive positive-measure inadequacy witness

For any integer m>=2, take nodes `v_j=j/m`, `j=0,...,m`. Set `b_j=binom(m,j)/2^m` and `nu_j=(-1)^(m-j)binom(m,j)/2^m`. The two **strictly positive** probability measures with masses `b_j +- nu_j/2` have identical unit moments `c_0,...,c_(m-1)` because an m-th finite difference annihilates every polynomial of degree <m. Yet their m-th moments differ by `m!/(2^m*m^m)`, and their **first** dilated moment `(B_m c)_1` differs by

`(-1)^(m+1) * m!/(2^m*m^m) != 0`. (U7N)

For m=3 this is exactly `+1/36`. Thus a first-order diluted result **does not factor through** a finite observation that retains fewer than m unit moments, even among positive normalized carrier measures. This is a fully explicit source-map/probe-gap witness for the proposed "duck-shaped" quotient. It does NOT refute exact full-infinite moment transport.

## U8. Genuine quadratic Pisot example, kept distinct from BBP

A two-coordinate algebraic-integer carrier `Z[phi]` has `phi^2=phi+1`. In basis `(1,phi)`, multiplication by phi is the integral matrix `[[0,1],[1,1]]` with characteristic `X^2-X-1` and eigenvalues phi and `-1/phi`; one direction expands, its real algebraic conjugate contracts. This produces exact Fibonacci propagation; it is a **nontrivial Pisot** instance of colored unit paths. The correct diamond is `V_phi S_1 = S_phi V_phi`, **not** `V_phi S_1 = S_1 V_phi`. Both sides are checked exactly over bounded Z² holdouts. The original BBP multiplier 16 and four rational poles do NOT inherit an arithmetically useful golden/Pisot connection from this toy alone.

## U9. Steelman, crucible, verdict

**STEELMAN.** Forms built from finite unit successors, integer dilation, rational localization and positive-measure completion may be transported between finite and analytic carriers by explicit noncommuting compositional laws while retaining realized paths and source labels.

**SURVIVES (paper proofs).** U1–U7 construct an exact carrier for this specified source class: affine history, rational BBP unit atoms, unimodular finite extrusion, sharp analytic Newton–Gamma completion, bounded Green selector, exponentially precise moving rational circle approximants, and full moment dilation transport. U8 provides a separate Pisot instance.

**PRODUCTIVE FAILURE / REFUTED oversells.** (i) Unit shift *alone* cannot generate x->3x; rational shifts need localization, general analytic forms require a completion. (ii) Endpoint equality does not identify path-cochain values. (iii) Low jets are insufficient for V_m (U7N). (iv) A fixed rational shadow is nonnormal; exponentially precise finite-horizon shadows do not prove π normal. (v) Positive moment/Gram and complete finite reconstructions do not imply genuine selected signed Weyl cancellation. A four-pole source and exact zero seed remain required.

**OPEN:** an unconditional original-source signed estimate `S_N(h)=o(N)` for every fixed nonzero h. The legal next probe must combine the genuine source, the selected zero boundary, the full phase products and first-birth/Poisson alias or Fejer lag current with all-horizon estimates, and must explicitly reject coherent changed-seed and matched-jet source controls. No such estimate was proved here.

### Scientific/classical provenance

- J.-G. Liu and R. L. Pego, *On generating functions of Hausdorff moment sequences* (CMU/Duke research), https://www.math.cmu.edu/CNA/Publications/publication_auto.php?cnacode=14-CNA-001 — classical complete monotonicity and moment representation, the leading-difference transform.
- G. Bruda, *On the convergence of Newton series and the asymptotics of finite differences*, https://arxiv.org/abs/2404.04288 — external general Newton-series convergence literature; **our specialized sharp `-1/8` domain is derived directly from the original `u^(-7/8)` density**, not borrowed as a published novel theorem.
- Brownlowe–Larsen–Stammeier, *On C*-algebras associated to right LCM semigroups*, https://citeseerx.ist.psu.edu/document?doi=d2865e21936f96b732a4b693aec8cb0047d397e&repid=rep1&type=pdf — classical `N ⋊ N^×` affine semigroup structure.
- SUCC main XVIII `observational_succ/proto_succ_variable_unit.py` and `clock_mahler_interpolation.py` — preexisting finite Newton/variable-unit and `p`-adic MAHLER research. This branch specializes these ideas to BBP source; does not supplant the existing category spine.
- SUCC main XVIII `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` and prior PRs #437–#439 — exact selected Weyl gate, positive Gamma source, Zak/Mellin signed alias and seed firewalls. Historical claims and original sources are not overwritten.
