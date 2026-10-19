# RAD/RIS transport: prime gates, successor nonlocality, exact CRT laws and the ABC boundary

**Research checkpoint:** 2026-10-19. **Base tree:** `femboy2112/SUCC@4de865766d53ea448555386d98f3e88e3ec605b6` (Academic Main IV integrated). **Authority:** elementary paper derivations, plus independent bounded exact tests in `tests/test_rad_ris_transport.py`. **Novelty:** no academic priority claim; these are classical arithmetic facts and new-to-project packaging. **RH proved: NO. ABC proved: NO. Original signed `S_4` positivity: OPEN.**

## 0. Steelman, crucible and verdict

Proposal: `rad(n)` records the distinct-prime support of `n`; call `ris(n)=n/rad(n)` the **residual multiplicity**. The identity `n=rad(n)+rad(n)(ris(n)-1)` resembles `V=IR` with one unit resistance and one remaining series resistance. We retain this mnemonic while refusing the claim that a resistor or conservation law was physically discovered. The question is what *additional, non-tautological laws* emerge when both SUCC (`S e_n=e_{n+1}`) and genuine-prime FUCC (`V_p e_n=e_{pn}`) act on the same coordinates.

**Verdict:** canonical factorization and prime switching are exact; source-limited successor prediction has an exact CRT obstruction; joint multiplicity/support Euler factors and their Gibbs covariance are computable with valid convergence domains. The Ohm identity by itself has no prime-specific content. The actual uniform ABC inequality and authentic completed Weil positivity are still separate hard problems.

## 1. Admissible coordinates and unique multiplicative transport (RRT-01)

For positive `n=prod_p p^{v_p(n)}`, define

\[
 r(n)=\prod_{v_p(n)>0}p,\qquad t(n)=\prod_p p^{\max(v_p(n)-1,0)}.
\]

Use `r(1)=t(1)=1`. The map `n -> (r,t)` is a bijection from positive integers to the pairs of positive integers satisfying **(i)** `r` squarefree, **(ii)** every prime of `t` divides `r`. Forwards: unique prime factorization. Backwards: `n=rt`; its prime exponents are `1+v_p(t)` on the support of `r`, hence `rad(n)=r`, `ris(n)=t`. This also proves the normalization and that the map loses no integer information.

For `m,n>0` put `g=gcd(r(m),r(n))` (the product of common *distinct* primes). Then

\[
 (r(m),t(m))\odot(r(n),t(n))
 =\left(\frac{r(m)r(n)}{g},\;t(m)t(n)g\right).
\]

At each prime, union of the two nonzero support indicators contributes one support copy; if both inputs contain that prime, the other copy transfers into residual multiplicity. The resulting pair encodes `mn`, so this operation is associative and commutative with unit `(1,1)`; no freestanding associativity assumption is needed. When `gcd(m,n)=1`, `g=1` and both coordinates multiply separately. **Status: CLASSICAL / paper proved; bounded implementation checked.**

## 2. Radical-depth layers are a lossless nested squarefree chain (RRT-02)

Define the zero-indexed prime-support layers

\[
 L_j(n)=\prod_{p:\,v_p(n)>j}p,\quad j=0,1,\ldots.
\]

Then `L_0=r(n)`, `L_1=r(t(n))`, `L_{j+1}|L_j`, and all but finitely many layers equal `1`.

\[
 n=\prod_{j\geq0}L_j(n),\qquad
 t(n)=\prod_{j\geq1}L_j(n).
\]

Indeed, a prime of exponent `e` occurs in exactly `e` layers. Conversely, **every finite nested chain of nonunit squarefree integers** `L_0,...,L_{h-1}`, with `L_{j+1}|L_j`, is uniquely the layer chain of their product. The nesting forces every prime `p` to occur in an *initial* segment of exactly `e` layers, giving `v_p(n)=e`. This is a precise support-depth filtration, not a claim about transfinite computation.

Example: `1008=2^4 3^2 7` has layers `(42,6,2,2)` and coordinate pair `(42,24)`. The maximal prime exponent is the number of nonunit layers. **Status: CLASSICAL / paper proved; independent trial-division oracle checked.**

## 3. A genuine prime-gated FUCC operator identity (RRT-03)

Work on `H=l²(N_{>=1})` with basis `e_n` and common dense invariant *algebraic finite-support* domain `c_00`. Define unbounded diagonal operators `R e_n=r(n)e_n`, `T e_n=t(n)e_n` on that domain, and a bounded projection `P_p e_n=1_{p|n}e_n`. For each genuine prime `p`, the prime dilation `V_p e_n=e_{pn}` obeys

\[
 \boxed{R V_p=V_p R\,[pI-(p-1)P_p]},\qquad
 \boxed{T V_p=V_p T\,[I+(p-1)P_p]}
 \quad\text{on }c_{00}.
\]

Proof: if `p\nmid n`, multiplication by `p` introduces it to the radical, and leaves `t` unchanged. If `p|n`, it leaves the radical unchanged and multiplies `t` by `p`. In both cases the product of the two displayed gate multipliers equals `p`: with `P=P_p`,

\[
 (pI-(p-1)P)(I+(p-1)P)=pI,\qquad P^2=P.
\]

Thus `RT e_n=n e_n=:N e_n`, and the known successor identity `[N,S]=S` yields the **exact** discrete product rule

\[
 \boxed{t(n)\,[r(n+1)-r(n)] + r(n+1)\,[t(n+1)-t(n)] = 1.}
\]

At `128->129` the terms are `64(129-2)=8128` and `129(1-64)=-8127`. Enormous cancellation is real; the constraint is an identity, *not* a positivity estimate. Full Hilbert-space operator extensions require separately specified closed domains; no bounded conjugacy, unitary equivalence or electrical-resistance model is asserted.

**Status: PROVED LOCAL exact algebra on `c_00`, classical ingredients; academic originality UNVERIFIED.**

## 4. Additive successor makes prime support nonlocal: a discriminating CRT no-go (RRT-04)

**Theorem (finite-window indistinguishability).** Fix any *finite* set `P` of genuine primes, and a genuine prime `q` not in `P`. There exist positive integers `n,m` such that

\[
 v_p(n)=v_p(m)=0\quad\forall p\in P,
 \qquad q\mid n+1,\quad q\nmid m+1.
\]

**Proof:** set `M=prod_{p in P}p` (`M=1` if `P` empty). By CRT, because `gcd(M,q)=1`, choose

\[
 n\equiv 1\pmod M,\quad n\equiv -1\pmod q;\qquad
 m\equiv1\pmod M,\quad m\equiv0\pmod q.
\]

Take positive representatives (add `Mq` if the representative is zero). The congruences force the claims. QED.

A concrete witness: observer window `P={2,3,5}`, outsider `q=7`; `n=181`, `m=91`. Both input valuation windows are `(0,0,0)`. Yet `7|182` and `7\nmid92`.

The correct interpretation is precise: **no map that reads only the fixed P-valuation vector of the input can determine all prime support of the successor**, even if it knows the full values of those finitely many coordinates. This does *not* prevent an observer who knows `n` exactly, is allowed to inspect `n+1`, or can adaptively acquire new prime probes from computing the result. It is a limitation of a specified instrument/closure, not a claim that arithmetic successor is uncomputable.

**Status: CLASSICAL CRT + PROVED LOCAL reconstruction; adversarial finite witness tested.**

### Exact valuation-probe density (RRT-05)

Let `A,B` be disjoint finite sets of primes, with prescribed positive exponents `e_p (p in A)` and `f_q (q in B)`. We insist on *exact* valuations `v_p(n)=e_p` and `v_q(n+1)=f_q`; unspecified primes remain unrestricted. For `p in A` the allowed classes modulo `p^{e_p+1}` are `n=p^{e_p}u`, `1<=u<p`. For `q in B` they are `n=-1+q^{f_q}u`, `1<=u<q`. CRT gives exactly

\[
 D=\prod_{p\in A\cup B}(p-1)
\]

distinct classes modulo

\[
 M=\prod_{p\in A}p^{e_p+1}\prod_{q\in B}q^{f_q+1}.
\]

The natural density exists and is `D/M`. In `1<=n<=X`, the exact count differs from `XD/M` in absolute value by **at most `D`**, since each CRT class contributes floor/ceiling of its expected share. This is an unconditional, computable local occupancy law. If `A` and `B` share any prime, no such positive-exponent simultaneous specification is possible because `gcd(n,n+1)=1`. The code enumerates exact residues and checks an independent valuation oracle, including this hostile overlap control.

**Scope:** finite fixed prime constraints, not a distributional ABC bound for unrestricted support.

## 5. A two-variable Euler deformation separating support and depth (RRT-06)

For complex `s,u` with `Re(s)>1`, `Re(u)>0`, define

\[
 Z_{r,t}(s,u)=\sum_{n\geq1}r(n)^{-s}t(n)^{-u}.
\]

Because the summand is multiplicative across coprime integers, its Euler factors are

\[
 \boxed{Z_{r,t}(s,u)
 =\prod_p\left(1+\frac{p^{-s}}{1-p^{-u}}\right).}
\]

The factor at `p^k` is `p^{-s}p^{-u(k-1)}` for `k>=1`. If `sigma=Re(s)>1` and `tau=Re(u)>0`,
`|1-p^{-u}|^{-1} <= (1-2^{-tau})^{-1}`; therefore `sum_p p^{-sigma}/|1-p^{-u}|` converges and the Euler product and Dirichlet series are absolutely convergent. On the diagonal `s=u=beta>1`, `r(n)t(n)=n`, so **`Z_{r,t}(beta,beta)=zeta(beta)`**; this is a reparameterization of the classical Euler product, not a zeta continuation or an RH proof. The Python API computes exact rational *single-prime* factors for integer `s>=2,u>=1`, with geometric-tail calibration.

This joint generating function provides an analytically clean way to ask whether an arithmetic observable responds to **prime births** or **prime multiplicity persistence**. It does not encode the additive law `a+b=c` by itself.

## 6. Independent prime Gibbs occupancy exposes an exact support/depth covariance (RRT-07)

For real `beta>1` let `P_beta(n)=n^{-beta}/zeta(beta)` be the normalized classical diagonal Gibbs distribution. Unique factorization and absolute convergence give independent prime valuations `K_p=v_p(n)` with

\[
 \Pr(K_p=k)=(1-q_p)q_p^k,\qquad q_p=p^{-\beta}.
\]

Set the support bit `B_p=1_{K_p>=1}` and excess multiplicity `E_p=(K_p-1)_+`. Direct geometric summation gives

\[
 \mathbb E B_p=q_p,\qquad
 \mathbb E E_p=\frac{q_p^2}{1-q_p},\qquad
 \boxed{\operatorname{Cov}(B_p,E_p)=q_p^2.}
\]

Indeed `B_p E_p=E_p` identically, so covariance is `(1-q_p)E E_p=q_p^2`. Since prime coordinates are independent and the log-moments converge when `beta>1`,

\[
 \boxed{\operatorname{Cov}_\beta(\log r(n),\log t(n))
  =\sum_p(\log p)^2p^{-2\beta}>0.}
\]

The sum is finite by comparison with `sum_{n>=2}(log n)^2 n^{-2beta}`. This is an **ordinary positive statistical covariance**, not a completed signed Weil form; treating it as source-derived RH positivity would be a type error explicitly forbidden by the repository's positivity firewall. The executable checks only finite local rational coefficients (`beta` integers >=2); the convergence is proved here by a separate analytic argument.

**Status: CLASSICAL probabilistic Euler-product consequence / elementary paper proof.**

## 7. ABC in RIS coordinates: exact re-expression, no new inequality (RRT-08)

For coprime positive `a+b=c`, the integers `a,b,c` are pairwise coprime. Write `r_a=r(a)`, `r_b=r(b)`, `r_c=r(c)`, `t_c=t(c)` and `R=r_a r_b r_c`. Define the usual quality `Q=log c/log R`. The exact equivalences are

\[
 Q>1\iff c>R\iff \boxed{t_c>r_a r_b},
\]

and

\[
 \boxed{Q-1=\frac{\log(t_c/(r_a r_b))}{\log R}.}
\]

The **conjectural** ABC bound, for each epsilon>0 with some K_epsilon independent of the primitive triple, is equivalent to

\[
 \boxed{t_c\leq K_\varepsilon (r_a r_b)^{1+\varepsilon}r_c^{\varepsilon}.}
\]

For `3+125=128`, `r_a=3,r_b=5,r_c=2,t_c=64`, so `Q>1` iff `64>15` and the excess ratio is exactly `64/15`.

**What remains unpaid:** nothing above bounds `t_c` uniformly in terms of *all three distinct-prime supports*. The `epsilon`-uniform quantifier for every primitive triple is the original hard conjecture. CRT constraints on fixed primes and equality `n=r t` cannot be promoted into it. The computation is a diagnostic of *individual triples* only.

## 8. Crucible: controls, failures, and what would change the verdict (RRT-09)

- **Vacuous-circuit mutant:** take `r_fake(n)=1`, `t_fake(n)=n`. Then `n=r_fake t_fake` and the discrete product law still hold for every `n`, but `r_fake(p)!=p` for every prime. Hence Kirchhoff/Ohm-shaped algebra alone is NOT a prime-source certificate.
- **Fake composite FUCC:** `p=6` must be rejected as a "new prime" even if its multiplication action is arithmetically well-defined; it violates the single genuine-prime occupation gate.
- **Impossible adjacent overlap:** positive valuations of the same prime at `n` and `n+1` must be rejected.
- **Missing source probe:** with finite `P` we can predict exact local CRT densities, but cannot determine unseen successor support. A probe that reveals a new `q` or full `n` repairs access; no extra positivity follows.
- **Claim laundering control:** replacing the actual radical by any positive factor `r_fake|n` retains a compensating identity. This cannot imply ABC; in particular, setting `r_fake=1` demonstrates nonidentification.
- **Signed-Weil firewall:** a positive Gibbs covariance or a local positive matrix is not the genuine completed Suzuki `S_4` form; the authentic first-window sign remains AMBIGUOUS and RH remains OPEN.

**Research next targets.** (1) Seek an *independently sourced, non-tautological* inequality on the additive transport of `(r,t)` for **all** coprime triples, not another rewriting of ABC; (2) use exact CRT to construct prime-observer probe-budget lower bounds with declared observation grammar, measuring which source queries repair the finite locality gap; (3) study rigorous joint Euler deformation derivatives to isolate information genuinely absent from one-variable zeta, and independently test whether any resulting inequality survives sham arithmetic sources. Failing these tests is productive information. The local covariance is not an analytic continuation, and no route from it to signed Weil positivity is supplied.

## Reproduction and authority boundaries

Run from repository root:

~~~sh
python -m unittest discover -s tests -p 'test_rad_ris_transport.py' -v
python -m compileall -q observational_succ/rad_ris_transport.py tests/test_rad_ris_transport.py
~~~

Full repository CI, provenance verification and Lean kernel results must be reported from actual runs, not inferred from local isolated results. The new module is independently factorized and has finite caps (`n<=1,000,000`, CRT modulus <=200,000, classes <=4096); the theorems are unrestricted when their mathematical hypotheses hold. The finite oracle uses a deliberately different divisor-enumeration method, not the module factorization routine. Tests are finite controls, **not** proofs of universal claims.

**Prior art and sources:** Fundamental theorem of arithmetic and Chinese remainder theorem (classical); NIST DLMF `27.4, [Euler products and Dirichlet series](https://dlmf.nist.gov/27.4); A. Granville and T. J. Tucker, [*It's As Easy As abc*](https://www.ams.org/notices/200210/fea-granville.pdf), *Notices AMS* 49 (2002), 1224–1231; [existing SUCC unit/prime source](../2026-10-16/UNIT_PRIME_SUCC_FLAT_CORRESPONDENCE.md). New-to-project algebraic presentation is not a certified new theorem in the literature.
