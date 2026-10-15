# Classical SUCC II: real Haar prime clocks repair Hilbert gluing, but nonunit FUCC changes the map type

**Parent branch:** `research/classical-affine-carrier-2026-10-15` | **Parent source:** SUCC `main` `03db44203147a7b28d445bb9f970fa71360e78c4`.

**Research boundary:** All source actions are on actual prime-power residue rings and are transported from the same integer SUCC/FUCC laws. The probability/Hilbert field is **real or complex**, not a `Q_p`-valued probability theory. Finite demonstrations use rational amplitudes. Existence of standard `Z_p` Haar measure and density of locally constant cylinders are classical measure theory, not a new physical law. No RH/Weil positivity inference.

## H1 — an exact isometric prime-clock tower (CLASSICAL / PROVED PAPER)

Fix a genuine prime `p`. At stage `r>=1`, set `C_r=Z/p^rZ`, `mu_r({a})=p^(-r)` as a **real** normalized probability and `H_r=L²(C_r,mu_r;C)`. For natural reduction `pi_r:C_(r+1)->C_r`, define

`(P_r f)(x) = f(pi_r x)`.

Then `P_r:H_r->H_(r+1)` is an isometric embedding: each residue has exactly `p` lifts and the high-level mass of its fiber is `p*p^(-(r+1))=p^(-r)`. Its Hilbert adjoint is the exact conditional average

`(E_r g)(a) = (1/p) sum_(j=0)^(p-1) g(a+j*p^r)`.

Consequently `E_r P_r=I` and `P_r E_r` is the orthogonal projection to level-`r` cylinder functions inside level `r+1`. This is a valid **positive repair** of the unbounded naive ket quotient from the companion classical note, but it is a *different functor*, with a declared normalized measure and opposite direction for the isometric map.

The limit of this directed isometric system is the closure of locally constant cylinder functions in `L²(Z_p,mu_Haar;C)`. Its validity follows from the standard compact/profinite Haar probability and density of continuous locally constant functions. The executable tests address exact finite stages, not the topological proof of this completion.

## H2 — lawful integer-source actions and Koopman variance (PROVED PAPER)

The original source is `n>=1`, with `S(n)=n+1`, `V_m(n)=mn`. On unit-origin chart `x=n-1`, transported actions at every prime-power level are

`S^k(x)=x+k`, `V_m(x)=m*x+(m-1) mod p^r`.

On reflected chart `u=1-n`, signs reverse:

`S^k(u)=u-k`, `V_m(u)=m*u+(1-m) mod p^r`.

These actions descend under every reduction `pi_r`, so their observable pullbacks commute with the isometric cylinder embeddings. In function representation, write `U_k f=f∘S^k`, `M_m f=f∘V_m`. **Contravariance reverses composition order**:

`U_k M_m = M_m U_(m*k)`

rather than the untyped use of the source map identity `V_m S^k=S^(m*k)V_m` as if operator composition order stayed unchanged.

Every SUCC translation is unitary on normalized Haar, because it is a bijection. Multiplication by `m` is unitary on `H_r` **if and only if** `gcd(m,p^r)=1`. Merely realizing an arithmetic map on a Hilbert carrier does not make it unitary.

## H3 — exact FUCC multiplier energy and partial isometries (PROVED PAPER)

Let `N=p^r`, `g=gcd(m,N)`. The affine map `A_m(x)=m*x+epsilon*(m-1)` has an image coset of cardinality `N/g`, and every attained image address has exactly `g` preimages. For `M_m f=f∘A_m`, exact fiber counting yields

`||M_m f||²_(H_r) = g * ||1_(image A_m) f||²_(H_r)`.

Thus `||M_m||²=g`, and the rescaled `W_m=g^(-1/2)M_m` is a **partial isometry** whose initial projection is `1_(image A_m)` and whose final projection is the subspace of functions constant on the fibers of `A_m`. This statement is about *composition operators with normalized real/complex Haar*, not arithmetic zeta Euler weights.

For `p|m`, `g>1`, the finite-level `A_m` is neither injective nor surjective. In the projective-limit ring `Z_p`, the same map `A_m(x)=m*x+epsilon*(m-1)` **is injective** for every nonzero integer `m`, because `Z_p` is torsion-free, but is not onto when `p|m`. Write `k=v_p(m)`. Its image is `epsilon*(m-1)+p^k Z_p`. Haar measure scales by `p^(-k)` along its image; consequently

`||M_m f||²_(L²(Z_p)) = p^k ||1_(image A_m) f||²`.

The infinite-level `p^(-k/2)M_m` is a **coisometry** (onto `L²(Z_p)` with initial projection supported on that image), unlike any nonunit finite-level rescaling, whose range is fiber-constant. In particular, the finite nonzero kernel of multiplication by `p` does **not** yield a coherent nonzero kernel element of the inverse-limit source; the new category/type of the limit is essential.

**Proof of the no-ghost limit kernel:** If `p x=0` in `Z_p`, reduction modulo `p^r` forces `x=0 mod p^(r-1)` for every `r`, hence every finite digit of `x` vanishes. The same proof with `v_p(m)=k` works for any nonzero integer `m`: `m x=0 mod p^r` implies `x=0 mod p^(r-k)` for `r>k`. Thus `x=0` as a compatible inverse-limit sequence. No physical supertask or algorithmically decidable global certificate is asserted.

## H4 — adjoints do not generally commute with nonunit FUCC (PROVED PAPER / REFUTED NAIVE GLUING)

The pullback `P_r` always intertwines the level `r` and `r+1` observable actions, since the **source maps** descend. But its adjoint `E_r` need not intertwine a noninvertible multiplier. A fully specified source counterexample:

- prime `p=2`, levels `C_1=Z/2`, `C_2=Z/4`, positive unit-origin chart;
- authentic arithmetic `m=2` action `A_2(x)=2x+1`;
- high-level test `f=1_{x=1}` (one real-valued source packet).

Then

`E_1(M_2 f) = (1,0)` while `M_2(E_1 f) = (1/2,1/2)`.

So `E_r M_m = M_m E_r` **fails** even while `P_r M_m=M_m P_r` holds! The source is not inconsistent. These are different categorical directions; the averaging operation changes the information and multiplicities. For `p`-adic-unit multipliers, the multiplier permutes each reduction fiber, so `E_r` commutes with it. Source-prime multiplication `m=p` is exactly the important nonunit case.

This provides an operationally useful warning for other finite→global branches: source action descent and isometric observational inclusion do **not** automatically give descent of every adjoint/conditional observer update.

## H5 — real Haar masses are not bounded `Q_p`-valued measures (CLASSICAL / PRECISION FIREWALL)

Real Haar assigns singleton masses `p^(-r)` on `Z/p^rZ`, consistent with real probabilistic/projective integration. Regard the *same rational values* as elements of `Q_p`; then

`|p^(-r)|_p=p^r -> infinity`.

Therefore the cylinder weights are **not uniformly bounded in the p-adic norm**, and one cannot silently transfer the real Hilbert tower into a bounded `Q_p`-valued integral or a p-adic Hilbert space. This agrees with the existing repo's distinct O668 bounded-cylinder-weight criterion; do not conflate number-field completions.

## Interface to sibling sessions

- A **valid** finite-to-global Hilbert lane now exists: isometric pullbacks among *normalized real Haar probability spaces*, with exact adjoints and a standard profinite limit.
- The **failed** lane remains failed: unweighted basis collapse `e_n -> e_(n mod N)` from `ell²(N_0)` is unbounded; normalized Haar does not retroactively make that map bounded.
- The authentic source unit-origin shift `m*x+(m-1)` must be retained in every residue chart, especially under nonunit `p` multiplication. Zero-fixed `mx` is a different origin/basepoint, although its fiber size is the same.
- Multiplicative unit versus nonunit and the change from finite noninjectivity to infinite injectivity are exactly proven *relative to the declared source topology*, not a mystical finite-to-global threshold.
- Any Tate/Weil interpretation requires the right multiplicative Haar measure on local fields, Fourier/Poisson normalization, actual prime-power coefficients and archimedean Gamma; no analogue of Weil sign is deduced.

## Reproduce and falsify

```
python -m unittest discover -s tests -p 'test_classical_haar_clock.py' -v
python scripts/classical_haar_clock_probe.py --verify
```

Independent finite oracles count genuine affine-map fibers, check all-preimage energy against Fraction arithmetic, independently compare adjoints, and force a nonunit conditional-expectation failure. The code uses an explicit finite-state budget, so a successful run certifies the implemented finite claims only. Paper proofs carry the universal quantifiers. No nontrivial zeros are used in any construction.
