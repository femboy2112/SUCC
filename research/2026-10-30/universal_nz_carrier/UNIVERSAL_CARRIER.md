# SUCC universal arithmetic carrier: from finite path counts to N and Z

**Status: formal candidate framework with verified classical identities.** It is a mathematical carrier *model*, not a claim that a physical observer constitutes or fully knows its carrier. Its role is to admit explicit, faithful source-realization maps. It neither proves base-16 normality of pi nor RH.

## 1. Recover a carrier before selecting a source

Work with the groupoid of finite labeled sets and bijections, and with finite injective chains. The rank of a finite set `S` is `|S| in N`; adjoining one new element is a time step. The words in `{0,1}^n` describe selection/omission of each of n labeled elements. Grade `k` means exactly k selections; its size is `C(n,k)`.

The **universal (Pascal) finite-path triangle** has vertices `(n,k)` for `0<=k<=n` and two edges `(n,k)->(n+1,k)` and `(n,k)->(n+1,k+1)`. Full histories are not the same object as endpoint grade. The finite identity

`C(n+1,k)=C(n,k)+C(n,k-1)`

is path composition, not an independent digit law for pi. The source-independent Vandermonde composition

`C(a+b,k)=sum_j C(a,j) C(b,k-j)`

is exact for natural integers; as a polynomial identity it extends to all `a,b in Z`.

**The integer completion:** `Z` is the Grothendieck group of finite-set cardinalities under disjoint union. The polynomial extension `C(n,k)=n(n-1)...(n-k+1)/k!` is integer valued at **every** `n in Z`. For negative n it is *signed algebra*, not a positive count of literal paths. Retain both the finite-positive count and the completed signed polynomial as separate typed layers.

## 2. Degree two is the load-bearing multiplication gate

Define `P_2(n)=C(n,2)`. Then

`ab=P_2(a+b)-P_2(a)-P_2(b)`

for all `a,b in Z`. The cross-grade counts pairs with one element from each colored summand. This means the additive **labeled and colored path category**, retaining its genuine mixed second-grade interaction, reconstructs the ordinary product. Then divisibility `a|b`, units, irreducibles, prime powers, gcd, valuations and Dirichlet convolution can be defined internally in the recovered ring `Z`.

Do not assert that an undifferentiated grade-2 sequence, after dropping the information about colored summands and their embeddings, automatically reconstructs *all* path relations: recovering the ring law requires the declared coherent direct-sum/polarization operation.

## 3. Discrete differential threading, with an exact interpolation map

Let `D=d/dx`, `Delta f(x)=f(x+1)-f(x)` and define the linear map `J` on polynomials by

`J(x^k/k!) = C(x,k)`.

Pascal gives, for every k>=1, `Delta C(x,k)=C(x,k-1)`; both sides vanish for k=0. Hence

`Delta J = J D` on Q[x].

This is an **exact intertwiner** between differentiation and finite differences. It does not require a limit of small steps. Because `C(x,k)=Gamma(x+1)/[Gamma(k+1)Gamma(x-k+1)]` on a domain where the quotient is defined (then polynomially continued), Gamma provides a classical analytic expression for the finite basis.

**Counterexample to a stronger claim:** `J(x^2)=x(x-1)` but `J(x)^2=x^2`. Thus J is not a ring homomorphism. Ordinary multiplication uses a *different* transported product (`f star g=J(J^-1 f * J^-1 g)`) or the mixed Pascal-grade polarization above. Failure to retain this defect would confuse finite differential threading with preservation of every arithmetic operation.

The discrete Leibniz rule is twisted: `Delta(fg)(x)=f(x+1) Delta g(x)+g(x) Delta f(x)`; it is not the ordinary product rule at finite step.

## 4. Embedding an observer into a carrier is NOT identifying model and carrier

A concrete arithmetic carrier state contains at least the source-independent clock, arithmetic value, full finite history, and (when selected) a branch/carry record. An *embedded observer* receives a declared finite-information quotient `q:C->M`, holds its own state and an optional full external history ledger, and uses a declared model transition `Fhat`.

The model is exact on a class of carrier states only if `q o F = Fhat o q` on that class. This holds precisely if `q(F(c))` is constant on each q-fiber. For example the first-hex-digit observation `q(x)=floor(16x)` does not close under `T(x)=16x mod1`: states `0` and `1/256` share first digit 0, but their successor first digits are 0 and 1. More history, the exact residual, or an explicitly stochastic **prediction** is required. This reproduces the correctness boundary of SUCC PR #414, not a newly discovered theorem.

The full observer model may use a positive Gamma/Pascal posterior, but that posterior is not the actual empirical distribution of digits unless a source-to-model adequacy theorem is independently proved. A uniform inverse-branch model always has Haar fixed point; that alone proves no normality of a selected concrete path.

## 5. Universal skew-product arithmetic and faithful source embeddings

For a radix `b>=2`, an explicitly chosen arithmetic source `r:N_{>=1}->Q` (or R), and initial `u_0=s`, define the **universal affine source instance**

`F_{b,r}(n,u)=(n+1,b*u+r(n+1))`.

The source is a label on an otherwise general arithmetic skew-product. The integer lift/carry is retained under reduction modulo Z. A finite observer may compute `u_n` exactly when r is rational at each finite n; an exact infinite future real is not assumed to be stored.

If `sum_{j>=1} b^-j |r(j)|<infinity`, put `alpha=s+sum_j b^-j r(j)` and `T_n=sum_{j>=1}b^-j r(n+j)` whenever the sums exist. Direct finite telescoping gives

`u_n=b^n alpha-T_n`, `T_(n+1)=b T_n-r(n+1)`, and `v_n=u_n+T_n=b^n alpha`.

The future correction is the unique **bounded** solution of the cohomological equation when it is bounded, because two solutions differ by `Cb^n`. Without boundedness, uniqueness is not asserted. This isolates source and initial boundary but does not turn `alpha` into a fair random seed.

The authentic BBP instance is the specialization

`b=16`, `s=0`, `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`.

All four poles arise as rational readings of the universal integer clock: define `ell_delta(n)=8(n-1)+delta`, `delta=(1,4,5,6)`, apply the signed linear observation `sum c_delta/ell_delta(n)` with `c=(4,-2,-1,-1)`. The original source has the positive Laplace form `r(n)=integral_0^infty exp(-(8n-7)t) Q(t)dt`, `Q(t)=4-2 exp(-3t)-exp(-4t)-exp(-5t)>0`.

This is a **faithful realization of BBP inside a source-parameterized arithmetic carrier**. It is not a derivation of the BBP coefficient vector from a universal counting axiom, not an identification of the auxiliary source posterior with the actual digit law, and not a proof that every carrier path is normal.

## 6. Boundary countercontrol

The same source with `s=-pi/16` has `alpha=0` and `u_n=-T_n`, so its completed radix orbit is the constant zero and is not normal. All positive source/Beta/Gamma observer identities remain unchanged. Therefore a valid normality proof must include a **selected zero-boundary-sensitive arithmetic premise**, not merely carrier symmetry, rank-two Gamma positivity or universal Pascal counts.

A finite digit prefix likewise cannot classify normality among unrestricted infinite sequences: normal and eventually-zero continuations share that prefix. The original arithmetic source and literal zero boundary are additional structural inputs, not replaceable by the observed prefix alone.

## Integration recommendation

Keep the universal N/Z carrier as a **separate freestanding module**; keep `R(a)`, four poles, source/carry and the rank-two Oily observer as a BBP-specific functor into it. Validate the two routes on integer arithmetic, Fibonacci and normal/nonnormal symbolic controls before attempting any new selected signed estimate. Do not merge this paper's source-neutral objects with the unmerged specialized PRs until their contracts are reconciled explicitly.