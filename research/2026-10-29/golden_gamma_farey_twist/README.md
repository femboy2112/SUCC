# The arithmetic triangular plane: Farey–totient Γ fields, 45° primitive defects, and a separating Eisenstein observer of BBP

**Research-only mathematical dossier, October 29, 2026.** Intended as an **additive child of SUCC draft PR #371** (`e418e465b7b0669997d8c67fcbcbd48c1df1681f`), whose original source comes through #370, #369 and #367. Read sibling research #368 and #372 for the other Pascal/Gamma and totient interpretations. Historical source, `U_0=0`, claim namespaces, production code and main remain immutable. **π base-16 normality and RH OPEN.** The identities below are classical mathematical ingredients assembled as SUCC research; academic novelty UNVERIFIED. No quantum/physical phase inference.

## Executive result, with exact scope

Three constructions are now coherent, but **three distinct source maps** must not be silently equated:

1. **The Farey tessellation really tiles the upper half-plane.** The modular group acts on the entire ideal-triangle complex. Totient/cototient label primitive versus nonprimitive denominator classes; Gamma variables give an honest, edge-compatible random field across every face. Its rank-two observable equals `lambda - gamma`. The Golden point is the fixed *ideal boundary point* of a specified hyperbolic modular matrix, **not** a canonical vertex of each tile.
2. **The integerized 45-degree map** `D=[[1,-1],[1,1]]` has `D^2=2[[0,-1],[1,0]]`, determinant 2, and maps a primitive integer vector to an imprimitive vector iff both coordinates are odd. For the **authentic original two-geometric Oily endpoint**, this parity/coprimality loss is a convergent Möbius series. Its Mellin transform has the exact factor `Gamma(s)*zeta(s-1)/[(1-2^-s)*zeta(s)]`, a legitimate 45-degree complex-contour rotation, and an **exact Euler-gamma cancellation in the pole-normalized first jet**.
3. **The Eisenstein primitive-lattice scalar on the same Farey plane** is modular invariant; each fixed-height translated horizontal profile has nonzero, explicitly positive Fourier coefficients. Applying its *whole translate family* to the actual rational zero-seeded BBP phase defines a nonnegative finite-horizon scalar energy whose vanishing at infinity is **equivalent** to normality. This is a source-faithful discriminating **instrument**, not a proved new cancellation estimate. The coherent counterseed has positive limiting energy.

The Farey/Gamma field, the Oily 45-degree defect and the actual zero-seeded signed orbit share an arithmetic framework, but no theorem derives a physical 45-degree dynamical twist or a selected signed Fourier decay from their common positive observations.

## 1. A literal arithmetic tiling of the hyperbolic plane

Let `H={x+iy:y>0}`. Its **Farey ideal triangulation** is the PSL2(Z)-orbit of the triangle with cusps `0,1,infinity`; each edge joins two rational cusps `a/b,c/d` for which `|ad-bc|=1`. A mediant `(a+c)/(b+d)` is reduced, and the new determinant-one edges are the exact arithmetic recursion. The upper half-plane is topologically a plane; this is its canonical *hyperbolic*, not Euclidean-equilateral, tiling once the integer modular structure is chosen. The circle `P^1(R)` is the boundary; the original unmarked circle alone does not specify this tessellation.

The modular matrix

```
A = [[1,1],[1,2]], det A=1, trace A=3
```

has attracting ideal boundary fixed point `lambda=(sqrt(5)-1)/2` and repelling point `-phi`. Proof: `z=(z+1)/(z+2)` reduces to `z^2+z-1=0`; its positive solution is lambda. Its orbit of `0/1` is `0/1,1/2,3/5,8/13,...`, consecutive even Fibonacci convergents. It transports genuine Farey triangles to Farey triangles and preserves the hyperbolic geodesic joining its two irrational fixed points. This is a **specified** golden itinerary, not a forced value of every modular observable.

### Totient/cototient–Gamma vertex decoration

For each reduced rational cusp `v=a/q`, `q>=1`, let `q_v=q`; assign `q_infinity=1` as a **declared cusp convention**. Let `phi(q)` be Euler's totient and `c(q)=q-phi(q)` its complementary (noncoprime) residue count. At each cusp independently sample **two** Gamma variables with *unit rate*:

```
P_v ~ Gamma(rP(v),1), rP(v)=1+phi(q_v)
C_v ~ Gamma(rC(v),1), rC(v)=1+c(q_v)
```

The `+1` neutral pseudocounts ensure positive shapes and are model choices, not consequences of modular geometry. `P_v+C_v~Gamma(q_v+2,1)`, and `P_v/(P_v+C_v)~Beta(1+phi(q_v),1+c(q_v))`. Every vertex is a single global variable; it is not independently resampled in each tile.

For triangle `T=(u,v,w)`, define barycentric weights using only its **primitive** channel `P`:

```
B_(u,T)=P_u/(P_u+P_v+P_w) and cyclic permutations.
```

The triangle law is `Dirichlet(rP(u),rP(v),rP(w))`. On an edge `(u,v)` shared by two triangles `T,T'`, the *reduced* edge ratio is exactly the SAME random variable,

```
B_(u,T)/(B_(u,T)+B_(v,T)) = P_u/(P_u+P_v)
= B_(u,T')/(B_(u,T')+B_(v,T')) ~ Beta(rP(u),rP(v)).
```

Thus the entire countably infinite face family **glues pathwise along edge projections** on a common probability space. The full three-component barycentric vectors do *not* coincide across edges: their third vertices/normalizers differ, and claiming that stronger gluing would be false. Exact moments: `E[B_u^a B_v^b B_w^c]=(r_u)_a(r_v)_b(r_w)_c/(r_u+r_v+r_w)_(a+b+c)`.

The primitive harmonic/golden/log field at vertex v is

```
D_P(v) = E[log P_v - exp(-lambda P_v)]
       = H_(phi(q_v)) - gamma - lambda^(1+phi(q_v)).
D_C(v) = H_(c(q_v)) - gamma - lambda^(1+c(q_v)).
```

These equations use `1+lambda=1/lambda`. At the reference cusp `q=1`, `rP=2`, so `D_P=1-gamma-lambda^2=lambda-gamma=Omega_OM` exactly. The cototient channel has rank 1 there. For any orientation `u->v`, the edge potential increment `D_P(v)-D_P(u)` sums to **zero** around every triangle and every closed loop. Consequently **a scalar vertex Gamma/harmonic/golden potential has flat holonomy**; it cannot by itself create the desired nontrivial selected BBP phase. Totient, cototient and Gamma edge gluing are genuine, but the labels are not PSL2(Z)-invariant: matrix transport sends a denominator to a different denominator and requires transporting its mark.

## 2. Integer arithmetic 45° and an exact 2-adic primitiveness defect

Let `D=[[1,-1],[1,1]]`. It is `sqrt(2)` times an ordinary Euclidean 45-degree rotation. `D^2=2S`, `S=[[0,-1],[1,0]]`; here S is an actual unimodular 90-degree quarter-turn. **D is NOT in SL2(Z)** (determinant 2). Therefore it is not a symmetry of the primitive Farey tessellation without an extra parity/scale register. For any primitive pair `(k,l)`, the gcd of `k-l,k+l` divides 2. It equals 2 iff `k,l` are both odd and equals 1 otherwise. Proof: the gcd divides twice each input, and the primitive input removes every odd common factor; both outputs are even exactly for odd/odd input. Of the three nonzero primitive classes mod 2, exactly one loses primitivity under D.

This is an exact **arithmetic parity defect**; it is not a claim that the complex Gamma integral *geometrically* rotates the integer lattice.

## 3. The original two-channel Oily law provides the weight

The inherited actual Oily endpoint decomposes `J=K+L`, with two independent geometric counts

```
P(K=k,L=l)=2^(-(k+l+2)), k,l>=0,
P(J=j)=(j+1)/2^(j+2).
```

Define the primitive-loss probability `p45=P(gcd(K,L)=1 and K,L both odd)`. Since both are odd, all common divisors are odd; Möbius inversion plus the original **two** geometric loops gives

```
p45 = (1/4) * SUM_{d>=1, odd} mu(d) * 4^(-d)/(1-4^(-d))^2
    = 0.10681992705865087306...
```

The series converges absolutely. An exact rational D-cutoff has absolute error `< 4^(-(D+1)) / [3(1-4^(-(D+1)))^2]`, since the neglected odd terms are bounded by an unrestricted geometric sum. The primitive-pair probability is independently

```
P(gcd(K,L)=1)
 = (1/4) SUM_{d>=1} mu(d)*[(1-2^(-d))^(-2)-1]
 = 0.46690770049625558...
```

**The minus one is essential**: the original law gives mass 1/4 to `(0,0)`, which is divisible by every integer; applying Möbius inversion to it without first removing it is invalid. The conditional 45-degree loss among primitive pairs is about `0.22878167771728`. Unlike the old Oily **grade** filter `J odd`, the primitive lattice-pair filter concerns `gcd(K,L)`. These are different observations and cannot be equated. Indeed, all lost primitive pairs have **even** grade `J`.

### A canonical totient heat trace, not just a chosen vertex label

Write `q=e^{-t}` and expand `q^d/(1-q^d)^2=SUM_{m>=1}m q^(dm)` in the preceding odd-Möbius formula. The coefficient of `q^n` in `4L(t)` is exactly

```
A(n)=SUM_{d|n, d odd}mu(d)*(n/d)
    =n*PRODUCT_{p|n, p odd}(1-1/p)
    =(1+1_{2|n})*phi(n).
```

The last equality is the **precise 2-adic index-two defect**: for odd n the coefficient is the ordinary number of primitive residues φ(n); for even n it is **twice** that number. Therefore

```
BOXED: 4L(t)=SUM_{n>=1} [1+1_{2|n}]*phi(n)*exp(-nt)
            =SUM_{n>=1} [1+1_{2|n}]*(n-c(n))*exp(-nt),
```

where `c(n)=n-phi(n)` is the cototient. This is an exact **positive arithmetic heat trace** for the Oily-weighted 45-degree primitive-loss model. It directly links the standard Farey denominator primitive counts to the original Oily/45-degree defect; no arbitrary agreement of two constants was imposed. At `t=log4`, both constructions give the same `p45`.

An independent **positive rational** lower/upper certificate is obtained by truncating at n=N: since `A(n)<=2n`, the error is at most

```
(1/2)*4^(-(N+1))*[(N+1)/(1-1/4)+(1/4)/(1-1/4)^2].
```

The original odd-Möbius partial sum and this positive-totient partial sum are independent expansions of the **same exact source** and their certified rational intervals intersect in the test suite. On the Mellin side, the same theorem gives the Euler product identity

```
SUM_{n>=1} [1+1_{2|n}]*phi(n)/n^s
  =zeta(s-1)/[(1-2^(-s))*zeta(s)], Re s>2.
```

Thus totient/cototient are **load-bearing coefficients** in the Gamma–zeta rotation below, not merely labels added to the planar triangles.

## 4. Gamma, zeta and the actual quarter-angle contour

Extend the original parity defect to a positive screening parameter `t>0`:

```
L(t) = (1/4) SUM_{d>=1, odd} mu(d) exp(-td)/(1-exp(-td))^2.
```

At `t=log 4` this is exactly p45. For `Re(s)>2` absolute summation/integration and `z/(1-z)^2=SUM_{m>=1}m z^m` give

```
M(s)=integral_0^infinity t^(s-1)*L(t) dt
    = Gamma(s)/4 * zeta(s-1) * SUM_{d odd} mu(d)/d^s
    = Gamma(s) zeta(s-1)/[4(1-2^(-s)) zeta(s)].
```

This is a **precise, original-Oily-weighted Gamma–Möbius arithmetic bridge**. The excluded prime 2 is exactly the determinant/index-2 obstruction in the 45-degree lattice map. For any `theta` with `|theta|<pi/2` the same transform admits a contour-rotated representation

```
M(s) = exp(i theta s) integral_0^infinity
       u^(s-1) L(exp(i theta)u) du.
```

The quarter-angle `theta=pi/4` is legitimate: each exponential term has a convergent rotated Gamma integral and the full double series is absolutely integrable for `Re(s)>2`. This is an **analytic** rotation of the *same* parity-defect function, with declared complex phase `exp(i pi s/4)`; it is not proof that physical source paths themselves rotate. An independent high-precision contour integral passed.

### The Euler–Mascheroni cancellation is exact

Since `zeta(s-1)` has a simple pole at `s=2`, use the genuine regularized finite part. Expanding `Gamma(2+eps)=1+(1-gamma)eps+O(eps²)` and `eps*zeta(1+eps)=1+gamma eps+O(eps²)`, the Euler constants cancel, giving

```
M(s) = (2/pi²)/(s-2) + (2/pi²)*[
         1 - log(2)/3 - zeta'(2)/zeta(2)] + O(s-2).
```

The pole residue is `2/pi²`, independently obtainable as `lim_{t->0+} t² L(t)=2/pi²` by dominated convergence of the absolutely convergent `SUM_{d odd}mu(d)/d²`. This is an exact **Gamma/zeta renormalization** of the original 45-degree arithmetic defect. It does **not** identify the rank-two Gamma shape with a physical spin or supply a signed BBP Weyl bound.

## 5. The modular Eisenstein field is a global primitive-lattice tile

For `z=x+iy in H` and real `s>1`, define

```
E(z,s)=(1/2)*SUM_{(c,d) in Z², gcd(c,d)=1}
        y^s/|c*z+d|^(2s).
```

This is the unmarked primitive-vector **nonholomorphic Eisenstein series**; it converges absolutely for `s>1`. Under `g=[[a,b],[c,d]] in SL2(Z)`, the change of integer basis `(m,n) -> (ma+nc,mb+nd)` proves `E(gz,s)=E(z,s)` exactly. Thus the SAME analytic function restricts to every Farey triangle with consistent edge gluing; no conflicting local formulas need be postulated. Primitivity is canonical for the arithmetic lattice. The cototient counts complementary residue classes in a *marked* denominator chart, but a fixed mark generally is not modular invariant unless transported.

At `z=i`, the Gaussian integer factorization of the square lattice gives the classical identity

```
E(i,s)=2*zeta(s)*beta(s)/zeta(2s),  Re(s)>1,
```

where beta is the Dirichlet beta function. It has the Laurent expansion

```
E(i,s)=(3/pi)/(s-1)
       +(3/pi)*[ gamma + beta'(1)/beta(1) - 2*zeta'(2)/zeta(2)]
       +O(s-1).
```

In other words the **same modularly tiled primitive lattice** independently carries Euler–Mascheroni as a canonical pole finite part, together with source-specific beta and zeta corrections. The completed Epstein/Eisenstein Mellin machinery uses `Gamma(s)`; the Gaussian heat kernel/Poisson transform leads to the usual half-argument `Gamma(s/2)` when using one-dimensional theta. These are distinct normalized conventions. The modular matrix `S:z->-1/z` is an integer 90-degree change of lattice basis; the Gaussian contour substitution `u->exp(i pi/4)u` rotates a quadratic exponential by 90 degrees in its phase. **They are not the same map**, even though Gaussian Fourier/Mellin analysis relates their functional equations. Cf. NIST DLMF §5.9 and §20.7.

## 6. A SINGLE modular energy that detects the actual π carrier at infinity

Specialize to `s=2`, `y>0`, and write `f_y(x)=E(x+iy,2)`, a periodic function. Poisson summation of the **full** lattice followed by division by `zeta(4)` gives the **exact** Fourier expansion

```
f_y(x) = A_0(y) + SUM_{h!=0} a_|h|(y) exp(2pi i h x),
A_0(y)=y² + pi*zeta(3)/(2*zeta(4)*y),
a_h(y)=pi*(1+2pi*h*y)*exp(-2pi*h*y)*sigma_{-3}(h)/[2*zeta(4)*y],
sigma_{-3}(h)=SUM_{d|h} d^(-3), h>=1.
```

**Every nonzero a_h(y) is STRICTLY POSITIVE.** Proof without a table of presumed Fourier coefficients: write the nonprimitive Epstein sum, apply Poisson to each integer d-line; for positive c, its relevant Fourier transform is

```
integral_R y² exp(-2pi i m u)/(u²+(c y)²)² du
 = pi*(1+2pi*|m*c|*y)*exp(-2pi*|m*c|*y)/(2*|c|³*y).
```

A mode `h` receives contributions precisely from divisors `c|h`, all positive; divide the full lattice sum by `2*zeta(4)` to project onto primitive vectors. This also proves exponential Fourier summability for fixed `y>0`.

Use the unchanged original four-pole arithmetic recurrence with **zero seed**:

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)
U_0=0, U_(n+1)=16 U_n+r(n+1).
```

The inherited exact BBP tail identity is `U_n=16^(n-1)*pi-T_n` with `T_n>0` and `T_n=O(n^-2)`; hence for each fixed h the Fourier sums of `U_n` and the base-16 orbit `16^(n-1)*pi` differ by `O_h(1)` before dividing by N. This supplies the required exact link to Weyl's base-16 normality criterion. Define the physically modest **observation** of these actual rational phases, sampled at the real circle:

```
D_N(a;y) = (1/N)*SUM_{n=1}^N f_y(a+U_n) - A_0(y),
ENERGY_N(y) = integral_0^1 |D_N(a;y)|² da.
```

Parseval, *not* a false probabilistic independence assumption, yields

```
ENERGY_N(y) = SUM_{h!=0} a_|h|(y)² * |(1/N)*SUM_{n=1}^N exp(2pi i h U_n)|².
```

This is finite-N **positive energy with complete selected phase content**, **not** positivity of a signed Weil form. Since every `a_h>0`,

```
THEOREM: For every fixed y>0,
lim_N ENERGY_N(y)=0
    <=> for every fixed integer h!=0, lim_N S_N(h)/N=0
    <=> pi is normal in base 16.
```

The forward implication bounds each Weyl coefficient by `sqrt(ENERGY_N)/a_h(y)`. The reverse implication uses dominated convergence and `SUM a_h²<infinity`. This is **proof of equivalence, not proof of its limit**. All translated profiles are essential: observing only a single unshifted value of E cannot distinguish all nonuniform measures. Indeed a continuous nonconstant periodic function has mean strictly between its minimum and maximum, so an appropriate mixture of two point masses duplicates that one mean while remaining nonuniform.

For any cutoff H, the EXACT finite-representation error satisfies

```
0 <= ENERGY_N(y) - 2*SUM_{1<=h<=H} a_h(y)² |S_N(h)/N|²
  <= 2*SUM_{h>H} a_h(y)².
```

The tail decays exponentially; one explicit bound follows by `sigma_-3(h)<=zeta(3)`, setting `C=pi*zeta(3)/(2*zeta(4)*y)`, `q=exp(-4pi*y)`, `B=2pi*y`, and `H>=0`:

```
tail <= 4*C²*q^(H+1)*[
    (1+B*(H+1))²/(1-q) + B²*q*(1+q)/(1-q)³].
```

The Gaussian modular observer is therefore a finite-horizon, rigorously truncatable, normality-complete **probe** of the deterministic arithmetic carrier. Its inversion is exponentially ill-conditioned for high frequencies (a_h goes to zero exponentially). A fixed finite-precision instrument cannot infer an unbounded-frequency theorem by fiat.

### Essential adversarial controls

* **Same original forcing, coherent seed** `U_0=-pi/16`: the inherited positive tail identity gives `U_n=-T_n->0`, hence `ENERGY_N(y) -> 2*SUM_{h>=1}a_h(y)²>0`, with the explicit lower bound `2*a_1(y)²`. The zero-seed and coherent counterseed share all positive Oily/Gamma/totient source weights. The new selected modular energy separates their outcomes when actually evaluated on the selected phases.
* **Constant-phase source** `z_n=1`: same nonzero energy, defeating any false claim that Gaussian/Gram positivity entails decay.
* **Periodic sequence** alternating circle points `0,1/2`: some modes vanish, but even modes survive and energy stays positive (albeit small for y=1). No one- or three-mode test suffices.
* **Nonuniform two-atom measure matching one scalar Eisenstein mean:** rejects the weaker, unshifted observer.
* **Wrong source / clock / grade mutations:** positive Oily/Γ/Cauchy/Möbius quantities may survive changes to the four poles or initial seed, while the actual selected signed energy changes. Never promote positive-field identity to π normality.

A local numerical sample of the original finite zero-seeded source's `ENERGY_N(1)` at N=16,64,160 is preserved in the independent oracle; decreasing finite values are **OBSERVED ONLY**, not evidence of convergence or a finite-to-global theorem. The formal acceptance criterion remains an actual original-source signed estimate controlling `ENERGY_N(y)->0` or certifying positive `limsup` for some frequency.

## 7. Proof and source classification

* **PROVED PAPER/CLASSICAL**: Farey gluing, modular invariance, totient/cototient vertex decorations under declared Gamma law, 45-degree parity defect, original-Oily Möbius loss series and Mellin identity, Gamma contour rotation, Euler constant cancellation, Eisenstein Fourier coefficients and normality-equivalent modular energy.
* **OBSERVED**: exact Fraction regressions, numerical quadrature/complex Mellin/Gamma/Eisenstein checks, finite true zero-seed modular energy. Finite tests are not independent universal proof.
* **CONJECTURED**: any future source-derived *signed* inequality showing the true zero-seeded Eisenstein energy tends to 0 (or stays nonzero). No proof/measure-theoretic randomness of π digits is asserted.
* **DARK / UNVERIFIED**: a functor equating the freely decorated Farey Gamma vertex field or twist M(s) with the authentic deterministic BBP carry evolution beyond the explicitly selected circle observable; canonical significance of a 45-degree *physical* twist; academic novelty and root SUCC/Lean/hosted validation.
* **REFUTED**: 45-degree integer map preserves all primitive vectors; scalar Gamma vertex potential yields nontrivial holonomy; an unshifted modular scalar suffices for equidistribution; a finite decrease of selected modular energy proves its infinite limit.

## 8. Reproducibility

```sh
python -m unittest discover -s tests -p 'test_golden_gamma_farey_twist.py' -v
python research/2026-10-29/golden_gamma_farey_twist/independent_oracle.py
python -m compileall -q research/2026-10-29/golden_gamma_farey_twist tests/test_golden_gamma_farey_twist.py
```

The stdlib test derives the original Oily p45 rational brackets, tests 2-adic parity exhaustively, Farey/Pascal ranks, exact beta moment gluing and original rational BBP carries; the *separate* SymPy/mpmath oracle checks the contour, Mellin jet, modular transforms, original phase finite windows and gamma rank. Both are code/test probes, not Lean or peer review. All new research files are additive. Required AGENTS.md full-native provenance/unit/observer/ordinal gates and hosted CI must be checked on an authentic full worktree before promoting anything.

### Primary/authoritative sources

* NIST DLMF [§5.9 Gamma integral, logarithmic jets and Hankel contours](https://dlmf.nist.gov/5.9) and [§20.7 theta modular inversion](https://dlmf.nist.gov/20.7); [§25.2 zeta Laurent constant](https://dlmf.nist.gov/25.2).
* SUCC original source: `observational_succ/oily_macaroni_totient.py`, `research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md`, `research/2026-10-27/FAREY_GAUSS_GOLDEN_GAMMA_GENESIS.md`.
* PRs [#367](https://github.com/femboy2112/SUCC/pull/367), [#368](https://github.com/femboy2112/SUCC/pull/368), [#369](https://github.com/femboy2112/SUCC/pull/369), [#370](https://github.com/femboy2112/SUCC/pull/370), [#371](https://github.com/femboy2112/SUCC/pull/371), and [#372](https://github.com/femboy2112/SUCC/pull/372) (separately sourced, not assumed merged).
